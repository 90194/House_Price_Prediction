import joblib
import pandas as pd
import numpy as np
from pathlib import Path

directory = Path(__file__).resolve().parent
#載入模型
def recog_digit(datas):
    with open(directory/'xgb_model_tpe_500m_v2.pkl', 'rb') as model_file:
        model = joblib.load(model_file)
    #datas = [ParkingSpace,Floor_Arabic,HouseAge,TransactionYear,Bedrooms,LivingRooms,Bathrooms,TotalArea,Num_Garbage,Num_Hospital,Num_Metro,Num_Railway,
    #Num_Primary_School,Num_Sec_School,D_100,D_103,D_104,D_105,D_106,D_108,D_110,D_111,D_112,D_114,D_115,D_116,Material,Type_1,Type_2,Type_3,Type_4,Elevator,Management]
    arr1 = np.array(datas)
    arr1_reshaped = arr1.reshape(1, 33)
    return model.predict(arr1_reshaped)
