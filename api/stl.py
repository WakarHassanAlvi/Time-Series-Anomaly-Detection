from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import StringIO

from pipeline.preprocess import get_preprocessed, sample_sensor_data
from pipeline.training import stl_model, get_anomalies, get_indexed_df, get_anomaly_limits


stl_decomposition = FastAPI()

# Routes
@stl_decomposition.post("/")
async def create_upload_file_stl(coef: str, sensor_data: UploadFile = File(...)):
   
   #read from csv
   df = pd.read_csv(StringIO(str(sensor_data.file.read(), 'utf-8')), encoding='utf-8')
   #preprocess data
   dframe = get_preprocessed(df)
   #define x
   df = dframe.iloc[:, 0:1]

   sampled_df = sample_sensor_data(df)
   stlData = stl_model(sampled_df)
   l, u = get_anomaly_limits(stlData.resid, coef)
   anomalies = get_anomalies(stlData.resid, sampled_df, l, u)
   anomalies = anomalies.reset_index()
   anomalies_list = anomalies.values.tolist()
   dfsensor = get_indexed_df(sampled_df, 0)
   dfsensor = dfsensor.reset_index()
   dfsensor_list = dfsensor.values.tolist()

   return {"anomalies_df_list": anomalies_list, "sensor_df_list": dfsensor_list}
