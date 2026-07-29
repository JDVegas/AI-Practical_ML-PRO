# -- CRUD FUNCTION CARDS TABLE --


# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
# Standard libraries
from typing import Dict

# SQL libraries
import sqlite3


# -- x----------------x --


# Flashcard functions
# -- x----------------x --
from  database import connect_database, close_db_connection
# -- x----------------x --

# -- x-------------------------------------x --



# -- FUNCTIONS
# -- x-------------------------------------x --
# Define a function to create a card 
def create_card(question: str, response: str, probability: float, id_theme: int):
    """ Function that allow to create a new card 
    
        Args : 
            question (str) : the question to ask to the user
            response (str) : the expected answer
            probability (float) : the good/wrong answer ratio 
            id_theme (int) : the theme the card is related to
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Insert data into the database to create a card
    cursor.execute('''
        INSERT INTO cards (question, response, probability, id_theme) 
        VALUES (?, ?, ?, ?);
    ''', (question, response, probability, id_theme))

    # Database closing protocol
    close_db_connection(conn)




# Define a function to get and return a card 
def get_card(id: int) -> Dict:
    """ Get and return a card

        Args : 
            id (int) : the card id we want to get
        
        Outputs : 
            card_dict (Dict) : the card we want to get
    """

    # Connect to the database
    conn, cursor = connect_database()

    # Extract the card that we want 
    cursor.execute(f'''
        SELECT * FROM cards WHERE id = {id}
    ''')

    # Extract the selected element
    card = cursor.fetchone()

    # Format data 
    # -- x----------------x --
    # Extract columns names 
    #col_names = [desc[0] for desc in cursor.description]
    #print(f"col_names: {col_names}")

    # Extract data from the cursor and format it into a dictionary 
    card_dict = {cursor.description[idx][0]: col for idx, col in enumerate(card)}
    #print(f"card_dict: {card_dict}")

    # -- x----------------x --

    # Database closing protocol
    close_db_connection(conn)

    return card_dict




# Define a function to update a card
def update_card(id: int, question: str, response: str, probability: float, id_theme: int):
    """ Update a card
        
        Args :
            id (int): the card unique identifier
            question (str): the question to ask the user
            response (str): the expected answer
            probability (float): the correct answer probability
            id_theme (int): the theme the card is related to
    """

    # Connect to the database
    conn, cursor = connect_database()

    # Update the card
    """cursor.execute(f'''
        UPDATE cards
        SET
            question = '{question}'
            , response = '{response}'
            , probability = {probability}
            , id_theme = {id_theme}
        WHERE id = {id};
    ''')"""

    # Other version that should be prefered with SQLite
    cursor.execute('''
            UPDATE cards
            SET
                question = ?
                , response = ?
                , probability = ?
                , id_theme = ?
            WHERE id = ?;
        ''', (question, response, probability, id_theme, id))

    # Display the modification
    print("\nThe card have been properly updated !\n")

    # Database closing protocol
    close_db_connection(conn)



# Define a function to remove a card from the deck
def delete_card(id: int):
    """ Remove a card from the deck

        Args :
            id (int): the id of the card that must be removed
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Remove a card
    cursor.execute('''
        DELETE FROM cards WHERE id = ?;
    ''', (id,))
    # Display a message 
    print(f"\nThe card {id} have been properly removed from the deck !\n")

    # Database closing protocol
    close_db_connection(conn)


# Define a function to get all cards
def get_all_cards() -> Dict:
    """ Retrieve all the cards of the deck

        Returns :
            cards_dict (Dict) : a dictionary containing all the cards of the deck
    """

    # Connect to the database
    conn, cursor = connect_database()

    # Extract all the cards from the deck
    cards = cursor.execute('''
        SELECT * from cards;
    ''')

    # Fetch the selected elements from the cursor
    cards = cursor.fetchall()
    

    # Extract all cards from the result and format them into a dictionary
    # -- x------------------------x --
    # Format as a dictionary of lists --> {'id': [...], 'question': [...], ...}
    cards_dict = {col[0]:[card[idx] for card in cards] for idx, col in enumerate(cursor.description)} 
    # --> Probably the better option as more compact
   
    # Format as a list of dictionaries --> [{'id':value, 'question':value, ...}, {'id':value, ...}, ...]
    #cards_dict = list(map(lambda x: {cursor.description[idx][0]: col for idx, col in enumerate(x)}, cards)) # 
    
    #print('\n', cards_dict)
    # -- x------------------------x --

    # Database closing protocol
    close_db_connection(conn)

    return cards_dict



# Define a function to get the number of cards 
def get_number_of_cards() -> int:
    """ Compute and return the total number of cards

        Returns :
            total_number (int) : The total number of cards of the deck 
    """

    # Connect to the database
    conn, cursor = connect_database()

    # Get the number of cards of the deck
    total_number = cursor.execute('''
    SELECT COUNT(*) FROM cards; 
    ''')

    # Extract the info from the cursor result
    total_number = total_number.fetchone()[0]

    # Database closing protocol
    close_db_connection(conn)

    return total_number


# Define a function that returns the card according to a selected theme
def get_cards_by_theme(id_theme: int) -> Dict:
    """ Extract all the cards for a specific theme

        Args : 
            id_theme (int) : the unique identifier of a theme

        Returns : 
            theme_cards_dict (Dict) : all the cards related the indicated theme
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Extract the cards from the database
    cards = cursor.execute('''
    SELECT * FROM cards
    WHERE id_theme = ?
    ''', (id_theme,))

    # Extract the data from the cursor result
    cards = cards.fetchall()

    # Format the data 
    cards_dict = {col[0]:[card[idx] for card in cards] for idx, col in enumerate(cursor.description)} 

    # Database closing protocol
    close_db_connection(conn)

    return cards_dict



# -- x-------------------------------------x --

