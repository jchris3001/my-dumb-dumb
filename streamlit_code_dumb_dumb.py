# -*- coding: utf-8 -*-
"""streamlit code dumb dumb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NCJbbuiOdCf6s7iyrU0a15AbbVwyLWfm
"""



import streamlit as st
import joblib
import numpy as np

# Load the machine learning model
model = joblib.load('decision_tree.sav')

def main():
    st.title('Machine Learning Deployment')
    st.title('0 = Clear , 1 = Clouds, 2 = Rain, 3 = Thunderstorm')

    # Add user input components for 5 features
    temp = st.slider('dt', min_value=0.0, max_value=50.0, value=0.01)
    temp = st.slider('temp', min_value=0.0, max_value=50.0, value=0.01)
    temp_min = st.slider('temp_min', min_value=0.0, max_value=50.0, value=0.01)
    temp_max = st.slider('temp_max', min_value=0.0, max_value=50.0, value=0.01)
    pressure = st.slider('pressure', min_value=1000.0, max_value=1050.0, value=0.1)
    humidity = st.slider('humidity', min_value=0.0, max_value=100.0, value=1.00)
    wind_speed = st.slider('wind_speed', min_value=0.0, max_value=20.0, value=0.01)
    wind_deg = st.slider('wind_deg', min_value=0.0, max_value=360.0, value=1.00)
    rain_1h = st.slider('rain_1h', min_value=0.0, max_value=2.0, value=0.01)
    rain_3h = st.slider('rain_3h', min_value=0.0, max_value=100.0, value=0.1)
    rain_6h = st.slider('rain_6h', min_value=0.0, max_value=100.0, value=0.1)
    rain_12h = st.slider('rain_12h', min_value=0.0, max_value=250.0, value=0.1)
    rain_24h = st.slider('rain_24h', min_value=0.0, max_value=200.0, value=0.1)
    clouds_all= st.slider('clouds_all', min_value=0.0, max_value=100.0, value=0.1)
    weather_main = st.slider('weather_main', min_value=0.0, max_value=3.0, value=1.00)
    weather_description = st.slider('weather_description', min_value=0.0, max_value=14.0, value=1.00)


    if st.button('Make Prediction'):
        features = [temp,temp_min,temp_max,pressure,humidity,wind_speed,wind_deg,rain_1h,rain_3h,rain_6h,rain_12h,rain_24h,clouds_all,weather_main,weather_description]
        result = make_prediction(features)
        st.success(f'The prediction is: {result}')

def make_prediction(features):
    # Use the loaded model to make predictions
    # Replace this with the actual code for your model
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

if __name__ == '__main__':
    main()
