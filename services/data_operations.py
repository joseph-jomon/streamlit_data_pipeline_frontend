import httpx
import streamlit as st

BASE_URL = "http://localhost:8000/flowfact"

def fetch_data(api_key):
    try:
        response = httpx.get(f"{BASE_URL}/fetch-data/", headers={"Authorization": api_key})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Failed to fetch data.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def validate_images(api_key):
    try:
        response = httpx.post(f"{BASE_URL}/validate-images/", headers={"Authorization": api_key})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Failed to validate images.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
