from abc import ABC, abstractmethod
from connections import Connect


class Storage(ABC):

    connect = None

    def __init__(self, connect: Connect):

        self.connect = connect

    @abstractmethod
    def close(self):
        pass


class AsyncPostgresStorage(Storage):

    async def close(self):

        if self.connect is not None:
            await self.connect.close()
            self.connect = None
