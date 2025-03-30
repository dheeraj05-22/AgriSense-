import streamlit as st
from PIL import Image
import os

# Set page configuration for a wide layout
st.set_page_config(page_title="AgriTech E-commerce", layout="wide")

# Dummy product data
PRODUCTS = {
    "Fertilizers": [
        {"id": 1, "name": "Organic Fertilizer", "brand": "AgroCo", "price": 500, "description": "Eco-friendly fertilizer.", "image_path": "images\organic_Fertlizer.jpg"},
        {"id": 2, "name": "Nitrogen Booster", "brand": "GrowFast", "price": 650, "description": "Enhances soil fertility.", "image_path": r"images\nitrogen_booster.jpeg"},
        {"id": 3, "name": "Potassium Enricher", "brand": "SoilMax", "price": 700, "description": "Boosts plant strength.", "image_path": "images\PotassiumEnricher.jpg"},
        {"id": 4, "name": "Phosphorus Mix", "brand": "AgriPro", "price": 600, "description": "Improves root growth.", "image_path": "images\PhosphorusMix.jpeg"},
        {"id": 5, "name": "Compost Mix", "brand": "EcoSoil", "price": 400, "description": "Rich in organic matter.", "image_path": "images\CompostMix.jpeg"},
        {"id": 6, "name": "Bio Fertilizer", "brand": "GreenGrow", "price": 550, "description": "Promotes microbial activity.", "image_path": "images\BioFertilizer.jpeg"},
        {"id": 7, "name": "Seaweed Extract", "brand": "MarineAgri", "price": 800, "description": "Natural plant stimulant.", "image_path": "images\SeaweedExtract.jpg"},
        {"id": 8, "name": "Liquid Fertilizer", "brand": "NutrientFlow", "price": 750, "description": "Fast-acting liquid formula.", "image_path": "images\LiquidFertilizer.jpeg"},
        {"id": 9, "name": "Vermicompost", "brand": "WormFarm", "price": 450, "description": "Nutrient-rich organic compost.", "image_path": "images\Vermicompost.jpeg"},
        {"id": 10, "name": "Humic Acid", "brand": "SoilCare", "price": 900, "description": "Enhances nutrient absorption.", "image_path": "images\HumicAcid.jpeg"}
    ],
    "Tools": [
        {"id": 11, "name": "Hand Trowel", "brand": "FarmTools", "price": 300, "description": "High-quality steel trowel.", "image_path": "images\HandTrowel.jpg"},
        {"id": 12, "name": "Pruning Shears", "brand": "GardenPro", "price": 450, "description": "Sharp and durable shears.", "image_path": "images\PruningShears.jpg"},
        {"id": 13, "name": "Garden Hoe", "brand": "AgriTools", "price": 500, "description": "Durable and efficient hoe.", "image_path": "images\GardenHoe.jpg"},
        {"id": 14, "name": "Weeding Fork", "brand": "WeedMaster", "price": 350, "description": "Removes weeds effectively.", "image_path": "images\WeedingFork.jpg"},
        {"id": 15, "name": "Spade", "brand": "DuraDig", "price": 600, "description": "Heavy-duty garden spade.", "image_path": "images\Spade.jpeg"},
        {"id": 16, "name": "Watering Can", "brand": "AquaGrow", "price": 250, "description": "Ergonomic design.", "image_path": "images\WateringCan.jpeg"},
        {"id": 17, "name": "Rake", "brand": "LandPro", "price": 550, "description": "Efficient for soil leveling.", "image_path": "images\Rake.jpeg"},
        {"id": 18, "name": "Garden Gloves", "brand": "HandSafe", "price": 200, "description": "Protective and durable.", "image_path": "images\GardenGloves.jpeg"},
        {"id": 19, "name": "Hedge Trimmer", "brand": "TrimTech", "price": 1500, "description": "Electric hedge trimmer.", "image_path": "images\HedgeTrimmer.jpeg"},
        {"id": 20, "name": "Soil Tester", "brand": "AgriScan", "price": 950, "description": "Analyzes soil nutrients.", "image_path": "images\SoilTester.jpeg"}
    ],
    "Gadgets": [
        {"id": 21, "name": "Soil Moisture Sensor", "brand": "TechAgri", "price": 1200, "description": "Monitors soil moisture levels.", "image_path": "images\SoilMoistureSensor.jpeg"},
        {"id": 22, "name": "Smart Irrigation Controller", "brand": "IrrigSmart", "price": 2500, "description": "Automates irrigation scheduling.", "image_path": "images\SmartIrrigationController.jpeg"},
        {"id": 23, "name": "Drone Sprayer", "brand": "AgriDrone", "price": 15000, "description": "Precision pesticide spraying.", "image_path": "images\DroneSprayer.jpeg"},
        {"id": 24, "name": "Weather Station", "brand": "ClimateWatch", "price": 5000, "description": "Real-time weather updates.", "image_path": "images\WeatherStation.jpeg"},
        {"id": 25, "name": "Automated Seeder", "brand": "SeedBot", "price": 8000, "description": "Automates seed planting.", "image_path": "images\AutomatedSeeder.jpeg"},
        {"id": 26, "name": "AI Crop Analyzer", "brand": "AgriAI", "price": 12000, "description": "AI-based crop health detection.", "image_path": "images\AICropAnalyzer.jpeg"},
        {"id": 27, "name": "Electric Weeder", "brand": "EcoWeed", "price": 4000, "description": "Non-chemical weed removal.", "image_path": "images\ElectricWeeder.jpeg"},
        {"id": 28, "name": "Solar-Powered Pump", "brand": "SolarFlow", "price": 10000, "description": "Eco-friendly water pumping.", "image_path": "images\SolarPoweredPump.jpeg"},
        {"id": 29, "name": "Livestock Tracker", "brand": "FarmTrack", "price": 3500, "description": "GPS-based livestock monitoring.", "image_path": "images\LivestockTracker.jpeg"},
        {"id": 30, "name": "Hydroponic Kit", "brand": "HydroFarm", "price": 6000, "description": "Indoor farming made easy.", "image_path": "images\HydroponicKit.jpeg"}
    ]
}


