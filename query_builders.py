""" Модуль для классов построителей запросов к хранилищу.
"""
from sqlalchemy import Table as SQLAlchemyTable

from tables import get_tables


class TableNotFound(Exception):
    pass


class QueryBuilder:
    """ Базовый класс для построителей запросов.
    """
    def __init__(self, components):
        self.components = components

    def get_component(self, name):
        return self.components[name]


class SQLAlchemyCoreBuilder(QueryBuilder):
    """ Построитель запросов для движка SQLAlchemy-Core.
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.tables = get_tables()

    def get_table(self, name: str) -> SQLAlchemyTable:
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
        component = self.get_component(params.name)
        print('===', component)

        query = table.select()

        return query
