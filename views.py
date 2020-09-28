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

    try:
        table = TABLES[name]

    except Exception:
        message = f"Table '{name}' not found!"
        raise TableNotFound(message)

    return table


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """

    table = get_table(params.table_name)

    query = table.select()  # Пока простой запрос на все записи таблицы

    rows = await storage.read(query)

    return ReadResult(name=params.table_name, length=len(rows), rows=rows)
