from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ml"))

from ml.predict import predict_disease

app = FastAPI()

class RequestData(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Medical Chatbot API is running "}

@app.post("/predict")
def predict(data: RequestData):
    result = predict_disease(data.message)
    return {"prediction": result}