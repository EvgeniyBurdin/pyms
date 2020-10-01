""" Обработчики запросов для емейлов пользователей.
"""
from sqlalchemy.sql import select

from api_decorators import api_method
from data_classes.requests import ReadUserEmailsParams
from data_classes.responses import Result
from service import storage
from tables import email, user


def users_emails() -> select:
    """ Заготовка для запросов по емейлам пользователя
    """
    query = select(
        [user.c.name, email.c.address]
    ).where(
        user.c.id == email.c.user_id
    )

    return query


@api_method
async def read_user_emails(params: ReadUserEmailsParams) -> Result:

    query = users_emails()

    if params.email_contains:
        # Конкретизируем запрос только емейлами, которые содержат подстроку
        query = query.where(email.c.address.like(f"%{params.email_contains}%"))

    if params.user_id:
        # Конкретизируем запрос только емейлами, определенного юзера
        query = query.where(user.c.id == params.user_id)

    result = await storage.read(query)

    return Result(name="user_emails", data=result)
