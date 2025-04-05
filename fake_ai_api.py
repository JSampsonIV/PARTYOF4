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

    # Simulating an API call to the LLM (this would be replaced by a real API call in production)
    # For now, we'll return a simulated response based on the prompt.
    
    summary = f"""
    **Summary of {employee_profile['name']}'s Performance:**

    **Strengths**:
    {employee_profile['name']} has consistently demonstrated exceptional technical skills in their role as a {employee_profile['role']}. They have excelled in using {', '.join(employee_profile['skills'])} to solve complex problems and drive results. In the performance review, {employee_profile['name']} was praised for their ability to manage projects effectively and work efficiently under pressure. One notable example was their success in delivering a critical system upgrade ahead of schedule, showcasing both technical expertise and strong time management skills.

    **Areas for Development**:
    Despite their strong performance, {employee_profile['name']} could improve their communication skills, especially when explaining complex technical concepts to non-technical stakeholders. Their self-assessment highlighted a desire to improve in this area, and their peer feedback echoed the sentiment. Developing these skills would help them collaborate more effectively with cross-functional teams and elevate their leadership potential.

    **Skills Impact**:
    The skills demonstrated by {employee_profile['name']} in Python, Machine Learning, and Data Analysis have significantly contributed to the team's success. Their ability to integrate data-driven insights into software development processes has led to improved product performance and efficiency. These skills are crucial to the company's continued success and position {employee_profile['name']} as a key contributor to the team.

    **Overall Summary**:
    {employee_profile['name']} is a highly valuable member of the team, with a proven track record of delivering high-quality work. While there are opportunities for growth in communication, their technical proficiency and problem-solving abilities are exceptional. With continued development in these areas, {employee_profile['name']} is well-positioned for future leadership roles.
    """

    return summary
