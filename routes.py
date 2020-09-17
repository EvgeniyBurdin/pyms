from aiohttp import web

from views import read

routes = [
    web.post("/read", read, name='read'),
]
