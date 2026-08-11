# -- CRUD FUNCTION CARDS TABLE --


# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
# Standard libraries
from typing import Dict, List

# SQL libraries
import sqlite3


# -- x----------------x --


# Flashcard functions
# -- x----------------x --
from  .database import connect_database, close_db_connection
# -- x----------------x --

# -- x-------------------------------------x --






# -- FUNCTIONS
# -- x-------------------------------------x --
# Def a function to create a theme 
def create_theme(theme: str):
    """ Add a new theme within the table 
    
        Args:
            theme (str) : The new theme to add
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Add the theme to the database only if it does not already exists 
    cursor.execute('''
        INSERT OR IGNORE INTO themes(theme)
        VALUES (?);
    ''', (theme, ))


    # Database closing protocol
    close_db_connection(conn)



# Def a function to get a theme 
def get_theme(id_theme: int) -> Dict:
    """ Extract a theme from its ID

        Args :
            id_theme (int) : the theme id 
    
        Returns : 
            theme (Dict) : a dictionary containing the theme and the ID
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Extract a theme from the database
    theme = cursor.execute('''
        SELECT * FROM themes WHERE id = ?;
    ''', (id_theme,))

    # Extract the theme from the cursor output
    theme = theme.fetchone()

    # Convert the theme into a dict
    theme = {cursor.description[idx][0]: col for idx, col in enumerate(theme)}

    # Database closing protocol
    close_db_connection(conn)

    return theme



# Define a function to update a theme 
def update_theme (id_theme: int, theme :str):
    """ Update a theme 
    
        Args :
            id_theme (int) : the unique identifier of the theme
            theme (str) :  the theme name
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Update the theme 
    cursor.execute('''
        UPDATE themes
        SET theme = ?
        WHERE id = ?;
    ''', (theme, id_theme))

    # Database closing protocol
    close_db_connection(conn)



# Def a function to remove a card
def delete_theme (id_theme: int):
    """ Remove a theme from the table
    
        Args :
            id_theme (int) : the id of the theme to remove
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Remove the theme
    cursor.execute('''
        DELETE FROM themes
        WHERE id = ?;
    ''', (id_theme, ))
    

    # Database closing protocol
    close_db_connection(conn)



# Def a function to get all themes
def get_all_themes () -> List[Dict]:
    """ Get all themes
    
         Returns :
            themes (List[Dict]) : A dictionary containing all the themes 
    """
    # Connect to the database
    conn, cursor = connect_database()

    # Extract all the themes from the database
    themes = cursor.execute('''
        SELECT * FROM themes ORDER BY theme ASC
    ''')

    # Extract the themes from the cursor result
    themes = themes.fetchall()

    # Help debugging 
    print(f'\n[THEMES]: {themes}\n')

    # Format the output
    # -- x--------------x --
    #themes = {[cursor.description[idx][0]] for theme in themes for idx, col in enumerate(theme)}
    # Format data into a dict like : {'id':[1, 2, 3, ...], `theme`:[theme_1, theme_2, theme_3, ...]}
    #themes = {col[0]:[theme[idx] for theme in themes] for idx, col in enumerate(cursor.description) }
    # Format data into a dict a simple mapping : {theme:id, theme:id, ... }
    #themes = {item[1]:item[0] for item in themes}
    # Format data into a dict format like : [{"id":1, "theme":theme_1}, {"id":2, "theme":theme_2}, ...]
    themes = [{col[0]: theme[idx] for idx, col in enumerate(cursor.description)} for theme in themes]

    # -- x--------------x --


    # Database closing protocol
    close_db_connection(conn)

    return themes


# -- x-------------------------------------x --
