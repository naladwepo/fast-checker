from fastapi import FastAPI
from ai_model import predict
from telegram_bot import send_message

app = FastAPI()

@app.get("/predict")
def get_prediction(data: str):
    result = predict(data)
    return {"prediction": result}

@app.post("/telegram")
def handle_telegram(message: dict):
    response = send_message(message)
    return {"status": "success", "response": response} 