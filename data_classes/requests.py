""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass

from data_classes.base import ApiDC


@dataclass
class SimpleParams(ApiDC):
    """ Параматры для простого обработчика.

        (для примера)
    """
    query: str = "How are you?"


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры запроса.
        :id:     Идентификатор запроса. Может быть установлен вызывающей
                 стороной для идентификации ответа.
    """
    params: dict
    id: int = 0
