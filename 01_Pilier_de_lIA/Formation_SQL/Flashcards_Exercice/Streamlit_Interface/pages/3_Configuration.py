# -- THIRD PAGE : CONFIGURATION --





# -- SETUP
# -- x-----------------------------------------x --

# Load libraries
# -- x-------------------------x --
# Standard libraries
import sys
from pathlib import Path
from typing import Dict, List
import pandas as pd

# Visualization libraries
import streamlit as st
# -- x-------------------------x --

# Load functions
# -- x-------------------------x --
# Manually force project modules path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from Modules.app_initialization import app_initialization, init_config_page
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



# Help Debugging
#print(f'\n[THEMES]: {st.session_state.themes}\n')



# -- FUNCTIONS
# -- x-----------------------------------------x --

# CARDS FUNCTIONS
# -- x-------------------x --
# Define a function to create a card
def new_card(question: str, answer: str, theme_id: int):
    """ Plumbing function that allow to 
    
        Args : 
            question (str) : the question that will be asked to the user
            answer (str) : the correct answer to the question
            theme_id (int): the theme to assign to the card 
    """

    try:
        cfct.create_card(question=question, response=answer, probability=0.5, id_theme=theme_id)
    except Exception as e:
        print(f"Error `new_card` function: {e}")

    # Update fields
    #st.session_state.form_selectbox = {"id":10, "theme":""}

    # Update cards within the session
    updated_cards = cfct.get_all_cards()
    st.session_state.cards = [{key:updated_cards[key][idx] for key in updated_cards.keys()} for idx in range(len(updated_cards['id']))]
    #print(f"\n[SESSION]: {st.session_state.cards}\n")

    # Rerun the streamlit page as form behavior prevent my table from refresh
    #st.rerun()
    
    # Inform the user
    st.toast("The new card have been properly added to the database", duration="short")
    


# Define a function to remove cards
def remove_cards(card_ids: List[int]):
    """ Plumbing function that allow to remove one or multiple cards. 

        Args:
            cards (List[int]) : a list of dict contaning all the cards to remove     
    """

    # Iterate through each card 
    for id in card_ids:
        try:
            cfct.delete_card(id)
        except Exception as e:
            print(f"Error `delete_theme` function : {e}")

        # Update cards within the session
        updated_cards = cfct.get_all_cards()
        st.session_state.cards = [{key:updated_cards[key][idx] for key in updated_cards.keys()} for idx in range(len(updated_cards['id']))]
        

        # Inform the user
        st.toast(f"The card(s) with the id '{id}' have been properly removed from the database", duration="short")
# -- x-------------------x --




# THEME FUNCTIONS
# -- x-------------------x --
# Def a plumbing function to add new theme
def add_theme(new_theme: str):
    """ Plumbing function that allow to add new themes 
     
        Args : 
            new_theme (str): the new theme to create
    """

    try :
        # Add the new theme to the database
        cftt.create_theme(new_theme)
    except Exception as e:
        print(f"Error `create_theme` function : {e}")

    # Update themes withtin the session 
    st.session_state.themes = cftt.get_all_themes()
    # Reset text_input field updating new_theme variable
    st.session_state.new_theme = ""
    # Reinitialize the new_theme_correct variable
    st.session_state.new_theme_correct = False

    # Inform the user
    st.toast("The theme have been properly added to the database", duration="short")



# Def a plumbing function to update themes 
def update_theme(id:int, new_theme: str):
    """ Plumbing function that allow to update a theme 
    
        Args:
            id (int): the id of the theme to update
            new_theme (str): the the to update
    """
    try:
        cftt.update_theme(id, new_theme)
    except Exception as e:
        print(f"Error `update_theme` function : {e}")

    # Update themes withtin the session 
    st.session_state.themes = cftt.get_all_themes()
    # Reset the text input field
    st.session_state.new_input_theme = ""
    # Reset the correct_theme_to_update variable
    st.session_state.correct_theme_to_update = False

    # Inform the user
    st.toast("The theme have been properly updated into the database", duration="short")



