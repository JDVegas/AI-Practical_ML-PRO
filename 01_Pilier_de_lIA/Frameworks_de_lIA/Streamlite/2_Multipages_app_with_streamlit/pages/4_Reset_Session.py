# -- PAGE 4 : RESET SESSION --





# -- SETUP
# -- x-----------------------------------------x --
# Visualization library
import streamlit as st

# Set page configuration 
st.set_page_config(page_title="Reset", layout="wide")
# -- x-----------------------------------------x --


st.title("Reset the session state")



# -- PAGE CONTAINT
# -- x-----------------------------------------x --

# Reset variable
# -- x-------------------------x --
# Define a button to reset the counter
if st.button("Reset counter"):
    st.session_state.counter = 0
    st.success("The counter have been properly reset")

# Define a button to reset the selected options
if st.button("Reset selection"):
    st.session_state.selection = []
    st.success("The selection have been properly reset")
# -- x-------------------------x --


# Remove variable
# -- x-------------------------x --
if st.button("Remove variable") and "counter" in st.session_state:
    st.session_state.pop("counter")
    if "counter" is not st.session_state:
        st.success("The counter key as been properly removed")
        st.write(f"The dictionary session keys are : {st.session_state.key}")
else :
    st.warning("There is no 'counter' key within the session dictionary!")
# -- x-------------------------x --


# -- x-----------------------------------------x --