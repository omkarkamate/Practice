from src.ML_Project.Exception import CustomException
from src.ML_Project.Component.Data_ingestion import DataIngestion
from src.ML_Project.logger import logging
import sys
import os
import pandas as pd
from src.ML_Project.Component.Data_processing import Data_Processing
if __name__=="__main__":
    try:
        # data_ingestion=DataIngestion()
        # data_ingestion.initiate_data_ingestion()
        data_processing=Data_Processing()
        data_processing.data_priprocessing("artifacts/train_df.csv","artifacts/test_df.csv")
    except Exception as e:
        raise CustomException(e,sys)