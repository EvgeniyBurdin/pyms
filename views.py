""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import ReadParams
from data_classes.responses import ReadResult
from service import storage


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """
    query = storage.query_builder.read_table(params)

    rows = await storage.read(query)

    return ReadResult(name=params.name, length=len(rows), rows=rows)
