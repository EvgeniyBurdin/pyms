""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod
from connections import Connection


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


class AsyncPostgresSACoreCRUDStorage(AsyncCRUDStorage):
    """ Класс асинхронного хранилища данных Postgres с доступом при
        помощи SQLAlchemy-core.
    """
    async def _create(self, query):
        pass

    async def _read(self, query):

        connection = await self.connection.get()

        async with connection.acquire() as conn:
            row = await conn.fetch(query.select())

        return row

    async def _update(self, query):
        pass

    async def _delete(self, query):
        pass
