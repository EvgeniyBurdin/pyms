""" Модуль для классов построителей запросов к хранилищу.
"""


class QueryBuilder:
    pass


class SQLAlchemyCoreBuilder(QueryBuilder):

    def read(self, table):

        query = table.select()  # Пока простой запрос на все записи таблицы

        return query
