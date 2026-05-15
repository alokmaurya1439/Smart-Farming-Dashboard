import streamlit as st # type: ignore
import joblib
import numpy as np

# Load trained model
model = joblib.load("crop_model.pkl")

st.title("🌱 Smart Farming Dashboard")
st.write("Get crop recommendations based on soil & weather data.")

# User Inputs
N = st.slider("Nitrogen (N)", 0, 150, 50)
P = st.slider("Phosphorus (P)", 0, 150, 50)
K = st.slider("Potassium (K)", 0, 200, 50)
ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 0, 300, 100)
temperature = st.slider("Temperature (°C)", 0, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 60)

if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"Recommended Crop: 🌾 {prediction[0]}")

