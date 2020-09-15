""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, connection_class=None, connection_params=None):

        self.connection_class = connection_class
        self.connection_params = connection_params
        print(self.connection_class)


class AsyncStorage(Storage, ABC):

    async def setup(self, _) -> None:
        """ Метод открывает хранилище для работы, а при повторном
            вызове - закрывает его.

            (используется для добавления в список
             aiohttp.web.Application.cleanup_ctx при старте приложения)
        """
        await self.open()

        yield

        await self.close()

    async def open(self):

        result = await self._open(query)

        return result

    async def close(self):

        result = await self._close(query)

        return result

    @abstractmethod
    async def _open(self):
        pass

    @abstractmethod
    async def _close(self):
        pass


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


class AsyncPostgresCRUDStorage(AsyncCRUDStorage):

    async def _create(self, query):
        pass

    async def _read(self, query):
        pass

    async def _update(self, query):
        pass

    async def _delete(self, query):
        pass
