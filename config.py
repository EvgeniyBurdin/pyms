import os

if os.getenv("PYMS_SERVICE_DEV") == "1":
    # Если запуск сервиса сделать так:
    # $ PYMS_SERVICE_DEV=1 python main.py
    # то загрузятся переменные среды из "env/develop.env"
    from pathlib import Path
    from dotenv import load_dotenv
    load_dotenv(Path("env/develop.env"), override=True, verbose=True)

PYMS_ENV_VARS_PREFIX = os.getenv("PYMS_ENV_VARS_PREFIX", "")

SERVICE_NAME = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_NAME")
SERVICE_HOST = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_HOST")
SERVICE_PORT = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_PORT")

POSTGRES_HOST = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_HOST")
POSTGRES_PORT = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_PORT")
POSTGRES_USER = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_PASSWORD")
