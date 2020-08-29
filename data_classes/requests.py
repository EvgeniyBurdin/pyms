""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass

from data_classes.base import ApiDC
from data_classes.data import DataDC


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры.
        :id:     Идентификатор.
    """
    params: DataDC
    id: int = 0
