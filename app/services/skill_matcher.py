def match_skills(resume_skills: list[str], job_skills: list[str]) -> dict:
    """
    Compare resume skills with the skills required by a job.
    """

    resume_set = {skill.lower() for skill in resume_skills}
    job_set = {skill.lower() for skill in job_skills}

    matched = sorted(resume_set.intersection(job_set))
    missing = sorted(job_set - resume_set)
    extra = sorted(resume_set - job_set)

    if len(job_set) > 0:
        match_percentage = (len(matched) / len(job_set)) * 100
    else:
        match_percentage = 0.0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
        "match_percentage": round(match_percentage, 2)
    }