import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Parikshitsinh Jadeja Portfolio",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Custom CSS ----
st.markdown("""
<style>
/* Global styles */
body {
    background-color: #0e1117;
    color: #ffffff;
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #FFD700;
}

section {
    padding: 50px 20px;
}

.stButton>button {
    background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
    color: #000;
    font-weight: 600;
    padding: 15px 25px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
}

.stButton>button:hover {
    background: linear-gradient(135deg, #FFA500 0%, #FFD700 100%);
    transform: translateY(-2px);
}

.project-card {
    background-color: #1c1f29;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
    border-left: 5px solid #FFD700;
}

.project-title {
    font-size: 24px;
    font-weight: 700;
    color: #FFD700;
}

.project-role, .project-dates {
    font-size: 14px;
    color: #aaa;
}

.project-desc {
    font-size: 16px;
    line-height: 1.6;
    color: #ddd;
}

.section-title {
    border-bottom: 2px solid #FFD700;
    display: inline-block;
    margin-bottom: 20px;
    font-size: 32px;
}
</style>
""", unsafe_allow_html=True)

# ---- Header ----
st.markdown("""
<div style="text-align:center; padding:50px 20px;">
    <h1>Parikshitsinh Jadeja</h1>
    <p style="font-size:22px; color:#FFD700;">Young Innovator | Robotics & AI Enthusiast</p>
</div>
""", unsafe_allow_html=True)

# ---- About Me ----
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
st.write("""
I am a young innovator focusing on **AI, Robotics, IoT**, and **sustainable solutions**.  
I love building advanced projects that combine **technology, environmental responsibility, and social impact**.
""")

# ---- Projects ----
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Project Qryptic",
        "role": "Team Lead, Ethical Encryptors",
        "dates": "Aug 2025 - Present",
        "desc": """
Developed a **quantum secure cyber defense system** for national-level simulated exam platforms.  
- Multi-layer security framework with decoy systems  
- Decentralized question bank with post-quantum encryption  
- Dynamic question randomization  
- Real-time monitoring & forensic logging
"""
    },
    {
        "title": "EcoCredit",
        "role": "",
        "dates": "Oct 2024 - Present",
        "desc": """
An **IoT-based waste credit system** that incentivizes recycling.  
- Smart machines track user contributions and award credits  
- Leaderboards & gamification boost engagement  
- Credits can be donated to environmental causes  
- Mobile app for tracking & rewards
"""
    },
    {
        "title": "EutroBot - World's First Autonomous Phytoremediation Robot",
        "role": "",
        "dates": "Oct 2024 - Present",
        "desc": """
Restores aquatic ecosystems using **AI-powered bioremediation**.  
- CV system detects harmful algal blooms  
- GPS navigation for autonomous movement  
- IoT monitoring of pH, turbidity, TDS  
- Bioremediation using water hyacinth, duckweed, microalgae  
- Circular waste management with bio-compost/biofuel
"""
    },
    {
        "title": "NeuroMove",
        "role": "",
        "dates": "",
        "desc": """
Affordable **robotic AI system** for assisting limb mobility in neurological patients.  
- Uses electrical stimulation & AI-guided motion  
- Low-cost sensors & open-source algorithms  
- Customizable for various neurological conditions  
- Smooth, safe, personalized assistance
"""
    },
    {
        "title": "Neurological Neural Networks (NNN) Engineering & Development",
        "role": "",
        "dates": "",
        "desc": """
Researching and prototyping new **computational frameworks inspired by neurological systems**  
to advance assistive technologies and AI applications.
"""
    },
]

for p in projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{p['title']}</div>
        <div class="project-role">{p['role']}</div>
        <div class="project-dates">{p['dates']}</div>
        <p class="project-desc">{p['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# ---- Skills ----
st.markdown('<h2 class="section-title">Skills & Tools</h2>', unsafe_allow_html=True)
st.write("""
- **Programming:** Python, C++, Arduino  
- **Technologies:** IoT, AI, Machine Learning, Robotics, Embedded Systems  
- **Tools:** Git, Figma, PCB Design, CAD, MATLAB
""")

# ---- Contact ----
st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
st.write("Feel free to reach out via email or check my GitHub & LinkedIn profiles.")

col1, col2 = st.columns(2)
with col1:
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Message")
    st.button("Send Message")
with col2:
    st.markdown("""
- **Email:** parikshitsinh@example.com  
- **GitHub:** [github.com/parikshitsinh](https://github.com/parikshitsinh)  
- **LinkedIn:** [linkedin.com/in/parikshitsinh](https://linkedin.com/in/parikshitsinh)
""")
