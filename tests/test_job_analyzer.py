from app.services.job_analyzer import analyze_job_description


def test_analyze_job_description():

    job_description = """
    We are looking for a candidate with strong knowledge of
    Python, Git, GitHub, Machine Learning, LLMs, APIs,
    Data Structures and AI/ML concepts.
    """

    result = analyze_job_description(job_description)

    skills = result["required_skills"]

    assert "Python" in skills
    assert "Git" in skills
    assert "GitHub" in skills
    assert "Machine Learning" in skills
    assert "LLM" in skills
    assert "APIs" in skills
    assert "Data Structures" in skills