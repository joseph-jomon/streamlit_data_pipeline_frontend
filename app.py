import streamlit as st
from services.auth import authenticate_api_key
from services.data_operations import fetch_data, validate_images

# Streamlit app
def main():
    st.title("Real Estate API Service")

    # Step 1: API Key Input Form
    with st.form(key="api_key_form"):
        api_key = st.text_input("Enter API Key:", type="password")
        submit_button = st.form_submit_button(label="Authenticate")

    if submit_button:
        # Step 2: Make API call to authenticate
        if authenticate_api_key(api_key):
            st.success("API Key authenticated successfully!")
            show_data_options(api_key)
        else:
            st.error("Authentication failed. Please check your API Key.")

# Function to display options after successful authentication
def show_data_options(api_key):
    st.subheader("Data Operations")

    # Fetch Data Button
    if st.button("Fetch Real Estate Data"):
        fetch_data(api_key)

    # Validate Images Button
    if st.button("Validate Images"):
        validate_images(api_key)

if __name__ == "__main__":
    main()
