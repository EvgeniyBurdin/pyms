""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import (CreateEmailParams, DeleteEmailParams,
                                   ReadEmailParams, UpdateEmailParams)
from data_classes.responses import Result
from service import storage


@api_method
async def create_email(params: CreateEmailParams) -> Result:

    query = ""

    result = await storage.create(query)

    return Result(name="email", data=result)


@api_method
async def read_email(params: ReadEmailParams) -> Result:

    query = ""

    result = await storage.read(query)

    return Result(name="email", data=result)


@api_method
async def update_email(params: UpdateEmailParams) -> Result:

    query = ""

    result = await storage.update(query)

    return Result(name="email", data=result)


@api_method
async def delete_email(params: DeleteEmailParams) -> Result:

    query = ""

    result = await storage.read(query)

    return Result(name="email", data=result)
