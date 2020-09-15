""" Модуль настройки используемых сервером сущностей.
"""
from connections import AsyncPGConnection, AsyncPGConnectionParams
from storages import AsyncSaPostgresCRUDStorage
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)

# Подключение к PostgreSQL ---------------------------------------------------

pg_connection_params = AsyncPGConnectionParams(
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD
)

pg_storage = AsyncSaPostgresCRUDStorage(
    connection=AsyncPGConnection(pg_connection_params)
)
