""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass

from data_classes.base import ApiDC
from data_classes.schema import PeapleData
from typing import Union, List


@dataclass
class ReadParams(ApiDC):
    """ Параметры для чтения из хранилища.
    """
    name: str
    query: dict
    limit: int = 1000
    offset: int = 0


@dataclass
class CreateParams(ApiDC):
    """ Параметры для создания записей в хранилище.
    """
    name: str
    data: Union[List[PeapleData]]


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры запроса.
        :id:     Идентификатор запроса. Может быть установлен вызывающей
                 стороной для идентификации ответа.
    """
    params: Union[CreateParams, ReadParams]
    id: int = 0
