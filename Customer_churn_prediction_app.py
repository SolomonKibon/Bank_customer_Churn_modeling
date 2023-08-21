import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
st.subheader('Solomon Kibon')
# Load the trained model
model = joblib.load('best_model1.pkl')

# Define the app title and layout
st.title("Bank Customer Churn Prediction App")

# Define input fields for features
credit_score = st.number_input("Credit Score", min_value=0, max_value=1000, value=600, step=1)
age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5, step=1)
balance = st.number_input("Balance", min_value=0.0, max_value=300000.0, value=10000.0, step=100.0)
num_of_products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_credit_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, max_value=300000.0, value=50000.0, step=100.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])

# Create a button for making predictions
if st.button("Predict"):
    # Process input values
    input_data = pd.DataFrame(
        {
            "CreditScore": [credit_score],
            "Age": [age],
            "Tenure": [tenure],
            "Balance": [balance],
            "NumOfProducts": [num_of_products],
            "HasCrCard": [has_credit_card],
            "IsActiveMember": [is_active_member],
            "EstimatedSalary": [estimated_salary],
            "Geography_Spain": [1 if geography == "Spain" else 0],
            
        }
    )

    # Scale input data using the same scaler used during training
    scaler = StandardScaler()
    input_data_scaled = scaler.fit_transform(input_data)

    # Make a prediction using the trained model
    prediction = model.predict(input_data_scaled)

    # Display the prediction
    if prediction[0] == 1:
        st.error("The customer is at risk of churn.")
    else:
        st.success("The customer is not at risk of churn.")
