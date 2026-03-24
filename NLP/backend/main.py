from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_sense

app = FastAPI()


# Input schema
class InputData(BaseModel):
    sentence: str
    word: str


@app.get("/")
def home():
    return {"message": "ContextSense AI API Running 🚀"}


@app.post("/predict")
def predict(data: InputData):
    result = predict_sense(data.sentence, data.word)
    return result