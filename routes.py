from aiohttp import web

from email_views import create_email, delete_email, read_email, update_email
from user_emails_views import read_user_emails
from user_views import create_user

routes = [
    web.post("/create_email", create_email, name='create_email'),
    web.post("/read_email", read_email, name='read_email'),
    web.post("/update_email", update_email, name='update_email'),
    web.post("/delete_email", delete_email, name='delete_email'),

    web.post("/read_user_emails", read_user_emails, name='read_user_emails'),

    web.post("/create_user", create_user, name='create_user'),
]
