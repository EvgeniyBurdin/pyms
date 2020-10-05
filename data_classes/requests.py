""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass
from typing import Optional

from data_classes.base import ApiDC


@dataclass
class CreateUserParams(ApiDC):
    """ Параметры для создания email.
    """
    name: str
    meta: dict


@dataclass
class CreateEmailParams(ApiDC):
    """ Параметры для создания email.
    """
    address: str
    user_id: str
    id: Optional[int] = None


@dataclass
class ReadEmailParams(ApiDC):
    """ Параметры для чтения email.
    """
    id: int


@dataclass
class UpdateEmailParams(ApiDC):
    """ Параметры для обновления email.
    """
    id: int
    address: str


@dataclass
class DeleteEmailParams(ApiDC):
    """ Параметры для удаления email.
    """
    id: int


@dataclass
class ReadUserEmailsParams(ApiDC):
    """ Параметры чтения email'ов пользователя.
    """
    user_id: str = ""
    email_contains: str = ""


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры запроса.
        :id:     Идентификатор запроса. Может быть установлен вызывающей
                 стороной для идентификации ответа.
    """
    params: dict
    id: int = 0
