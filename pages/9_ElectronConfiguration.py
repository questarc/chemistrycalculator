import streamlit as st
import pandas as pd

st.title("🧲 Electron Configurations")

st.markdown("""
**Concept:**  
The electron configuration of an element describes how electrons are distributed in its atomic orbitals. It follows a standard notation where electron-containing subshells are listed with the number of electrons in superscript. For example, sodium’s electron configuration is **1s² 2s² 2p⁶ 3s¹**. For elements with higher atomic numbers, an abbreviated notation uses the noble gas core, e.g., sodium as **[Ne] 3s¹**.
""")

st.markdown("""
**Why are Electron Configurations Important?**  
- Determine the **valency** of an element.  
- Predict **properties** of elements with similar configurations.  
- Interpret **atomic spectra**.
""")

st.subheader("Shells and Subshells")
st.markdown("""
- **Shells**: Defined by the principal quantum number (n). The maximum number of electrons in a shell is **2n²**.  
  - K shell (n=1): 2 electrons  
  - L shell (n=2): 8 electrons  
  - M shell (n=3): 18 electrons  
  - N shell (n=4): 32 electrons  

- **Subshells**: Defined by the azimuthal quantum number (l). Possible subshells are s (l=0), p (l=1), d (l=2), and f (l=3).  
  - Maximum electrons in a subshell: **2(2l + 1)**.  
  - Example: s (2 electrons), p (6 electrons), d (10 electrons), f (14 electrons).
""")

st.subheader("Rules for Filling Electrons")
st.markdown("""
1. **Aufbau Principle**: Electrons fill orbitals from lowest to highest energy (e.g., 1s → 2s → 2p → 3s → 3p → 4s → 3d).  
   *Note*: Exceptions like copper ([Ar] 3d¹⁰ 4s¹) occur due to stability of filled subshells.  
2. **Pauli Exclusion Principle**: No two electrons in an atom can have the same four quantum numbers; each orbital holds up to 2 electrons with opposite spins.  
3. **Hund’s Rule**: Electrons singly occupy orbitals in a subshell before pairing, with identical spins to maximize total spin.
""")

st.markdown("**Example of Hund’s Rule**: For oxygen (1s² 2s² 2p⁴), the 2p subshell has one electron in each of three orbitals before pairing.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Bohr Model of Hydrogen (1s¹)**")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/1_H_Bohr_model.png/800px-1_H_Bohr_model.png")
with col2:
    st.markdown("**Aufbau Principle: Order of Filling**")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aufbau_Principle.png/800px-Aufbau_Principle.png")

st.subheader("Electron Configurations for First 20 Elements")
data = {
    "Atomic Number": list(range(1, 21)),
    "Element": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
                "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"],
    "Configuration": ["1s¹", "1s²", "1s² 2s¹", "1s² 2s²", "1s² 2s² 2p¹", "1s² 2s² 2p²", "1s² 2s² 2p³", 
                      "1s² 2s² 2p⁴", "1s² 2s² 2p⁵", "1s² 2s² 2p⁶", "1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁶ 3s²", 
                      "1s² 2s² 2p⁶ 3s² 3p¹", "1s² 2s² 2p⁶ 3s² 3p²", "1s² 2s² 2p⁶ 3s² 3p³", "1s² 2s² 2p⁶ 3s² 3p⁴", 
                      "1s² 2s² 2p⁶ 3s² 3p⁵", "1s² 2s² 2p⁶ 3s² 3p⁶", "[Ar] 4s¹", "[Ar] 4s²"],
    "Valence Electrons": [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
}
df = pd.DataFrame(data)
st.table(df)

st.markdown("**Periodic Table with Electron Shells**")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Periodic_Table_of_Elements_showing_Electron_Shells.svg/800px-Periodic_Table_of_Elements_showing_Electron_Shells.svg.png")

st.subheader("Interactive Calculator")
atomic_number = st.number_input("Enter atomic number (1-20):", min_value=1, max_value=20, step=1)
if st.button("Show Electron Configuration"):
    element = df[df["Atomic Number"] == atomic_number]["Element"].iloc[0]
    config = df[df["Atomic Number"] == atomic_number]["Configuration"].iloc[0]
    valence = df[df["Atomic Number"] == atomic_number]["Valence Electrons"].iloc[0]
    st.success(f"✅ Element: **{element}** | Configuration: **{config}** | Valence Electrons: **{valence}**")
