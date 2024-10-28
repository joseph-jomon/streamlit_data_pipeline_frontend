import streamlit as st
from services.auth import authenticate_api_key
from services.data_operations import fetch_data, validate_images, prepare_dataset, start_batch_processing

# Streamlit app
def main():
    st.title("Real Estate API Service")

    # Step 1: API Key Input Form
    api_key = st.text_input("Enter API Key:", type="password")
    
    if api_key:
        # Step 2: Make API call to authenticate once API key is provided
        st.write("Authenticating API Key...")
        if authenticate_api_key(api_key):
            st.success("API Key authenticated successfully!")

            # Automatically call endpoints in sequence
            st.write("Fetching real estate data...")
            #fetch_data(api_key)

            st.write("Validating images...")
            #validate_images(api_key)

            st.write("Preparing dataset...")
            #prepare_dataset(api_key)

            st.write("Sending data to vectorizer service")
            start_batch_processing(api_key)

            st.success("Process completed!")
        else:
            st.error("Authentication failed. Please check your API Key.")

if __name__ == "__main__":
    main()
