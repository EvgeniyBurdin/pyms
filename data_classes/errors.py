""" Модуль датаклассов ошибок API.
"""
from dataclasses import dataclass
from typing import Optional

from data_classes.base import ApiDC


@dataclass
class ErrorDC(ApiDC):
    """ Ошибка API.

        :code:    Код.
        :message: Сообщение.
        :extra:   Словарь с дополнительными данными об ошибке.
    """
    code: str
    message: str
    extra: Optional[dict] = None
