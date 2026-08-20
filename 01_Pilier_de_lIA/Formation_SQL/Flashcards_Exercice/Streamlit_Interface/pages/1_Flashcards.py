# -- FIRST PAGE : FLASHCARDS --





# -- SETUP
# -- x-----------------------------------------x --

# Load libraries
# -- x-------------------------x --
# Standard libraries
import sys
import math
import random
from typing import List, Dict
from itertools import islice
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
import Modules.statistics as stat
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
    st.session_state.selected_theme_cards = [{key:cards[key][idx] for key in cards.keys()} for idx in range(len(cards['id']))]

    # Help debugging 
    print(f"[selected_theme_cards]:\n{st.session_state.selected_theme_cards}")

    # Update the theme in the session
    st.session_state.selected_theme = theme_index[theme_id]

    # Display a message to the users to indicate that the card are well loaded
    if st.session_state.selected_theme_cards :
        st.toast(f"The card related to the theme '{theme_index[theme_id]}' have been properly loaded. The Deck contains {len(st.session_state.selected_theme_cards)} cards.")


# Define a plumbing function to prepare the deck to stury
def session_deck_to_study(num_cards_to_study: int):
    """ Plumbig function to build the deck with the cards from the theme the user want to study 
    
        Args :
            num_cards_to_study (int): the number of card the user want to study during a specific session
    """
    # IF .. the amount of card to study is changing, then update the session value
    if num_cards_to_study != st.session_state.number_cards_to_study:
        st.session_state.number_cards_to_study = num_cards_to_study


    # Order the card from the `selected_theme_cards` according to their probability
    sorted_cards_by_prob =  sorted(st.session_state.selected_theme_cards, key=lambda item: item["probability"], reverse=True)
    #sorted_cards_by_prob =  sorted(st.session_state.cards, key=lambda item: item["probability"], reverse=True)

    #print(f"\n[sorted_cards_by_prob]: {sorted_cards_by_prob}\n")
    #print(f"\n[sorted_cards_by_prob]: {type(sorted_cards_by_prob)}\n")


    # Define the number of cards to extract
    # -- x------------x --
    # 60 % must be the less known cards
    wrongly_known_number = math.ceil(num_cards_to_study*0.6)
    # 30 % must be well know card to study them back
    well_known_number = math.ceil((num_cards_to_study - wrongly_known_number)*0.3)
    # 10 % must be new news cards : 
    new_cards_number = num_cards_to_study - wrongly_known_number - well_known_number

    # Help debuggin 
    print(f"\n[wrongly_known_number]: {wrongly_known_number} | [well_known_number]: {well_known_number}\n")
    # -- x------------x --


    # Extract wrongly known cards
    wrongly_know_cards = [item for item in sorted_cards_by_prob if item["probability"] < 0.8]
    # Extract well known cards
    well_know_cards = [item for item in sorted_cards_by_prob if item["probability"] >= 0.8]
    # Extract new cards
    #new_cards = [item for item in sorted_cards_by_prob if item["new"] == True]



    # Select the cards for the session   : MUST BE UPDATED AND ADJUSTED WHEN THE BOOLEAN COLUMN WILL BE CREATED WITHIN DATABASE
    # -- x------------x --
    # 60 % must be the less known cards
    training_session_cards = wrongly_know_cards[:wrongly_known_number]
    #print(len(training_session_cards))
    # 30 % must be well know card to study them back
    training_session_cards += random.sample(
        well_know_cards
        , well_known_number if well_known_number < len(well_know_cards) else len(well_know_cards)
    )
    # 10 % must be new news cards : 
    #training_session_cards += random.sample(sorted_cards_by_prob, num_cards_to_study-len(training_session_cards))
    training_session_cards += random.sample(sorted_cards_by_prob, min(num_cards_to_study, len(training_session_cards)))

    # Help debugging
    print("\nNumber of card within the session deck: ", len(training_session_cards))
    print("Current session deck:\n", training_session_cards)


    # 10 % must be new news cards : 
    # -> Think about adding a boolean column into the card table to indicate the new cards
    # -- x------------x --

    return training_session_cards


# Define a function to start a session
def start_session():
    """ Indicate that the session has started """
    st.session_state.learning_session_running = True


# Define a function to save user answers and return results
def save_and_go_next(answers: str): #-> Dict[List[(bool, str)]]:
    """  Plumbing function that allow to update the current card probability
    
        Args :
            answers (str): the user answers list

        Return: 
            result (): the session results
    """

    # Iterate through each answer
    for id, answer in answers:
        print(f"\n[ID]: {id} | [Answer]: {answer}\n")

    '''
        # Define a match case structure
        match answer:
            case "correct":
                # Update card probability
                stat.update_card_probability(id, True)
                # Update stats
                stat.update_stats(True)
            case "no_idea":
                # Update card probability
                stat.update_card_probability(id, False)
                # Update stats
                stat.update_stats(False)
            case "wrong":
                # Update card probability
                stat.update_card_probability(id, False)
                # Update stats
                stat.update_stats(False)

    # Update the selected cards in case the user would do another learning session 
    load_cards_by_theme(selected_theme['id'])
    '''


    
    

