"""
    Скрипт запуска сервера.
"""
from aiohttp import web

from service import app
from settings import SERVICE_HOST, SERVICE_PORT


web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
