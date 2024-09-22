import logger
import os 
from datetime import datetime


## Create a log file with the name of this point of thime 
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), "LOGS")

os.makedirs(log_path, exist_ok=True)