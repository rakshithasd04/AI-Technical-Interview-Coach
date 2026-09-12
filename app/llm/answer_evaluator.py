from app.llm.ollama_client import generate_response


def evaluate_answer(
    question: str,
    answer: str
) -> str:
    """
    Evaluate a candidate's answer using the local LLM.
    """

    prompt = f"""
You are an expert technical interviewer.

Evaluate the candidate's answer to the technical interview question.

Question:
{question}

Candidate Answer:
{answer}

Provide your evaluation in the following format:

Score: X/10

Strengths:
- List the strong points in the answer.

Weaknesses:
- List the missing or incorrect points.

Suggestions:
- Explain how the candidate can improve the answer.

Be fair and technically accurate.
Do not invent information about the candidate.
"""

    return generate_response(prompt)