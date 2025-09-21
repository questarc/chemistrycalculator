import streamlit as st

st.title("🧪 Chemistry Quiz")

st.markdown("""
Welcome to the **Chemistry Quiz**!  
Test your knowledge on key concepts like mole calculations, gas laws, and stoichiometry.  
Select the best answer for each question and get instant feedback.
""")

# Quiz questions
quiz = [
    {
        "question": "What is the molar mass of water (H₂O)?",
        "options": ["18 g/mol", "20 g/mol", "10 g/mol", "16 g/mol"],
        "answer": 0,
        "explanation": "Water (H₂O) = 2×1 (H) + 16 (O) = 18 g/mol."
    },
    {
        "question": "Which gas law relates pressure and volume at constant temperature?",
        "options": ["Ideal Gas Law", "Avogadro's Law", "Boyle's Law", "Charles's Law"],
        "answer": 2,
        "explanation": "Boyle’s Law: P₁V₁ = P₂V₂ at constant temperature."
    },
    {
        "question": "What is the formula to calculate molarity?",
        "options": [
            "M = moles / volume",
            "M = mass / volume",
            "M = moles / mass",
            "M = volume / moles"
        ],
        "answer": 0,
        "explanation": "Molarity = moles of solute / liters of solution."
    },
    {
        "question": "Which is the limiting reactant if 10g of A (5 g/mol, coeff=1) and 20g of B (10 g/mol, coeff=2) are used?",
        "options": ["Reactant B", "Both are limiting", "Cannot be determined", "Reactant A"],
        "answer": 0,
        "explanation": "Moles A = 2, Moles B = 2 → A: 2/1 = 2, B: 2/2 = 1 → B is limiting."
    },
    {
        "question": "What is the empirical formula of a compound with 40% C, 6.7% H, 53.3% O?",
        "options": ["CHO", "C₆H₁₂O₆", "C₂H₄O₂", "CH₂O"],
        "answer": 3,
        "explanation": "Moles: C ≈ 3.33, H = 6.7, O ≈ 3.33 → divide by 3.33 → CH₂O."
    }
]

# Quiz logic
score = 0
for i, q in enumerate(quiz):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio(f"Choose your answer:", q["options"], key=f"q{i}")
    if st.button(f"Submit Q{i+1}", key=f"submit{i}"):
        correct = q["options"][q["answer"]]
        if selected == correct:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: **{correct}**")
        st.info(f"Explanation: {q['explanation']}")

# Final score
if st.button("Show Final Score"):
    st.markdown(f"### 🧠 Your Score: **{score} / {len(quiz)}**")
    if score == len(quiz):
        st.balloons()
        st.success("Perfect score! You're a chemistry whiz!")
