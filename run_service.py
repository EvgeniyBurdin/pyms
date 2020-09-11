""" Скрипт запуска сервера.
"""
from aiohttp import web

from middlewares import json_server
from routes import routes
from service import pg_storage
from settings import SERVICE_HOST, SERVICE_PORT


app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)

storages = [pg_storage, ]

# Обеспечим старт и корректное закрытие всех хранилищ
app.cleanup_ctx.extend([storage.setup for storage in storages])


web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
