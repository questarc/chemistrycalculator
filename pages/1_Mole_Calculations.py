import streamlit as st

st.title("🧪 Mole Calculations")

st.markdown("""
**Concept:**  
A mole is a unit that represents **6.022 × 10²³ particles** of a substance.  
To convert between grams and moles, use the formula:

**Moles = Mass (g) / Molar Mass (g/mol)**
""")

mass = st.number_input("Enter mass (grams):", min_value=0.0, format="%.2f")
molar_mass = st.number_input("Enter molar mass (g/mol):", min_value=0.0, format="%.2f")

if st.button("Calculate Moles"):
    if molar_mass > 0:
        moles = mass / molar_mass
        st.success(f"✅ Moles of substance: **{moles:.4f} mol**")
    else:
        st.error("Molar mass must be greater than zero.")
