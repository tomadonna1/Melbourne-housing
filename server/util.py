import json
from joblib import load
import pickle
import numpy as np

# Global variables
__locations = None
__data_columns = None
__model = None

# Price prediction
def get_estimated_price(location,house_type,distance,bedroom2,bathroom,car,landsize,buildingArea,yearBuilt,lattitude,longtitude):
    try:
        loc_index = __data_columns.index(location.lower())  # Get the index of the location
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = house_type
    x[1] = distance
    x[2] = bedroom2
    x[3] = bathroom
    x[4] = car
    x[5] = landsize
    x[6] = buildingArea
    x[7] = yearBuilt
    x[8] = lattitude
    x[9] = longtitude
    
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2) # round to 2 decimal places


# Return the location names
def get_location_names():
    return __locations

# Loading data from the artifacts file
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    
    # Load the column json
    with open("D:/python projects/Melbourne-housing-main/server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[10:]
    
    # Load the modelS
    with open("D:/python projects/Melbourne-housing-main/server/artifacts/model.pickle", "rb") as f:
        __model = pickle.load(f)
        
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("Airport West", 0, 13.5, 3, 1, 3, 614, 151, 1964, -37, 144))
    print(get_estimated_price("Sunshine West",1, 21.3, 3, 2, 2, 173, 140, 2009, -37, 145))
    
    