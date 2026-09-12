from app.services.session_manager import (
    create_session,
    get_session,
    delete_session
)


def test_session_manager():

    questions = [
        "What is Python?",
        "What is an API?"
    ]

    # Create session
    session_id = create_session(questions)

    assert session_id
    assert isinstance(session_id, str)

    # Retrieve session
    session = get_session(session_id)

    assert session is not None
    assert session.get_current_question() == "What is Python?"

    # Delete session
    deleted = delete_session(session_id)

    assert deleted is True

    # Session should no longer exist
    assert get_session(session_id) is None