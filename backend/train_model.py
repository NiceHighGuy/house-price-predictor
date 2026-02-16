from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("house_price_model.pkl")

# Define input format
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {"message": "House Price Prediction API Running 🚀"}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    input_data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]])

    prediction = model.predict(input_data)

    return {
        "predicted_price": round(float(prediction[0]), 3)
    }
