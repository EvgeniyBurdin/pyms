""" Модуль датаклассов ответов.
"""
from dataclasses import dataclass
from typing import Optional, Union

from data_classes.base import ApiDC


@dataclass
class ErrorResult(ApiDC):
    """ Ошибка API.

        :error_type: Тип ошибки.
        :message:    Сообщение об ошибке.
        :extra:      Словарь с дополнительными данными об ошибке.
    """
    error_type: str
    message: str
    extra: Optional[dict] = None


@dataclass
class Result(ApiDC):
    """ Результат чтения.
    """
    method: str
    length: int
    rows: list


@dataclass
class CreateResult(ApiDC):
    """ Результат чтения.
    """
    name: str
    message: str = "ok"


@dataclass
class ResponseDC(ApiDC):
    """ Ответ от сервиса.

        :status: Статус ответа. Если в этом поле `false`, то поле `result`
                 содержит описание ошибки.
        :result: Результат ответа.
        :id:     Идентификатор исходного запроса к сервису. Если это поле
                 было установлено в запросе, то в ответе будет идентичное
                 значение.
    """
    status: bool
    result: Union[dict, ErrorResult]
    id: int = 0
