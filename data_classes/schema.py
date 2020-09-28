from dataclasses import dataclass, field
from typing import Optional

from data_classes.base import ApiDC


@dataclass
class UserData(ApiDC):
    """ Поля таблицы user.

        :id:         Идентификатор пользователя (строка UUID).
        :name:       Имя пользователя.
        :birth_date: День рождения (timestamp в секундах).
        :meta:       Словарь с дополнительной информацией.
    """
    name: str
    id: Optional[str] = None
    birth_date: Optional[int] = None
    meta: dict = field(default_factory=dict)


@dataclass
class EmailData(ApiDC):
    """ Поля таблицы email.

        :id:      Идентификатор адреса.
        :address: Адрес электронной почты.
        :user_id: Идентификатор пользователя (строка UUID).
    """
    id: int
    address: str
    user_id: str


@dataclass
class TeamData(ApiDC):
    """ Поля таблицы team.

        :id:      Идентификатор команды.
        :name:    Имя команды.
        :created: Дата создания (timestamp в секундах).
        :updated: Дата обновления (timestamp в секундах).
    """
    id: int
    name: str
    created: Optional[int] = None
    updated: Optional[int] = None


@dataclass
class UsersInTeamsData(ApiDC):
    """ Поля таблицы users_in_teams.

        :user_id: Идентификатор пользователя (строка UUID).
        :team_id: Идентификатор команды.
    """
    user_id: str
    team_id: int