# Def a plumbing function to remove themes 
def remove_themes(themes: Dict):
    """ Plumbing function that allow to remove a bunch a themes
     
        Args :
            themes (List[Dict]) : a list of themes to remove
    """
    # Iterate through each theme to remove
    for theme in themes: 
        try:
            # Remove the current theme
            cftt.delete_theme(theme['id'])
        except Exception as e:
            print(f"Error `delete_theme` function : {e}")

    # Update themes withtin the session 
    st.session_state.themes = cftt.get_all_themes()
    # Reset remove_theme variable
    st.session_state.remove_themes = []

    # Inform the user
    st.toast("The theme(s) have been properly removed from the database", duration="short")



# -- x-------------------x --

# -- x-----------------------------------------x --







# -- PAGE CONTAINT
# -- x-----------------------------------------x --
st.title('CONFIGURATION')

# Create a table 
tab1, tab2 = st.tabs(["Card Management", "Theme Management"])


# CARD MANAGEMENT
# -- x-------------------x --
with tab1 : 
    st.subheader('CARD MANAGEMENT')
    
    st.markdown("<h3><u>Existing Cards</u></h3>", unsafe_allow_html=True)
    # Create a dataframe from tje theme list save into the session
    cards_df = pd.DataFrame(st.session_state.cards)
    # Display the existing themes
    st.dataframe(cards_df)



    # Expandable section to create a card 
    with st.expander("Create a card"):
        """
        NOTE : I here used a formular for the experimentation but it woudl have been easier to simply
        add widgets to take the user input and a button to apply the function. With keys, 
        each field woudld have been cleaned after running the function
        """
        with st.form("Create_card"):
            # Ask the user to choose a theme
            #one_select = st.selectbox(label="Choose a theme", options=st.session_state.themes[["theme", "id"]].sort_values(by=["theme"]))
            one_select = st.selectbox(
                            label="Choose a theme"
                            , options=st.session_state.themes
                            , format_func=lambda x: x["theme"]
                            #, key="form_selectbox"
                        )

            # Help debugging 
            #print(f'\n[one_select]: {one_select}\n')

            # Instantiate the field to ger the user question and answer
            question = st.text_input("Question")
            answer = st.text_area("Answer")

            #submit_button = st.form_submit_button(
            #        label= "Submit"
            #        , on_click=new_card
            #        , args=(question, answer, one_select["id"])
            #        #, on_click=cfct.create_card(question, answer, 0.5, one_select["id"])
            #        #, disabled=not (bool(question) and bool(answer))
            #    )
            submit_button = st.form_submit_button(label="Submit")

        # IF .. the form have been submitted
        if submit_button:
            # IF .. the answer is missing, then display a message 
            if bool(question) and not bool(answer.strip()):
                st.warning("An answer is missing. The card can not be created")
            # ELIF .. the question is missing, then display a message
            elif not bool(question.strip()) and bool(answer):
                st.warning("An question is missing. The card can not be created")
            # ELIF .. the two fields are missing, then ...
            elif not bool(question.strip()) and not bool(answer.strip()):
                st.warning("The question and its answer are missing. The card can not be created")
            # ELSE .. both fields are filled,then create the card
            else:
                new_card(question.strip(), answer.strip(), one_select['id'])
                # Rerun the streamlit page as form behavior prevent my table from refresh
                st.rerun()


    # Expandable section to update a card
    with st.expander("Update a card"):
        st.write("alice")



    # Expandable section to remove a card 
    with st.expander("Remove cards"):

        with st.container():

            with st.container(height=600):

                # Initialise a checked list
                checked_cards = []

                # Iterate through each card 
                for card in st.session_state.cards:
                    with st.container(border=True):

                        col1, col2 = st.columns([5, 1])

                        col1.markdown(f"<p>Theme: {theme_index[card['id_theme']]}</p>", unsafe_allow_html=True)
                        #with col2: 
                        #    toggled = st.toggle(label="Update", value=False, label_visibility="hidden", key= "toggle_"+str(card['id']) )
                        with col2:
                            checked = st.checkbox(label="Remove", value=False, label_visibility="hidden", key="checkbox_"+str(card['id']) )
                            

                        st.markdown(f"<p style='text-align:center;'>{card['question']}</p>", unsafe_allow_html=True)
                        st.markdown(f"<p style='text-align:center;'>{card['response']}</p>", unsafe_allow_html=True)

                    # IF .. the card have been selected then add it to the list 
                    if checked:
                        checked_cards.append(card['id'])
                    # ELIF .. if the card is unselected, after being selected then remove it 
                    elif not checked and card['id'] in checked_cards:
                        checked_cards.remove(card['id'])

        print(f"\n[Checked_cards]: {checked_cards}\n")

                    
                        #st.markdown(f"""
                        #                {card["question"]}\n
                        #                {card['response']}
                        #                ---
                        #            """)
                    
        st.button(
            label="Remove selected cards"
            , on_click=remove_cards
            , args=(checked_cards,)
            , disabled=not checked_cards
        )

                


