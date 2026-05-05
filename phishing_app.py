import streamlit as st

st.set_page_config(page_title="Phishing Awareness Trainer")

st.title("🎣 Phishing Awareness Trainer")

st.write("Practice identifying phishing emails. Select your answer and get instant feedback.")

# --- SCENARIOS ---
scenarios = [
    {
        "email": "From: IT Support\nSubject: Urgent Password Reset\n\nYour password expires today. Click here immediately to reset your password.",
        "answer": "Phishing",
        "explanation": "Urgent language and a request to click a link are common phishing tactics."
    },
    {
        "email": "From: HR Department\nSubject: Updated Benefits Info\n\nPlease review the updated benefits document attached.",
        "answer": "Safe",
        "explanation": "No urgency or suspicious link. This is a typical internal communication."
    },
    {
        "email": "From: PayPal Support\nSubject: Account Suspended\n\nYour account has been suspended. Log in here to restore access: http://fake-paypal-login.com",
        "answer": "Phishing",
        "explanation": "Suspicious URL and urgency indicate phishing."
    }
]

score = 0

# --- LOOP THROUGH SCENARIOS ---
for i, scenario in enumerate(scenarios):
    st.subheader(f"Scenario {i+1}")

    st.code(scenario["email"])

    choice = st.radio(
        "Is this email phishing or safe?",
        ["Phishing", "Safe"],
        key=f"q{i}"
    )

    if st.button(f"Check Answer {i+1}", key=f"b{i}"):
        if choice == scenario["answer"]:
            st.success("Correct!")
            score += 1
        else:
            st.error("Not quite.")

        st.info(scenario["explanation"])

    st.markdown("---")

# --- SO WHAT? ---
st.subheader("So What?")

st.write(
    "Phishing works because it pressures people to act quickly before they stop and think. "
    "The goal of this practice is not just to get the answers right, but to build the habit of pausing, "
    "checking the sender, looking closely at links, and verifying unexpected requests before clicking."
)

st.success("Thanks for paying closer attention. Pause. Verify. Don’t click.")
