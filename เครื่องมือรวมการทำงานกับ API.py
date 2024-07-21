import streamlit as st
import requests

def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

st.title("API Integration Tool")

api_url = st.text_input("Enter API URL:")
if api_url:
    data = get_api_data(api_url)
    st.write("API Response:")
    st.json(data)
