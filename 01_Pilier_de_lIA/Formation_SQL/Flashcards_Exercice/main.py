# -- MAIN SCRIPT --




# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
# Libraries sql
import sqlite3



# -- x----------------x --

# Flashcard functions
# -- x----------------x --
import database as db
import crud_functions_cards_table as cfct
# -- x----------------x --


# -- x-------------------------------------x --




# -- SCRIPT
# -- x-------------------------------------x --
# Initialise 
#db.init_db()

# Create 3 cards
#cfct.create_card("What is the capital of France ?", "Paris", "1", 2)
#cfct.create_card("What is the capital of Great Britain ? ", "London", "1", 7)
#cfct.create_card("What is the capital of Australia ?", "Camberra", "1", 6)

# Get a card
#card = cfct.get_card(2)

# Update a card 
#cfct.update_card(3, "What is my Australian prefered destination ?", 'Sydney', 0.5, 9)

# -- x-------------------------------------x --