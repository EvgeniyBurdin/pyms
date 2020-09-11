"""
    Скрипт запуска сервера.
"""

from main import app
from aiohttp import web

from settings import SERVICE_HOST, SERVICE_PORT


web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
