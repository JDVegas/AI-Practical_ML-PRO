


# -- SETUP -- 
# -- x------------------------x --
# Standard libraries
import os
import joblib
import pandas as pd
from pathlib import Path

# APIs libraries
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException



# Instantiate the API
app = FastAPI(title="Flight Price API")



# -- Model infos 
# -- x-----------x --
# Load the model at the start
MODEL_PATH = Path('artifacts') / "flight_price_model.joblib"
# Initialise the model variable to None
model = None
# -- x-----------x --



# -- Pydantic schemas : for input data validation
# -- x-----------x --
class FlightRequest(BaseModel):
    airline: str
    source_city: str
    destination_city: str
    departure_time: str
    arrival_time: str
    duration: float
    days_left: int
    stops_label: int
    class_label: str
# -- x-----------x --



# -- Mappings
# -- x-----------x --
STOPS_LABEL_TO_NUM = {"zero": 0, "one": 1, "two_or_more": 2}
CLASS_LABEL_TO_NUM = {"Economy": 0, "Business": 1}
# -- x-----------x --


# -- x------------------------x --










# -- SCRIPT -- ENDPOINTS
# -- x------------------------x --
# Define a function to load model, to which we asscociate the @app decorator
@app.on_event("startup")
def load_model():
    """Allow to load the model as soon s the computer starts up"""
    # Define a global variable 
    global model
    # IF .. the model path does not exist, then raise an error
    if not MODEL_PATH.exists():
        raise RuntimeError(f"The model has not been found at : {MODEL_PATH}") 

    # Load the model
    model = joblib.load(MODEL_PATH)
    print("\nModel loading have been successfull\n")


# Define a function to predict flights prices
@app.post("/predict")
def predict_price(req: FlightRequest):  # Use the defined pydantic input data schema
    # IF .. the model is not loaded, then raise an error
    if not model:
        raise HTTPException(status_code=503, detail="Model not loaded")

    # Transforme the data into a DataFrame to fit model input shape
    input_data = pd.DataFrame([{
        "airline": req.airline
        , "source_city": req.source_city
        , "destination_city": req.destination_city
        , "departure_time": req.departure_time
        , "arrival_time": req.arrival_time
        , "duration": req.duration
        , "days_left": req.days_left
        , "stops_num": STOPS_LABEL_TO_NUM.get(req.stops_label, 0)
        , "class_num": CLASS_LABEL_TO_NUM.get(req.class_label, 0)    
    }])

    try :
        # Infer on the model
        prediction = model.predict(input_data[0])
        # return a dict that will be converted into a JSON
        return {"estimated_price": max(0, float(prediction))}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Define a function to check if the model have been properly loaded
@app.get("/health")
def health_check():
    # IF .. the model is not None, then it must have been loaded,then return healty message 
    if model is not None:
        return {"status":"healty"}

    raise HTTPException(status_code=503, detail="Model loading in progress")


# -- x------------------------x --