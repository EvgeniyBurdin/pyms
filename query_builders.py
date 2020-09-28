""" Модуль для классов построителей запросов к хранилищу.
"""
from sqlalchemy import Table as SQLATable

from tables import get_tables

# Соберем все таблицы в словарь, где ключ - имя таблицы
TABLES = get_tables()


class TableNotFound(Exception):
    pass


def get_table(name: str) -> SQLATable:
    """ Возвращает таблицу с указанным в name именем.
    """
    try:
        table = TABLES[name]

    except Exception as error:
        message = f"Table '{name}' not found ({type(error).__name__})!"
        raise TableNotFound(message)

    return table


class QueryBuilder:
    """ Базовый класс для построителей запросов.
    """
    pass


class SQLAlchemyCoreBuilder(QueryBuilder):
    """ Построитель запросов для движка SQLAlchemy-Core.
    """
    def read_table(self, params):

        table = get_table(params.name)

        query = table.select()

        return query
