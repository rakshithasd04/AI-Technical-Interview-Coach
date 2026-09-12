from app.services.skill_extractor import extract_skills


def analyze_job_description(job_description: str) -> dict:
    """
    Analyze a job description and extract required technical skills.
    """

    skills = extract_skills(job_description)

    return {
        "required_skills": skills,
        "skill_count": len(skills)
    }