# Define a function to switch card
def next_card(answer: dict):
    """ Plumbing function that allow to change card """
    # Update the learning_session_answers table
    st.session_state.learning_session_answers.append(answer)
    print(f"\n{st.session_state.current_card} - [answer_list]: {st.session_state.learning_session_answers}\n")


    # Increment the current_card value
    st.session_state.current_card += 1
    # Reset the show_answer variable
    st.session_state.show_answer = False
    print(f"\n[CURRENT CARD NUMBER after next_card function]: {st.session_state.current_card}\n")


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
    if selected_theme != st.session_state.selected_theme:
        load_cards_by_theme(selected_theme['id'])
        # Help debugging
        print(f"\n[selected_theme_cards]: {st.session_state.selected_theme_cards}\n")

        

    #st.write("Chopse the number of cards to study:")
    # Create a list for sliders
    #range_cards_to_study = list(range(5, 50, 5))
    # Instantiate a slider to choose the number of card to study each session
    num_cards_to_study = st.slider(
        label="Choose the number of cards to study:"
        , min_value=5
        , max_value=50
        , value=st.session_state.number_cards_to_study
        , step=5
    )

    # IF .. the number of cards to study change OR the theme to study change, then rebuild the deck
    if num_cards_to_study != st.session_state.number_cards_to_study \
        or selected_theme != st.session_state.selected_theme:

        # Call the function to prepare the deck to study for the session
        training_session_cards = session_deck_to_study(num_cards_to_study)

    
    # -- x------------x --








# -- x-----------------------------------------x --









# -- PAGE CONTAINT
# -- x-----------------------------------------x --
st.title("Flashcards")

# Insert Space below the title
#st.write("##")
st.markdown("<br>", unsafe_allow_html=True)

# IF .. a theme is selected, then indicat its name
if selected_theme["theme"] != "":
    #print("THEME SELECTED")

    
    st.markdown(f"<b><u>THEME</u>: {selected_theme['theme']}<b>", unsafe_allow_html=True) 
    st.markdown(f"This theme contains {len([card for card in st.session_state.cards if card['id_theme'] == selected_theme['id']])} cards")

    st.write("<br>", unsafe_allow_html=True)

    # Create 3 columns
    col1, col2, col3 = st.columns((1, 3, 1))

    if  st.session_state.learning_session_running:

        # Create 3 columns
        #col1, col2, col3 = st.columns((1, 3, 1))

        # Renitialiaze the training session 
        #st.session_state.current_card = 0
        # Initialize the answer list
        #answer_list = []
        

        # Build the column elements 
        with col2:


            # Build a container to display a card shape
            with st.container(border=True, height=300, width="stretch"
                            , horizontal_alignment="center"
                            , vertical_alignment="top"):
                

                #st.markdown(f"""<h1 style="background-color:powderblue;">My_theme</h1>""",unsafe_allow_html=True) 
                # Build a container without border to display the question
                with st.container(height="stretch", width="stretch"
                                , horizontal_alignment="center"
                                , vertical_alignment="center"):   


                    # Help debugging 
                    print(f"\n[CURRENT CARD NUMBER]: {st.session_state.current_card}\n")

                    # IF .. the user did not ask to see the answer, then only display the question
                    if not st.session_state.show_answer:   
                        st.markdown(f"<p style='text-align:center;'>{training_session_cards[st.session_state.current_card]['question']}</p>", unsafe_allow_html=True)
                    # ELSE .. the user asked to see the answer, thenk show the question and the answer
                    else : 
                        st.markdown(f"<p style='text-align:center;'>{training_session_cards[st.session_state.current_card]['question']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='text-align:center;'>{training_session_cards[st.session_state.current_card]['response']}</p>", unsafe_allow_html=True)

            # Define a button to let the user see the answer to check if he found the correct one
            st.button(label="Show answer", width="stretch", on_click=toggle_answer)


            # Define three columns to contain 3 buttons, 1 button each 
            # The user will have to indicate of he found the correct answer in his head
            subcol21, subcol22, subcol23 = st.columns(3)

     

            # Define a button s
            with subcol21: 
                # Define a button that will answer the specified answer
                st.button(
                    label="Correct"
                    , width="stretch"
                    , on_click=next_card
                    , args = (
                        {
                            "id": training_session_cards[st.session_state.current_card]["id"]
                            , "answer": "correct"
                        }, 
                    )
                )
       


            with subcol22: 
                # Define a button that will answer the specified answer
                st.button(
                    label="No Idea"
                    , width="stretch"
                    , on_click=next_card
                    , args = (
                        {
                            "id": training_session_cards[st.session_state.current_card]["id"]
                            , "answer": "no_idea"
                        }, 
                    )
                )

            with subcol23: 
                # Define a button that will answer the specified answer
                st.button(
                    label="Wrong"
                    , width="stretch"
                    , on_click=next_card
                    , args = (
                        {
                            "id": training_session_cards[st.session_state.current_card]["id"]
                            , "answer": "wrong"
                        }, 
                    )
                )

            print(f"[answer_list]: {st.session_state.learning_session_answers}")

            # Update the session learning_session_answers
            #st.session_state.learning_session_answers = answer_list

            # IF .. all the training session deck have been explored, then stop the session
            if len(training_session_cards) == st.session_state.current_card:
                st.session_state.learning_session_running = False


    elif not st.session_state.learning_session_running and st.session_state.learning_session_answers:
        print("BOB")

    else:
        with col2:
            st.button(label="Start Session", width="stretch", on_click=start_session)
