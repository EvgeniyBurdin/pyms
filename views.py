""" Обработчики запросов.
"""
from sqlalchemy import Table as SQLATable

import tables as app_tables
from api_decorators import api_method
from data_classes.requests import ReadParams
from data_classes.responses import ReadResult
from service import storage

# Соберем все таблицы в словарь, где ключ - имя таблицы
TABLES = {
    getattr(app_tables, attr_name).name:  getattr(app_tables, attr_name)
    for attr_name in dir(app_tables)
    if isinstance(getattr(app_tables, attr_name), SQLATable)
}


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """

    table = TABLES[params.table_name]

    query = table.select()  # Пока простой запрос на все записи таблицы

    rows = await storage.read(query)

    return ReadResult(name=params.table_name, length=len(rows), rows=rows)
