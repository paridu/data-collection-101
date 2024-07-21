import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string  # Just an example, you can customize this

st.title("Web Scraping Tool")

url = st.text_input("Enter website URL:")
if url:
    title = scrape_website(url)
    st.write(f"Website Title: {title}")
