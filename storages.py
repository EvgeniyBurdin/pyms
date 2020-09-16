""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod
from connections import Connection


class Storage:

    def __init__(self, connection: Connection):

        self.connection = connection


class AsyncStorage(Storage):

    async def setup(self, _) -> None:
        """ Метод открывает хранилище для работы, а при повторном
            вызове - закрывает его.

            (используется для добавления в список
             aiohttp.web.Application.cleanup_ctx при старте приложения)
        """
        await self.init()

        yield

        await self.close()

    async def init(self):

        await self.connection.create()

    async def close(self):

        await self.connection.close()


class AsyncCRUDStorage(AsyncStorage, ABC):

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


class AsyncSaPostgresCRUDStorage(AsyncCRUDStorage):

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
