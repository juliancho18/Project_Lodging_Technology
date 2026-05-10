import streamlit as st

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="My Technology",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================================
# CSS
# ======================================================

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================================================
# NAVBAR
# ======================================================

col1, col2, col3, col4 = st.columns([2,1,1,1])

with col1:
    st.image("assets/logo.png", width=180)

with col2:
    st.markdown("<div class='nav-btn'>Home</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='nav-btn'>About</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='nav-btn'>Contact</div>", unsafe_allow_html=True)

st.divider()

# ======================================================
# HERO SECTION
# ======================================================

left, right = st.columns(2)

with left:

    st.markdown("""
    <div class='hero-title'>
    EFFECTIVE.<br>
    RELIABLE.<br>
    MODERN.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='hero-text'>
    Smart technology solutions for modern businesses.
    Reduce costs, automate processes and improve efficiency.
    </div>
    """, unsafe_allow_html=True)

    st.button("Learn More")

with right:
    st.image("assets/hero.jpeg")

# ======================================================
# FEATURES
# ======================================================

st.markdown("<h2 class='section-title'>Our Services</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='card'>
        <h3>Automation</h3>
        <p>Automated intelligent systems.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
        <h3>Analytics</h3>
        <p>Real time dashboards and reports.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='card'>
        <h3>AI Vision</h3>
        <p>Computer vision and image analysis.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# CTA
# ======================================================

st.markdown("""
<div class='cta'>
    <h1>Ready to modernize your company?</h1>
</div>
""", unsafe_allow_html=True)

st.button("Contact Us")

# ======================================================
# FOOTER
# ======================================================

st.divider()

st.markdown("""
<div class='footer'>
© 2026 My Technology
</div>
""", unsafe_allow_html=True)