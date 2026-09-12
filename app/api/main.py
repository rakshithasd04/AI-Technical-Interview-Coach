from fastapi import FastAPI, UploadFile, File, Form
import tempfile
import os

from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
from app.services.job_analyzer import analyze_job_description
from app.services.skill_matcher import match_skills


app = FastAPI(title="AI Technical Interview Coach")


@app.get("/")
def home():
    return {
        "message": "AI Technical Interview Coach API is running!"
    }


@app.post("/analyze-resume")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Analyze a resume against a job description.
    """

    if not resume.filename.lower().endswith(".pdf"):
        return {
            "error": "Only PDF files are supported."
        }

    contents = await resume.read()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(contents)
        temp_file_path = temp_file.name

    try:
        # Step 1: Extract resume text
        resume_text = extract_text_from_pdf(temp_file_path)

        # Step 2: Extract resume skills
        resume_skills = extract_skills(resume_text)

        # Step 3: Analyze job description
        job_analysis = analyze_job_description(job_description)

        job_skills = job_analysis["required_skills"]

        # Step 4: Compare resume and job skills
        match_result = match_skills(
            resume_skills,
            job_skills
        )

        return {
            "resume_filename": resume.filename,
            "resume_skills": resume_skills,
            "job_required_skills": job_skills,
            "matched_skills": match_result["matched_skills"],
            "missing_skills": match_result["missing_skills"],
            "extra_skills": match_result["extra_skills"],
            "match_percentage": match_result["match_percentage"]
        }

    finally:
        os.remove(temp_file_path)