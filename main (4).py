import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model and preprocessor
model = pickle.load(open('delivery_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
expected_features = pickle.load(open('feature_columns.pkl', 'rb'))

# UI
st.title("🚚 Food Delivery Time Predictor")

# User Inputs
weather = st.selectbox("Weather Condition", ['Clear', 'Cloudy', 'Rainy', 'Foggy', 'Snowy', 'Windy'])
traffic = st.selectbox("Traffic Condition", ['Low', 'Medium', 'High'])
vehicle = st.selectbox("Vehicle Type", ['Bike', 'Car', 'Scooter'])
order_time = st.selectbox("Order Time", ['Morning', 'Afternoon', 'Evening', 'Night'])
order_size = st.slider("Order Size (items)", 1, 10, 2)
experience = st.slider("Courier Experience (yrs)", 0, 10, 2)
distance = st.slider("Delivery Distance (km)", 0.5, 10.0, 2.0)

# Map Order Time to Hour
time_map = {'Morning': 9, 'Afternoon': 14, 'Evening': 19, 'Night': 22}
order_hour = time_map[order_time]

# Determine if Peak
peak = 1 if order_hour in [11, 12, 13, 14, 18, 19, 20, 21] else 0

# Base features
input_data = {
    'delivery_distance_km': distance,
    'Order_Size': order_size,
    'Courier_Experience_yrs': experience,
    'Order_Hour': order_hour,
    'Time_Period_Peak': peak,
}

# Add encoded categorical values
categorical_features = {
    f'Weather_Condition_{weather}': 1,
    f'Traffic_Conditions_{traffic}': 1,
    f'Vehicle_Type_{vehicle}': 1
}
input_data.update(categorical_features)

# Ensure all expected features exist
final_input = {}
for feature in expected_features:
    final_input[feature] = input_data.get(feature, 0)

# Create input DataFrame
input_df = pd.DataFrame([final_input])

# Scale and Predict
scaled_input = scaler.transform(input_df)
prediction = model.predict(scaled_input)

st.success(f"⏱️ Estimated Delivery Time: {prediction[0]:.2f} minutes")
