""" Модуль для классов построителей запросов к хранилищу.
"""


class QueryBuilder:
    pass


class SQLAlchemyCoreBuilder(QueryBuilder):

    def read_table(self, table, query=None):

        if query is None:
            query = table.select()  # "Запрос на все записи таблицы

        return query
