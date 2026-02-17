import pandas as pd
from src.ML_Project.logger import logging
from src.ML_Project.Exception import CustomException
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
import os
import pickle

@dataclass
class Model_Training_Config:
    model_path=os.path.join("artifacts","trained_Model.pkl")

class Model_Training:
    def __init__(self):
        self.model_training_config=Model_Training_Config()

    def initiate_model_training(self,X_train,y_train,X_test,y_test):
        logging.info("Model training initiated")
        try:
            models={
                "Linear Regression":LinearRegression(),
                "KNN Regressor":KNeighborsRegressor(),
                "Decision Tree Regressor":DecisionTreeRegressor(),
                "SVR":SVR(),
                "Random Forest Regressor":RandomForestRegressor(),
                "Gradient Boosting Regressor":GradientBoostingRegressor(),
                "AdaBoost Regressor":AdaBoostRegressor()
            }

            model_report={}

            for i in range(len(models)):
                model=list(models.values())[i]
                model.fit(X_train,y_train)

                y_train_pred=model.predict(X_train)
                y_test_pred=model.predict(X_test)

                train_model_score=r2_score(y_train,y_train_pred)
                test_model_score=r2_score(y_test,y_test_pred)

                model_report[list(models.keys())[i]]=test_model_score

            best_model_score=max(model_report.values())
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            logging.info(f"Best model found on both training and testing dataset is {best_model_name} with r2 score of {best_model_score}")
            print(f"Best model found on both training and testing dataset is {best_model_name} with r2 score of {best_model_score}")

            with open(self.model_training_config.model_path,"wb") as f:
                pickle.dump(best_model,f)
            
        except Exception as e:
            raise CustomException(e,sys)
