# -- CRUD FUNCTION CARDS TABLE --


# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
import sqlite3

# -- x----------------x --


# Flashcard functions
# -- x----------------x --
from  database import connect_database, close_db_connection
# -- x----------------x --

# -- x-------------------------------------x --



# -- FUNCTIONS
# -- x-------------------------------------x --
# Define a function to ...
def create_card(question: str, response: str, probability: float, id_theme: int):
    """ Function that allow to create a new card 
    
        Inputs : 
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
    '''), (question, response, probability, id_theme)

    # CLOSING PROTOCOL
    close_db_connection(conn)
# -- x-------------------------------------x --

