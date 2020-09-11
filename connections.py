""" Модуль для классов соединений.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import asyncpg
import asyncpgsa


# ----------------------------------------------------------------------------

@dataclass
class ConnectionParams:
    """ Основные параметры соединения.
    """
    host: str
    port: str


class Connection(ABC):

    def __init__(self, params: ConnectionParams):

        self.params = params

    @abstractmethod
    def create(self) -> Any:
        pass

    @abstractmethod
    def close(self):
        pass


# ----------------------------------------------------------------------------

@dataclass
class AsyncPGConnectionParams(ConnectionParams):
    """ Дополнительные параметры для соединения с асинхронным Postgres.
    """
    db: str
    user: str
    password: str
    min_size: int = 5
    max_size: int = 10


class AsyncPGConnection(Connection):

    def __init__(self, params: AsyncPGConnectionParams):
        super().__init__(params)
        self.pools = []

    async def create(self, params: AsyncPGConnectionParams = None
                     ) -> asyncpg.pool.Pool:
        """ Создает и возвращает новый пулл подключений к Постгресу.

            Созданный пул добавляется в список пулов экземпляра.
        """
        if isinstance(params, dict):
            params = AsyncPGConnectionParams(**params)

        if params is None:
            params = self.params

        pool = await asyncpgsa.create_pool(
            host=params.host,
            port=params.port,
            database=params.db,
            user=params.user,
            password=params.password,
            min_size=params.min_size,
            max_size=params.max_size
        )
        self.pools.append(pool)

        return pool

    async def close(self):
        """ Закрывает все пулы подключений экземпляра.
        """
        while self.pools:
            pool = self.pools.pop()
            await pool.close()
