from src.ML_Project.Exception import CustomException
from src.ML_Project.Component.Data_ingestion import DataIngestion
from src.ML_Project.logger import logging
import sys
import os
import pandas as pd
from src.ML_Project.Component.Data_processing import Data_Processing
from src.ML_Project.Component.Model_Training import Model_Training
import pickle



if __name__ == "__main__":
    try:
        with open("artifacts/Processed_data.pkl", "rb") as file:
            preprocessor = pickle.load(file)

        data = {}
        data["gender"]=[input("Enter gender :")]
        data["race/ethnicity"] = [input("Enter race/ethnicity :")]
        data["parental level of education"] = [input("Enter parental level of education :")]
        data["lunch"] = [input("Enter lunch type :")]
        data["test preparation course"] = [input("Enter test preparation course :")]
        data["reading score"] = [int(input("Enter reading score :"))]
        data["writing score"] = [int(input("Enter writing score :"))]

        

        df = pd.DataFrame(data)

        # print("Original Input DataFrame:")
        # print(df)

        df_preprocessed = preprocessor.transform(df)

        # print("\nPreprocessed Output:")
        # print(df_preprocessed)
        
        with open("artifacts/trained_Model.pkl", "rb") as file:
            model = pickle.load(file)

        prediction = model.predict(df_preprocessed)
        print(f"Predicted writing score: {prediction[0]}")

    except Exception as e:
        raise CustomException(e, sys)
