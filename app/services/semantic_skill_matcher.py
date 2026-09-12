from app.services.semantic_matcher import semantic_similarity


def semantic_skill_match(
    resume_skills: list[str],
    job_skills: list[str],
    threshold: float = 0.5
) -> dict:
    """
    Match resume skills with job skills using semantic similarity.
    """

    matched_skills = []
    missing_skills = []

    for job_skill in job_skills:

        best_similarity = 0.0
        best_resume_skill = None

        for resume_skill in resume_skills:

            similarity = semantic_similarity(
                resume_skill,
                job_skill
            )

            if similarity > best_similarity:
                best_similarity = similarity
                best_resume_skill = resume_skill

        if best_similarity >= threshold:
            matched_skills.append({
                "job_skill": job_skill,
                "resume_skill": best_resume_skill,
                "similarity": best_similarity
            })
        else:
            missing_skills.append(job_skill)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }