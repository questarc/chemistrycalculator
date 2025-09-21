import streamlit as st

st.title("🌬️ Gas Laws Calculator")

st.markdown("""
**Concepts:**  
Gas laws describe how pressure, volume, and temperature relate in gases.

**Boyle’s Law:**  
**P₁ × V₁ = P₂ × V₂** (at constant temperature)

**Charles’s Law:**  
**V₁ / T₁ = V₂ / T₂** (at constant pressure)
""")

law = st.selectbox("Choose a gas law:", ["Boyle's Law", "Charles's Law"])

if law == "Boyle's Law":
    p1 = st.number_input("Initial Pressure (P₁):", min_value=0.0)
    v1 = st.number_input("Initial Volume (V₁):", min_value=0.0)
    p2 = st.number_input("Final Pressure (P₂):", min_value=0.0)

    if st.button("Calculate Final Volume (V₂)"):
        if p2 > 0:
            v2 = (p1 * v1) / p2
            st.success(f"✅ Final Volume (V₂): **{v2:.2f} L**")
        else:
            st.error("Final pressure must be greater than zero.")

elif law == "Charles's Law":
    v1 = st.number_input("Initial Volume (V₁):", min_value=0.0)
    t1 = st.number_input("Initial Temperature (T₁ in K):", min_value=0.0)
    t2 = st.number_input("Final Temperature (T₂ in K):", min_value=0.0)

    if st.button("Calculate Final Volume (V₂)"):
        if t1 > 0:
            v2 = (v1 / t1) * t2
            st.success(f"✅ Final Volume (V₂): **{v2:.2f} L**")
        else:
            st.error("Initial temperature must be greater than zero.")
