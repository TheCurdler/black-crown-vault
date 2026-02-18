import streamlit as st
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Black Crown Vault", page_icon="👑", layout="centered")

# ---------------- SESSION STATE ----------------
if "stage" not in st.session_state:
    st.session_state.stage = "landing"

if "player" not in st.session_state:
    st.session_state.player = ""

if "team" not in st.session_state:
    st.session_state.team = ""

# ---------------- STYLING + MOUSE REACTIVE BG ----------------
st.markdown("""
<style>

.stApp {
    background-color: #0b0b0b;
    color: #00ff88;
    font-family: monospace;
    text-align: center;
    overflow: hidden;
}

/* Mouse reactive glow */
.mouse-glow {
    position: fixed;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(0,255,136,0.15) 0%, rgba(0,0,0,0) 70%);
    border-radius: 50%;
    pointer-events: none;
    transform: translate(-50%, -50%);
    z-index: -1;
}

/* Buttons */
.stButton>button {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
    padding: 10px 25px;
}

/* Inputs */
.stTextInput>div>div>input {
    background-color: black;
    color: #00ff88;
    border: 1px solid #00ff88;
}

/* Fade animation */
.fade-in {
    animation: fadeIn 1.5s ease forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0px); }
}

/* Vault door split */
.vault-container {
    position: relative;
    width: 300px;
    height: 200px;
    margin: auto;
}

.vault-door-left,
.vault-door-right {
    position: absolute;
    width: 50%;
    height: 100%;
    background: #111;
    border: 2px solid #00ff88;
    animation-duration: 2s;
    animation-fill-mode: forwards;
}

.vault-door-left {
    left: 0;
    animation-name: openLeft;
}

.vault-door-right {
    right: 0;
    animation-name: openRight;
}

@keyframes openLeft {
    to { transform: translateX(-150px); opacity: 0; }
}

@keyframes openRight {
    to { transform: translateX(150px); opacity: 0; }
}

.message-box {
    border: 1px solid #00ff88;
    padding: 20px;
    margin-top: 20px;
}

</style>

<div class="mouse-glow" id="glow"></div>

<script>
document.addEventListener("mousemove", function(e) {
    var glow = document.getElementById("glow");
    glow.style.left = e.clientX + "px";
    glow.style.top = e.clientY + "px";
});
</script>
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

# ---------------- STAGE 1: LANDING ----------------
if st.session_state.stage == "landing":

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("THE BLACK CROWN")
    st.write("Access to the Inner Circle is restricted.")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("ENTER THE VAULT"):
        time.sleep(1)
        st.session_state.stage = "login"
        st.rerun()

# ---------------- STAGE 2: LOGIN ----------------
elif st.session_state.stage == "login":

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🔐 VAULT AUTHENTICATION")
    st.write("Dual authentication required.")
    st.markdown('</div>', unsafe_allow_html=True)

    team_input = st.text_input("ENTER TEAM CODENAME")
    player_input = st.text_input("ENTER PLAYER NAME")

    if st.button("INITIATE ACCESS"):

        team_input = team_input.strip().upper()
        player_input = player_input.strip().title()

        with st.spinner("Decrypting credentials..."):
            time.sleep(2)

        if team_input in teams and player_input in teams[team_input]["players"]:
            st.session_state.stage = "vault"
            st.session_state.player = player_input
            st.session_state.team = team_input
            st.rerun()
        else:
            st.error("✖ SECURITY BREACH DETECTED")

# ---------------- STAGE 3: VAULT OPENING ----------------
elif st.session_state.stage == "vault":

    st.markdown("""
    <div class="vault-container">
        <div class="vault-door-left"></div>
        <div class="vault-door-right"></div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)

    st.title("ACCESS GRANTED")

    st.markdown(f"""
    <div class="message-box">
    <h2>Welcome {st.session_state.player} of the Circle of {st.session_state.team}</h2>
    <p>The Black Crown recognizes your allegiance.</p>
    <p>May your strategy be ruthless and your reasoning flawless.</p>
    <p><strong>Good luck.</strong></p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("CLASSIFIED INTEL")
    st.code(teams[st.session_state.team]["hint"])
