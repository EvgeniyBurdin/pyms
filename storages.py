""" Модуль для классов хранилищ данных
"""
from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, connection):

        self.connection = connection


class AsyncCRUDStorage(Storage, ABC):

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
