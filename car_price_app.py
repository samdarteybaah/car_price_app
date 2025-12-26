import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('car_price_model.pkl')

st.title("Car Price Prediction")

st.write("Enter the details of your car to predict its price:")

col1, col2 = st.columns(2)
coli, colii =st.columns(2)
# User inputs
with col1:
    enginesize = st.number_input("Engine Size", min_value=50, max_value=500, value=130)
with col2:
    curbweight = st.number_input("Curb Weight", min_value=500, max_value=5000, value=2500)
with col1:
    horsepower = st.number_input("Horsepower", min_value=50, max_value=500, value=120)
with col2:
    carwidth = st.number_input("Car Width", min_value=50.0, max_value=100.0, value=65.0)
with coli:
    cylindernumber = st.selectbox("Number of Cylinders", [2,3,4,5,6,8,12], index=4)
with col1:
    highwaympg = st.number_input("Highway MPG", min_value=10, max_value=60, value=27)
with col2:
    citympg = st.number_input("City MPG", min_value=5, max_value=50, value=21)
with colii:
    carlength = st.number_input("Car Length", min_value=100.0, max_value=300.0, value=170.0)

# Predict button
if st.button("Predict Price"):
    input_data = pd.DataFrame({
        'enginesize': [enginesize],
        'curbweight': [curbweight],
        'horsepower': [horsepower],
        'carwidth': [carwidth],
        'cylindernumber': [cylindernumber],
        'highwaympg': [highwaympg],
        'citympg': [citympg],
        'carlength': [carlength]
    })
    
    predicted_price = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ${predicted_price:,.2f}")
