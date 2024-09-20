from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans

app = FastAPI()

#adding CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# loaded_model = joblib.load('models/academicperformanceprediction.pkl')

class feature(BaseModel):
    features:conlist(float, min_length = 5, max_length = 5)

@app.post('/group')
def predict():
# def predict(data: feature):
    try:
        return 'check'
        #getting standardscaled value from scaler
        # scaler = joblib.load('models/scaler.pkl')
        # features = np.array(data.features).reshape(1, -1)
        # features_reshape = scaler.transform(features)
        # prediction = loaded_model.predict(features_reshape)
        # return (int(prediction))
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))