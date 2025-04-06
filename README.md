# 🥳 PARTYOF4: Intellimatch 
*AI-Powered Employee Evaluation & Job Matching Dashboard*

**PARTYOF4's** *Intellimatch* is an interactive Streamlit dashboard designed for **HR managers** to evaluate employees and match them with **internal job opportunities** using AI. The application aggregates insights from self, peer, and performance reviews to build a comprehensive employee profile, which is then compared against job descriptions to provide **AI-powered job match scores**. Our application uses Google's genAI API to access their gemini 2.0 flash model to formulate employee summary profiles and employee job matching.

This project was built for **North Carolina A&T State University's** spring 2025 hackathon hosted by ACM. Our team was given **Chevron's** problem statement of: You are tasked with developing a system that leverages AI for Chevron to assess employees’ skills and match them with the most suitable roles within the company. The system should analyze various data sources, such as performance reviews, project outcomes, and self-assessments, to create detailed skill profiles for each employee. It should then compare these profiles with the requirements of available roles to identify the best matches. Additionally, the system should account for soft skills by incorporating qualitative data from peer reviews and feedback.

**Results:** 2nd Place!

**Presentation:** https://www.canva.com/design/DAGjxaOlO5c/geo5CDG5yGycnbBzGJYQCw/view?utm_content=DAGjxaOlO5c&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h7418261035
 
---

## 🚀 Features

- 👤 View and manage employee information (role, department, skills, experience)
- 🧠 Self-assessment from employees
- 🤝 Peer reviews collection
- 👨‍💼 Manager performance review inputs
- 📄 AI-generated employee summaries
- 📌 Match employees to internal jobs with AI-driven fit scoring

---

## ⚙️ Setup Instructions

Follow the steps below to set up the app locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PARTYOF4.git
cd PARTYOF4
```

### 2. Create and Activate a Virtual Environment
```
# Create a virtual environment
python -m venv venv

# Activate the environment (macOS/Linux)
source venv/bin/activate

# Activate the environment (Windows)
venv\Scripts\activate
```

### 3. Installed Required Packages
```
pip install -r requirements.txt
```

### 4. Running the App
```
streamlit run app.py
```

## 👥 Authors
- **Rickey Johnson**
- **John Sampson**
- **Anthony Charleston**
- **Evan Jones**