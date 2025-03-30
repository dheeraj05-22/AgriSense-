import streamlit as st
from PIL import Image
import os

# Set page configuration for a wide layout
st.set_page_config(page_title="AgriTech E-commerce", layout="wide")

# Function to get the correct image path
def get_image_path(filename):
    path = os.path.join("images", filename)
    if os.path.exists(path):
        return path
    else:
        return None  # Handle missing images

# Dummy product data
PRODUCTS = {
    "Fertilizers": [
        {"id": 1, "name": "Organic Fertilizer", "brand": "AgroCo", "price": 500, "description": "Eco-friendly fertilizer.", "image_path": "organic_Fertlizer.jpg"},
        {"id": 2, "name": "Nitrogen Booster", "brand": "GrowFast", "price": 650, "description": "Enhances soil fertility.", "image_path": "nitrogen_booster.jpeg"},
        {"id": 3, "name": "Potassium Enricher", "brand": "SoilMax", "price": 700, "description": "Boosts plant strength.", "image_path": "PotassiumEnricher.jpg"},
        {"id": 4, "name": "Phosphorus Mix", "brand": "AgriPro", "price": 600, "description": "Improves root growth.", "image_path": "PhosphorusMix.jpeg"},
        {"id": 5, "name": "Compost Mix", "brand": "EcoSoil", "price": 400, "description": "Rich in organic matter.", "image_path": "CompostMix.jpeg"}
    ],
    "Tools": [
        {"id": 6, "name": "Hand Trowel", "brand": "FarmTools", "price": 300, "description": "High-quality steel trowel.", "image_path": "HandTrowel.jpg"},
        {"id": 7, "name": "Pruning Shears", "brand": "GardenPro", "price": 450, "description": "Sharp and durable shears.", "image_path": "PruningShears.jpg"},
        {"id": 8, "name": "Garden Hoe", "brand": "AgriTools", "price": 500, "description": "Durable and efficient hoe.", "image_path": "GardenHoe.jpg"}
    ],
    "Gadgets": [
        {"id": 9, "name": "Soil Moisture Sensor", "brand": "TechAgri", "price": 1200, "description": "Monitors soil moisture levels.", "image_path": "SoilMoistureSensor.jpeg"},
        {"id": 10, "name": "Smart Irrigation Controller", "brand": "IrrigSmart", "price": 2500, "description": "Automates irrigation scheduling.", "image_path": "SmartIrrigationController.jpeg"}
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
            cols = st.columns(2)  # Using two columns for better layout
            for idx, product in enumerate(products):
                with cols[idx % 2]:  # Distribute items among two columns
                    image_path = get_image_path(product["image_path"])
                    if image_path:
                        st.image(image_path, width=150)
                    else:
                        st.warning("Image not found!")
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
