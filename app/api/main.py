from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from app.services.resume_parser import extract_text_from_pdf


app = FastAPI(title="AI Technical Interview Coach")


@app.get("/")
def home():
    return {
        "message": "AI Technical Interview Coach API is running!"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are supported."
        }

    contents = await file.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(contents)
        temp_file_path = temp_file.name

    try:
        text = extract_text_from_pdf(temp_file_path)

        return {
            "filename": file.filename,
            "text": text
        }

    finally:
        os.remove(temp_file_path)