import streamlit as st

st.set_page_config(page_title="Links", layout="centered")

st.title("Links")
st.write("---")

# Reemplazá por tus links reales
GITHUB_URL = "https://github.com/tobiaslp3880-coder/streamlit-app"
STREAMLIT_URL = "https://app-app-vr9ytr3qsneubr9u8ggxiw.streamlit.app/"

texto = f"""
1. repo de GitHub: {GITHUB_URL}
2. URL de mi App: {STREAMLIT_URL}
"""

# Mostrarlo como bloque tipo "terminal/código"
st.code(texto, language="")

# (Opcional) también mostrar como links clicables
st.markdown(f"- **Repo en GitHub:** [{GITHUB_URL}]({GITHUB_URL})")
st.markdown(f"- **URL de la App:** [{STREAMLIT_URL}]({STREAMLIT_URL})")
