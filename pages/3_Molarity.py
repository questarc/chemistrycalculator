import streamlit as st

st.title("🧪 Molarity Calculator")

st.markdown("""
**Concept:**  
Molarity (M) is the concentration of a solution, defined as:

**M = Moles of solute / Volume of solution (L)**
""")

moles = st.number_input("Enter moles of solute:", min_value=0.0, format="%.2f")
volume = st.number_input("Enter volume of solution (liters):", min_value=0.0, format="%.2f")

if st.button("Calculate Molarity"):
    if volume > 0:
        molarity = moles / volume
        st.success(f"✅ Molarity: **{molarity:.2f} mol/L**")
    else:
        st.error("Volume must be greater than zero.")
