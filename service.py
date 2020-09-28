""" Модуль настройки используемых сервером сущностей.
"""
from connections import AsyncpgConnectionParams, AsyncpgsaConnection
from query_builders import SQLAlchemyCoreBuilder
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)
from storages import AsyncpgsaStore
from components import classes as components_classes


# Хранилище на PostgreSQL ----------------------------------------------------

pg_connection_params = AsyncpgConnectionParams(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    db=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

storage = AsyncpgsaStore(connection=AsyncpgsaConnection(pg_connection_params))

# ------

query_builder = SQLAlchemyCoreBuilder()

# ------
methods = {}

for component_class in components_classes:
    component = component_class(storage=storage, query_builder=query_builder)
    methods[f"{component.name}.read"] = component.read
