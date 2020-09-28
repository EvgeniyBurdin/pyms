""" Модуль датаклассов запросов.
"""
from dataclasses import dataclass
from typing import List, Union, Optional

from data_classes.base import ApiDC
from data_classes.schema import EmailData, TeamData, UserData, UsersInTeamsData


@dataclass
class Params(ApiDC):
    """ Параметры для чтения из хранилища. временно
    """
    method: str
    fields: Optional[List[str]] = None
    limit: int = 1000
    offset: int = 0


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
