# --  CREATE THE FLASHCARDS PROJECT DATABASE --


# -- SETUP
# -- x-------------------------------------x --

# Libraries sql
import sqlite3

# -- x-------------------------------------x --



# FUNCTIONS
# -- x-------------------------------------x --
# Function to initialise the database
def init_db():
    """Function that create the database tables and populate with a set of default themes """


    # CONFIGURATION
    # -- x----------------x --
    # Create a connexion to the database
    conn = sqlite3.connect("flashcards.db")

    # Create a cursor to execute sql requests
    cursor = conn.cursor()

    # Display a message
    print("\nConnection to the database is operational !\n")
    # -- x----------------x --



    # CREATE TABLES
    # -- x----------------x --

    # Create CARDS table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INT PRIMAARY KEY
            , reponse TEXT 
            , probability REAL
            , id_theme INT 
            , FOREIGN KEY (id_theme) REFERENCES themes(id) ON DELETE RESTRICT
        );
    ''')

    # Create THEMES table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS themes (
            id INT PRIMARY KEY
            , theme TEXT NOT NULL
        );
    ''')

    # Create STATS table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INT PRIMARY KEY
            , good_answers INT
            , wrong_answers INT
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
    # -- x----------------x --
    # Validate modifications
    conn.commit()
    # Close the connection
    conn.close()
    # Display a message
    print('\nThe database connexion have been properly closed !\n')
    # -- x----------------x --


# -- x-------------------------------------x --
