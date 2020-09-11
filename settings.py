import os

# Инициализация переменных среды (используется, например, при разработке) ----

if os.getenv("PYMS_SERVICE_DEV") == "1":
    # Если запуск сервиса сделать так:
    # $ PYMS_SERVICE_DEV=1 python run_service.py
    # то загрузятся переменные среды из "env/develop.env"
    from pathlib import Path
    from dotenv import load_dotenv
    load_dotenv(Path("env/develop.env"), override=True, verbose=True)


# Загрузка переменных среды --------------------------------------------------

PYMS_ENV_VARS_PREFIX = os.getenv("PYMS_ENV_VARS_PREFIX", "")

SERVICE_NAME = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_NAME")
SERVICE_HOST = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_HOST")
SERVICE_PORT = os.getenv(f"{PYMS_ENV_VARS_PREFIX}SERVICE_PORT")

POSTGRES_DB = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_DB")
POSTGRES_HOST = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_HOST")
POSTGRES_PORT = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_PORT")
POSTGRES_USER = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv(f"{PYMS_ENV_VARS_PREFIX}POSTGRES_PASSWORD")


# Формирование урла подключения к БД Постгрес --------------------------------

class DatabaseSettingsError(Exception):
    pass


def get_postgres_connection_url() -> str:
    """ Собирает ссылку для подключения к БД и возращает её.
    """
    db = POSTGRES_DB
    host = POSTGRES_HOST
    port = POSTGRES_PORT
    user = POSTGRES_USER
    password = POSTGRES_PASSWORD

    if not all([db, host, port, user, password]):
        raise DatabaseSettingsError(
            "Not all database connection settings are specified: "
            f"{[db, host, port, user, password]}."
        )

    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


POSTGRES_CONNECTION_URL = get_postgres_connection_url()
