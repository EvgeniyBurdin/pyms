""" Скрипт запуска сервера.
"""
from aiohttp import web

from middlewares import json_server
from routes import routes
from service import storage
from settings import SERVICE_HOST, SERVICE_PORT

app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)

service_items = [storage, ]

# Обеспечим настройку всех частей приложения
app.cleanup_ctx.extend([item.setup for item in service_items])


web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
