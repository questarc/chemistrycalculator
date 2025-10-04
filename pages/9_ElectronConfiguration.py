import streamlit as st
import pandas as pd

#st.set_page_config(page_title="Chemistry Calculator", layout="wide")

#st.sidebar.title("🧪 Chemistry Topics")
#topic = st.sidebar.selectbox("Select a topic:", ["Welcome", "Introduction to Electron Configurations"])

#if topic == "Welcome":
#    st.markdown("""
#    # Welcome to the Chemistry Calculator App!
#    This tool helps 10th graders learn and practice key chemistry calculations interactively.
#    """)
#elif topic == "Introduction to Electron Configurations":
    st.title("🧲 Introduction to Electron Configurations")
    
    st.markdown("""
    ### What is Electron Configuration?
    Electron configuration describes the distribution of electrons in the shells (energy levels) around the nucleus of an atom. 
    According to Bohr's model, electrons occupy fixed shells: K (n=1), L (n=2), M (n=3), N (n=4), and so on.
    
    The maximum number of electrons a shell can hold is given by the formula **2n²**, where **n** is the shell number:
    - K shell (n=1): 2 electrons
    - L shell (n=2): 8 electrons
    - M shell (n=3): 18 electrons
    - N shell (n=4): 32 electrons
    
    Electrons fill the shells starting from the innermost (K) shell outward.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Bohr Model of Hydrogen Atom (K shell with 1 electron)**")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/1_H_Bohr_model.png/800px-1_H_Bohr_model.png")
    with col2:
        st.markdown("""
        ### Key Concepts:
        - **Valence Electrons**: Electrons in the outermost shell. They determine the chemical properties and valency of the element.
        - **Valency**: The combining capacity of an atom, often equal to the number of valence electrons (for groups 1-2) or 8 minus valence electrons (for groups 13-17).
        - In the Periodic Table, elements in the same group have the same number of valence electrons.
        """)
    
    st.subheader("Filling Order")
    st.markdown("""
    Electrons fill shells sequentially from inner to outer. For example:
    - Hydrogen (H, Z=1): 1 electron in K shell → Configuration: 1
    - Helium (He, Z=2): 2 electrons in K shell → Configuration: 2
    - Sodium (Na, Z=11): 2 in K, 8 in L, 1 in M → Configuration: 2, 8, 1
    """)
    
    st.markdown("**Simplified Aufbau Principle: Order of Filling Shells and Subshells**")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aufbau_Principle.png/800px-Aufbau_Principle.png")
    
    st.subheader("Electron Configurations for First 20 Elements")
    data = {
        "Atomic Number": list(range(1, 21)),
        "Element": ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", 
                    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"],
        "Configuration": ["1", "2", "2,1", "2,2", "2,3", "2,4", "2,5", "2,6", "2,7", "2,8", 
                          "2,8,1", "2,8,2", "2,8,3", "2,8,4", "2,8,5", "2,8,6", "2,8,7", "2,8,8", "2,8,8,1", "2,8,8,2"],
        "Valence Electrons": [1, 2, 1, 2, 3, 4, 5, 6, 7, 8, 
                              1, 2, 3, 4, 5, 6, 7, 8, 1, 2]
    }
    df = pd.DataFrame(data)
    st.table(df)
    
    st.markdown("""
    ### Visual: Periodic Table with Electron Shells
    The image below shows the periodic table highlighting the electron shells for elements.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Periodic_Table_of_Elements_showing_Electron_Shells.svg/1200px-Periodic_Table_of_Elements_showing_Electron_Shells.svg.png")
    
    st.markdown("""
    ### Quick Practice
    - **Example**: What is the electron configuration of Carbon (C, Z=6)?  
      **Answer**: 2,4 (2 in K shell, 4 in L shell). Valence electrons: 4.
    
    Use this knowledge to understand why elements in Group 1 (like Na) are reactive—they have 1 valence electron to lose easily!
    """)
