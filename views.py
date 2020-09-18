""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import ReadParams, CreateParams
from data_classes.responses import ReadResult, CreateResult
from service import storage


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """
    rows = await storage.read(params)

    return ReadResult(name=params.table_name, length=len(rows), rows=rows)


@api_method
async def create(params: CreateParams) -> CreateResult:
    """ Запись в хранилище.
    """
    await storage.create(params)

    return CreateResult(name=params.table_name)
