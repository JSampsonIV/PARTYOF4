import re
from google import genai
from google.genai import types
from API_KEY import API_KEY

def call_llm(prompt):
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are an internal AI within Chevron. You are tasked with creating an employee profile for the given employee, and create a profile for them to find the job that best suits them. Please answer with professional language."),
        contents=prompt
    )
    return response.text

def fake_call_llm(prompt: str) -> str:
    return """
    Match Percentage: 87%
    Reason: Based on the candidate’s experience with Python and Machine Learning, they are highly suited for the role of Senior Machine Learning Engineer. Their strengths align well with the required job skills.
    """

def generate_prompt(employee_profile, performance_review_responses, self_assessment_responses, peer_review_responses):
    prompt = f"""
    Based on the following responses to performance, self-assessment, and peer reviews, as well as the employee profile, please generate a comprehensive and detailed summary of the employee's overall performance, contributions, and areas for improvement. The employee's profile and feedback should be analyzed holistically to provide a thorough assessment.

    **Employee Profile:**
    Name: {employee_profile['name']}
    Role: {employee_profile['role']}
    Department: {employee_profile['department']}
    Skills: {', '.join(employee_profile['skills'])}
    Years of Experience: {employee_profile['years_experience']}

    **Performance Review Q&A:**
    {performance_review_responses}

    **Self-Assessment Q&A:**
    {self_assessment_responses}

    **Peer Review Q&A:**
    {peer_review_responses}

    Please ensure the following in your summary:
    1. **Strengths and Key Contributions**: Highlight the employee's key strengths and notable contributions to their role. Use specific examples from the reviews to illustrate these strengths.
    2. **Areas for Development**: Clearly identify areas where the employee may need to improve or focus on. Provide actionable recommendations for development.
    3. **Skills Impact**: Emphasize the skills the employee has demonstrated and how they have contributed to their performance.
    4. **Overall Summary**: Provide an overall evaluation of the employee’s performance, including notable achievements or challenges, and how they impact the employee’s future potential.
    
    Please ensure the summary is clear, specific, and paints a well-rounded picture of the employee's performance.
    """
    
    return prompt

def generate_employee_profile_summary(employee_profile, performance_review_responses, self_assessment_responses, peer_review_responses):
    # Generate the prompt for the LLM
    prompt = generate_prompt(employee_profile, performance_review_responses, self_assessment_responses, peer_review_responses)
    summary = call_llm(prompt=prompt)
    return summary

def generate_job_match_prompt(employee_profile: str, job: dict) -> str:
    return f"""
        You are an expert career advisor and HR AI assistant.

        Given the following employee profile and job description, assess how well the employee fits the role.
        Return a single number representing the match percentage (0-100), along with a short rationale.

        ### Employee Profile:
        {employee_profile}

        ### Job Title:
        {job.get('title', 'Unknown')}

        ### Job Description:
        {job.get('description', 'No description provided.')}

        ### Response Format:
        Match Percentage: <number>%
        Reason: <1-2 sentence summary>
        """

def get_job_match_score(employee_profile: str, job: dict) -> dict:
    prompt = generate_job_match_prompt(employee_profile, job)
    llm_response = call_llm(prompt)

    # Extract match percentage
    percentage_match = re.search(r"Match Percentage: (\d+)%", llm_response)
    score = int(percentage_match.group(1)) if percentage_match else 0

    # Extract reason
    reason_match = re.search(r"Reason:([\s\S]*)", llm_response)
    reason = reason_match.group(1).strip() if reason_match else "No explanation provided."

    return {
        "score": score,
        "job_title": job.get("title", "Unknown"),
        "job_description": job.get("description", "Not provided"),
        "reason": reason
    }
