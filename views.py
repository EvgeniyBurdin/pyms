""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import ReadParams
from data_classes.responses import ReadResult
from service import storage
from tables import people as people_table
from sqlalchemy import Table


TABLES = (people_table, )


def get_table(name: str) -> Table:

    for table in TABLES:
        if table.name == name:
            return table


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """
    table = get_table(params.name)

    result = await storage.read(table, params.query)

    return ReadResult(str(result))
