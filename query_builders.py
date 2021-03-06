""" Модуль для классов построителей запросов к хранилищу.
"""
from sqlalchemy import Table as SQLATable

from tables import get_tables


class TableNotFound(Exception):
    pass


class QueryBuilder:
    """ Базовый класс для построителей запросов.
    """
    pass


class SQLAlchemyCoreBuilder(QueryBuilder):
    """ Построитель запросов для движка SQLAlchemy-Core.
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.tables = get_tables()

    def get_table(self, name: str) -> SQLATable:
        """ Возвращает таблицу с указанным в name именем.
        """
        try:
            table = self.tables[name]

        except Exception as error:
            message = f"Table '{name}' not found ({type(error).__name__})!"
            raise TableNotFound(message)

        return table

    def read_table(self, params):

        table = self.get_table(params.name)

        query = table.select()

        return query
