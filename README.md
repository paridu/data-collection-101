# data-collection-101

เครื่องมือระบุแหล่งข้อมูล
ฟังก์ชัน: สร้างเครื่องมือที่ช่วยในการค้นหาและประเมินคุณภาพของแหล่งข้อมูล
การพัฒนา: สร้างหน้าต่างใน Streamlit ที่ให้ผู้ใช้ป้อนคำค้นหาและแสดงแหล่งข้อมูลที่เกี่ยวข้อง

นี่คือตัวอย่างโค้ดรวมทั้งหมดในไฟล์ `app.py`:

```python
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function for Data Source Identification
def find_data_sources(query):
    # Placeholder function for searching data sources
    # You would replace this with actual search logic
    return [f"Source related to {query}"]

# Function for Web Scraping
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string  # Just an example, you can customize this

# Function for API Integration
def get_api_data(api_url):
    response = requests.get(api_url)
    return response.json()

# Function for Data Privacy Compliance Check
def check_data_compliance(data):
    # Placeholder function for data compliance check
    # You would replace this with actual compliance logic
    return "Compliance check passed!"

st.title("Data Collection Tools")

# Data Source Identification
st.header("Data Source Identification")
query = st.text_input("Enter search query:")
if query:
    sources = find_data_sources(query)
    st.write("Found Data Sources:")
    for source in sources:
        st.write(source)

# Web Scraping
st.header("Web Scraping Tool")
url = st.text_input("Enter website URL:")
if url:
    title = scrape_website(url)
    st.write(f"Website Title: {title}")

# API Integration
st.header("API Integration Tool")
api_url = st.text_input("Enter API URL:")
if api_url:
    data = get_api_data(api_url)
    st.write("API Response:")
    st.json(data)

# Data Privacy Compliance Checker
st.header("Data Privacy Compliance Checker")
data = st.text_area("Enter data description:")
if data:
    compliance_status = check_data_compliance(data)
    st.write(compliance_status)
```

### วิธีการใช้งาน
1. **ติดตั้งไลบรารีที่จำเป็น**: หากยังไม่ได้ติดตั้ง ไลบรารีเหล่านี้ให้ใช้คำสั่ง:
   ```bash
   pip install beautifulsoup4 requests streamlit
   ```

2. **สร้างไฟล์ `app.py`** และวางโค้ดข้างต้นลงไป

3. **รันแอป Streamlit** โดยใช้คำสั่ง:
   ```bash
   streamlit run app.py
   ```

4. **เปิดเว็บเบราว์เซอร์** ไปที่ [http://localhost:8501](http://localhost:8501) เพื่อเข้าถึงแอปของคุณ

ตอนนี้คุณมีเครื่องมือที่รวมฟังก์ชันต่าง ๆ สำหรับการรวบรวมข้อมูลทั้งหมดในแอปเดียวครับ!
