from app.services.semantic_matcher import semantic_similarity


def test_semantic_similarity():

    similarity = semantic_similarity(
        "Python software development",
        "developing software using Python"
    )

    print("Similarity:", similarity)

    assert similarity > 0.3