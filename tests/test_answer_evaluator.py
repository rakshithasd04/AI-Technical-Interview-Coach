from app.llm.answer_evaluator import evaluate_answer


def test_evaluate_answer():

    question = "What is the difference between a Python list and a tuple?"

    answer = """
    A list is mutable, which means we can change its elements.
    A tuple is immutable, so once it is created, its elements
    cannot be changed.
    """

    evaluation = evaluate_answer(
        question,
        answer
    )

    print("\nEvaluation:\n", evaluation)

    assert evaluation
    assert isinstance(evaluation, str)