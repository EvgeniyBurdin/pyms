""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod
from dataclasses import asdict

from sqlalchemy import Table as SQLATable

import tables as app_tables
from connections import Connection

# Соберем все таблицы в словарь, где ключ - имя таблицы
TABLES = {
    getattr(app_tables, attr_name).name:  getattr(app_tables, attr_name)
    for attr_name in dir(app_tables)
    if isinstance(getattr(app_tables, attr_name), SQLATable)
}


class Storage:
    """ Базовый класс хранилища данных
    """
    def __init__(self, connection: Connection):

        self.connection = connection


class AsyncStorage(Storage):
    """ Базовый класс асинхронного хранилища данных
    """
    async def setup(self, _) -> None:
        """ Метод подключает хранилище для работы, а при повторном
            вызове - закрывает его.

            Добавляется в список aiohttp.web.Application.cleanup_ctx при
            старте приложения.
        """
        await self.connect()

        yield

        await self.disconnect()

    async def connect(self) -> None:
        """  Подключает хранилище
        """
        await self.connection.create()

    async def disconnect(self) -> None:
        """ Закрывает подключение к хранилищу
        """
        await self.connection.close()


class AsyncCRUDStorage(AsyncStorage, ABC):
    """ Базовый класс асинхронного хранилища данных с методами CRUD
    """
    async def create(self, query):

        result = await self._create(query)

        return result

    async def read(self, query):

        result = await self._read(query)

        return result

    async def update(self, query):

        result = await self._update(query)

        return result

    async def delete(self, query):

        result = await self._delete(query)

        return result

    @abstractmethod
    async def _create(self, query):
        pass

    @abstractmethod
    async def _read(self, query):
        pass

    @abstractmethod
    async def _update(self, query):
        pass

    @abstractmethod
    async def _delete(self, query):
        pass


class AsyncpgsaStore(AsyncCRUDStorage):
    """ Класс асинхронного хранилища данных Postgres с доступом при
        помощи библиотеки asyncpgsa.
    """
    async def _create(self, query):
        """ Вставка в таблицу. (еще в разработке)
        """
        table = TABLES[query.table_name]
        query = asdict(query)
        data = query['data']

        pool = await self.connection.get()

        async with pool.acquire() as conn:
            await conn.fetchrow(table.insert().values(data))

    async def _read(self, query):
        """ Чтение из таблицы. (еще в разработке)
        """
        table = TABLES[query.table_name]

        pool = await self.connection.get()

        async with pool.acquire() as conn:
            # Пока простой select всех записей
            rows = await conn.fetch(table.select())

        return [{key: value for key, value in row.items()} for row in rows]

    async def _update(self, query):
        pass

    async def _delete(self, query):
        pass
