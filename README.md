# 🏠 House Price Predictor (Full Stack ML Project)

A **Full Stack Machine Learning Web Application** that predicts house prices based on user input features.  
This project includes:

✅ Machine Learning Model (Scikit-Learn)  
✅ FastAPI Backend API  
✅ React Frontend UI  
✅ End-to-End Project Structure  

---

## 🚀 Project Overview

This project predicts house prices using a trained Machine Learning model based on the **California Housing Dataset**.  
Users can enter housing-related features like median income, house age, location coordinates, etc., and the model returns the predicted price.

---

## 🛠 Tech Stack Used

### Frontend
- React.js (Vite)
- HTML / CSS
- Fetch API

### Backend
- FastAPI
- Python
- Scikit-learn
- Joblib
- NumPy

### Machine Learning
- Regression Model trained on dataset
- Saved model using `.pkl`

---

## 📂 Folder Structure

house-price-predictor/
│
├── backend/
│ ├── main.py
│ ├── train_model.py
│ ├── house_price_model.pkl
│
├── frontend/
│ ├── src/
│ ├── package.json
│ ├── vite.config.js
│
├── .gitignore
├── .gitattributes
└── README.md


---

## ⚙️ Features

- Predict house prices based on 8 input parameters
- FastAPI backend for prediction API
- React frontend UI for user interaction
- Clean project structure suitable for GitHub & LinkedIn showcase

---

## 🧠 Input Features Used

| Feature | Description |
|--------|-------------|
| MedInc | Median income in block group |
| HouseAge | Average age of houses |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Population in block group |
| AveOccup | Average occupants per household |
| Latitude | Latitude coordinate |
| Longitude | Longitude coordinate |

---

## 🖥️ Sample Input Values (For Testing)

Use these values in the frontend:

MedInc: 5
HouseAge: 20
AveRooms: 6
AveBedrms: 1
Population: 1000
AveOccup: 3
Latitude: 34
Longitude: -118


---

## 🏃‍♂️ How to Run the Project Locally

### ✅ Step 1: Clone Repository



git clone https://github.com/NiceHighGuy/house-price-predictor.git
cd house-price-predictor

cd backend

python -m venv venv

venv\Scripts\activate

source venv/bin/activate

pip install fastapi uvicorn joblib numpy scikit-learn

uvicorn main:app --reload

Backend will start at:
📌 http://127.0.0.1:8000

---

Frontend Setup (React)

Open new terminal and go to frontend folder

cd frontend

Install Node Modules

npm install

Start Frontend

npm run dev

Frontend will start at:

http://localhost:5173

---

{
  "MedInc": 5,
  "HouseAge": 20,
  "AveRooms": 6,
  "AveBedrms": 1,
  "Population": 1000,
  "AveOccup": 3,
  "Latitude": 34,
  "Longitude": -118
}

{
  "predicted_price": 20228949
}


📌 Output
The model returns the predicted price in INR format, displayed on the frontend.

Example:

✅ Predicted Price: ₹2,02,28,949


📌 Output
The model returns the predicted price in INR format, displayed on the frontend.

Example:

✅ Predicted Price: ₹2,02,28,949

🎯 Future Improvements

Add better UI/UX styling

Deploy backend using Render / Railway

Deploy frontend using Vercel

Add model performance metrics (RMSE, MAE)

Add feature scaling pipeline

👨‍💻 Author

Prem Yelwande
2nd Year B.Tech Student | AI/ML & Data Science Enthusiast
GitHub: https://github.com/NiceHighGuy

