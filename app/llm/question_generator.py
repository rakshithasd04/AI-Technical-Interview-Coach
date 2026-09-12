from app.llm.ollama_client import generate_response


def generate_interview_questions(
    resume_text: str,
    job_description: str
) -> str:
    """
    Generate personalized technical interview questions
    using the candidate's resume and job description.
    """

    prompt = f"""
You are an expert technical interviewer.

Analyze the candidate's resume and the job description below.

Candidate Resume:
{resume_text}

Job Description:
{job_description}

Generate 5 personalized technical interview questions.

Requirements:
- Focus on skills relevant to the job.
- Consider the candidate's resume.
- Include questions of different difficulty levels.
- Questions should be technical and suitable for an interview.
- Do not provide answers.
- Number the questions from 1 to 5.
"""

    return generate_response(prompt)