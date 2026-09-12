import json

from app.llm.ollama_client import generate_response


def evaluate_answer_structured(
    question: str,
    answer: str
) -> dict:
    """
    Evaluate a candidate's answer and return
    structured JSON data.
    """

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.
Do not include markdown.
Do not include ```.

Use exactly this structure:

{{
    "score": 0,
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

Rules:
- score must be an integer from 0 to 10.
- strengths must be a list of strings.
- weaknesses must be a list of strings.
- suggestions must be a list of strings.
- Be technically accurate and fair.
"""

    response = generate_response(prompt)

    return json.loads(response)