from src.ML_Project.Exception import CustomException
from src.ML_Project.Component.Data_ingestion import DataIngestion
from src.ML_Project.logger import logging
import sys
if __name__=="__main__":
    try:
        logging.info("Data ingestion initiated")
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e,sys)