# -- x-------------------x --









# THEME MANAGEMENT
# -- x-------------------x --
with tab2 : 
    st.subheader('THEME MANAGEMENT')

    st.markdown("<h3><u>Existing Themes</u></h3>", unsafe_allow_html=True)
    # Create a dataframe from tje theme list save into the session
    themes_df = pd.DataFrame(st.session_state.themes)
    # Display the existing themes
    st.dataframe(themes_df)


    st.markdown("<h3><u>Operations</u></h3>", unsafe_allow_html=True)

    # Expandable section to create a new theme 
    with st.expander("Create a theme"):
        text_input = st.text_input("Write a new theme", key="new_theme").strip()
        #print(f'\n[Text Input]: {text_input}\n')
  

        # IF .. the theme does not already exists then add it to the list
        if text_input and not text_input.lower() in [x.lower() for x in themes_df["theme"].to_list()]:

            # Allow thrfe theme to be added 
            st.session_state.new_theme_correct = True
            # Inform the user
            st.success("The theme does not exist within the list. It can be added.")

        # ELIF .. the theme does not exist, then block the button and inform the user
        elif text_input and text_input.lower() in [x.lower() for x in themes_df["theme"].to_list()]:
            st.session_state.new_theme_correct = False
            st.warning("The theme already exists withtin the list. It can not be added")

        # Add buttons
        left, middle, _ = st.columns(3)
        left.button(label="Add the theme"
                    , on_click=add_theme
                    , args=(text_input, )
                    , disabled=not st.session_state.new_theme_correct
                    )
        # CAUTION : THIS IS NOT ALLOWED  
        #if middle.button(label="Reset field containt"):
        #    st.session_state.new_theme = ""


        
    # Expandable section to update a theme
    with st.expander("Update a theme"):
        # Instantiate a select box
        update_theme_select = st.selectbox(
            "Select a theme to update"
            , options=st.session_state.themes
            , format_func=lambda x: x["theme"]
            #, key="theme_to_update"
        )

        # Instantiate a text input widget
        new_theme_to_update = st.text_input("Write down what is the new theme name", key="new_input_theme") 

        # IF .. the new theme does not exist then update the selected theme
        if update_theme_select and new_theme_to_update \
            and not new_theme_to_update.lower() in [theme.lower() for theme in themes_df["theme"].to_list() if theme != update_theme_select["theme"]]:
            st.session_state.correct_theme_to_update = True   
            st.success("The new name can be used")      
        # ELIF .. the new theme already exists then inform the user
        elif update_theme_select and new_theme_to_update \
            and new_theme_to_update.lower() in [theme.lower() for theme in themes_df["theme"].to_list() if theme != update_theme_select["theme"]]:
            st.session_state.correct_theme_to_update = False   
            st.warning("The new name already exist. It can not be used")      


        # Instantiate a button to update the theme
        st.button(
            label="Update the theme"
            , on_click=update_theme
            , args=(update_theme_select["id"], new_theme_to_update)
            , disabled=not st.session_state.correct_theme_to_update
        )



    # Expandable section to remove a theme 
    with st.expander("Remove a theme"): 
        # Instantiate a multiselector widget
        multiselect_rm_themes = st.multiselect(
                                    "Select one or multiple theme(s) to remove"
                                    , st.session_state.themes
                                    , format_func= lambda x :x['theme']
                                    , key="remove_themes"
                                )


        # Add buttons
        st.button(label="Remove selected theme(s)"
                    , on_click=remove_themes
                    , args=(multiselect_rm_themes, )
                    , disabled=not bool(multiselect_rm_themes)
                )
                            
# -- x-------------------x --



# -- x-----------------------------------------x --