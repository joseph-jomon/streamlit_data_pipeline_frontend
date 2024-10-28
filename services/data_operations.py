import httpx
import streamlit as st

BASE_URL = "http://backend.kundalin.com/flowfact"


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
                            timeout=00.0)
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Image validation completed!")
            st.json(response.json())  # Display the invalid images, if any
        else:
            st.error(f"Failed to validate images. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Prepare dataset function
def prepare_dataset(api_key):
    try:
        # Make the API request
        response = httpx.post(f"{BASE_URL}/prepare-dataset/",
                            params={"api_key": api_key}, 
                            timeout=900.0)
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Dataset preparation completed!")
        else:
            st.error(f"Failed to prepare dataset. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def start_batch_processing():
    try:
        # Trigger the batch processing via the FastAPI endpoint
        response = httpx.post(f"{BASE_URL}/start-batch-processing/", timeout=900.0)
        if response.status_code == 200:
            st.success("Batch processing started!")
        else:
            st.error(f"Failed to start batch processing. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")