import streamlit as st
import asyncio
from services.auth import authenticate_api_key
from services.data_operations import fetch_data, validate_images, prepare_dataset, start_batch_processing

async def run_process(api_key):
    # Step 2: Make API call to authenticate once API key is provided
    st.write("Authenticating API Key...")
    authenticated = await authenticate_api_key(api_key)
    if authenticated:
        st.success("API Key authenticated successfully!")

        # Sequentially call each function with await to enforce order
        st.write("Fetching real estate data...")
        await fetch_data(api_key)
        
        st.write("Validating images...")
        await validate_images(api_key)
        
        st.write("Preparing dataset...")
        await prepare_dataset(api_key)
        
        st.write("Sending data to vectorizer service")
        await start_batch_processing(api_key)

        st.success("Process completed!")
    else:
        st.error("Authentication failed. Please check your API Key.")

# Streamlit app
def main():
    st.title("Real Estate API Service")

    # Step 1: API Key Input Form
    api_key = st.text_input("Enter API Key:", type="password")
    
    if api_key:
        # Run the sequential process
        asyncio.run(run_process(api_key))

if __name__ == "__main__":
    main()
