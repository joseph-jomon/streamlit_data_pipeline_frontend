import httpx
import streamlit as st

BASE_URL = "http://host.docker.internal:8000/flowfact"

def authenticate_api_key(api_key):
    try:
        response = httpx.post(f"{BASE_URL}/authenticate/", json={"api_key": api_key})
        return response.status_code == 200
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False
