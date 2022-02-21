""" 
ML App

Author: Luis Sedas
Date: Feb 2022
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pandas.core.frame import DataFrame
import pandas as pd
import numpy as np
import joblib
from starter.data import process_data
from starter.model import inference
import starter.utils as utils

app = FastAPI()

model = joblib.load('model/model.joblib')
encoder = joblib.load('model/encoder.joblib')
lb = joblib.load('model/lb.joblib')

@app.get("/")
async def hello():
    """docstring"""
    return {"message":"Welcome to Earth!"}


class Data(BaseModel):
    """docstring"""
    age: int
    workclass: str
    education: str
    marital_status: str = Field(alias='marital-status')
    occupation: str
    relationship: str
    race: str
    sex: str
    hours_per_week: int = Field(alias='hours-per-week')
    native_country: str = Field(alias='native-country')

    class Config:
        schema_extra = {
            "example": {               
                "age": 39,
                "workclass": "State-gov",
                "education": "Bachelors",
                "marital-status": "Never-married",
                "occupation": "Adm-clerical",
                "relationship": "Not-in-family",
                "race": "White",
                "sex": "Male",
                "hours-per-week": 40,
                "native-country": "United-States"              
            }
        }    


@app.post("/")
async def new_inference(data: Data):
    
    data_to_predict_dict = data.dict(by_alias=True)
    data_to_predict = pd.DataFrame(data_to_predict_dict, index=[0])

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    X, _, _, _ = process_data(
        data_to_predict,
        categorical_features=utils.cat_features,
        encoder=encoder,
        lb=lb,
        training=False
    )

    y_pred = inference(model, X)

    predicted_class = lb.inverse_transform(y_pred)[0]

    return {"prediction": predicted_class}