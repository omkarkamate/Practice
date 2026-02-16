import pandas as pd
import pymysql
from dotenv import load_dotenv
from src.ML_Project.Exception import CustomException
from src.ML_Project.logger import logging
import os
import sys
from src.ML_Project.Exception import CustomException

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('database')

def Read_Data_From_Mysql():
    # logging.info("Reading data from MySQL database")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db
            )
        
        df=pd.read_sql_query("SELECT * FROM students",mydb)
        print(df.head())
        return df   
    
    except Exception as e:
        raise CustomException(e,sys)   