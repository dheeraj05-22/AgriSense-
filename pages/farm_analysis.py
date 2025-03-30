import streamlit as st
import random
import time
import plotly.express as px
import pandas as pd

# Set up Streamlit page
st.set_page_config(page_title="Farm Analysis Dashboard", page_icon="🌱", layout="wide")

# Page Title
st.markdown("""
    <h1 style='text-align: center; color: green;'>🌱 Farm Analysis Dashboard 🌱</h1>
    <p style='text-align: center;'>Upload satellite imagery or provide your farm location to receive AI-powered insights for precision agriculture.</p>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")

# Sample states and locations
states = {
    "Andhra Pradesh": [
        {"name": "Vijayawada", "lat": 16.5062, "lon": 80.6480},
        {"name": "Visakhapatnam", "lat": 17.6868, "lon": 83.2185},
        {"name": "Guntur", "lat": 16.3067, "lon": 80.4365},
        {"name": "Tirupati", "lat": 13.6288, "lon": 79.4192},
        {"name": "Kakinada", "lat": 16.9891, "lon": 82.2475},
        {"name": "Rajahmundry", "lat": 17.0005, "lon": 81.8040},
        {"name": "Nellore", "lat": 14.4426, "lon": 79.9865},
        {"name": "Anantapur", "lat": 14.6819, "lon": 77.6006},
        {"name": "Kadapa", "lat": 14.4673, "lon": 78.8242},
        {"name": "Eluru", "lat": 16.7107, "lon": 81.0952},
    ],
    "Tamil Nadu": [
        {"name": "Chennai", "lat": 13.0827, "lon": 80.2707},
        {"name": "Madurai", "lat": 9.9252, "lon": 78.1198},
        {"name": "Coimbatore", "lat": 11.0168, "lon": 76.9558},
        {"name": "Tiruchirappalli", "lat": 10.7905, "lon": 78.7047},
        {"name": "Salem", "lat": 11.6643, "lon": 78.1460},
        {"name": "Erode", "lat": 11.3410, "lon": 77.7172},
        {"name": "Vellore", "lat": 12.9165, "lon": 79.1325},
        {"name": "Thoothukudi", "lat": 8.7642, "lon": 78.1348},
        {"name": "Nagercoil", "lat": 8.1773, "lon": 77.4344},
        {"name": "Dindigul", "lat": 10.3624, "lon": 77.9708},
    ],
    "Karnataka": [
        {"name": "Bengaluru", "lat": 12.9716, "lon": 77.5946},
        {"name": "Mysuru", "lat": 12.2958, "lon": 76.6394},
        {"name": "Hubballi", "lat": 15.3647, "lon": 75.1240},
        {"name": "Mangaluru", "lat": 12.9141, "lon": 74.8560},
        {"name": "Belagavi", "lat": 15.8497, "lon": 74.4977},
        {"name": "Shivamogga", "lat": 13.9299, "lon": 75.5681},
        {"name": "Davangere", "lat": 14.4644, "lon": 75.9210},
        {"name": "Ballari", "lat": 15.1394, "lon": 76.9214},
        {"name": "Tumakuru", "lat": 13.3409, "lon": 77.1010},
        {"name": "Hassan", "lat": 13.0068, "lon": 76.0996},
    ]
}

st.subheader("📍 Select a State and Farm Location")
selected_state = st.selectbox("Choose a State:", list(states.keys()))
selected_location = st.selectbox("Choose a Location:", [loc["name"] for loc in states[selected_state]])

if st.button("Analyze Farm Data"):
    selected_coords = next((loc for loc in states[selected_state] if loc["name"] == selected_location), None)
    if selected_coords:
        st.map(pd.DataFrame([selected_coords], columns=["lat", "lon"]))
        st.success(f"Farm location set: {selected_location}, {selected_state}")

        # Analyze Farm Data
        st.success("Processing farm data...")
        time.sleep(2)  # Simulating data processing

        vegetation_health = round(random.uniform(0.5, 0.9), 2)
        water_stress = random.choice(["Low", "Moderate", "High"])
        soil_temp = random.randint(15, 25)
        sunlight_exposure = random.randint(70, 95)
        precipitation = random.randint(30, 60)
        wind_conditions = random.randint(5, 20)

        col3, col4, col5 = st.columns(3)
        with col3:
            st.metric("🌿 Vegetation Health", f"{vegetation_health} NDVI", "Healthy vegetation")
        with col4:
            st.metric("💧 Water Stress", water_stress, "Adequate moisture")
        with col5:
            st.metric("🌡️ Soil Temperature", f"{soil_temp}°C", "Optimal for crops")

        st.subheader("🌦 Weather & Growth Conditions")
        st.write("Current and 7-day forecast")

        progress_col1, progress_col2 = st.columns(2)
        with progress_col1:
            st.progress(sunlight_exposure / 100)
            st.text(f"Sunlight Exposure: {sunlight_exposure}%")
            st.progress(precipitation / 100)
            st.text(f"Precipitation: {precipitation}%")
        with progress_col2:
            st.progress(wind_conditions / 100)
            st.text(f"Wind Conditions: {wind_conditions}%")

        st.subheader("🤖 AI Recommendations")
        st.info("🔹 **Irrigation Plan:** Reduce irrigation in the northern section by 15%.")
        st.info("🔹 **Fertilizer Recommendation:** Apply nitrogen-rich fertilizer within 5 days.")
        st.warning("⚠ **Pest & Disease Alert:** Monitor early signs of fungal infections.")
        
        st.subheader("📊 Crop Health Distribution")
        labels = ["Excellent Crop Health", "Good Crop Health", "Moderate Stress"]
        values = [vegetation_health * 40, 35, 25]
        fig = px.pie(names=labels, values=values, title="Farm Crop Condition")
        st.plotly_chart(fig, use_container_width=True)
