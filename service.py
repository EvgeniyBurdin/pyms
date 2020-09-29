""" Модуль настройки используемых сервером сущностей.
"""
from connections import AsyncpgConnectionParams, AsyncpgsaConnection
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)
from storages import AsyncpgsaStore

# Хранилище на PostgreSQL ----------------------------------------------------

pg_connection_params = AsyncpgConnectionParams(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    db=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

storage = AsyncpgsaStore(
    connection=AsyncpgsaConnection(pg_connection_params),
)
