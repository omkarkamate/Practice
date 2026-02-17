from src.ML_Project.Exception import CustomException
from src.ML_Project.Component.Data_ingestion import DataIngestion
from src.ML_Project.logger import logging
import sys
import os
import pandas as pd
from src.ML_Project.Component.Data_processing import Data_Processing
from src.ML_Project.Component.Model_Training import Model_Training
if __name__=="__main__":
    try:
        # data_ingestion=DataIngestion()
        # data_ingestion.initiate_data_ingestion()
        data_processing=Data_Processing()
        X_train,y_train,X_test,y_test=data_processing.data_priprocessing(train_path=os.path.join("artifacts","train_df.csv"),test_path=os.path.join("artifacts","test_df.csv"))
        model_training=Model_Training()
        model_training.initiate_model_training(X_train,y_train,X_test,y_test)
    except Exception as e:
        raise CustomException(e,sys)