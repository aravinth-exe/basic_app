import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def index():
    data_source = load_iris()
    df = pd.DataFrame(data=data_source.data, columns=data_source.feature_names)
    # Convert the top 5 rows to a list of dicts for JSON response
    return df.head(5).to_dict(orient='records')
