""" Модуль настройки сервера.
"""
from aiohttp import web

from middlewares import json_server
from routes import routes
from settings import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                      POSTGRES_PORT, POSTGRES_USER)

from connections import AsyncPGConnect, AsyncPGConnectParams
from storages import AsyncPostgresStorage


# Хранилище PostgreSQL -------------------------------------------------------

pg_connect_params = AsyncPGConnectParams(
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD
)

pg_connect = AsyncPGConnect(pg_connect_params)
pg_storage = AsyncPostgresStorage(pg_connect.create())


# Экземпляр приложения aiohttp -----------------------------------------------

storages = [pg_storage, ]


app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)

# Обеспечим корректное закрытие всех хранилищ
app.on_cleanup.extend(storage.close for storage in storages)
