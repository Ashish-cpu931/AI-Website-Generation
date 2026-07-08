import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="AI Career Hub Pro",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

.stApp{
background: linear-gradient(-45deg,#0f172a,#1e3a8a,#7c3aed,#ec4899);
background-size:400% 400%;
animation:gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.hero{
background:rgba(255,255,255,0.12);
backdrop-filter:blur(15px);
padding:50px;
border-radius:25px;
text-align:center;
box-shadow:0 8px 32px rgba(0,0,0,0.4);
margin-bottom:20px;
}

.glass{
background:rgba(255,255,255,0.12);
backdrop-filter:blur(15px);
padding:20px;
border-radius:20px;
box-shadow:0 8px 32px rgba(0,0,0,0.3);
margin-bottom:20px;
}

.feature-card{
background:rgba(255,255,255,0.1);
padding:20px;
border-radius:15px;
text-align:center;
transition:0.4s;
}

.feature-card:hover{
transform:translateY(-8px);
}

.footer{
text-align:center;
padding:30px;
font-size:18px;
}

h1,h2,h3,h4{
color:white !important;
}

[data-testid="stMetric"]{
background:rgba(255,255,255,0.12);
padding:15px;
border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class='hero'>
<h1>🚀 AI Career Hub Pro</h1>
<h3>Future Ready Learning Platform Powered by Artificial Intelligence</h3>
<p>Learn • Build • Get Hired • Grow</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "🛣 Career Roadmap",
        "📊 Analytics",
        "💬 AI Assistant",
        "🏆 Achievements",
        "📞 Contact"
    ]
)

# ==========================
# HOME
# ==========================

if page == "🏠 Home":

    st.header("📈 Platform Statistics")

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("Students", "5,000+", "+450")

    with col2:
        st.metric("Projects", "850+", "+60")

    with col3:
        st.metric("Placements", "1,200+", "+90")

    with col4:
        st.metric("Success Rate", "98%", "+2%")

    st.markdown("---")

    st.header("🔥 Features")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class='feature-card'>
        <h3>🤖 AI Learning</h3>
        <p>Learn AI & Machine Learning through practical projects.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='feature-card'>
        <h3>📄 Resume Review</h3>
        <p>Get ATS optimization suggestions instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='feature-card'>
        <h3>💼 Career Guidance</h3>
        <p>Personalized roadmaps for your dream career.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================
# RESUME ANALYZER
# ==========================

elif page == "📄 Resume Analyzer":

    st.header("📄 AI Resume Analyzer")

    file = st.file_uploader(
        "Upload Resume",
        type=["pdf","docx"]
    )

    if file:

        score = random.randint(75,98)

        st.success("Resume Uploaded Successfully")

        st.subheader("ATS Score")

        st.progress(score/100)

        st.metric("ATS Score", f"{score}%")

        st.markdown("### Skills Detected")

        st.success("✔ Python")
        st.success("✔ Machine Learning")
        st.success("✔ SQL")
        st.success("✔ Data Analytics")

        if score > 90:
            st.balloons()

# ==========================
# ROADMAP
# ==========================

elif page == "🛣 Career Roadmap":

    st.header("🛣 AI Career Roadmap Generator")

    career = st.selectbox(
        "Choose Career Path",
        [
            "AI Engineer",
            "Data Scientist",
            "Machine Learning Engineer",
            "Full Stack Developer",
            "Cyber Security Analyst"
        ]
    )

    if st.button("Generate Roadmap"):

        st.success(f"Career Roadmap for {career}")

        roadmap = {
            "AI Engineer":[
                "Python",
                "Statistics",
                "Machine Learning",
                "Deep Learning",
                "Generative AI",
                "MLOps",
                "AI Engineer"
            ],
            "Data Scientist":[
                "Python",
                "SQL",
                "Statistics",
                "Data Visualization",
                "Machine Learning",
                "Data Scientist"
            ],
            "Machine Learning Engineer":[
                "Python",
                "ML",
                "Deep Learning",
                "TensorFlow",
                "Deployment",
                "ML Engineer"
            ],
            "Full Stack Developer":[
                "HTML",
                "CSS",
                "JavaScript",
                "React",
                "Python",
                "Django",
                "Full Stack Developer"
            ],
            "Cyber Security Analyst":[
                "Networking",
                "Linux",
                "Security",
                "Ethical Hacking",
                "SOC",
                "Cyber Security Analyst"
            ]
        }

        for step in roadmap[career]:
            st.info(step)

# ==========================
# ANALYTICS
# ==========================

elif page == "📊 Analytics":

    st.header("📊 Industry Skill Demand")

    data = pd.DataFrame({
        "Skill":[
            "Python",
            "AI",
            "Machine Learning",
            "SQL",
            "Cloud",
            "Data Science",
            "Cyber Security"
        ],
        "Demand":[95,92,90,80,88,89,85]
    })

    fig = px.bar(
        data,
        x="Skill",
        y="Demand",
        title="Top Technology Skills Demand 2026"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    pie = px.pie(
        data,
        names="Skill",
        values="Demand",
        title="Technology Market Share"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

# ==========================
# AI ASSISTANT
# ==========================

elif page == "💬 AI Assistant":

    st.header("💬 AI Career Assistant")

    user_question = st.text_input(
        "Ask anything about Career, AI or Internships"
    )

    if user_question:

        st.chat_message("user").write(user_question)

        response = """
        Based on current industry trends:

        • Focus on Python
        • Learn Machine Learning
        • Build 5+ Projects
        • Create a Strong GitHub Profile
        • Apply for AI & Data Science Internships
        """

        st.chat_message("assistant").write(response)

# ==========================
# ACHIEVEMENTS
# ==========================

elif page == "🏆 Achievements":

    st.header("🏆 Achievement Dashboard")

    st.success("Python Master Badge")
    st.success("AI Explorer Badge")
    st.success("ML Practitioner Badge")
    st.success("Career Ready Badge")

    st.progress(0.85)

    st.write("Overall Learning Progress: 85%")

# ==========================
# CONTACT
# ==========================

elif page == "📞 Contact":

    st.header("📞 Contact Us")

    with st.form("contact"):

        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")

        submit = st.form_submit_button("Send")

        if submit:

            if name and email and msg:
                st.success("Message Sent Successfully 🚀")
            else:
                st.error("Please fill all fields.")

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown("""
<div class='footer'>
🚀 AI Career Hub Pro <br>
Built with Python • Streamlit • Plotly • Artificial Intelligence
</div>
""", unsafe_allow_html=True)
