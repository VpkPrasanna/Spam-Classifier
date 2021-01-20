import config
import model
from fastapi import FastAPI, File, UploadFile
from model import BERTBaseUncased
from inference import sentence_prediction
import torch.nn as nn
import time
import torch
import uvicorn

app = FastAPI()

MODEL = model.BERTBaseUncased()
MODEL.load_state_dict(torch.load("results(2)/model.bin",map_location=torch.device('cpu')))
MODEL.to(config.DEVICE)
MODEL.eval()


@app.post("/predict")
def predict(sentence):
    start_time = time.time()
    positive_prediction = sentence_prediction(MODEL,sentence)
    negative_prediction = 1 - positive_prediction
    temp = None
    if positive_prediction > negative_prediction:
        temp = "Ham"
    else:
        temp = "Spam"
    response = {}
    response["response"] = {
        "Ham": str(positive_prediction),
        "Spam": str(negative_prediction),
        "sentence": str(sentence),
        "time_taken": str(time.time() - start_time),
        "Result":str(temp)
    }
    return response

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)