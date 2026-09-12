from app.services.interview_session import InterviewSession
from app.llm.structured_evaluator import evaluate_answer_structured


def submit_answer(
    session: InterviewSession,
    answer: str
) -> dict:
    """
    Evaluate the candidate's answer, store the evaluation,
    and move the interview to the next question.
    """

    question = session.get_current_question()

    if question is None:
        return {
            "error": "Interview is already complete."
        }

    evaluation = evaluate_answer_structured(
        question,
        answer
    )

    session.add_evaluation(evaluation)

    return {
        "question": question,
        "evaluation": evaluation,
        "progress": session.get_progress()
    }