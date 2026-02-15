import os
import sys
from src.ML_Project.Exception import CustomException
from src.ML_Project.logger import logging
from src.ML_Project.util import Read_Data_From_Mysql
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','raw_df.csv')
    test_data_path: str=os.path.join('artifacts','train_df.csv')
    raw_data_path: str=os.path.join('artifacts','test_df.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df=Read_Data_From_Mysql()
            logging.info("Read the dataset from mysql")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) 
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Saved the raw data to artifacts folder")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,)
            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Split the data into train and test and saved it to artifacts folder")

        except Exception as e:
            raise CustomException(e,sys)
