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
import Modules.database as db
import Modules.crud_functions_cards_table as cfct
import Modules.crud_functions_themes_table as cftt
import Modules.statistics as stat
# -- x----------------x --


# -- x-------------------------------------x --




# -- SCRIPT TO TEST dataset.py SCRIPT
# -- x-------------------------------------x --
# Initialise 
#db.init_db()
# -- x-------------------------------------x --



# -- SCRIPT TO TEST crud_functions_cards_table.py SCRIPT
# -- x-------------------------------------x --
# Create 3 cards
#cfct.create_card("What is the capital of France ?", "Paris", "1", 2)
#cfct.create_card("What is the capital of Great Britain ? ", "London", "1", 7)
#cfct.create_card("What is the capital of Australia ?", "Camberra", "1", 6)
#cfct.create_card("What is the capital of the USA ?", "Washington D.C", "1", 9)

# Get a card
#card = cfct.get_card(2)

# Update a card 
#cfct.update_card(3, "What is my Australian prefered destination ?", 'Sydney', 0.5, 9)

# Remove a card
# cfct.delete_card(2)

# Extract all cards
#cards = cfct.get_all_cards()
#print(cards)


# Get the number of card of the deck
#total_number = cfct.get_number_of_cards()
#print(total_number)



# Get the number of cards from a category
#cards = cfct.get_cards_by_theme('9')
#print(cards)
# -- x-------------------------------------x --




# -- SCRIPT TO TEST crud_functions_themes_table.py SCRIPT
# -- x-------------------------------------x --
# Add new themes
#cftt.create_theme("English")
#cftt.create_theme("Math")

# Get a theme 
#theme = cftt.get_theme(10)
#print(theme)

# Update a theme 
#cftt.update_theme(10, "Español")

# Remove a theme 
cftt.delete_theme(10)

# Extract all the themes
#themes = cftt.get_all_themes()
#print(themes)
# -- x-------------------------------------x --




# -- SCRIPT TO TEST statistsics.py functions
# -- x-------------------------------------x --
# Test to create and update today stats
#stat.update_stats(True)

# Test to update a card probability
#stat.update_card_probability(2, False)

# Get all statistics
#print(stat.get_stats()) 
# -- x-------------------------------------x --