""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import (CreateEmailParams, DeleteEmailParams,
                                   ReadEmailParams, UpdateEmailParams)
from data_classes.responses import Result
from service import storage
from tables import email


@api_method
async def create_email(params: CreateEmailParams) -> Result:

    query = email.insert().values(
        address=params.address, user_id=params.user_id
    )

    result = await storage.create(query)

    return Result(name="email", data=result)


@api_method
async def read_email(params: ReadEmailParams) -> Result:

    query = email.select().where(email.c.id == params.id)

    result = await storage.read(query)

    return Result(name="email", data=result)


@api_method
async def update_email(params: UpdateEmailParams) -> Result:

    query = email.update().values(address=params.address).where(
        email.c.id == params.id
    )

    result = await storage.update(query)

    return Result(name="email", data=result)


@api_method
async def delete_email(params: DeleteEmailParams) -> Result:

    query = email.delete().where(email.c.id == params.id)

    result = await storage.delete(query)

    return Result(name="email", data=result)
