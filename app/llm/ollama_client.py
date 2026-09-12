import ollama


MODEL_NAME = "llama3.2"


def generate_response(prompt: str) -> str:
    """
    Send a prompt to the local Ollama LLM
    and return its response.
    """

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]