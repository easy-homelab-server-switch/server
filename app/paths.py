import os

from constants import APP_DATA_DIR_NAME

def get_app_data_dir() -> str:
    base_dir = os.getcwd()
    data_dir = os.path.join(base_dir, APP_DATA_DIR_NAME)

    os.makedirs(data_dir, exist_ok=True)

    return data_dir