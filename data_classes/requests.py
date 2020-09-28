""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass
from typing import List, Union, Optional, Literal

from data_classes.base import ApiDC
from data_classes.schema import EmailData, TeamData, UserData, UsersInTeamsData


@dataclass
class ReadQuery(ApiDC):
    """ Запрос на чтение.
    """
    method: Literal['read']
    fields: Optional[List[str]] = None
    limit: int = 1000
    offset: int = 0


@dataclass
class Params(ApiDC):
    """ Параметры запроса.
    """
    component: str
    query: Union[ReadQuery]


@dataclass
class CreateParams(ApiDC):
    """ Параметры для создания записей в хранилище.
    """
    name: str
    data: Union[
        List[EmailData], List[TeamData], List[UserData],
        List[UsersInTeamsData],
    ]


@dataclass
class RequestDC(ApiDC):
    """ Запрос к сервису.

        :params: Параметры запроса.
        :id:     Идентификатор запроса. Может быть установлен вызывающей
                 стороной для идентификации ответа.
    """
    params: Union[CreateParams, Params]
    id: int = 0
