import os
from pathlib import Path

APP_NAME = "Grimlock"
APP_VERSION = "0.1.0"
CONFIG_DIR = ".grimlock"

def get_app_name() -> str:
    return APP_NAME

def get_app_version() -> str:
    return APP_VERSION

def get_app_work_dir() -> str:
    return os.getcwd()

def get_app_author() -> str:
    return "AQJS4"

def get_app_config_dir() -> Path:
    config_dir = Path.home() / CONFIG_DIR

    config_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    return config_dir
