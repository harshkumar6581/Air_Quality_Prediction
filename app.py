import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(
    page_title="AQI Prediction System",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Air Quality Index (AQI) Prediction")
st.write(
    "Enter pollutant values below to predict the Air Quality Index."
)

st.sidebar.header("Pollutant Values")

pm25 = st.sidebar.number_input("PM2.5", min_value=0.0, value=50.0)
pm10 = st.sidebar.number_input("PM10", min_value=0.0, value=100.0)
no = st.sidebar.number_input("NO", min_value=0.0, value=20.0)
no2 = st.sidebar.number_input("NO2", min_value=0.0, value=30.0)
nox = st.sidebar.number_input("NOx", min_value=0.0, value=40.0)
nh3 = st.sidebar.number_input("NH3", min_value=0.0, value=20.0)
co = st.sidebar.number_input("CO", min_value=0.0, value=1.0)
so2 = st.sidebar.number_input("SO2", min_value=0.0, value=20.0)
o3 = st.sidebar.number_input("O3", min_value=0.0, value=40.0)
benzene = st.sidebar.number_input("Benzene", min_value=0.0, value=2.0)
toluene = st.sidebar.number_input("Toluene", min_value=0.0, value=5.0)
xylene = st.sidebar.number_input("Xylene", min_value=0.0, value=1.0)

input_data = pd.DataFrame({
    "PM2.5": [pm25],
    "PM10": [pm10],
    "NO": [no],
    "NO2": [no2],
    "NOx": [nox],
    "NH3": [nh3],
    "CO": [co],
    "SO2": [so2],
    "O3": [o3],
    "Benzene": [benzene],
    "Toluene": [toluene],
    "Xylene": [xylene]
})

st.subheader("Input Data")
st.dataframe(input_data)

if st.button("Predict AQI"):

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted AQI: {prediction:.2f}")

    if prediction <= 50:
        category = "Good"
    elif prediction <= 100:
        category = "Satisfactory"
    elif prediction <= 200:
        category = "Moderate"
    elif prediction <= 300:
        category = "Poor"
    elif prediction <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    st.info(f"AQI Category: {category}")