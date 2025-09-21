import streamlit as st

st.title("🧪 Limiting Reactant Calculator")

st.markdown("""
**Concept:**  
The limiting reactant is the substance that runs out first, limiting the amount of product formed.

**Steps:**
1. Convert mass to moles.
2. Compare mole ratios based on the balanced equation.
""")

mass_a = st.number_input("Mass of Reactant A (g):", min_value=0.0)
molar_mass_a = st.number_input("Molar Mass of A (g/mol):", min_value=0.0)
coeff_a = st.number_input("Coefficient of A:", min_value=1)

mass_b = st.number_input("Mass of Reactant B (g):", min_value=0.0)
molar_mass_b = st.number_input("Molar Mass of B (g/mol):", min_value=0.0)
coeff_b = st.number_input("Coefficient of B:", min_value=1)

if st.button("Determine Limiting Reactant"):
    if molar_mass_a > 0 and molar_mass_b > 0:
        moles_a = mass_a / molar_mass_a
        moles_b = mass_b / molar_mass_b
        ratio_a = moles_a / coeff_a
        ratio_b = moles_b / coeff_b

        if ratio_a < ratio_b:
            st.success("✅ Limiting Reactant: **Reactant A**")
        elif ratio_b < ratio_a:
            st.success("✅ Limiting Reactant: **Reactant B**")
        else:
            st.info("Both reactants are in perfect stoichiometric ratio.")
    else:
        st.error("Molar masses must be greater than zero.")
