""" Обработчики запросов.
"""
from sqlalchemy import Table as SQLATable

from api_decorators import api_method
from data_classes.requests import ReadParams
from data_classes.responses import ReadResult
from service import storage
from tables import get_tables

# Соберем все таблицы в словарь, где ключ - имя таблицы
TABLES = get_tables()


class TableNotFound(Exception):
    pass


def get_table(name: str) -> SQLATable:
    """ Возвращает таблицу с указанным в name именем.
    """
    try:
        table = TABLES[name]

    except Exception as error:
        message = f"Table '{name}' not found ({type(error).__name__})!"
        raise TableNotFound(message)

    return table


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """

    table = get_table(params.name)

    query = storage.query_builder.read(table)

    rows = await storage.read(query)

    return ReadResult(name=params.name, length=len(rows), rows=rows)
