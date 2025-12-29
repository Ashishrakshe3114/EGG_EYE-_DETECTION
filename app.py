import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="EEG Eye State Prediction", layout="centered")

@st.cache_resource
def load_model():
    model = joblib.load("models/random_forest_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

model, scaler = load_model()

st.title("🧠 EEG Eye State Prediction")
st.write("Predict whether eyes are **Open or Closed** using EEG signals.")

st.subheader("Enter EEG Channel Values")

inputs = []
for i in range(14):
    value = st.number_input(
        f"EEG Channel {i+1}",
        value=0.0,
        format="%.4f"
    )
    inputs.append(value)

if st.button("Predict"):
    input_array = np.array(inputs).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("👁️ Eye State: **CLOSED**")
    else:
        st.success("👁️ Eye State: **OPEN**")
