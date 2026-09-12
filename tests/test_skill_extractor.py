from app.services.skill_extractor import extract_skills


def test_extract_skills():
    text = """
    I have experience with Python, Git, GitHub,
    Machine Learning and FastAPI.
    """

    skills = extract_skills(text)

    assert "Python" in skills
    assert "Git" in skills
    assert "GitHub" in skills
    assert "Machine Learning" in skills
    assert "FastAPI" in skills