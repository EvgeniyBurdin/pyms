from aiohttp import web

from settings import SERVICE_HOST, SERVICE_PORT
from middlewares import json_server
from routes import routes


app = web.Application(middlewares=[json_server], client_max_size=4*1024*1024)

app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app, host=SERVICE_HOST, port=SERVICE_PORT)
