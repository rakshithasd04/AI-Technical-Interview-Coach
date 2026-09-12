import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Technical Interview Coach",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Technical Interview Coach")

st.write(
    "Analyze your resume against a job description "
    "and generate personalized technical interview questions."
)


st.header("📄 Resume & Job Analysis")


resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste the Job Description",
    height=200
)


if st.button("🔍 Analyze Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")

    elif not job_description.strip():
        st.error("Please enter the job description.")

    else:

        with st.spinner("Analyzing resume..."):

            files = {
                "resume": (
                    resume_file.name,
                    resume_file.getvalue(),
                    "application/pdf"
                )
            }

            data = {
                "job_description": job_description
            }

            response = requests.post(
                f"{API_URL}/analyze-resume",
                files=files,
                data=data
            )

        if response.status_code == 200:

            result = response.json()

            st.success("Resume analysis completed!")

            st.subheader("🧠 Resume Skills")

            st.write(result["resume_skills"])

            st.subheader("🎯 Required Job Skills")

            st.write(result["job_required_skills"])

            st.subheader("✅ Matched Skills")

            st.write(result["matched_skills"])

            st.subheader("❌ Missing Skills")

            st.write(result["missing_skills"])

            st.subheader("📊 Skill Match")

            st.metric(
                "Match Percentage",
                f'{result["match_percentage"]}%'
            )

            st.subheader("🤖 AI Interview Questions")

            st.write(result["interview_questions"])

        else:

            st.error(
                f"API Error: {response.status_code}"
            )