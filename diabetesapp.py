import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes.joblib")

# Create simple label encoders matching the model's training logic
gender = {"Female": 0, "Male": 1}
smoking_history = {"No Info": 0, "Current": 1, "Ever": 2, "Former": 3, "Never": 4, "Not Current": 5}

# Streamlit UI
st.title("Diabetes Prediction App")

# Input fields
age = st.number_input("Age", min_value=0.0)
hypertension = st.number_input("Hypertension", min_value=0.0)
heart_disease = st.number_input("Heart Disease", min_value=0.0)
body_mass = st.number_input("Body Mass", min_value=0.0)
hemoglobin_level = st.number_input("Hemoglobin Level", min_value=0)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0)

# Categorical inputs
gender = st.selectbox("Gender", list(gender.keys()))
smoking_history = st.selectbox("Smoking History", list(smoking_history.keys()))

# Encode values
input_data = pd.DataFrame([{
    "Gender": gender,
    "Age": age,
    "Hypertension": hypertension,
    "HeartDisease": heart_disease,
    "SmokingHistory": smoking_history,
    "BodyMass": body_mass,
    "HemoglobinLevel": hemoglobin_level,
    "BloodGlucoseLevel": blood_glucose_level,
}])

# Make prediction
if st.button("Predict Diabetes"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Is Diabetic (1)' if prediction[0] == 1 else 'Is Not Diabetic (0)'}")
