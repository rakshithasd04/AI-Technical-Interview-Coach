from app.services.interview_session import InterviewSession
import uuid


sessions = {}


def create_session(questions: list[str]) -> str:
    """
    Create a new interview session and return its ID.
    """

    session_id = str(uuid.uuid4())

    sessions[session_id] = InterviewSession(questions)

    return session_id


def get_session(session_id: str) -> InterviewSession | None:
    """
    Retrieve an interview session by its ID.
    """

    return sessions.get(session_id)


def delete_session(session_id: str) -> bool:
    """
    Delete an interview session.
    """

    if session_id in sessions:
        del sessions[session_id]
        return True

    return False