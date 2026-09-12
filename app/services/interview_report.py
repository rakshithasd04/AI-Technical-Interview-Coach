def generate_interview_report(evaluations: list[dict]) -> dict:
    """
    Generate an overall interview performance report
    from individual question evaluations.
    """

    if not evaluations:
        return {
            "overall_score": 0.0,
            "questions_answered": 0,
            "strengths": [],
            "weaknesses": [],
            "recommendations": []
        }

    scores = [
        evaluation["score"]
        for evaluation in evaluations
    ]

    overall_score = sum(scores) / len(scores)

    strengths = []
    weaknesses = []
    recommendations = []

    for evaluation in evaluations:

        strengths.extend(
            evaluation.get("strengths", [])
        )

        weaknesses.extend(
            evaluation.get("weaknesses", [])
        )

        recommendations.extend(
            evaluation.get("suggestions", [])
        )

    return {
        "overall_score": round(overall_score, 2),
        "questions_answered": len(evaluations),
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }