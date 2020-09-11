from abc import ABC, abstractmethod
from connections import Connection


class Storage(ABC):

    connection = None

    def __init__(self, connection: Connection):

        self.connection = connection

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


class AsyncPostgresStorage(Storage):

    async def connect(self):

        if self.connection is not None:
            await self.connection.create()

    async def close(self):

        if self.connection is not None:
            await self.connection.close()
            self.connection = None

    async def setup(self, _=None):

        await self.connect()

        yield

        await self.close()

    async def fetch(self):
        print('fetch()')
