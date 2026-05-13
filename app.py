import streamlit as st

st.title("Моето първо приложение!")

name = st.text_input("Въведи твоето име:")
if name:
    st.write(f"Здравей, {name}!")
