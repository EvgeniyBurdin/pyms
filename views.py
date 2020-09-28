""" Обработчики запросов.
"""
from tables import metadata
from api_decorators import api_method
from data_classes.requests import ReadParams
from data_classes.responses import ReadResult
from service import storage

# Соберем все таблицы в словарь, где ключ - имя таблицы
TABLES = metadata.tables


@api_method
async def read(params: ReadParams) -> ReadResult:
    """ Чтение из хранилища.
    """

    table = TABLES[params.table_name]

    query = table.select()  # Пока простой запрос на все записи таблицы

    rows = await storage.read(query)

    return ReadResult(name=params.table_name, length=len(rows), rows=rows)
