from aiohttp import web

from views import simple

routes = [
    web.post("/simple", simple, name='simple'),
]
