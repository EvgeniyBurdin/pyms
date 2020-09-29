from aiohttp import web

from views import create_email, delete_email, read_email, update_email

routes = [
    web.post("/create_email", create_email, name='create_email'),
    web.post("/read_email", read_email, name='read_email'),
    web.post("/update_email", update_email, name='update_email'),
    web.post("/delete_email", delete_email, name='delete_email'),
]
