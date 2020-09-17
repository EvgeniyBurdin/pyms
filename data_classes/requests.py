""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass

from data_classes.base import ApiDC
from typing import Any


@dataclass
class ReadParams(ApiDC):
    """ Параметры для чтения из хранилища.
    """
    name: str
    query: dict
    limit: int = 1000
    offset: int = 0


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры запроса.
        :id:     Идентификатор запроса. Может быть установлен вызывающей
                 стороной для идентификации ответа.
    """
    params: dict
    id: int = 0
