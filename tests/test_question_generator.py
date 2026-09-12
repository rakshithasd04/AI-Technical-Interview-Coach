from app.llm.question_generator import generate_interview_questions


def test_generate_interview_questions():

    resume_text = """
    I have experience with Python, Machine Learning,
    FastAPI and Git.
    """

    job_description = """
    We are looking for a candidate with Python,
    Machine Learning, APIs, LLMs and Data Structures.
    """

    questions = generate_interview_questions(
        resume_text,
        job_description
    )

    print("\nGenerated Questions:\n", questions)

    assert questions
    assert isinstance(questions, str)