import logging
import os
from datetime import datetime

# name of specific log file
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
# generally appending any log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# path of that specific log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[%(asctime)s - %(module)s : %(lineno)d - %(levelname)s - %(message)s",
                    level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging has started")
