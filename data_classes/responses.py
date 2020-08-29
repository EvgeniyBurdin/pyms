""" Модуль датаклассов ответов.
"""
from dataclasses import dataclass
from typing import Union

from data_classes.base import ApiDC
from data_classes.data import DataDC
from data_classes.errors import ErrorDC


@dataclass
class ResponseDC(ApiDC):
    """ Ответ от сервиса.

        :status:   Статус.
        :response: Результат.
    """
    status: bool
    result: Union[DataDC, ErrorDC]
