import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from googletrans import Translator

st.set_page_config(page_title="Farmer Survey", page_icon="🌾", layout="wide")
translator = Translator()

# Language Selection
language_options = {"English": "en", "Hindi": "hi", "Telugu": "te", "Kannada": "kn", "Tamil": "ta"}
selected_language = st.sidebar.selectbox("Select Language", list(language_options.keys()))
lang_code = language_options[selected_language]

def translate_text(text):
    return translator.translate(text, dest=lang_code).text if lang_code != "en" else text

st.title(translate_text("🌾 Monthly Farmer Survey for Crop Season Monitoring"))

# General Information
st.header(translate_text("1. General Information"))
name = st.text_input(translate_text("Farmer’s Name"))
location = st.text_input(translate_text("Location (Village/District)"))
contact = st.text_input(translate_text("Contact Number (Optional)"))
survey_date = st.date_input(translate_text("Date of Survey"))

# Crop Details
st.header(translate_text("2. Crop Details"))
crops = st.text_area(translate_text("What crop(s) are you currently cultivating?"))
growth_stage = st.radio(translate_text("What is the current growth stage of your main crop?"), 
                        [translate_text(stage) for stage in ["Land preparation", "Sowing/Planting", "Germination/Early growth", 
                         "Vegetative growth", "Flowering", "Fruiting/Pod formation", 
                         "Maturity/Harvesting", "Post-harvest"]], index=None)

# Weather & Environmental Conditions
st.header(translate_text("3. Weather & Environmental Conditions"))
weather = st.radio(translate_text("How would you describe this month’s weather conditions?"), 
                   [translate_text(option) for option in ["Excessive rain", "Normal rain", "Drought/Low rainfall", "Heatwave", "Cold spell", "Other"]])
extreme_weather = st.radio(translate_text("Were there any extreme weather events (floods, storms, hail, etc.)?"), [translate_text("Yes"), translate_text("No")])
if extreme_weather == translate_text("Yes"):
    impact = st.text_area(translate_text("Describe the impact"))

# Soil & Irrigation
st.header(translate_text("4. Soil & Irrigation"))
soil_moisture = st.radio(translate_text("What is the current soil moisture condition?"), [translate_text("Too dry"), translate_text("Adequate"), translate_text("Waterlogged")])
irrigation_method = st.selectbox(translate_text("What irrigation method are you using?"), 
                                 [translate_text(option) for option in ["Rainfed", "Canal irrigation", "Tube well/Borewell", "Drip/Sprinkler", "Other"]])
soil_issues = st.radio(translate_text("Any noticeable soil issues (salinity, erosion, nutrient deficiency)?"), [translate_text("Yes"), translate_text("No")])
if soil_issues == translate_text("Yes"):
    soil_issues_details = st.text_area(translate_text("Specify the issue"))

# Submit Survey
if st.button(translate_text("Submit Survey")):
    st.success(translate_text("Survey submitted successfully!"))
    
    # Generate Charts
    st.subheader(translate_text("📊 Data Visualization"))
    fig, ax = plt.subplots()
    categories = [translate_text("Weather"), translate_text("Soil Issues"), translate_text("Pest/Disease"), translate_text("Market Price")]
    values = [
        1 if weather in [translate_text("Excessive rain"), translate_text("Drought/Low rainfall")] else 0,
        1 if soil_issues == translate_text("Yes") else 0,
        1 if extreme_weather == translate_text("Yes") else 0,
        np.random.randint(0, 2)  # Placeholder for market price condition
    ]
    ax.bar(categories, values, color=['blue', 'brown', 'red', 'green'])
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Generate Survey Report
    st.subheader(translate_text("📄 Survey Report"))
    report = f"""
    {translate_text("Farmer's Name")}: {name}
    {translate_text("Location")}: {location}
    {translate_text("Contact Number")}: {contact}
    {translate_text("Date of Survey")}: {survey_date}
    {translate_text("Current Crops")}: {crops}
    {translate_text("Growth Stage")}: {growth_stage}
    {translate_text("Weather Condition")}: {weather}
    {translate_text("Extreme Weather Events")}: {extreme_weather}
    {translate_text("Soil Moisture")}: {soil_moisture}
    {translate_text("Irrigation Method")}: {irrigation_method}
    {translate_text("Soil Issues")}: {soil_issues}
    """
    st.text_area(translate_text("Survey Report"), report, height=250)
    
    st.write(translate_text("💡 Keep using the survey for better crop planning and profitability!"))
