# -- APP INITIALIZATION --

"""

The objective of this script is to define a set of function that will initialize the application parameters. 
More specifically, we will here create all the environment variable that will be stored into the session state. 

"""


# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
# Standard libraries
from typing import Dict

# SQL libraries
import sqlite3

# Visualization libraries
import streamlit as st
# -- x----------------x --


# Flashcard Modules
# -- x----------------x --
from  .database import connect_database, close_db_connection
import Modules.crud_functions_cards_table as cfct 
import Modules.crud_functions_themes_table as cftt
# -- x----------------x --

# -- ENVIRONMENT VARIABLES
# -- x-------------------------------------x --
DEFAULT_TEXT_INPUT = ""
DEFAUL_TEXT_AREA = ""
# DEFAULT_SELECTEBOX = 
# DEFAULT_MULTISELECT = 

# -- x-------------------------------------x --




# -- PAGE 0 - HOME
# -- x-------------------------------------x --
# Define a function that initialize the page 0

# -- x-------------------------------------x --




# -- PAGE 1 - FLASCARDS
# -- x-------------------------------------x --
# Define a function that initialize the page 1
def init_flashcards_page():
    """ Initialize flashcards page """


    # Help Debugging
    print(f"[init_flashcards_page] have been run !")
# -- x-------------------------------------x --





# -- PAGE 2 - STATISTICS
# -- x-------------------------------------x --
# Define a function that initialize the page 2
def init_stat_page():
    """ Initialize statistics page """

    # Help Debugging
    print(f"[init_stat_page] have been run !")
# -- x-------------------------------------x --




# -- PAGE 3 - CONFIGURATION
# -- x-------------------------------------x --
# Define a function that initialize the page 3
def init_config_page():
    """ Initialize configiguration page """

    # Card part 
    # -- x--------------x --
    # Load cards list from the database
    if "cards" not in st.session_state:
        cards = cfct.get_all_cards()
        # Format cards
        cards = [{key:cards[key][idx] for key in cards.keys()} for idx in range(len(cards['id']))]
        #print(f'\n[CARDS]:\n {cards}\n')
        st.session_state.cards = cards
        #print(f'\n[CARDS]:\n {st.session_state.cards}\n')

    # Create keys to initialise form 
    if "form_create_card_version" not in st.session_state:
        st.session_state.form_create_card_version = 0
        # Create keys to initialise form 
    if "form_update_card_version" not in st.session_state:
        st.session_state.form_update_card_version = 0
    # -- x--------------x --




    # Add theme part 
    # -- x--------------x --
    # Load theme list within the session
    if "themes" not in st.session_state:
        # Extract the themes from the databae and format them into a dataframe
        #themes_df = pd.DataFrame.from_dict(cftt.get_all_themes())
        # Save the dataframe within the session 
        #st.session_state.themes =  themes_df
        
        # Extract the themes from the database and save it into the sessions
        st.session_state.themes = cftt.get_all_themes()

    # Help Debugging
    #print(f'\n[THEMES]: {st.session_state.themes}\n')

    # Add a key for the input field
    if "new_theme" not in st.session_state:
        st.session_state.new_theme = ""

    # Initialize add theme button 
    if "new_theme_correct" not in st.session_state:
        st.session_state.new_theme_correct = False
    # -- x--------------x --


    # Update theme part
    # -- x--------------x --
    # Initialize a select box default value
    #if "theme_to_update" not in st.session_state:
    #    st.session_state.theme_to_update = {"id":None, "theme":None}

    # Initialize a key for the input field
    if "new_input_theme" not in st.session_state:
        st.session_state.new_input_theme = ""

    # Initialize a text input correct value
    if "correct_theme_to_update" not in st.session_state:
        st.session_state.correct_theme_to_update = False
    # -- x--------------x --




    # Remove theme part
    # -- x--------------x --
    # Inialize multiselect to remove themes
    if "remove_themes" not in st.session_state:
        st.session_state.remove_themes = []
    # -- x--------------x --



    # Help Debugging
    print(f"[init_config_page] have been run !")
# -- x-------------------------------------x --



# Define a function that initialise the app
def app_initialization():
    """ Initialize the app """

    print("\nStart app initialization !")

    # Run each table page initialization
    init_flashcards_page()
    init_stat_page()
    init_config_page()

    print("End app initialization !\n")
    
