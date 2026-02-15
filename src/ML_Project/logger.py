import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

file_name = f"{datetime.now().strftime('%d-%m-%y_%H-%M-%S')}.log"

log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Logger initialized successfully")
