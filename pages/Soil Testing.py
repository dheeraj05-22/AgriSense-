import numpy as np
import streamlit as st
import pandas as pd
import joblib
from PIL import Image
import json
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Soil Testing AI",
    page_icon="🌿",
    layout="wide"
)

text = 'Soil Nutrient Prediction using AI'
title = f"""
        <div style='
            font-family: arial;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
        '>{text}<br><br>
        </div>
        """
st.markdown(title, unsafe_allow_html=True)

co1, co2, co3 = st.columns([1, 1, 1])
coo1, coo2, coo3 = st.columns([1, 4, 1])

data = pd.read_csv('info.csv')

# Load the model
model = joblib.load('model_xgb.pkl')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

logo = load_lottiefile('soil.json')

def calculate_average_rgb(image):
    img = image.convert('RGB')
    data = img.getdata()
    r_total, g_total, b_total = 0, 0, 0
    for r, g, b in data:
        r_total += r
        g_total += g
        b_total += b
    num_pixels = len(data)
    return int(r_total / num_pixels), int(g_total / num_pixels), int(b_total / num_pixels)

def predict_pH(red, green, blue):
    input_data = pd.DataFrame({'blue': [int(blue)], 'green': [int(green)], 'red': [int(red)]})
    prediction = model.predict(input_data)
    return prediction[0]

def classify_soil_type(r, g, b):
    if r > 100 and g > 50 and b < 50:
        return "Red Soil", "Reddish"
    elif r < 80 and g > 100 and b < 80:
        return "Black Soil", "Dark Black"
    elif r > 150 and g > 130 and b > 100:
        return "Sandy Soil", "Light Brown"
    elif r > 120 and g > 100 and b > 80:
        return "Loamy Soil", "Brown"
    else:
        return "Unknown Soil", "Unknown Color"

with co2:
    st_lottie(logo, speed=1, width=400, height=400, key="initial")

with st.sidebar:
    st.title("Experience the power of AI in Agriculture")
    st.info("Upload an image of the soil to predict pH, soil type, and suitable crops.")
    input_type = st.selectbox("Pick one", ["Upload Image", "Camera Input" ])
    if input_type == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...")

if input_type == "Upload Image":
    with co2:
        if uploaded_file is None:
            st.warning("Please upload an image to get started.")
        else:
            with coo2:
                st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
if input_type == "Camera Input":
    with coo2:
        uploaded_file = st.camera_input("Capture the soil image.")

if uploaded_file is not None:
    with coo2:
        if st.button("Test the Soil Image"):
            image = Image.open(uploaded_file)
            avg_r, avg_g, avg_b = calculate_average_rgb(image)
            predicted_pH = predict_pH(avg_r, avg_g, avg_b)
            soil_name, soil_color = classify_soil_type(avg_r, avg_g, avg_b)
            
            if int(predicted_pH) < 4:
                chemical = data['Chemical Characteristics'][0]
                nutrients = data['Deficient Nutrients'][0]
                crops = data['Suitable Crops'][0]
            elif int(predicted_pH) >= 4 and int(predicted_pH) < 6:
                chemical = data['Chemical Characteristics'][1]
                nutrients = data['Deficient Nutrients'][1]
                crops = data['Suitable Crops'][1]
            elif int(predicted_pH) == 6:
                chemical = data['Chemical Characteristics'][2]
                nutrients = data['Deficient Nutrients'][2]
                crops = data['Suitable Crops'][2]
            elif int(predicted_pH) == 7:
                chemical = data['Chemical Characteristics'][3]
                nutrients = data['Deficient Nutrients'][3]
                crops = data['Suitable Crops'][3]
            elif int(predicted_pH) == 8:
                chemical = data['Chemical Characteristics'][4]
                nutrients = data['Deficient Nutrients'][4]
                crops = data['Suitable Crops'][4]
            elif int(predicted_pH) >= 9:
                chemical = data['Chemical Characteristics'][5]
                nutrients = data['Deficient Nutrients'][5]
                crops = data['Suitable Crops'][5]

            st.success(f"The pH of the Soil is {int(predicted_pH)}.")
            st.info(f"Soil Type: {soil_name}\nSoil Color: {soil_color}")
            st.success(f"Chemical Characteristics: {chemical}")
            st.success(f"Deficient Nutrients: {nutrients}")
            if 4 <= int(predicted_pH) <= 8:
                st.info(f"Suitable Crops: {crops}")
            else:
                st.warning("The soil is not suitable for any crops.")
