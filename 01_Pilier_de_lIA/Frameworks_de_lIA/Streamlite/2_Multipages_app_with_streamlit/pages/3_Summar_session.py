# -- PAGE 3 : SUMMARY SESSION --





# -- SETUP
# -- x-----------------------------------------x --
# Visualization library
import streamlit as st

# Set page configuration 
st.set_page_config(page_title="Summary", layout="wide")
# -- x-----------------------------------------x --



# -- PAGE CONTAINT
# -- x-----------------------------------------x --
st.title("Session summary")
st.subheader("Counter values")

# IF .. a counter key exists then display the value
if 'counter' in st.session_state:
    st.write('The counter value is : ', st.session_state.counter)
# ELSE .. indicate that the counter has not been initialized yet
else:
    st.write('The Counter has not been initialized yet')

st.subheader('Option selected')

if 'selection' in st.session_state and st.session_state.selection:
    st.write('You have selected those options : ', st.session_state.selection)
else:
    st.write('No option have been selected.')

# -- x-----------------------------------------x --

