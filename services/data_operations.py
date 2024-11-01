import httpx
import streamlit as st

BASE_URL = "http://backend.kundalin.com/flowfact"

# Fetch data function
async def fetch_data(api_key):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/fetch-data/", 
                params={"api_key": api_key},
                timeout=520.0  # Timeout set to 520 seconds
            )
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Data fetched successfully!")
            st.json(response.json())  # Display the fetched data in JSON format
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Validate images function
async def validate_images(api_key):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/validate-images/", 
                params={"api_key": api_key},
                timeout=600.0  # Adjust timeout as needed
            )
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Image validation completed!")
            st.json(response.json())  # Display the invalid images, if any
        else:
            st.error(f"Failed to validate images. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Prepare dataset function
async def prepare_dataset(api_key):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/prepare-dataset/",
                params={"api_key": api_key}, 
                timeout=900.0  # Adjust timeout as needed
            )
        
        # Check if the response is successful
        if response.status_code == 200:
            st.success("Dataset preparation completed!")
        else:
            st.error(f"Failed to prepare dataset. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Start batch processing function
async def start_batch_processing(api_key):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/start-batch-processing/",
                params={"api_key": api_key},
                timeout=9000.0  # Adjust timeout as needed
            )
        
        if response.status_code == 200:
            st.success("Batch processing started!")
        else:
            st.error(f"Failed to start batch processing. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
