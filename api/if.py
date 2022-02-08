from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import StringIO
import pickle
import os


from pipeline.preprocess import get_preprocessed

ifr = FastAPI()

# Routes
# @ifr.get("/")
# async def index():
#    return {"api_name": "Isolation Forest"}


@ifr.post("/")
async def create_upload_file_if(sensor_data: UploadFile = File(...)) -> pd.DataFrame:
    #read from csv
   dframe = pd.read_csv(StringIO(str(sensor_data.file.read(), 'utf-8')), encoding='utf-8')
   #preprocess data
   dframe = get_preprocessed(dframe)
   #define x
   X = dframe.iloc[:, 0:1]
   #X = X.dropna()
   
   #load model
   loaded_model = pickle.load(open('./models/model_if.pkl', 'rb'))
   #make prediction
   y_pred = loaded_model.predict(X)

   res = pd.concat([X.reset_index(), pd.DataFrame(data=y_pred, columns=['PredictedAnamoly'])], axis=1)
   res['timestamp'] = pd.to_datetime(res['timestamp'])
   res = res.set_index('timestamp')

   res['PredictedAnamoly'] = res['PredictedAnamoly'].map(
                   {1:'1' , -1:'-1'})
   #print(res['PredictedAnamoly'].value_counts())

   res['machine_status'] = dframe['machine_status']
   print(res)

   # filepath = "./data/uploads/ifr.csv"
   # res.to_csv(os.path.abspath(filepath), index=False)
   
   # return {"csv": os.path.abspath(filepath)}

   return {"df_len": res.size}