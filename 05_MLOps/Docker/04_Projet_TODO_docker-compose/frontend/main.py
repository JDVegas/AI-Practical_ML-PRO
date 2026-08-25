# -- PROKECT 4 : FRONTEND --


# -- SETUP --
# -- x---------------------------x --
# Standard libraries
import os
import requests

# Visualization libraries
import streamlit as st


# -- x---------------------------x --



# -- SCRIPT --
# -- x---------------------------x --
st.title("Architecture Microservices")

# Get the API URL from environment variable
API_URL = os.getenv("API_URL")


st.write(f"Connected to the backend: {API_URL}")


# Build a form to add items
with st.form("my_form"):
    # Create a input text field
    new_item = st.text_input("Add a task")
    # Create a button to submit input data
    submitted = st.form_submit_button("Add")

    # IF .. the form have been submitted and that there is a new value, 
    # then use the backend API to save the data into the database
    if submitted and new_item:
        try:
            # Call API (POST) method
            response = requests.post(f"{API_URL}/items", json={"name": new_item})
            # IF .. the API returned a response then display a success message
            if response.status_code == 200:
                st.success("Added with success")
            else:
                st.error("Error server side")
        except requests.exceptions.ConnectionError:
            st.error("Impossible to connect with the API (Backend stopped ?)")



# Display the list 
st.subheader("Tasks list (from the DB)")
# IF .. the refresh button have been pushed
if st.button("Refresh"):
    try:
        # Call API (GET) method
        response = requests.get(f"{API_URL}/items")
        # Format the response into a JSON
        items = response.json()
        # Iterate through each item
        for item in items:
            st.write(f"- {item}")

    except Exception as e:
        st.error("Connection Error: {e}")
# -- x---------------------------x --