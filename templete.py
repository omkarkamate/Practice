import os
import logging
from pathlib import Path

project_name="ML_Project"

logging.basicConfig(level=logging.INFO)

files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/util.py",
    f"src/{project_name}/Component/__init__.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/Exception.py",
    f"src/{project_name}/Component/Data_ingestion.py",
    f"src/{project_name}/Component/Data_processing.py",
    f"src/{project_name}/Component/Data_Training.py",
    f"src/{project_name}/Component/Monitoring.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/Training_pipeline.py",
    f"src/{project_name}/pipeline/Prediction_pipeline.py",
    "requirements.txt",
    "setup.py"
    ".env"
]


for file in files:
    file_path = Path(file)
    file_dir,file_name=os.path.split(file_path)

    if(file_dir!=""):
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir}") 

    if(not os.path.exists(file_path)):
        with open(file_path,"w") as f:
            pass
        logging.info(f"Creating file: {file}")
    else:     logging.info(f"File already exists: {file}")    