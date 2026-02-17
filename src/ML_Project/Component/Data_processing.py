import pandas as pd
from src.ML_Project.logger import logging
from src.ML_Project.Exception import CustomException
import sys
from dataclasses import dataclass
import os
import pickle
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import pickle


@dataclass
class Data_Processing_Config:
    processed_data_path=os.path.join("artifacts","processed_data.pkl")

class Data_Processing:
    def __init__(self):
        self.data_processing_config=Data_Processing_Config()

    def initiate_data_processing(self):
        logging.info("Data processing initiated")
        try:
            num_columns=["reading score","writing score"]
            cat_columns=["gender","race/ethnicity","parental level of education","lunch","test preparation course"]

            # SScaler=StandardScaler()
            # OHE=OneHotEncoder()

            num_pipeline=Pipeline(steps=[
                
                ("imputer",SimpleImputer(strategy="mean")),
                ("scaler",StandardScaler())
            ])

            cat_pipline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("Encoding",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])

            preprocessor=ColumnTransformer([
                ("num_pipeline",num_pipeline,num_columns),
                ("cat_pipeline",cat_pipline,cat_columns)
            ])

            return preprocessor

            
        except Exception as e:
            raise CustomException(e,sys)
        
    def data_priprocessing(self,train_path,test_path):
        try:

            tarin_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)  
            preprocessor=self.initiate_data_processing()

    
            X_train=tarin_df.drop(columns=["math score"])
            y_train=tarin_df["math score"]
            X_test=test_df.drop(columns=["math score"])
            y_test=test_df["math score"]

            X_train=preprocessor.fit_transform(X_train)
            X_test=preprocessor.transform(X_test)

            train_df=np.c_[X_train,np.array(y_train)]
            test_df=np.c_[X_test,np.array(y_test)]

            with open(self.data_processing_config.processed_data_path,"wb") as f:
                pickle.dump((train_df,test_df),f)
            logging.info("Data processing completed")
            return X_train,y_train,X_test,y_test
        except Exception as e:
            raise CustomException(e,sys)
        
        
