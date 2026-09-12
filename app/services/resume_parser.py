import fitz
import re


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from all pages of a PDF file.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text() + "\n"

    document.close()

    return clean_text(text)


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.
    """

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove spaces at the beginning/end of lines
    lines = [line.strip() for line in text.splitlines()]

    # Remove completely empty lines
    lines = [line for line in lines if line]

    return "\n".join(lines)