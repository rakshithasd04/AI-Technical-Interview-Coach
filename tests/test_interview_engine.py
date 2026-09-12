from app.services.interview_session import InterviewSession
from app.services.interview_engine import submit_answer


def test_submit_answer():

    questions = [
        "What is Python?",
        "What is machine learning?"
    ]

    session = InterviewSession(questions)

    result = submit_answer(
        session,
        "Python is a high-level programming language."
    )

    print("\nInterview Result:")
    print(result)

    assert "question" in result
    assert "evaluation" in result
    assert "progress" in result

    assert isinstance(result["evaluation"], dict)
    assert "score" in result["evaluation"]

    assert result["progress"]["completed"] == 1

    assert session.get_current_question() == "What is machine learning?"