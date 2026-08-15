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



# Indexes
# -- x-------------------------x --
# Build a theme index
theme_index = {item['id']:item["theme"] for item in st.session_state.themes}
# -- x-------------------------x --


# -- x-----------------------------------------x --



# -- FUNCTIONS
# -- x-----------------------------------------x --
def toggle_answer():
    st.session_state.show_answer = not st.session_state.show_answer


# Define a plumbing function to load card by theme 
def load_cards_by_theme(theme_id: int):
    """ Plumbing function that allow to load cards by theme
    
        Args : 
            theme_id (int): the id of the selected theme
    """

    # Load the cards related to this theme
    cards = cfct.get_cards_by_theme(theme_id)
    # Format theme
    st.session_state.cards_selected_theme = [{key:cards[key][idx] for key in cards.keys()} for idx in range(len(cards['id']))]

    # Help debugging 
    print(f"[cards_selected_theme]:\n{st.session_state.cards_selected_theme}")

    # Display a message to the users to indicate that the card are well loaded
    if st.session_state.cards_selected_theme :
        st.toast(f"The card related to the theme '{theme_index[theme_id]}' have been properly loaded. The Deck contains {len(st.session_state.cards_selected_theme)} cards.")
# -- x-----------------------------------------x --




# -- SIDEBAR CONTAINT
# -- x-----------------------------------------x --
with st.sidebar:
    st.write(f"Total number of cards:\n {cfct.get_number_of_cards()}")
    #st.write("---")

    # Instantiate a selectbox to select a theme
    selected_theme = st.selectbox(
                        label="Select the theme you want to study"
                        ,options=st.session_state.themes
                        , format_func=lambda x: x["theme"]
                    )

    # IF .. the user select a theme, then load the cards related to this thele
    if selected_theme:
        load_cards_by_theme(selected_theme['id'])



# -- x-----------------------------------------x --







""'''
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
        st.button(label="Wrong", width="stretch")'''""