import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="AI Job Description Decoder",
    page_icon="💼",
    layout="wide"
)

# Title
st.title("💼 AI Job Description Decoder")

st.write(
    "Paste a job description below and decode the important "
    "skills, requirements, experience, education, and keywords."
)

# Job description input
job_description = st.text_area(
    "📄 Job Description",
    height=300,
    placeholder="Paste the job description here..."
)

# Decode button
if st.button("🔍 Decode Job Description"):

    if not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        text = job_description.lower()

        # Skills
        skills_list = [
            "python",
            "java",
            "javascript",
            "sql",
            "html",
            "css",
            "react",
            "node.js",
            "machine learning",
            "deep learning",
            "artificial intelligence",
            "data analysis",
            "pandas",
            "numpy",
            "streamlit",
            "git",
            "github",
            "docker",
            "aws",
            "azure",
            "power bi",
            "excel"
        ]

        found_skills = [
            skill.title()
            for skill in skills_list
            if skill in text
        ]

        # Experience
        
        experience = []

        for i in range(1, 11):
            if f"{i} year" in text or f"{i} years" in text:
                experience.append(f"{i} years")

            if f"{i}+ year" in text or f"{i}+ years" in text:
                experience.append(f"{i}+ years")
                
        # Education
        education_list = [
            "b.tech",
            "b.e",
            "bachelor's degree",
            "bachelors degree",
            "bachelor degree",
            "m.tech",
            "m.e",
            "master's degree",
            "masters degree",
            "master degree",
            "mca",
            "mba",
            "computer science",
            "information technology",
            "engineering"
        ]

        found_education = [
            education.title()
            for education in education_list
            if education in text
        ]

        # Success message
        st.success("Job description decoded successfully!")

        # Skills
        st.subheader("🛠️ Skills")

        if found_skills:
            cols = st.columns(3)

            for index, skill in enumerate(found_skills):
                cols[index % 3].success(skill)
        else:
            st.info("No specific technical skills detected.")

        # Experience
        st.subheader("💼 Experience")

        if experience:
            st.write(", ".join(experience))
        else:
            st.write("Experience requirement not detected.")

        # Education
        st.subheader("🎓 Education / Qualifications")

        if found_education:
            st.write(", ".join(found_education))
        else:
            st.write("No specific education requirement detected.")

        # Requirements
        st.subheader("📋 Requirements")

        st.write("• Strong technical skills")
        st.write("• Relevant experience")
        st.write("• Good problem-solving skills")

        # Important Keywords
        st.subheader("🔑 Important Keywords")

        keywords = [
            "responsibilities",
            "requirements",
            "qualification",
            "skills",
            "experience",
            "developer",
            "engineer",
            "analyst",
            "intern",
            "full-time",
            "part-time"
        ]

        found_keywords = [
            keyword.title()
            for keyword in keywords
            if keyword in text
        ]

        if found_keywords:
            st.write(", ".join(found_keywords))
        else:
            st.write("No major keywords detected.")