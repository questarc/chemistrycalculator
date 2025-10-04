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
   *Note*: Exceptions like chromium ([Ar] 3d⁵ 4s¹) and copper ([Ar] 3d¹⁰ 4s¹) occur due to stability of half-filled or fully filled subshells.  
2. **Pauli Exclusion Principle**: No two electrons in an atom can have the same four quantum numbers; each orbital holds up to 2 electrons with opposite spins.  
3. **Hund’s Rule**: Electrons singly occupy orbitals in a subshell before pairing, with identical spins to maximize total spin.
""")

st.markdown("**Example of Hund’s Rule**: For oxygen (1s² 2s² 2p⁴), the 2p subshell has one electron in each of three orbitals before pairing.")

st.subheader("Electron Configurations for All 118 Elements")
st.markdown("Below is a table showing electron configurations for all 118 known elements. The first 20 elements are commonly covered in the 10th-grade syllabus, while higher elements include d- and f-block orbitals. Configurations are given in abbreviated form where applicable, using the noble gas core.")

# Data for all 118 elements
data = {
    "Atomic Number": list(range(1, 119)),
    "Element": [
        "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
        "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
        "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
        "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
        "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
        "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
        "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
        "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
        "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
        "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
        "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
    ],
    "Configuration": [
        "1s¹", "1s²", "1s² 2s¹", "1s² 2s²", "1s² 2s² 2p¹", "1s² 2s² 2p²", "1s² 2s² 2p³",
        "1s² 2s² 2p⁴", "1s² 2s² 2p⁵", "1s² 2s² 2p⁶", "1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁶ 3s²",
        "1s² 2s² 2p⁶ 3s² 3p¹", "1s² 2s² 2p⁶ 3s² 3p²", "1s² 2s² 2p⁶ 3s² 3p³", "1s² 2s² 2p⁶ 3s² 3p⁴",
        "1s² 2s² 2p⁶ 3s² 3p⁵", "1s² 2s² 2p⁶ 3s² 3p⁶", "[Ar] 4s¹", "[Ar] 4s²",
        "[Ar] 3d¹ 4s²", "[Ar] 3d² 4s²", "[Ar] 3d³ 4s²", "[Ar] 3d⁵ 4s¹", "[Ar] 3d⁵ 4s²",
        "[Ar] 3d⁶ 4s²", "[Ar] 3d⁷ 4s²", "[Ar] 3d⁸ 4s²", "[Ar] 3d¹⁰ 4s¹", "[Ar] 3d¹⁰ 4s²",
        "[Ar] 3d¹⁰ 4s² 4p¹", "[Ar] 3d¹⁰ 4s² 4p²", "[Ar] 3d¹⁰ 4s² 4p³", "[Ar] 3d¹⁰ 4s² 4p⁴",
        "[Ar] 3d¹⁰ 4s² 4p⁵", "[Ar] 3d¹⁰ 4s² 4p⁶", "[Kr] 5s¹", "[Kr] 5s²", "[Kr] 4d¹ 5s²",
        "[Kr] 4d² 5s²", "[Kr] 4d⁴ 5s¹", "[Kr] 4d⁵ 5s¹", "[Kr] 4d⁵ 5s²", "[Kr] 4d⁷ 5s¹",
        "[Kr] 4d⁸ 5s¹", "[Kr] 4d¹⁰", "[Kr] 4d¹⁰ 5s¹", "[Kr] 4d¹⁰ 5s²", "[Kr] 4d¹⁰ 5s² 5p¹",
        "[Kr] 4d¹⁰ 5s² 5p²", "[Kr] 4d¹⁰ 5s² 5p³", "[Kr] 4d¹⁰ 5s² 5p⁴", "[Kr] 4d¹⁰ 5s² 5p⁵",
        "[Kr] 4d¹⁰ 5s² 5p⁶", "[Xe] 6s¹", "[Xe] 6s²", "[Xe] 5d¹ 6s²", "[Xe] 4f¹ 5d¹ 6s²",
        "[Xe] 4f² 6s²", "[Xe] 4f³ 6s²", "[Xe] 4f⁴ 6s²", "[Xe] 4f⁵ 6s²", "[Xe] 4f⁶ 6s²",
        "[Xe] 4f⁷ 6s²", "[Xe] 4f⁷ 5d¹ 6s²", "[Xe] 4f⁹ 6s²", "[Xe] 4f¹⁰ 6s²", "[Xe] 4f¹¹ 6s²",
        "[Xe] 4f¹² 6s²", "[Xe] 4f¹³ 6s²", "[Xe] 4f¹⁴ 6s²", "[Xe] 4f¹⁴ 5d¹ 6s²",
        "[Xe] 4f¹⁴ 5d² 6s²", "[Xe] 4f¹⁴ 5d³ 6s²", "[Xe] 4f¹⁴ 5d⁴ 6s²", "[Xe] 4f¹⁴ 5d⁵ 6s²",
        "[Xe] 4f¹⁴ 5d⁶ 6s²", "[Xe] 4f¹⁴ 5d⁷ 6s²", "[Xe] 4f¹⁴ 5d⁹ 6s¹", "[Xe] 4f¹⁴ 5d¹⁰ 6s¹",
        "[Xe] 4f¹⁴ 5d¹⁰ 6s²", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²",
        "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴", "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵",
        "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "[Rn] 7s¹", "[Rn] 7s²", "[Rn] 6d¹ 7s²", "[Rn] 6d² 7s²",
        "[Rn] 5f² 6d¹ 7s²", "[Rn] 5f³ 6d¹ 7s²", "[Rn] 5f⁴ 6d¹ 7s²", "[Rn] 5f⁶ 7s²",
        "[Rn] 5f⁷ 7s²", "[Rn] 5f⁷ 6d¹ 7s²", "[Rn] 5f⁹ 7s²", "[Rn] 5f¹⁰ 7s²", "[Rn] 5f¹¹ 7s²",
        "[Rn] 5f¹² 7s²", "[Rn] 5f¹³ 7s²", "[Rn] 5f¹⁴ 7s²", "[Rn] 5f¹⁴ 6d¹ 7s²",
        "[Rn] 5f¹⁴ 6d² 7s²", "[Rn] 5f¹⁴ 6d³ 7s²", "[Rn] 5f¹⁴ 6d⁴ 7s²", "[Rn] 5f¹⁴ 6d⁵ 7s²",
        "[Rn] 5f¹⁴ 6d⁶ 7s²", "[Rn] 5f¹⁴ 6d⁷ 7s²", "[Rn] 5f¹⁴ 6d⁹ 7s¹", "[Rn] 5f¹⁴ 6d¹⁰ 7s¹",
        "[Rn] 5f¹⁴ 6d¹⁰ 7s²", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²",
        "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴", "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵",
        "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶"
    ],
    "Valence Electrons": [
        1, 2, 1, 2, 3, 4, 5, 6, 7, 8,  # H-Ne (Groups 1, 2, 13-18)
        1, 2, 3, 4, 5, 6, 7, 8, 1, 2,  # Na-Ca (Groups 1, 2, 13-18)
        2, 2, 2, 1, 2, 2, 2, 2, 1, 2,  # Sc-Zn (Groups 3-12, transition metals, simplified)
        3, 4, 5, 6, 7, 8, 1, 2, 2, 2,  # Ga-Zr (Groups 13-18, 3-4)
        1, 1, 2, 1, 1, 0, 1, 2, 3, 4,  # Nb-Sn (Groups 5-12, 13-14)
        5, 6, 7, 8, 1, 2, 2, 2, 2, 2,  # Sb-Nd (Groups 15-18, lanthanides)
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Pm-Yb (lanthanides, simplified)
        2, 2, 2, 2, 2, 2, 2, 1, 1, 2,  # Lu-Hg (Groups 3-12)
        3, 4, 5, 6, 7, 8, 1, 2, 2, 2,  # Tl-Th (Groups 13-18, actinides)
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Pa-Fm (actinides, simplified)
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # Md-Ds (actinides, Groups 3-10)
        1, 2, 3, 4, 5, 6, 7, 8  # Rg-Og (Groups 11-18)
    ]
}

df = pd.DataFrame(data)
st.table(df)

st.subheader("Interactive Calculator")
st.markdown("Enter an atomic number (1–20) to view its electron configuration, as these are commonly studied in the 10th-grade syllabus. For elements beyond 20, refer to the table above.")
atomic_number = st.number_input("Enter atomic number (1-20):", min_value=1, max_value=20, step=1)
if st.button("Show Electron Configuration"):
    element = df[df["Atomic Number"] == atomic_number]["Element"].iloc[0]
    config = df[df["Atomic Number"] == atomic_number]["Configuration"].iloc[0]
    valence = df[df["Atomic Number"] == atomic_number]["Valence Electrons"].iloc[0]
    st.success(f"✅ Element: **{element}** | Configuration: **{config}** | Valence Electrons: **{valence}**")
