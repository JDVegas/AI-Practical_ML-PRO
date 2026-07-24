# -- FIRST PAGE : COUNTER --





# -- SETUP
# -- x-----------------------------------------x --
# Visualization library
import streamlit as st


# Set the page configuration
st.set_page_config(page_title = "Counter", layout='wide')

# -- x-----------------------------------------x --




# -- PAGE CONTAINT
# -- x-----------------------------------------x --

st.title("Counter page")


# Associate a counter within the session
# -- x-------------------------x --
# Define a counter associated with the session
if "counter" not in st.session_state:
    st.session_state.counter = 0 

# Definer a widget to get a number from a user
increment = st.number_input("Value to add", min_value=1, value=1)

# Create a button to add the value set by a user to our counter
if st.button("Increment"):
    st.session_state.counter += increment
    # Display a message to the use
    st.success(f"Counter incremented of {increment}")

# Display a text 
st.write(f"Current counter value: {st.session_state.counter}")
# -- x-------------------------x --

# Draw a separation line
st.write('---')

# Define a counter (not related to the session)
# -- x-------------------------x --
standard_counter = 0

# IF .. the button is bushed, then increment it of one
if st.button("Increment standard button"):
    standard_counter += 1

# Display this counter current vamue
st.write('Standard counter value : ', standard_counter)
# -- x-------------------------x --


# -- x-----------------------------------------x --