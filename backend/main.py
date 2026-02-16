# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
from ollama import chat  # your AI chat

# ----------------- FastAPI App ----------------- #
app = FastAPI()

# Enable CORS so React frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- AI Chat Endpoint ----------------- #
class AIRequest(BaseModel):
    message: str

@app.post("/ask-ai")
def ask_ai(request: AIRequest):
    response = chat(
        model="llama3",
        messages=[{"role": "user", "content": request.message}]
    )
    return {"reply": response.message.content}

# ----------------- House Price Prediction ----------------- #
class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Load your trained model
model = joblib.load("house_price_model.pkl")  # ensure path is correct

@app.post("/predict")
def predict(data: HouseData):
    features = [[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]]

    # Raw model prediction (usually in 100k USD)
    prediction = model.predict(features)[0]

    # Convert to INR: prediction * 100,000 USD * USD-to-INR rate
    price_inr = float(prediction) * 100000 * 83  # adjust 83 if USD rate changes

    # Round to nearest rupee and return
    return {"predicted_price": round(price_inr, 0)}

# ----------------- Health Check ----------------- #
@app.get("/")
def home():
    return {"message": "AI + House Price Prediction API Running 🚀"}
