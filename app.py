import streamlit as st
import requests

st.title("🌤️ Weather App")

city = st.text_input("Въведи град:")
lat = st.number_input("Latitude:", value=42.70)
lon = st.number_input("Longitude:", value=23.32)

if st.button("Провери времето"):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url)
        data = response.json()
        weather = data["current_weather"]
        st.success(f"🌡️ Температура: {weather['temperature']}°C")
        st.info(f"💨 Скорост на вятъра: {weather['windspeed']} km/h")
    except:
        st.error("Грешка при зареждане на данните!")
