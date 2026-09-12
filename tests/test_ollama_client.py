from app.llm.ollama_client import generate_response


def test_generate_response():

    response = generate_response(
        "Explain Python in one short sentence."
    )

    print("LLM Response:", response)

    assert response
    assert isinstance(response, str)