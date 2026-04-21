from employees import Employee
##from sklearn.preprocessing import pipeline
from fastapi import FastAPI
import pickle
import uvicorn
import pandas as pd
import numpy as np


app = FastAPI()
pickle_in = open("pipeline.pkl", "rb")
pipeline = pickle.load(pickle_in)

@app.post("/predict")
def predict(data: Employee):
    data = data.dict()
    YearsExperience = data["YearsExperience"]
    jobTitle = data["jobTitle"]

    df = pd.DataFrame([[YearsExperience, jobTitle]],
                  columns=["Years Of Experience", "Job Title"])

    prediction = pipeline.predict(df)

    return {"predicted salary is": prediction[0]}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

