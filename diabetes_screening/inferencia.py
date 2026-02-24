import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="🩺 Detector de Diabetes", layout="centered")

def load_assets():
    """Cargamos el modelo previamente entrenado usando joblib y el scaler."""
    try:
        model = joblib.load('modelo/modelo_diabetes.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except FileNotFoundError:
        st.error("Archivos modelo 'modelo_diabetes.pkl' y scaler 'scaler.pkl' no encontrados.")
        return None
    except Exception as e:
        st.error(f"Ha ocurrido un error: {e}")
        return None, None

def main():
    st.title("🩺 Detector de Diabetes")
    st.markdown("""
  Esta aplicación utiliza el **Conjunto de datos de diabetes** para predecir la probabilidad de diabetes según mediciones clínicas. Ingrese los datos del paciente a continuación.
    """)

    model, scaler = load_assets()
    
    if model and scaler:
        st.header("Datos del Paciente")
        col1, col2 = st.columns(2)
     

        with col1:
            # Rangos realistas basados ​​en las estadísticas del conjunto de datos Pima
            pregnancies = st.number_input("Embarazos", min_value=0, max_value=20, value=0, step=1)
            glucose = st.number_input("Glucosa (mg/dL)", min_value=0, max_value=200, value=100)
            blood_pressure = st.number_input("Presión Arterial (mm Hg)", min_value=0, max_value=130, value=70)
            skin_thickness = st.number_input("Espesor del pliegue cutáneo (mm)", min_value=0, max_value=100, value=20)

        with col2:
            insulin = st.number_input("Insulina (mu U/ml)", min_value=0, max_value=900, value=80)
            bmi = st.number_input("IMC (Indice de masa corporal)", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
            dpf = st.number_input("Función de pedigrí de diabetes", min_value=0.0, max_value=3.0, value=0.5, format="%.3f")
            age = st.number_input("Edad (Años)", min_value=21, max_value=100, value=30)

        # --- LÓGICA DE PREDICCIÓN ---
        if st.button("Ejecutar diagnóstico"):
            # 1.Preparar el vector de características para el modelo
            # Note: The order must match the order the model was trained on
            input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, 
                                 insulin, bmi, dpf, age]])

            # 2. Escalar los datos utilizando el scaler cargado
    
            std_data = scaler.transform(input_data)
            
            # 3. Hacer la predicción
            prediction = model.predict(std_data)
            
            st.markdown("---")
            st.subheader("Resultado:")

            if prediction[0] == 1:
                # Outcome 1: Positive for Diabetes
                st.markdown(f"<h2 style='color: #ff4b4b;'>Positivo (Outcome 1)</h2>", unsafe_allow_html=True)
                st.warning("El modelo sugiere una alta probabilidad de diabetes. Consulte con un profesional de la salud.")
            else:
                # Outcome 0: Negative for Diabetes
                st.markdown(f"<h2 style='color: #28a745;'>Negativo (Outcome 0)</h2>", unsafe_allow_html=True)
                st.success("El modelo sugiere una baja probabilidad de diabetes.")

        st.info("**Disclaimer:** Esta es una herramienta de demostración con fines educativos y no debe utilizarse como un diagnóstico médico definitivo.")

if __name__ == "__main__":
    main()
