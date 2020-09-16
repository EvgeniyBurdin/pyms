""" Скрипт запуска сервера.
"""
from aiohttp import web

from middlewares import json_server
from routes import routes
from service import storage
from settings import SERVICE_HOST, SERVICE_PORT

app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)

services = [storage, ]

# Обеспечим старт и корректное закрытие всех подключений
app.cleanup_ctx.extend([service.setup for service in services])


web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
