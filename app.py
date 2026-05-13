import streamlit as st
import requests

st.title("🌤️ Weather App")

city = st.text_input("Въведи град:")

if st.button("Провери времето"):
    try:
        # Първо намираме координатите
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        if "results" not in geo_data:
            st.error("Градът не е намерен!")
        else:
            lat = geo_data["results"][0]["latitude"]
            lon = geo_data["results"][0]["longitude"]
            country = geo_data["results"][0]["country"]

            # После взимаме времето
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()
            weather = weather_data["current_weather"]

            st.success(f"📍 {city}, {country}")
            st.metric("🌡️ Температура", f"{weather['temperature']}°C")
            st.metric("💨 Скорост на вятъра", f"{weather['windspeed']} km/h")

    except Exception as e:
        st.error(f"Грешка: {e}")
