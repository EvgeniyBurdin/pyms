""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, connection_class=None, connection_params=None):

        self.connection_class = connection_class
        self.connection_params = connection_params
        print(self.connection_class)


class AsyncStorage(Storage, ABC):

    @abstractmethod
    async def open(self):
        pass

    @abstractmethod
    async def close(self):
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

    async def open(self):
        pass

    async def close(self):
        pass

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
