import streamlit as st 

# Configuración general de la página (se aplica a todas)
st.set_page_config(page_title="🩺 Detector de Diabetes", layout="wide")

# --- DEFINICIÓN DE LAS PÁGINAS ---

# 1. Página de Inicio (Bienvenida)
pg_inicio = st.Page("intro.py", title="Inicio")

# 2. Proyecto : Detector de Diabetes

pg_eda_basica = st.Page("diabetes_screening/estadisticos_basicos.py", title="Análisis Exploratorio")
pg_diabetes_inf = st.Page("diabetes_screening/inferencia.py", title="Inferencia")


navigation_env = st.navigation(
    {
        "General": [pg_inicio],
        "Proyecto: Detector de Diabetes": [pg_eda_basica, pg_diabetes_inf]      
    }
)

navigation_env.run()

