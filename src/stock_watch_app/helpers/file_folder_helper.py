import os

from src.stock_watch_app.utils import logger

logging = logger.get_logger(__name__)


def create_directory(folder_path, exist_ok=True, mode=0o777):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=exist_ok, mode=mode)
        # wait for the folder to be created
        while not os.path.exists(folder_path):
            pass
        logging.info(f'Created folder: {folder_path}')
    else:
        logging.info(f'Folder already exists: {folder_path}')


def create_directories(directories: list):
    for directory in directories:
        create_directory(directory)


def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'a').close()
        logging.info(f'Created file: {file_path}')
    else:
        logging.info(f'File already exists: {file_path}')
