
import streamlit as st
from ml import extract_text, extract_skills, extract_experience, score_resume


st.title("🚀 Smart Resume Analyzer")


# File Upload

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)")

if uploaded_file:
    
    # Extract Resume Text
    
    text = extract_text(uploaded_file)
    st.subheader("📄 Extracted Resume Text")
    st.write(text)

    
    # Extract Skills
    
    skills_found = extract_skills(text)
    st.subheader("💡 Skills Found")
    st.write(skills_found)

    
    # Extract Experience
    
    experience = extract_experience(text)
    st.subheader("⏳ Experience (Years)")
    st.write(experience)

    
    # Compute Resume Score

    total_score = score_resume(skills_found, experience)
    st.subheader("🏆 Resume Score")
    st.write(f"{total_score} / 100")
