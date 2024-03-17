import logging
from pythonjsonlogger import jsonlogger


def setup_logging(logs_output_file, logger_name):

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    formatter = jsonlogger.JsonFormatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s", "%m-%d-%Y %H:%M:%S")

    # add logs to file
    file_logger = logging.FileHandler(logs_output_file, 'a')
    file_logger.setFormatter(formatter)
    logger.addHandler(file_logger)

    # add logs to terminal
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(formatter)
    logger.addHandler(console_logger)