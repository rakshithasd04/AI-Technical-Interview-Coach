from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import tempfile
import os

from app.services.resume_parser import extract_text_from_pdf
from app.services.skill_extractor import extract_skills
from app.services.job_analyzer import analyze_job_description
from app.services.skill_matcher import match_skills
from app.services.semantic_skill_matcher import semantic_skill_match
from app.llm.question_generator import generate_interview_questions
from app.services.session_manager import create_session, get_session
from app.services.interview_engine import submit_answer
from app.services.interview_report import generate_interview_report


app = FastAPI(title="AI Technical Interview Coach")

class AnswerSubmissionRequest(BaseModel):
    session_id: str
    answer: str
class InterviewStartRequest(BaseModel):
    questions: list[str]


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

        # Step 4: Exact skill matching
        match_result = match_skills(
            resume_skills,
            job_skills
        )

        # Step 5: Semantic skill matching
        semantic_result = semantic_skill_match(
            resume_skills,
            job_skills
        )

        # Step 6: Generate personalized interview questions
        interview_questions = generate_interview_questions(
            resume_text,
            job_description
        )

        return {
            "resume_filename": resume.filename,
            "resume_skills": resume_skills,
            "job_required_skills": job_skills,
            "matched_skills": match_result["matched_skills"],
            "missing_skills": match_result["missing_skills"],
            "extra_skills": match_result["extra_skills"],
            "match_percentage": match_result["match_percentage"],
            "semantic_matched_skills": semantic_result["matched_skills"],
            "semantic_missing_skills": semantic_result["missing_skills"],
            "interview_questions": interview_questions
        }

    finally:
        os.remove(temp_file_path)


@app.post("/start-interview")
def start_interview(request: InterviewStartRequest):
    """
    Start a new interview session.
    """

    if not request.questions:
        return {
            "error": "At least one question is required."
        }

    session_id = create_session(request.questions)

    return {
        "session_id": session_id,
        "first_question": request.questions[0],
        "total_questions": len(request.questions)
    }
@app.post("/submit-answer")
def submit_interview_answer(request: AnswerSubmissionRequest):
    """
    Submit an answer for the current interview question.
    """

    session = get_session(request.session_id)

    if session is None:
        return {
            "error": "Interview session not found."
        }

    if session.is_complete():
        return {
            "error": "Interview is already complete."
        }

    result = submit_answer(
        session,
        request.answer
    )

    return {
        "evaluation": result["evaluation"],
        "progress": result["progress"],
        "next_question": session.get_current_question()
    }
@app.get("/interview-report")
def get_interview_report(session_id: str):
    """
    Generate the final interview performance report.
    """

    session = get_session(session_id)

    if session is None:
        return {
            "error": "Interview session not found."
        }

    report = generate_interview_report(
        session.evaluations
    )

    return {
        "session_id": session_id,
        "progress": session.get_progress(),
        "report": report
    }