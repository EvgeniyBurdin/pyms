""" Модуль для классов соединений.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import asyncpg
import asyncpgsa


@dataclass
class ConnectParams:
    """ Основные параметры соединения.
    """
    host: str
    port: str


@dataclass
class AsyncPGConnectParams(ConnectParams):
    """ Дополнительные параметры для соединения с асинхронным Postgres.
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
    def create(self) -> Any:
        pass

    @abstractmethod
    def close(self):
        pass


class AsyncPGConnect(Connect):

    def __init__(self, params: AsyncPGConnectParams):
        super().__init__(params)
        self.pools = []

    async def create(self,
                     params: AsyncPGConnectParams = None) -> asyncpg.pool.Pool:
        """ Создает и возвращает новый пулл подключений к Постгресу.

            Созданный пул добавляется в список пулов экземпляра.
        """
        if isinstance(params, dict):
            params = AsyncPGConnectParams(**params)

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
