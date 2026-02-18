import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Black Crown Vault",
    page_icon="👑",
    layout="centered"
)

# ---------------- STYLING + ANIMATIONS ----------------
st.markdown("""
<style>

/* General App Styling */
.stApp {
    background-color: #0b0b0b;
    color: #00ff88;
    font-family: monospace;
}

/* Rotating Crown Background */
.crown-bg {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 600px;
    transform: translate(-50%, -50%);
    opacity: 0.05;
    z-index: -1;
    animation: rotateCrown 40s linear infinite;
}

@keyframes rotateCrown {
    from { transform: translate(-50%, -50%) rotate(0deg); }
    to { transform: translate(-50%, -50%) rotate(360deg); }
}

/* Headings */
h1, h2, h3 {
    text-align: center;
    color: #00ff88;
}

/* Input Styling */
.stTextInput>div>div>input {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
}

/* Button Styling */
.stButton>button {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
}

/* Vault Door Animation */
.vault-door {
    width: 200px;
    height: 200px;
    margin: auto;
    border-radius: 50%;
    border: 4px solid #00ff88;
    animation: openVault 2s forwards;
}

@keyframes openVault {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.2); }
    100% { transform: scale(5); opacity: 0; }
}

/* Welcome Box */
.message-box {
    border: 1px solid #00ff88;
    padding: 20px;
    margin-top: 20px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- ROTATING CROWN IMAGE ----------------
st.markdown("""
<div class="crown-bg">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Crown_icon_black.svg/1024px-Crown_icon_black.svg.png" width="100%">
</div>
""", unsafe_allow_html=True)

# ---------------- DATABASE ----------------
teams = {
    "OMERTA": {
        "players": ["Asmita", "Taru", "Samit", "Satvik", "Pradnya"],
        "hint": "... --- -- . - .... .. -. --."
    },
    "CARMORA": {
        "players": ["Vinayak", "Mansimar", "Kunal", "Vedant", "Vanessa", "Sanchit"],
        "hint": "- .... . / .--. .-.. . .-"
    },
    "STRADA NERA": {
        "players": ["Mohit", "Kartik", "Suryansh", "Srishti", "Aman", "Harbaksh"],
        "hint": ".- .-.. .. -... .."
    },
    "VASTANO": {
        "players": ["Drishti", "Suryanshi", "Suhani", "Karishma", "Parth", "Aditya"],
        "hint": "- .-. ..- ... -"
    },
    "LA SIERRA": {
        "players": ["Avani", "Aviral", "Kanishka", "Samarth", "Bhaskar", "Vidyanshi"],
        "hint": "... . -.-. .-. . -"
    },
    "KUROKAI": {
        "players": ["Rudraans", "Farhan", "Tanjot", "Anima", "Kashvi"],
        "hint": ".--. .-.. .- -."
    }
}

# ---------------- SESSION STATE ----------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "player" not in st.session_state:
    st.session_state.player = ""
if "team" not in st.session_state:
    st.session_state.team = ""

# ---------------- LOGIN PAGE ----------------
if not st.session_state.authenticated:

    st.title("🔐 BLACK CROWN VAULT")
    st.write("Dual authentication required to access the Inner Circle.")

    team_input = st.text_input("ENTER TEAM CODENAME")
    player_input = st.text_input("ENTER PLAYER NAME")

    if st.button("INITIATE ACCESS"):

        team_input = team_input.strip().upper()
        player_input = player_input.strip().title()

        with st.spinner("Validating credentials..."):
            time.sleep(2)

        if team_input in teams and player_input in teams[team_input]["players"]:
            st.session_state.authenticated = True
            st.session_state.player = player_input
            st.session_state.team = team_input
            st.rerun()
        else:
            st.error("✖ SECURITY BREACH DETECTED")

# ---------------- VAULT WELCOME PAGE ----------------
else:

    # Vault opening animation
    st.markdown('<div class="vault-door"></div>', unsafe_allow_html=True)
    time.sleep(2)

    st.title("ACCESS GRANTED")

    st.markdown(f"""
    <div class="message-box">
    <h2>Welcome {st.session_state.player} of the Circle of {st.session_state.team}</h2>
    <p>The Black Crown acknowledges your allegiance.</p>
    <p>May your logic be lethal and your arguments undeniable.</p>
    <p><strong>Good luck in the battle that awaits.</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("CLASSIFIED INTEL")
    st.code(teams[st.session_state.team]["hint"])