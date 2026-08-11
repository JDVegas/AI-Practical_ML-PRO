# -- FIRST PAGE : FLASHCARDS --





# -- SETUP
# -- x-----------------------------------------x --

# Load libraries
# -- x-------------------------x --
# Standard libraries
import sys
from pathlib import Path
import pandas as pd

# Visualization libraries
import streamlit as st
# -- x-------------------------x --


# Load functions
# -- x-------------------------x --
# Manually force project modules path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from Modules.app_initialization import app_initialization
import Modules.crud_functions_cards_table as cfct 
import Modules.crud_functions_themes_table as cftt
# -- x-------------------------x --




# Configure page
# -- x-------------------------x --
st.set_page_config(page_title="Flashcards", layout='wide')

# Initialize app
app_initialization()
# -- x-------------------------x --

# -- x-----------------------------------------x --



# -- FUNCTIONS
# -- x-----------------------------------------x --
def toggle_answer():
    st.session_state.show_answer = not st.session_state.show_answer

# -- x-----------------------------------------x --




# -- PAGE CONTAINT
# -- x-----------------------------------------x --
st.title("Flashcards")

# Insert Space below the title
st.write("##")

# Create 3 columns
col1, col2, col3 = st.columns((1, 3, 1))

# Build the column elements 
with col2:

    # Build a container to display a card shape
    with st.container(border=True, height=300, width="stretch"
                    , horizontal_alignment="center"
                    , vertical_alignment="top"):
        

        st.markdown(f"""<h1 style="background-color:powderblue;">My_theme</h1>""",unsafe_allow_html=True) 
        # Build a container without border to display the question
        with st.container(height="stretch", width="stretch"
                        , horizontal_alignment="center"
                        , vertical_alignment="center"):   


            # IF ...  
            if not st.session_state.show_answer:   
                st.markdown("<p style='text-align:center;'>My_question</p>", unsafe_allow_html=True)
            else : 
                st.markdown("<p><span style='text-align:center;'>My_question</span></p>", unsafe_allow_html=True)
                st.markdown("<p style='text-align:center;'>The_correct_answer</p>", unsafe_allow_html=True)

    st.button(label="Show answer", width="stretch", on_click=toggle_answer)

    subcol21, subcol22, subcol23 = st.columns(3)

    with subcol21: 
        #if 
        st.button(label="Correct", width="stretch")


    with subcol22: 
        #if 
        st.button(label="No Idea", width="stretch")

    with subcol23: 
        #if 
        st.button(label="Wrong", width="stretch")