import streamlit as st 
import pandas as pd
import matplotlib as plt 
import seaborn as sns
import plotly.express as px
import io
import plotly.graph_objects as go

st.markdown("## Datos Crudos del dataset")
#cargar el dataset
df = pd.read_csv("Training.csv")

#mostrar dataset
st.dataframe(df.head(500))


st.markdown("## Datos sobre el dataset")
#mostrar descripción del dataset
st.dataframe(df.describe().T)


st.markdown(f"#### El tamaño del dataset es: {df.shape}")
st.markdown(f"#### Tenemos {df.shape[0]} filas y {df.shape[1]} columnas.")
st.markdown("#### Nuestras variables son:")
st.markdown(list(df.columns))

st.markdown("## Estadisticos básicos")

st.dataframe(df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']].describe().T[['count','std', 'mean', 'min', 'max']])

st.markdown("## Distribución de las variables")
#Mostrar boxplots para visualizar outliers o valores atipicos 
#Mostrar distribución de las variables


target_col = "Outcome"

feature_cols = [
    c for c in df.columns
    if df[c].dtype != "object"
]

#Seleccionar 3 columnas por defecto
selected_cols = st.multiselect(
    "Seleccione columnas de características para visualizar",
    options=feature_cols,
    default=feature_cols[:3],
    key="distribution_columns"
)

#Opción para comparar distribuciones por objetivo (0 vs 1)
color_by_target = st.checkbox("Color por columna Outcome")


for col in selected_cols:
    if color_by_target:
        fig = px.histogram(
            df,
            x=col,
            color="Outcome",
            nbins=30,
            barmode="overlay",
            marginal="box",
            title=f"{col} distribución por columna Outcome (Columna objetivo)"
        )

        fig.update_traces(opacity=0.6)

    else:
        fig = px.histogram(
            df,
            x=col,
            nbins=30,
            marginal="box",
            title=f"Distribución de  {col}"
        )

    fig.update_layout(bargap=0.05)
    st.plotly_chart(fig, use_container_width=True)

#Se muestra por separado la variable objectivo outcome
st.subheader("Distribución variable objetivo - Outcome")
st.markdown("#### 1: Diagnostico Positivo, 0: Diagnostico Negativo")

st.write(df[target_col].value_counts())

st.markdown("## Matriz de correlación")

#definir variable objetivo 
target_col = "Outcome"

numeric_features = [
    c for c in df.select_dtypes(include="number").columns
    if c != target_col
]

#Seleccionar método de correlación
corr_method = st.selectbox(
    "Método de Correlación",
    ["pearson", "spearman", "kendall"]
)

##Seleccionar columnas para visualizar la matriz de correlación, exluyendo variable objetivo, por defecto 5
selected_corr_cols = st.multiselect(
    "Select columns",
    numeric_features,
    default=numeric_features[:5]
)

if len(selected_corr_cols) >= 2:
    corr_df = df[selected_corr_cols].corr(method=corr_method)

    fig = px.imshow(
        corr_df,
        text_auto=".2f",
        color_continuous_scale="RdBu",
        zmin=-1,
        zmax=1,
        title="Matriz de correlación"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Seleccione al menos dos columnas.")


