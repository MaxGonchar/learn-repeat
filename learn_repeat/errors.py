import logging
from datetime import datetime


def error_logger(func):
    def wrapper():
        try:
            func()
        except Exception as error:
            logging.basicConfig(filename='../error_log.txt')
            logging.debug(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                          f' - {str(error)}')
    return wrapper
