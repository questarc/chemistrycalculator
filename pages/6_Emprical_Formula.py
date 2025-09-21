import streamlit as st

st.title("🧬 Empirical Formula Calculator")

st.markdown("""
**Concept:**  
The empirical formula shows the simplest whole-number ratio of atoms in a compound.

**Steps:**
1. Convert mass to moles for each element.
2. Divide by the smallest mole value.
3. Round to nearest whole number.
""")

mass1 = st.number_input("Mass of Element A (g):", min_value=0.0)
molar_mass1 = st.number_input("Molar Mass of Element A (g/mol):", min_value=0.0)

mass2 = st.number_input("Mass of Element B (g):", min_value=0.0)
molar_mass2 = st.number_input("Molar Mass of Element B (g/mol):", min_value=0.0)

if st.button("Calculate Empirical Ratio"):
    if molar_mass1 > 0 and molar_mass2 > 0:
        moles1 = mass1 / molar_mass1
        moles2 = mass2 / molar_mass2
        min_moles = min(moles1, moles2)
        ratio1 = round(moles1 / min_moles)
        ratio2 = round(moles2 / min_moles)
        st.success(f"✅ Empirical formula ratio: A{ratio1}B{ratio2}")
    else:
        st.error("Molar masses must be greater than zero.")
