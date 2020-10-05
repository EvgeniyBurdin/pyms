""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import CreateUserParams
from data_classes.responses import Result
from service import storage
from tables import user


@api_method
async def create_user(params: CreateUserParams) -> Result:

    query = user.insert().values(
        name=params.name, meta=params.meta
    )

    result = await storage.create(query)

    return Result(name="user", data=result)
