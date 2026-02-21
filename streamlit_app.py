import streamlit as st 

pg_intro = st.Page("intro.py", title="Introducción")
pg_eda_intro = st.Page("seccion_eda/introduccion.py", title="Intro EDA")

navigation_env = st.navigation(
    {
    "Inicio": [pg_intro],
    "EDA": [pg_eda_intro]
    }
)

navigation_env.run()