# -- STATISTICS FUNCTIONS --


# -- SETUP
# -- x-------------------------------------x --

# LIBRARIES
# -- x----------------x --
# Standard libraries
from typing import Dict
import datetime as dt

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
# Def a function to create or update daily statistics 
def update_stats(is_correct:  bool):
    """ Create and update daily statistics 
    
        Args:
            is_correct (bool) : describe if the user answer is correct or not 
    """

    # Connect to the database
    conn, cursor = connect_database()   

    # Get and format today's date 
    today = dt.datetime.now().strftime('%Y-%m-%d')

    try :
        # Check if there is a date within the database
        stat_row = cursor.execute('''
            SELECT * FROM stats WHERE date = ?;
        ''', (today, ))
    except Exception as e:
        print(f"Select request Exception: {e}")
        #raise Exception(e)

    # Extract the selected row
    stat_row = stat_row.fetchone()

    # IF .. a stat already exists then update it 
    if stat_row:
        # Extact answers 
        good_answers = stat_row[1]
        wrong_answers = stat_row[2]

        # IF .. is_correct is true then increment good_answer
        if is_correct:
            good_answers +=1
        # ELSE .. is_correct is false then invrement wrong_answer
        else: 
            wrong_answers +=1

        try : 
            # Update the row 
            cursor.execute('''
                UPDATE stats
                SET good_answers = ? 
                , wrong_answers = ?
                WHERE id = ?
            ''', (good_answers, wrong_answers, stat_row[0]))
        except Exception as e:
                print(f"Update request Exception: {e}")

    # ELSE .. no stat exists, then initialize it
    else :
        # Initialise answers
        good_answers = 1 if is_correct else 0
        wrong_answers = 0 if is_correct else 1 

        try:
            # Create a new stat 
            cursor.execute('''
                INSERT INTO stats (good_answers, wrong_answers, date)
                VALUES 
                    (?, ?, ?)
            ''', (good_answers, wrong_answers, today))
        except Exception as e:
                print(f"Insert request Exception: {e}")


    # Database closing protocol
    close_db_connection(conn)




# Define a function to update a card probability 
def update_card_probability(card_id: int, is_correct: bool):
    """ Update a card probability
    
        Args : 
            card_id (int) : the card unique identifier 
            is_correct (bool) : indicate if the answer given is correct or not 
    """
    # Connect to the database
    conn, cursor = connect_database()   

    try : 
        # Extract current probability 
        card = cursor.execute('''
            SELECT * FROM cards WHERE id = ?
        ''', (card_id,)).fetchone()
    except Exception as e:
        print(f"Select request Exception: {e}")

    # Extract probability
    proba = card[3]

    # IF .. answer is TRUE then reduce proba
    if is_correct:
        new_proba = proba * 0.9
    # ELSE .. answer is FALSE then increade proba
    else :
        new_proba = proba * 1.1

    # Control that new proba is limited
    new_proba = max(0.1, min(new_proba, 1.0))

    try:
        # Update the proba 
        cursor.execute('''
            UPDATE cards
            SET probability = ?
            WHERE id = ?;
        ''', (new_proba, card_id))
    except Exception as e:
        print(f"Update request Exception: {e}")


    # Database closing protocol
    close_db_connection(conn)







# Def a function to retrieve all statistics 
def get_stats() -> Dict:
    """ Get and return all statistics 
    
        Returns :
            statistics (Dict) : All the statistics 
    """
    # Connect to the database
    conn, cursor = connect_database()   


    # Extract all the statistics from the database
    stats = cursor.execute('''
        SELECT * FROM stats ORDER BY date DESC
    ''')
    # Extract data from results
    stats = stats.fetchall()

    # Format extraction into a dictionary 
    statistics = { stat[0]:{col[0] : stat[idx] for idx, col in enumerate(cursor.description[1:], 1)} for stat in stats }
    # Database closing protocol
    close_db_connection(conn)

    return statistics

# -- x-------------------------------------x --
