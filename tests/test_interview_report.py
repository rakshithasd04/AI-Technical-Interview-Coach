from app.services.interview_report import generate_interview_report


def test_generate_interview_report():

    evaluations = [
        {
            "score": 8,
            "strengths": ["Good Python knowledge"],
            "weaknesses": ["Needs more examples"],
            "suggestions": ["Practice advanced Python"]
        },
        {
            "score": 6,
            "strengths": ["Understands ML basics"],
            "weaknesses": ["Limited depth"],
            "suggestions": ["Study ML algorithms"]
        },
        {
            "score": 9,
            "strengths": ["Strong API knowledge"],
            "weaknesses": [],
            "suggestions": ["Practice system design"]
        }
    ]

    report = generate_interview_report(evaluations)

    print("\nInterview Report:")
    print(report)

    assert report["overall_score"] == 7.67
    assert report["questions_answered"] == 3

    assert "Good Python knowledge" in report["strengths"]
    assert "Limited depth" in report["weaknesses"]
    assert "Study ML algorithms" in report["recommendations"]