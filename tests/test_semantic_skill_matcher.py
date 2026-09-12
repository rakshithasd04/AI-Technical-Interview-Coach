from app.services.semantic_skill_matcher import semantic_skill_match


def test_semantic_skill_match():

    resume_skills = [
        "Python",
        "machine learning",
        "software development"
    ]

    job_skills = [
        "Python",
        "ML",
        "software engineering"
    ]

    result = semantic_skill_match(
        resume_skills,
        job_skills,
        threshold=0.5
    )

    print("Result:", result)

    assert len(result["matched_skills"]) >= 2