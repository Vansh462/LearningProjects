import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

__locations= None
__data_columns=None
__model=None  # writing global here does nothing
# (cpp doesnt have global keyword it just makes use of scope)

def get_estimated_price(location,total_sqft,bath,bhk):
  try:
      loc_index=__data_columns.index(location.strip().lower())
  except:
      loc_index=-1
# we didnt mentioned global here as we arent modifying them
  a=np.zeros(len(__data_columns))
  a[0]=total_sqft
  a[1]=bath
  a[2]=bhk
  if loc_index>=0:
    a[loc_index]=1
  return round(__model.predict([a])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations  # creating global so it doesn't create locals
    global __model

    with open("./artifacts/columns.json",'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations= __data_columns[3:]

    with open("./artifacts/bengaluru_House_Data.pkl",'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts ... done")


if __name__== '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Indira Nagar',1500,2,2))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))