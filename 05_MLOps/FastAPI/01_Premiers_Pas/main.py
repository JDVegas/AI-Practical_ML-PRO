


# -- SETUP -- 
# -- x-------------------------------x --
# Standard libraries
import math 

# API libraries
from fastapi import FastAPI, Query, Path
from fastapi.middleware.cors import CORSMiddleware



# Instantiate the FastAPI APP oject
app = FastAPI(
	title = "First Steps With FastAPI"
	, description = "Demo API"
	, version = "1.0.0"
)

# Add middleware
app.add_middleware(
	CORSMiddleware
	, allow_origins=["*"]
)
# -- x-------------------------------x --







# -- SCRIPT -- 
# -- x-------------------------------x --
# Create a function associating a decorator
@app.get("/")
def root():
	return {"message": "Welcome on the API FastAPI"} 


# Create a function to compute the sigmoif of an input value
@app.get("/sigmoid")
def sigmoid(x: float = Query(..., description="Entry value for the sigmoid function")
	, precision: int= Query(4, ge=1, le=10, description="Number of decimals")):
	""" Compute the sigmoid function """
	
	result = 1/(1+math.exp(-x))
	return {
		"input": x
		, "sigmoid": round(result, precision)
	} 


# Create and endpoint using a decorator that require a input parameter id
@app.get("/item/{item_id}")
# Create the function that will get the item from the database 
# This function take the id as parameters
def get_item_by_id(item_id: int =  Path(..., ge=1, description="ID de l'item")):
	"""Rethrieve an item by its ID"""
	# -> My code to connect the database and extract the results 
	return {"item_id":item_id, "name":f"Item numéro {item_id}"}

# -- x-------------------------------x --