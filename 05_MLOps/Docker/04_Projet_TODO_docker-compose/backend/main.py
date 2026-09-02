

# -- SETUP -- 
# -- x---------------------------------------x --
# Standard libraries
import os
import time

# Backend libraries
import psycopg2
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

# -- x---------------------------------------x --



# -- SCRIPT -- 
# -- x---------------------------------------x --

# Instantiate a FastAPI App
app = FastAPI()

# Define an API key to get Environment variable 
API_KEY = os.getenv("API_KEY")
print(f"API KEY loaded from environment variable : {API_KEY}")



# Define the data model class (validation) 
class Item(BaseModel):
    name: str


# Define a function to connect to the database
def get_db_connection():
    while True:
        try:
            # Open a connection to the database using the DB URL (contained into a environment variable)
            conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            return conn 
        except psycopg2.OperationalError:
            print("The DB is not ready yet, new trial in 2 sec ...")
            time.sleep(2)



# Initialise starting table
@app.on_event("startup")
def startup():
    # Get the connector to the database
    conn = get_db_connection()

    # Use the db cursor to execute SQL request
    with conn.cursor() as cur:
        # Create the item table
        cur.execute("CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT)")
        # Commit the new table
        conn.commit()

    # Close the connection 
    conn.close()


# Function to extract all existing items from the table `items`
@app.get("/items")
def read_items():
    # Get the connector to the database
    conn = get_db_connection()

    # Use the db cursor to execute SQL request
    with conn.cursor() as cur:
        # Extract name columns from items table
        cur.execute("SELECT name FROM items")
        # Extract the name into a list
        items = [row[0] for row in cur.fetchall()]

    # Close the connection 
    conn.close()
    return items


# Function to add new items to the table `items`
@app.post("/items")
def create_item(item: Item):
    # Get the connector to the database
    conn = get_db_connection()

    # Use the db cursor to execute SQL request
    with conn.cursor() as cur:
        # Insert an item into the table items
        cur.execute("INSERT INTO items (name) VALUES (%s)", (item.name,))
        # Commit the change 
        conn.commit()

    # Close the connection 
    conn.close()
    return {"message": "Item added"}
