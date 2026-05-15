import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open("best_model.pkl", "rb") as file:
        return pickle.load(file)
    
model = load_model()

st.title("🌱 Smart Farming Dashboard")

st.set_page_config(page_title="Smart Farming Dashboard", page_icon=":Farming:", layout="wide")

col1, col2 = st.columns(2)

with col1:
    N = st.slider("Nitrogen (N)", 0, 200, 10)
    P = st.slider("Phosphorus (P)", 0, 200, 10)
    K = st.slider("Potassium (K)", 0, 200, 10)

with col2:
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=5.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, step=50.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=150.0, step=10.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=200.0, step=10.0)


if st.button("Predict Crop"):
    input_data = pd.DataFrame(
        {
            "Nitrogen":[N],
            "Phosphorus":[P],
            "Potassium":[K],
            "Soil pH":[ph],
            "Rainfall":[rainfall],
            "Temperature":[temperature],
            "Humidity":[humidity]
        }
    )

    prediction = model.predict(input_data)
    st.success(f"Recommended Crop: 🌾 {prediction[0]}")