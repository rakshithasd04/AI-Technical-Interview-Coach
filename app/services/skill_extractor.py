import re


SKILLS = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Django",
    "FastAPI",
    "Flask",
    "SQL",
    "MongoDB",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "AI",
    "NLP",
    "LLM",
    "RAG",
    "LangChain",
    "LangGraph",
    "OpenCV",
    "MediaPipe",
    "REST API",
    "APIs",
    "Data Structures",
]


def extract_skills(text: str) -> list[str]:
    """
    Find known technical skills in the given text.
    """

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"s?\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills