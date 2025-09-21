import streamlit as st

st.title("📊 Percent Composition Calculator")

st.markdown("""
**Concept:**  
Percent composition tells us the percentage by mass of each element in a compound.

**Formula:**  
**% Element = (Mass of element / Molar mass of compound) × 100**
""")

element_mass = st.number_input("Mass of element (g):", min_value=0.0)
compound_mass = st.number_input("Molar mass of compound (g/mol):", min_value=0.0)

if st.button("Calculate Percent Composition"):
    if compound_mass > 0:
        percent = (element_mass / compound_mass) * 100
        st.success(f"✅ Percent composition: **{percent:.2f}%**")
    else:
        st.error("Compound mass must be greater than zero.")
