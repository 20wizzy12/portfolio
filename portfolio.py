import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Wizzy's Portfolio ⚡",
    page_icon="⚡",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    /* Background */
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: transparent;
    }

    /* Headers (high contrast + large font) */
    h1 {
        color: #FFD700 !important;
        font-size: 2.5em !important;
        font-weight: 800 !important;
        text-align: center;
    }
    h2 {
        color: #ffcc00 !important;
        font-size: 1.8em !important;
        font-weight: 700 !important;
    }
    h3 {
        color: #ffffff !important;
        font-size: 1.3em !important;
        font-weight: 600 !important;
    }

    /* Links */
    a {
        color: #00ffcc !important;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.1em;
    }
    a:hover {
        text-decoration: underline;
        color: #00ffaa !important;
    }

    /* Card Style (accessible padding + contrast) */
    .card {
        padding: 25px;
        border-radius: 15px;
        background: #2d2d44;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        line-height: 1.6;
    }

    /* Paragraphs (more readable size + line spacing) */
    p, li, div, span {
        font-size: 1.05em;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------
st.title("⚡ Wizzy's Portfolio")
st.subheader("Football fan | Student | Aspiring Developer")
st.markdown("---")

# ---------------- ABOUT ----------------
st.header("👋 About Me")
st.write("""
Yo! I'm **Wisdom** — curious, playful, and always experimenting.  
I build apps, chatbots, and random projects — but with a **savage + fun twist**.  
Not here for the boring corporate vibes.  
I want my creations to feel **youthful, alive, and actually fun** to use. 🚀
""")
st.markdown("---")

# ---------------- PROJECTS ----------------
st.header("🚀 Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><h3>💬 AI Chatbot</h3></div>', unsafe_allow_html=True)
    st.write("An intelligent companion for guidance, learning, and everyday support.")
    st.markdown("[👉 Try It](https://11chatbot.streamlit.app)")

with col2:
    st.markdown('<div class="card"><h3>🔒 Secure Chat App</h3></div>', unsafe_allow_html=True)
    st.write("End-to-end chatting built with SQLite + Streamlit UI. 🔐")

st.markdown("---")

# ---------------- CONTACT ----------------
st.header("📫 Contact Me")
st.write("Hit me up if you vibe with my work!")

st.write("📞 **Phone:** 08033600585")  

# ✅ FORCE EMAIL TO OPEN (HTML Anchor Tag)
st.markdown(
    '<p>📧 <strong>Email:</strong> <a href="mailto:wisdomgodsonezeakachi@gmail.com">wisdomgodsonezeakachi@gmail.com</a></p>',
    unsafe_allow_html=True
)

# ✅ GITHUB LINK (also as HTML for consistency)
st.markdown(
    '<p>🌐 <strong>GitHub:</strong> <a href="https://github.com/20wizzy12" target="_blank">github.com/20wizzy12</a></p>',
    unsafe_allow_html=True
)


# 🎈 Fun effect
st.balloons()
