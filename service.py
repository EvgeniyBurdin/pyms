""" Модуль настройки используемых сервером сущностей.
"""
from connections import AsyncPGConnection, AsyncPGConnectionParams
from storages import AsyncPostgresSQLAlchemyCore
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)

# Хранилище на PostgreSQL ----------------------------------------------------

pg_connection_params = AsyncPGConnectionParams(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    db=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

storage = AsyncPostgresSQLAlchemyCore(
    connection=AsyncPGConnection(pg_connection_params)
)
