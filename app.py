import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# ======================================================
# CONFIGURACIÓN STREAMLIT
# ======================================================

st.set_page_config(
    page_title="Lodging Technology",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================================
# RUTAS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

LOGO = ASSETS_DIR / "logo.png"
HERO = ASSETS_DIR / "hero.png"
HOTEL = ASSETS_DIR / "hotel.png"
HVAC = ASSETS_DIR / "hvac.png"
ROOM_TECH = ASSETS_DIR / "room-tech.png"

# ======================================================
# FUNCIONES
# ======================================================

def image_to_base64(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


# ======================================================
# VALIDACIONES
# ======================================================

if not ASSETS_DIR.exists():
    st.error("No existe la carpeta 'assets'. Debe estar junto al archivo app.py.")
    st.stop()

required_images = [LOGO, HERO, HOTEL, HVAC, ROOM_TECH]
missing_images = [img.name for img in required_images if not img.exists()]

if missing_images:
    st.error("Faltan estas imágenes dentro de la carpeta assets: " + ", ".join(missing_images))
    st.stop()

logo_img = image_to_base64(LOGO)
hero_img = image_to_base64(HERO)
hotel_img = image_to_base64(HOTEL)
hvac_img = image_to_base64(HVAC)
room_img = image_to_base64(ROOM_TECH)

# ======================================================
# CSS PARA LIMPIAR STREAMLIT EXTERNO
# ======================================================

st.markdown(
    """
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        .stApp {
            background: #020b0f;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================================================
# HTML COMPLETO
# ======================================================

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg-dark: #020b0f;
    --bg-deep: #041d24;
    --green: #68f279;
    --green-strong: #1ee66e;
    --blue: #2daeff;
    --text-main: #ffffff;
    --text-soft: #d9ebe6;
    --text-muted: #9fb5ad;
    --glass: rgba(255,255,255,0.08);
    --glass-border: rgba(255,255,255,0.16);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Inter', sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    background:
        radial-gradient(circle at top left, rgba(0, 255, 132, 0.18), transparent 30%),
        radial-gradient(circle at top right, rgba(0, 123, 255, 0.16), transparent 34%),
        linear-gradient(135deg, #020b0f 0%, #041d24 45%, #020509 100%);
    color: white;
    overflow-x: hidden;
}

.page {
    width: 100%;
    min-height: 100vh;
    padding: 34px 48px 48px 48px;
}

/* ==============================
   NAVBAR
============================== */

.navbar {
    max-width: 1480px;
    margin: 0 auto 42px auto;
    position: sticky;
    top: 20px;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 28px;
    padding: 22px 30px;
    border-radius: 28px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.16);
    backdrop-filter: blur(22px);
    box-shadow: 0 20px 70px rgba(0,0,0,0.38);
}

.brand-wrap {
    display: flex;
    align-items: center;
    gap: 15px;
}

.brand-logo-box {
    width: 58px;
    height: 58px;
    border-radius: 16px;
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.14);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.brand-logo {
    width: 48px;
    height: 48px;
    object-fit: contain;
}

.brand {
    font-size: 29px;
    font-weight: 900;
    letter-spacing: -1.2px;
    color: white;
    white-space: nowrap;
}

.brand span {
    color: var(--green);
}

.navlinks {
    display: flex;
    align-items: center;
    gap: 24px;
    flex-wrap: wrap;
    justify-content: flex-end;
}

.navlinks a {
    color: #d9ebe6;
    text-decoration: none;
    font-size: 15px;
    font-weight: 800;
    transition: all 0.25s ease;
}

.navlinks a:hover {
    color: var(--green);
}

/* ==============================
   HERO
============================== */

.hero {
    max-width: 1480px;
    margin: 0 auto;
    min-height: 720px;
    position: relative;
    overflow: hidden;
    border-radius: 42px;
    padding: 92px 82px;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 40px 120px rgba(0,0,0,0.55);
    background:
        linear-gradient(90deg, rgba(2,8,12,0.97), rgba(4,38,36,0.82), rgba(0,0,0,0.36)),
        url("__HERO_IMAGE__");
    background-size: cover;
    background-position: center;
}

.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
    background-size: 46px 46px;
    mask-image: linear-gradient(to bottom, rgba(0,0,0,.85), transparent 90%);
    pointer-events: none;
}

.hero-content {
    position: relative;
    z-index: 5;
    max-width: 790px;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 13px 23px;
    border-radius: 999px;
    background: rgba(104,242,121,0.14);
    border: 1px solid rgba(104,242,121,0.48);
    color: #b5ffbe;
    font-weight: 900;
    font-size: 15px;
    margin-bottom: 34px;
    box-shadow: 0 0 36px rgba(104,242,121,.18);
}

.hero-title {
    font-size: clamp(56px, 6vw, 92px);
    line-height: 0.98;
    font-weight: 900;
    letter-spacing: -4px;
    color: white;
}

.hero-title span {
    color: var(--green);
    text-shadow: 0 0 28px rgba(104,242,121,.28);
}

.hero-subtitle {
    margin-top: 32px;
    font-size: 23px;
    line-height: 1.68;
    color: #d9ebe6;
    max-width: 760px;
}

.hero-actions {
    margin-top: 46px;
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
}

.btn-primary,
.btn-secondary {
    display: inline-block;
    text-decoration: none;
    padding: 18px 34px;
    border-radius: 18px;
    font-weight: 900;
    transition: all .28s ease;
}

.btn-primary {
    background: linear-gradient(135deg, #1ee66e, #7df252);
    color: #03130b;
    box-shadow: 0 18px 44px rgba(69,255,120,.28);
}

.btn-primary:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 24px 64px rgba(69,255,120,.45);
}

.btn-secondary {
    color: white;
    border: 1px solid rgba(255,255,255,0.30);
    background: rgba(255,255,255,0.11);
}

.btn-secondary:hover {
    transform: translateY(-4px);
    border-color: rgba(104,242,121,.75);
}

.orb {
    position: absolute;
    right: 120px;
    top: 95px;
    width: 205px;
    height: 205px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(104,242,121,.54), rgba(0,140,255,.05));
    animation: floatOne 7s ease-in-out infinite;
    z-index: 2;
}

.orb2 {
    position: absolute;
    right: 360px;
    bottom: 120px;
    width: 118px;
    height: 118px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(45,174,255,.56), rgba(255,255,255,.05));
    animation: floatTwo 8s ease-in-out infinite;
    z-index: 2;
}

.scan-line {
    position: absolute;
    width: 430px;
    height: 2px;
    right: 130px;
    top: 265px;
    background: linear-gradient(90deg, transparent, #68f279, transparent);
    animation: scan 3.5s linear infinite;
    z-index: 2;
}

@keyframes floatOne {
    0%,100% { transform: translateY(0) translateX(0); }
    50% { transform: translateY(35px) translateX(-22px); }
}

@keyframes floatTwo {
    0%,100% { transform: translateY(0) translateX(0); }
    50% { transform: translateY(-26px) translateX(35px); }
}

@keyframes scan {
    0% { opacity: .15; transform: translateX(-60px); }
    50% { opacity: 1; }
    100% { opacity: .15; transform: translateX(60px); }
}

/* ==============================
   SECTIONS
============================== */

.section {
    max-width: 1480px;
    margin: 0 auto;
}

.section-title {
    text-align: center;
    font-size: clamp(34px, 4vw, 50px);
    font-weight: 900;
    margin-top: 90px;
    margin-bottom: 18px;
    letter-spacing: -1.4px;
}

.section-text {
    text-align: center;
    color: #c3d8d2;
    font-size: 19px;
    max-width: 980px;
    margin: 0 auto 54px auto;
    line-height: 1.82;
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}

.card {
    min-height: 292px;
    padding: 34px;
    border-radius: 30px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 22px 70px rgba(0,0,0,0.28);
    transition: all .30s ease;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: "";
    position: absolute;
    inset: -1px;
    background: linear-gradient(135deg, rgba(104,242,121,.24), transparent 42%, rgba(0,140,255,.22));
    opacity: 0;
    transition: .3s ease;
}

.card:hover::before {
    opacity: 1;
}

.card:hover {
    transform: translateY(-10px);
    border-color: rgba(104,242,121,0.65);
}

.card-content {
    position: relative;
    z-index: 2;
}

.card-icon {
    font-size: 44px;
    margin-bottom: 20px;
}

.card h3 {
    font-size: 25px;
    margin-bottom: 14px;
}

.card p {
    font-size: 16.5px;
    line-height: 1.72;
    color: #d5e5df;
}

/* ==============================
   IMAGE GALLERY
============================== */

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 28px;
}

.visual-card {
    border-radius: 30px;
    overflow: hidden;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 24px 80px rgba(0,0,0,0.32);
    transition: all .3s ease;
}

.visual-card:hover {
    transform: translateY(-9px);
    border-color: rgba(104,242,121,.6);
}

.visual-image {
    width: 100%;
    height: 280px;
    object-fit: cover;
    display: block;
}

.visual-body {
    padding: 28px;
}

.visual-body h3 {
    color: var(--green);
    font-size: 25px;
    margin-bottom: 12px;
}

.visual-body p {
    color: #d5e5df;
    font-size: 16.5px;
    line-height: 1.78;
}

/* ==============================
   PRODUCT
============================== */

.product-box {
    margin-top: 84px;
    padding: 66px;
    border-radius: 40px;
    background:
        radial-gradient(circle at top right, rgba(104,242,121,.20), transparent 36%),
        linear-gradient(135deg, rgba(4,45,48,.96), rgba(7,89,58,.86));
    border: 1px solid rgba(255,255,255,0.16);
    box-shadow: 0 30px 95px rgba(0,0,0,.36);
}

.product-grid {
    display: grid;
    grid-template-columns: 1.15fr .85fr;
    gap: 44px;
    align-items: center;
}

.product-title {
    font-size: clamp(34px, 4vw, 50px);
    font-weight: 900;
    margin-bottom: 26px;
}

.product-title span {
    color: var(--green);
}

.product-text {
    font-size: 19px;
    line-height: 1.9;
    color: #d9ebe6;
}

.tech-panel {
    padding: 36px;
    border-radius: 30px;
    background: rgba(0,0,0,.22);
    border: 1px solid rgba(255,255,255,.15);
}

.tech-row {
    display: flex;
    justify-content: space-between;
    gap: 22px;
    padding: 13px 0;
    border-bottom: 1px solid rgba(255,255,255,.09);
    color: #d9ebe6;
    font-size: 16px;
}

.tech-row:last-child {
    border-bottom: none;
}

.tech-value {
    color: var(--green);
    font-weight: 900;
    text-align: right;
}

/* ==============================
   METRICS
============================== */

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
}

.metric-box {
    text-align: center;
    padding: 40px 24px;
    border-radius: 30px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.14);
    transition: .3s ease;
}

.metric-box:hover {
    transform: translateY(-8px);
    border-color: rgba(104,242,121,.65);
}

.metric-number {
    font-size: 48px;
    font-weight: 900;
    color: var(--green);
    margin-bottom: 10px;
}

.metric-label {
    font-size: 16px;
    color: #d5e8e2;
}

/* ==============================
   APPLICATIONS
============================== */

.apps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 26px;
}

.app-box {
    padding: 32px;
    border-radius: 30px;
    background: rgba(255,255,255,.075);
    border: 1px solid rgba(255,255,255,.14);
    min-height: 245px;
}

.app-box h3 {
    color: var(--green);
    font-size: 25px;
    margin-bottom: 18px;
}

.app-box ul {
    color: #d5e5df;
    line-height: 1.9;
    font-size: 16px;
    padding-left: 18px;
}

/* ==============================
   NOVA STATIC SECTION
============================== */

.nova-box {
    margin-top: 84px;
    padding: 48px;
    border-radius: 38px;
    background:
        radial-gradient(circle at top left, rgba(0,140,255,.20), transparent 36%),
        linear-gradient(135deg, rgba(255,255,255,.08), rgba(255,255,255,.035));
    border: 1px solid rgba(255,255,255,.15);
    box-shadow: 0 28px 90px rgba(0,0,0,.30);
}

.nova-title {
    font-size: 38px;
    font-weight: 900;
    margin-bottom: 14px;
}

.nova-title span {
    color: var(--green);
}

.nova-text {
    color: #cfe1dc;
    font-size: 18px;
    line-height: 1.75;
    max-width: 1080px;
}

.nova-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 26px;
}

.nova-tag {
    padding: 11px 17px;
    border-radius: 999px;
    background: rgba(104,242,121,0.12);
    border: 1px solid rgba(104,242,121,0.32);
    color: #b5ffbe;
    font-size: 14px;
    font-weight: 800;
}

/* ==============================
   CTA FOOTER
============================== */

.cta {
    text-align: center;
    padding: 86px 42px;
    margin-top: 84px;
    border-radius: 40px;
    background:
        radial-gradient(circle at top, rgba(104,242,121,.25), transparent 38%),
        linear-gradient(135deg, #061d24, #0d4434);
    border: 1px solid rgba(255,255,255,.15);
    box-shadow: 0 28px 86px rgba(0,0,0,.35);
}

.cta h1 {
    font-size: clamp(34px, 4vw, 52px);
    font-weight: 900;
    margin-bottom: 20px;
    letter-spacing: -1.3px;
}

.cta p {
    font-size: 20px;
    color: #d4e8e1;
    line-height: 1.7;
    max-width: 920px;
    margin: 0 auto;
}

.footer {
    text-align: center;
    padding: 42px;
    color: #9fb5ad;
    font-size: 15px;
}

/* ==============================
   RESPONSIVE
============================== */

@media (max-width: 1180px) {
    .cards-grid,
    .gallery-grid,
    .metrics-grid,
    .apps-grid {
        grid-template-columns: 1fr 1fr;
    }

    .product-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 850px) {
    .page {
        padding: 22px 18px 34px 18px;
    }

    .navbar {
        flex-direction: column;
        align-items: flex-start;
    }

    .navlinks {
        justify-content: flex-start;
    }

    .hero {
        padding: 62px 34px;
        min-height: 650px;
    }

    .hero-title {
        letter-spacing: -2px;
    }

    .cards-grid,
    .gallery-grid,
    .metrics-grid,
    .apps-grid {
        grid-template-columns: 1fr;
    }

    .tech-row {
        flex-direction: column;
    }
}
</style>
</head>

<body>
<div class="page">

    <nav class="navbar">
        <div class="brand-wrap">
            <div class="brand-logo-box">
                <img class="brand-logo" src="__LOGO_IMAGE__" alt="Lodging Technology Logo">
            </div>
            <div class="brand">Lodging <span>Technology</span></div>
        </div>

        <div class="navlinks">
            <a href="#home">Home</a>
            <a href="#solutions">Solutions</a>
            <a href="#gallery">Technology</a>
            <a href="#gemlink">GEM Link®</a>
            <a href="#applications">Applications</a>
            <a href="#nova">NOVA</a>
        </div>
    </nav>

    <section class="hero" id="home">
        <div class="orb"></div>
        <div class="orb2"></div>
        <div class="scan-line"></div>

        <div class="hero-content">
            <div class="badge">● Intelligent Hospitality Automation</div>

            <div class="hero-title">
                Effective.<br>
                Reliable.<br>
                <span>Versatile.</span>
            </div>

            <div class="hero-subtitle">
                Wireless guest-room technology designed to improve comfort, reduce unnecessary HVAC consumption
                and support measurable operational savings for modern lodging environments.
            </div>

            <div class="hero-actions">
                <a class="btn-primary" href="#gemlink">Explore GEM Link®</a>
                <a class="btn-secondary" href="#nova">View NOVA Concept</a>
            </div>
        </div>
    </section>

    <section class="section" id="solutions">
        <h2 class="section-title">Smart Technology for Lodging Environments</h2>
        <p class="section-text">
            Lodging Technology provides intelligent wireless systems for hospitality operators who need practical automation,
            reliable room control and energy-focused performance without compromising guest comfort.
        </p>

        <div class="cards-grid">
            <div class="card">
                <div class="card-content">
                    <div class="card-icon">📊</div>
                    <h3>Effective</h3>
                    <p>Helps reduce HVAC and appliance-related energy costs while supporting lower carbon emissions and operational efficiency.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-content">
                    <div class="card-icon">🔋</div>
                    <h3>Reliable</h3>
                    <p>Designed for long-term operation with low intervention, durable battery life and fail-safe functionality.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-content">
                    <div class="card-icon">💡</div>
                    <h3>Versatile</h3>
                    <p>Connects with multiple HVAC configurations, including PTACs, split systems, fan coil units and electric heaters.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-content">
                    <div class="card-icon">🛠️</div>
                    <h3>Support</h3>
                    <p>Built around practical deployment, technical support and long-term system value for hospitality operators.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="gallery">
        <h2 class="section-title">Technology in Action</h2>
        <p class="section-text">
            Explore the operational environment, the HVAC focus and the room-level technology that support modern lodging automation.
        </p>

        <div class="gallery-grid">
            <div class="visual-card">
                <img class="visual-image" src="__HOTEL_IMAGE__" alt="Hospitality Environment">
                <div class="visual-body">
                    <h3>Hospitality Environment</h3>
                    <p>
                        Designed for hotels, lodging properties and hospitality operators that want a better guest experience,
                        smarter room operation and improved energy awareness.
                    </p>
                </div>
            </div>

            <div class="visual-card">
                <img class="visual-image" src="__HVAC_IMAGE__" alt="HVAC Intelligence">
                <div class="visual-body">
                    <h3>HVAC Intelligence</h3>
                    <p>
                        Focused on HVAC optimization through occupancy-based control, intelligent temperature recovery
                        and practical energy conservation logic.
                    </p>
                </div>
            </div>

            <div class="visual-card">
                <img class="visual-image" src="__ROOM_IMAGE__" alt="Room-Level Technology">
                <div class="visual-body">
                    <h3>Room-Level Technology</h3>
                    <p>
                        Wireless room technology that helps deliver comfort, automation, reliability and lower unnecessary
                        energy consumption at the room level.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="gemlink">
        <div class="product-box">
            <div class="product-grid">
                <div>
                    <div class="product-title">GEM Link<sup>®</sup> <span>Wireless</span></div>

                    <div class="product-text">
                        GEM Link<sup>®</sup> Wireless automatically determines the physical presence of guests by detecting
                        infrared body heat instead of motion. This enables a more precise room experience while allowing
                        guests to maintain complete control of the room temperature while present.
                        <br><br>
                        When the room becomes unoccupied, the system resets the temperature to energy-conserving levels
                        previously selected by management. This helps reduce wasteful HVAC consumption, improve operating
                        efficiency and support a more sustainable lodging strategy.
                    </div>

                    <br>
                    <a class="btn-primary" href="#applications">View Applications</a>
                </div>

                <div class="tech-panel">
                    <div class="tech-row"><span>Presence detection</span><span class="tech-value">Infrared body heat</span></div>
                    <div class="tech-row"><span>Guest experience</span><span class="tech-value">Comfort-first</span></div>
                    <div class="tech-row"><span>Installation model</span><span class="tech-value">Wireless</span></div>
                    <div class="tech-row"><span>Energy focus</span><span class="tech-value">HVAC optimization</span></div>
                    <div class="tech-row"><span>Operational model</span><span class="tech-value">Low intervention</span></div>
                    <div class="tech-row"><span>Target environment</span><span class="tech-value">Hotels & lodging</span></div>
                </div>
            </div>
        </div>
    </section>

    <section class="section">
        <h2 class="section-title">Designed for Measurable Impact</h2>
        <p class="section-text">
            A professional and intelligent technology experience focused on comfort, energy performance,
            sustainability and long-term operational value.
        </p>

        <div class="metrics-grid">
            <div class="metric-box">
                <div class="metric-number">35–45%</div>
                <div class="metric-label">Potential HVAC energy reduction</div>
            </div>

            <div class="metric-box">
                <div class="metric-number">$250</div>
                <div class="metric-label">Estimated annual savings per room</div>
            </div>

            <div class="metric-box">
                <div class="metric-number">24</div>
                <div class="metric-label">Months or less simple payback</div>
            </div>
        </div>
    </section>

    <section class="section" id="applications">
        <h2 class="section-title">Applications</h2>
        <p class="section-text">
            GEM Link<sup>®</sup> Wireless is designed to support multiple operational scenarios inside modern hospitality facilities.
        </p>

        <div class="apps-grid">
            <div class="app-box">
                <h3>Reliable Operation</h3>
                <ul>
                    <li>Systems operating after 20+ years.</li>
                    <li>Two-year warranty approach.</li>
                    <li>Programmable features stored in non-volatile memory.</li>
                    <li>Fail-safe operation for HVAC continuity.</li>
                </ul>
            </div>

            <div class="app-box">
                <h3>Versatile Deployment</h3>
                <ul>
                    <li>Compatible with different HVAC ages and configurations.</li>
                    <li>Supports energy reduction for HVAC and lighting expenses.</li>
                    <li>Useful for PTACs, split systems and electric heaters.</li>
                    <li>Can support appliance control in selected lodging scenarios.</li>
                </ul>
            </div>

            <div class="app-box">
                <h3>Effective Savings</h3>
                <ul>
                    <li>Reduces HVAC and appliance energy expense.</li>
                    <li>Supports lower carbon footprint.</li>
                    <li>Helps improve room-level operational control.</li>
                    <li>Supports measurable return on investment.</li>
                </ul>
            </div>
        </div>
    </section>

    <section class="section" id="nova">
        <div class="nova-box">
            <div class="nova-title">Meet <span>NOVA StayTech</span></div>
            <div class="nova-text">
                NOVA StayTech is presented as a virtual assistant concept for Lodging Technology. It can support product communication,
                answer basic questions about GEM Link<sup>®</sup> Wireless, explain energy savings, describe HVAC optimization and guide
                hospitality operators through the value of intelligent room-level automation.
            </div>

            <div class="nova-tags">
                <span class="nova-tag">Energy savings</span>
                <span class="nova-tag">Guest comfort</span>
                <span class="nova-tag">Wireless installation</span>
                <span class="nova-tag">HVAC optimization</span>
                <span class="nova-tag">Hospitality automation</span>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="cta">
            <h1>Modernize every room with intelligent control.</h1>
            <p>
                Reliable wireless technology for hospitality environments that demand comfort,
                efficiency, sustainability and measurable performance.
            </p>
            <br><br>
            <a class="btn-primary" href="#home">Back to Top</a>
        </div>
    </section>

    <div class="footer">
        © 2026 Lodging Technology · Smart Hospitality Solutions · Powered by NOVA StayTech
    </div>

</div>
</body>
</html>
"""

html = (
    html_template
    .replace("__LOGO_IMAGE__", logo_img)
    .replace("__HERO_IMAGE__", hero_img)
    .replace("__HOTEL_IMAGE__", hotel_img)
    .replace("__HVAC_IMAGE__", hvac_img)
    .replace("__ROOM_IMAGE__", room_img)
)

components.html(
    html,
    height=5400,
    scrolling=False
)