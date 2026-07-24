# -- HOME PAGE MULTIPAGES APP WITH STREAMLIT --





# -- SETUP
# -- x-----------------------------------------x --

# Load libraries
# -- x-------------------------x --
# Standard libraries
import pandas as pd

# Visualization libraries
import streamlit as st
# -- x-------------------------x --

# Configure page
# -- x-------------------------x --
st.set_page_config(page_title="Home", page_icon=':house:', layout='wide')
# -- x-------------------------x --

# -- x-----------------------------------------x --







# -- Page containt
# -- x-----------------------------------------x --
st.title("Home")



# Associate a counter within the session
# -- x-------------------------x --
# IF .. `counter` key does not exist in the dictionary, then creat and initialise it
if 'counter' not in st.session_state:
    st.session_state.counter = 0 


# Create a button to increment the session counter
if st.button('Increment'):
    st.session_state.counter += 1

# Display the counter value
st.write('Counter value :', st.session_state.counter)
# -- x-------------------------x --

# Draw a separation line
st.write('---')


# Define a counter (not related to the session)
# -- x-------------------------x --
# Instantiate and initialise a counter
standard_counter = 0

# IF .. the button is pushed, then increment the counter
if st.button('Increment standard counter'):
    standard_counter += 1

# Display standard counter value
st.write('Standard counter value :', standard_counter)
# -- x-------------------------x --

st.write('---')



# Load CSV file
# -- x-------------------------x --
st.subheader("Load CSV file")

# Define a widget to upload file
upload_file = st.file_uploader("Choose a CSV file: ", type=['csv'])

# IF .. a user upload / select a CSV file then apply the protocol
if upload_file is not None : 
    # Read the file
    df = pd.read_csv(upload_file)
    # Store the DataFrame within the session
    st.session_state['df'] = df
    
    # Display a message to the user
    st.success("CSV file upload is a success")
    # Display the first 5 row of the file
    st.write(df.head())

# ELSE .. there is no CSV file, then return an "info" message to the user 
else : 
    st.info("Please, upload a CSV file to us it within the app")
# -- x-------------------------x --


# -- x-----------------------------------------x --



