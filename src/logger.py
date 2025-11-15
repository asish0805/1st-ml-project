import logging
import os
import sys
from datetime import datetime
from exception import CustomException   # <<< important

# ---------------- LOGGING SETUP ---------------- #

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
)

def get_logger(name: str = __name__):
    """
    Returns a logger that logs to both file & console
    without repeating handlers.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
        )
        logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    logger = get_logger(__name__)
    logger.info("Logger has been configured.")

    try:
        logger.info("Testing ZeroDivisionError...")
        x = 1 / 0                          # <<< intentional error
    except ZeroDivisionError as e:
        logger.error("An error occurred: %s", e)
        raise CustomException(e, sys)
