import streamlit as st

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🧭",
    layout="centered"
)
import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)
st.title("🧭 AI Learning Roadmap Generator")
st.write("Create a simple learning roadmap based on your goals.")

domain = st.text_input(
    "Domain/field",
    placeholder="Example: Python, Networking, Data Science"
)

skill_level = st.selectbox(
    "Skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

time_available = st.number_input(
    "Time available (hours per week)",
    min_value=1,
    max_value=60,
    value=5,
    step=1
)

if st.button("Generate Roadmap"):
    if not domain.strip():
        st.warning("Please enter a domain or field.")
    else:
        st.success("Your learning roadmap is ready!")

        st.subheader(f"Learning Roadmap: {domain}")
        st.write(f"**Skill level:** {skill_level}")
        st.write(f"**Time available:** {time_available} hours per week")

        st.markdown("### Week 1: Understand the basics")
        st.write(
            f"Learn the basic concepts of {domain}. "
            "Use beginner tutorials, documentation, and simple examples."
        )

        st.markdown("### Week 2: Practice important skills")
        st.write(
            f"Practice the main skills required for {domain}. "
            "Complete small exercises and practical tutorials."
        )

        st.markdown("### Week 3: Build a small project")
        st.write(
            f"Create a beginner-level project related to {domain}. "
            "Focus on applying what you have learned."
        )

        st.markdown("### Week 4: Review and improve")
        st.write(
            "Review your progress, identify weak areas, and improve your project."
        )

        st.info(
            "Tip: Study consistently and adjust the roadmap according to your "
            "available time and progress."
        )
