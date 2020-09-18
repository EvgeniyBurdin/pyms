from aiohttp import web

from views import read, create

routes = [
    web.post("/read", read, name='read'),
    web.post("/create", create, name='create'),
]