# Cart storage
if "cart" not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(product_id, product):
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id]['quantity'] += 1
    else:
        st.session_state.cart[product_id] = {"quantity": 1, **product}
    st.success(f"Added {product['name']} to cart!")

def clear_cart():
    st.session_state.cart = {}

def main():
    st.title("AgriTech E-commerce Store")

    tabs = st.tabs(["Fertilizers", "Tools", "High-Tech Gadgets", "Cart & Checkout"])

    for i, (category, products) in enumerate(PRODUCTS.items()):
        with tabs[i]:
            st.subheader(category)
            cols = st.columns(3)  # Now using three columns
            for idx, product in enumerate(products):
                with cols[idx % 3]:  # Distribute items among three columns
                    st.image(product["image_path"], width=150)
                    st.write(f"**{product['name']}**")
                    st.write(f"Brand: {product['brand']}")
                    st.write(f"Price: ₹{product['price']}")
                    st.write(product["description"])
                    if st.button("Add to Cart", key=f"add_{product['id']}"):
                        add_to_cart(product['id'], product)

    with tabs[3]:
        st.subheader("Your Cart")
        if not st.session_state.cart:
            st.info("Your cart is empty.")
        else:
            total = 0
            for item in st.session_state.cart.values():
                st.write(f"{item['name']} (x{item['quantity']}) - ₹{item['price']} each")
                total += item['price'] * item['quantity']
            st.write(f"**Total: ₹{total}**")
            if st.button("Clear Cart"):
                clear_cart()
                st.success("Cart cleared!")

if __name__ == "__main__":
    main()