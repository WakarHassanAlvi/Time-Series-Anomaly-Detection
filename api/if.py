from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import StringIO
import pickle

from pipeline.preprocess import get_preprocessed, impute_missing

ifr = FastAPI()

# Routes
@ifr.get("/")
async def index():
   return {"api_name": "Isolation Forest"}

@ifr.post("/IF")
async def create_upload_file_if(sensor_data: UploadFile = File(...)):
   #read from csv
   df = pd.read_csv(StringIO(str(sensor_data.file.read(), 'utf-8')), encoding='utf-8')
   #preprocess data
   dframe = get_preprocessed(df)
   #define x
   X = dframe.iloc[:, 0:1]
   #X = X.dropna()
   
   #load model
   loaded_model = pickle.load(open('./models/model_if.pkl', 'rb'))
   #make prediction
   y_pred = loaded_model.predict(X)
   predictions = y_pred.tolist()
   
   df = impute_missing(df)
   df['PredictedAnamoly'] = predictions

   df_list = df.values.tolist()

   return {"anomalies_df": df_list}