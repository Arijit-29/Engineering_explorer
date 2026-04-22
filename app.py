from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
engineering_departments = [
    "Computer Science Engineering",
    "Information Technology",
    "Electronics and Communication Engineering",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Chemical Engineering",
    "Aerospace Engineering",
    "Automobile Engineering",
    "Biotechnology Engineering",
    "Biomedical Engineering",
    "Environmental Engineering",
    "Industrial Engineering",
    "Production Engineering",
    "Materials Science and Engineering",
    "Polymer Science and Technology",
    "Optics and Optoelectronics Engineering",
    "Geotechnical Engineering",
    "Power Engineering",
    "Mining Engineering",
    "Metallurgical Engineering",
    "Petroleum Engineering",
    "Agricultural Engineering",
    "Marine Engineering",
    "Robotics Engineering",
    "Artificial Intelligence and Data Science",
    "Cyber Security Engineering",
    "Mechatronics Engineering",
    "Instrumentation Engineering",
    "Textile Engineering",
    "Food Technology Engineering",
    "Nanotechnology Engineering",
    "Structural Engineering",
    "Printing and Packaging Engineering",
]
model = ChatGroq(model="openai/gpt-oss-120b")
st.markdown("<h1 style='text-align: center;'>⚙️ Engineering Explorer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get insights into different engineering fields 🚀</p>", unsafe_allow_html=True)
with st.container():
    st.subheader("📌 Choose Your Preferences")

    col1, col2 = st.columns(2)

    with col1:
        dept_input = st.selectbox("🔧 Department", engineering_departments)

    with col2:
        style_input = st.radio("🎨 Style", ["Beginner-Friendly", "Technical", "Funny"])

    length_input = st.selectbox(
        "📏 Explanation Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
    )

template= load_prompt('dept_template.json')
if st.button("🚀 Get Insights"):

    with st.spinner("Generating insights... ⏳"):
        chain = template | model
        response = chain.invoke({
            "dept_input": dept_input,
            "style_input": style_input,
            "length_input": length_input
        })

    st.success("Done! 🎉")

    # Output section
    st.markdown("### 📖 Explanation")

    st.markdown(f"""
    <div class="output-box">
    {response.content}
    </div>
    """, unsafe_allow_html=True)