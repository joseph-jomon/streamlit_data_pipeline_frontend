import httpx
import streamlit as st

BASE_URL = "http://host.docker.internal:8000/flowfact"

# Fetch data function
def fetch_data(api_key):
    try:
        # Increase the timeout to allow for longer requests (e.g., 120 seconds)
        # Make the API request
        response = httpx.get(f"{BASE_URL}/fetch-data/", 
                            params={"api_key": api_key},
                            timeout=520.0)  # Timeout set to 120 seconds
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Data fetched successfully!")
            st.json(response.json())  # Display the fetched data in JSON format
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Validate images function
def validate_images(api_key):
    try:
        # Make the API request
        response = httpx.post(f"{BASE_URL}/validate-images/", 
                            params={"api_key": api_key},
                            timeout=900.0)
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Image validation completed!")
            st.json(response.json())  # Display the invalid images, if any
        else:
            st.error(f"Failed to validate images. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
