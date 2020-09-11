"""
    Модуль настройки сервера.
"""
from aiohttp import web

from middlewares import json_server
from routes import routes

app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)
