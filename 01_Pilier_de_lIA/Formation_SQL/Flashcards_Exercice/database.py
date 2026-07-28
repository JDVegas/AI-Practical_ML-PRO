# --  CREATE THE FLASHCARDS PROJECT DATABASE --


# -- SETUP
# -- x-------------------------------------x --
# Srandard libraries 
from typing import Tuple

# Libraries sql
import sqlite3

# -- x-------------------------------------x --



# FUNCTIONS
# -- x-------------------------------------x --

# Function to connect to the database
def connect_database() -> Tuple:
    """ Connect database and generate a cursor """ 
    # Create a connexion to the database
    conn = sqlite3.connect("flashcards.db")

    # Activate the foreign_keys parameters 
    conn.execute("PRAGMA foreign_keys = ON;")

    # Display a message
    print("\nConnection to the database is operational !\n")

    # Create a cursor to execute sql requests
    cursor = conn.cursor()

    return (conn, cursor)

# Function to save and disconnect the database
def close_db_connection(conn):
    """ Save the modification done and properly close the database connection """
    # Validate modifications
    conn.commit()
    # Close the connection
    conn.close()
    # Display a message
    print('\nThe database connexion have been properly closed !\n')


# Function to initialise the database
def init_db():
    """Function that create the database tables and populate with a set of default themes """

    # Connect to database and create cursor
    conn, cursor = connect_database()

    # CREATE TABLES
    # -- x----------------x --

    # Create CARDS table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INT PRIMAARY KEY
            , question TEXT STRICT
            , response TEXT STRICT
            , probability REAL STRICT
            , id_theme INT STRICT
            , FOREIGN KEY (id_theme) REFERENCES themes(id) ON DELETE RESTRICT
        );
    ''')

    # Create THEMES table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS themes (
            id INT PRIMARY KEY
            , theme TEXT STRICT NOT NULL
        );
    ''')

    # Create STATS table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INT STRICT PRIMARY KEY
            , good_answers INT STRICT
            , wrong_answers INT STRICT
            , date DATE
        );
    ''')
    # -- x----------------x --



    # POPULATE THEMES TABLE
    # -- x----------------x --
    cursor.execute('''
        INSERT INTO themes (id, theme) VALUES
        (1, 'Python')
        , (2, 'SQL')
        , (3, 'Pandas')
        , (4, 'Visualization')
        , (5, 'MLOps')
        , (6, 'Streamlit')
        , (7, 'Math')
        , (8, 'Machine_Learning')
        , (9, 'Deep_Learning');
    ''')

    # -- x----------------x --


    # CLOSING PROTOCOL
    close_db_connection(conn)


# -- x-------------------------------------x --
