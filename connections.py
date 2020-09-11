"""
    Модуль для классов соединений.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

import asyncpgsa
import asyncpg


@dataclass
class ConnectParams:
    """
        Основные параметры соединения.
    """
    host: str
    port: str


@dataclass
class AsyncPGConnectParams(ConnectParams):
    """
        Дополнительные параметры для соединения с асинхронным Postgres.
    """
    db: str
    user: str
    password: str
    min_size: int = 5
    max_size: int = 10


class Connect(ABC):

    def __init__(self, params: ConnectParams):

        self.params = params

    @abstractmethod
    def init(self):
        pass


class AsyncPGConnect(Connect):

    async def init(self,
                   params: AsyncPGConnectParams = None) -> asyncpg.pool.Pool:

        if isinstance(params, dict):
            params = AsyncPGConnectParams(**params)

        if params is None:
            params = self.params

        self.connect = await asyncpgsa.create_pool(
            host=params.host,
            port=params.port,
            database=params.db,
            user=params.user,
            password=params.password,
            min_size=params.min_size,
            max_size=params.max_size
        )


if __name__ == "__main__":

    import settings
    import asyncio

    async def main():

        params = AsyncPGConnectParams(
            settings.POSTGRES_HOST,
            settings.POSTGRES_PORT,
            settings.POSTGRES_DB,
            settings.POSTGRES_USER,
            settings.POSTGRES_PASSWORD
        )

        storage = AsyncPGConnect(params)
        print(params)
        await storage.init()
        print(storage.connect)

    asyncio.run(main())
