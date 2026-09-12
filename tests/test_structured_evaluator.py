from app.llm.structured_evaluator import evaluate_answer_structured


def test_evaluate_answer_structured():

    question = "What is the difference between a list and a tuple in Python?"

    answer = """
    A list is mutable, while a tuple is immutable.
    Lists are generally used when the data may need to change,
    while tuples are useful for fixed collections of values.
    """

    result = evaluate_answer_structured(
        question,
        answer
    )

    print("\nStructured Evaluation:")
    print(result)

    assert isinstance(result, dict)
    assert "score" in result
    assert "strengths" in result
    assert "weaknesses" in result
    assert "suggestions" in result

    assert isinstance(result["score"], int)
    assert 0 <= result["score"] <= 10