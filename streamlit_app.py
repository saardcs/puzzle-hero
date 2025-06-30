import streamlit as st
import qrcode
import io
import random
import math
from PIL import Image

st.set_page_config(page_title="Code Combinator & GCD Master", layout="centered")

char_pools = {
    'lowercase': 26,
    'uppercase': 26,
    'numbers': 10
}

LEVEL_IMAGES = [f"level{i}.webp" for i in range(3)]
RANKS = [
    "Novice Cipherer",   # 0–4
    "Puzzle Adept",      # 5–9
    "Master of Numbers"  # 10
]

# --- Session init ---
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.problem = None
    st.session_state.submitted = False
    st.session_state.correct = False
    st.session_state.user_answer = ""

# Sidebar with QR code
st.sidebar.header("Open this app on your mobile device")

qr_link = "https://puzzle-hero.streamlit.app"
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

st.sidebar.image(buf, width=300, caption=qr_link)

# --- Rank ---
def get_rank(score):
    if score >= 10:
        return RANKS[2], LEVEL_IMAGES[2]
    elif score >= 5:
        return RANKS[1], LEVEL_IMAGES[1]
    else:
        return RANKS[0], LEVEL_IMAGES[0]

# --- Combination Problem Generator ---
def generate_combination_problem():
    char_types = random.sample(list(char_pools.keys()), k=random.randint(1, 3))
    allow_repeat = random.choice([True, False])
    code_length = random.randint(3, 5)

    total_chars = sum(char_pools[c] for c in char_types)

    if allow_repeat:
        formula_parts = [str(total_chars)] * code_length
    else:
        formula_parts = [str(total_chars - i) for i in range(code_length)]

    return {
        "type": "combination",
        "char_types": char_types,
        "allow_repeat": allow_repeat,
        "code_length": code_length,
        "formula_parts": formula_parts
    }

# --- GCD Problem Generator (Fixed Version) ---
def generate_gcd_problem():
    gcd_val = random.randint(2, 15)

    # Ensure m and n are co-prime
    while True:
        m = random.randint(2, 10)
        n = random.randint(2, 10)
        if math.gcd(m, n) == 1:
            break

    a = gcd_val * m
    b = gcd_val * n

    return {
        "type": "gcd",
        "a": a,
        "b": b,
        "gcd": gcd_val
    }

# --- Generate New Problem based on score ---
def generate_problem():
    if st.session_state.score < 5:
        return generate_combination_problem()
    else:
        return generate_gcd_problem()

# --- Normalize function ---
def normalize_formula(s):
    return s.replace(" ", "").replace("*", "×").replace("x", "×")

# --- Load/Create Problem ---
if st.session_state.problem is None:
    st.session_state.problem = generate_problem()

rank, image_path = get_rank(st.session_state.score)
st.image(Image.open(image_path), width=100)
st.subheader(f"Rank: {rank} | Score: {st.session_state.score}/10")

# --- End of Game ---
if st.session_state.score >= 10:
    st.balloons()
    st.success("🏆 You’ve completed all challenges and reached Master of Numbers!")
    if st.button("🔁 Restart"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    st.stop()

# --- Display Problem ---
problem = st.session_state.problem

if problem["type"] == "combination":
    st.markdown(f"### Suppose that the {problem['code_length']}-character code has the following restrictions:")

    if "numbers" in problem["char_types"] and (
        "uppercase" in problem["char_types"] or "lowercase" in problem["char_types"]
    ):
        st.markdown("- Numbers and letters")
    elif set(problem["char_types"]) == {"numbers"}:
        st.markdown("- Numbers only")

    if "uppercase" in problem["char_types"] and "lowercase" in problem["char_types"]:
        st.markdown("- Uppercase and lowercase letters")
    elif "uppercase" in problem["char_types"] and "lowercase" not in problem["char_types"]:
        st.markdown("- Uppercase letters only")
    elif "lowercase" in problem["char_types"] and "uppercase" not in problem["char_types"]:
        st.markdown("- Lowercase letters only")

    if not problem["allow_repeat"]:
        st.markdown("- Characters cannot repeat")

    st.image(f"{problem['code_length']}char.png", width=150)

    correct_formula = " × ".join(problem["formula_parts"])

    if not st.session_state.submitted:
        with st.form("combo_form"):
            user_input = st.text_input("👉 Enter multiplication steps (e.g., 62 × 61 × 60):", key="combo_input")
            submit = st.form_submit_button("✅ Submit")

            if submit:
                st.session_state.user_answer = user_input
                user_norm = normalize_formula(user_input)
                correct_norm = normalize_formula(correct_formula)
                st.session_state.correct = (user_norm == correct_norm)
                st.session_state.submitted = True
                st.rerun()
    else:
        st.text_input("👉 Your multiplication steps:", value=st.session_state.user_answer, disabled=True)

        if st.session_state.correct:
            st.success("✅ Correct! Move on.")
            if st.button("➡️ Next Problem"):
                st.session_state.score += 1
                st.session_state.problem = generate_problem()
                st.session_state.submitted = False
                st.session_state.user_answer = ""
                st.rerun()
        else:
            st.error("❌ Incorrect.")
            st.markdown("### Correct solution:")
            st.markdown(f"**Formula:** {correct_formula}")
            if st.button("➡️ Try New Problem"):
                st.session_state.problem = generate_problem()
                st.session_state.submitted = False
                st.session_state.user_answer = ""
                st.rerun()

elif problem["type"] == "gcd":
    st.markdown("### Find the GCD (Greatest Common Divisor):")
    st.markdown(f"**What is the GCD of {problem['a']} and {problem['b']}?**")

    if not st.session_state.submitted:
        with st.form("gcd_form"):
            user_input = st.text_input("👉 Enter the GCD:", key="gcd_input")
            submit = st.form_submit_button("✅ Submit")

            if submit:
                st.session_state.user_answer = user_input.strip()
                st.session_state.correct = (user_input.strip() == str(problem["gcd"]))
                st.session_state.submitted = True
                st.rerun()
    else:
        st.text_input("👉 Your answer:", value=st.session_state.user_answer, disabled=True)

        if st.session_state.correct:
            st.success("✅ Correct!")
            if st.button("➡️ Next Problem"):
                st.session_state.score += 1
                st.session_state.problem = generate_problem()
                st.session_state.submitted = False
                st.session_state.user_answer = ""
                st.rerun()
        else:
            st.error("❌ Incorrect.")
            st.markdown(f"**Correct answer:** {problem['gcd']}")
            if st.button("➡️ Try New Problem"):
                st.session_state.problem = generate_problem()
                st.session_state.submitted = False
                st.session_state.user_answer = ""
                st.rerun()
