from app.services.interview_session import InterviewSession


def test_interview_session():

    questions = [
        "What is Python?",
        "What is machine learning?",
        "What is an API?"
    ]

    session = InterviewSession(questions)

    # First question
    assert session.get_current_question() == "What is Python?"

    progress = session.get_progress()

    assert progress["current_question"] == 1
    assert progress["total_questions"] == 3
    assert progress["completed"] == 0
    assert progress["is_complete"] is False

    # Answer first question
    session.add_evaluation({
        "score": 8
    })

    assert session.get_current_question() == "What is machine learning?"

    # Answer second question
    session.add_evaluation({
        "score": 7
    })

    assert session.get_current_question() == "What is an API?"

    # Answer third question
    session.add_evaluation({
        "score": 9
    })

    assert session.is_complete() is True
    assert session.get_current_question() is None
    assert len(session.evaluations) == 3