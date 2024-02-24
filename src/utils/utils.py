# utils.py

import logging
from datetime import datetime

def setup_logging(log_file_path):
    """
    Sets up logging for the application.

    :param log_file_path: Path to the log file.
    """
    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_message(message, level="info"):
    """
    Logs a message.

    :param message: Message to log.
    :param level: Severity level of the log ('info', 'warning', 'error').
    """
    if level.lower() == "info":
        logging.info(message)
    elif level.lower() == "warning":
        logging.warning(message)
    elif level.lower() == "error":
        logging.error(message)

def current_timestamp():
    """
    Returns the current timestamp in a readable format.

    :return: Current timestamp as a string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def convert_to_utc(local_time):
    """
    Converts local time to UTC.

    :param local_time: Local time as a datetime object.
    :return: UTC time as a datetime object.
    """
    return local_time.astimezone(datetime.timezone.utc)

