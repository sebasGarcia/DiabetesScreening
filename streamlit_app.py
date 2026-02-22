import streamlit as st 

pg_intro = st.Page("intro.py", title="Introducción")

#Paginas EDA
pg_eda_intro = st.Page("seccion_eda/intro_eda.py", title="Intro EDA")
pg_eda_basica = st.Page("seccion_eda/estadisticos_basicos.py", title="Información básica")

navigation_env = st.navigation(
    {
    "Inicio": [pg_intro],
    "EDA": [pg_eda_intro, pg_eda_basica]
    }
)

navigation_env.run()