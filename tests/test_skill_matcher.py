from app.services.skill_matcher import match_skills


def test_match_skills():

    resume_skills = [
        "Python",
        "Git",
        "GitHub",
        "React",
        "SQL"
    ]

    job_skills = [
        "Python",
        "Git",
        "GitHub",
        "Machine Learning",
        "LLM",
        "APIs"
    ]

    result = match_skills(resume_skills, job_skills)

    assert "python" in result["matched_skills"]
    assert "git" in result["matched_skills"]
    assert "github" in result["matched_skills"]

    assert "machine learning" in result["missing_skills"]
    assert "llm" in result["missing_skills"]
    assert "apis" in result["missing_skills"]

    assert "react" in result["extra_skills"]
    assert "sql" in result["extra_skills"]

    assert result["match_percentage"] == 50.0