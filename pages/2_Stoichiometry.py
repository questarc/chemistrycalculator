import streamlit as st

st.title("⚖️ Stoichiometry Calculator")

st.markdown("""
**Concept:**  
Stoichiometry helps us calculate the amount of reactants or products in a chemical reaction using mole ratios from a balanced equation.

**Formula:**  
**Moles of product = Moles of reactant × (Product coefficient / Reactant coefficient)**
""")

reactant_moles = st.number_input("Enter moles of reactant:", min_value=0.0, format="%.2f")
reactant_coeff = st.number_input("Reactant coefficient:", min_value=1)
product_coeff = st.number_input("Product coefficient:", min_value=1)

if st.button("Calculate Moles of Product"):
    product_moles = reactant_moles * (product_coeff / reactant_coeff)
    st.success(f"✅ Moles of product: **{product_moles:.2f} mol**")
