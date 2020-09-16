""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import SimpleParams
from data_classes.responses import SimpleResult
from service import storage
from tables import people as people_table


@api_method
async def simple(params: SimpleParams) -> SimpleResult:
    """ Простой апи-метод (для примера).
    """
    query = params.query
    # Просто напечатаем запрос
    print('Request received:', query)

    # Пример работы с БД

    row = await storage.read(people_table)

    # Просто вернем из метода строку с результатом запроса к БД
    message = str(row)

    return SimpleResult(message=message)
