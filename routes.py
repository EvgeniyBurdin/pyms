from aiohttp import web

from views import main

routes = [
    web.post("/", main, name='main'),
]
