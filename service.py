""" Модуль настройки сервера.
"""
from connections import AsyncPGConnection, AsyncPGConnectionParams
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)
from storages import AsyncPostgresStorage

# Хранилище PostgreSQL -------------------------------------------------------

pg_connect_params = AsyncPGConnectionParams(
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD
)

pg_connect = AsyncPGConnection(pg_connect_params)
pg_storage = AsyncPostgresStorage(pg_connect)
