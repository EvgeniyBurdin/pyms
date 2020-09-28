""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod

from connections import Connection
from query_builders import QueryBuilder


class Storage:
    """ Базовый класс хранилища данных
    """
    def __init__(self, connection: Connection, query_builder: QueryBuilder):

        self.connection = connection
        self.query_builder = query_builder


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
    @abstractmethod
    async def create(self, query):
        pass

    @abstractmethod
    async def read(self, query):
        pass

    @abstractmethod
    async def update(self, query):
        pass

    @abstractmethod
    async def delete(self, query):
        pass


class AsyncpgsaStore(AsyncCRUDStorage):
    """ Класс асинхронного хранилища данных Postgres с доступом при
        помощи библиотеки asyncpgsa.
    """
    async def create(self, query):
        pass

    async def read(self, query):
        """ Чтение из таблицы. (еще в разработке)
        """
        print(query)  # Логирование запроса

        try:
            pool = await self.connection.get()
            async with pool.acquire() as conn:
                rows = await conn.fetch(query)
        except Exception as error:
            print(error)  # Логирование ошибки
            raise

        return [{key: value for key, value in row.items()} for row in rows]

    async def update(self, query):
        pass

    async def delete(self, query):
        pass
