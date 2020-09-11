""" Модуль для классов подключений.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import asyncpg
import asyncpgsa


# ----------------------------------------------------------------------------

@dataclass
class ConnectionParams:
    """ Основные параметры подключения.
    """
    host: str
    port: str


class AsyncConnection(ABC):
    """ Класс асинхронного подключения.
    """
    def __init__(self, params: ConnectionParams):

        self.params = params
        self.current_connection = None

    async def get(self) -> Any:
        """ Возвращает текущее подключение.
        """
        return self.current_connection or await self.create()

    async def setup(self, _=None):
        """ Метод создает подключение а при повторном вызове - закрывает его.

            (используется для добавления в список
            aiohttp.web.Application.cleanup_ctx при старте приложения)
        """
        await self.create()

        yield

        await self.close()

    @abstractmethod
    def create(self) -> Any:
        """ Метод должен создать текущее подключение и вернуть его.
        """
        pass

    @abstractmethod
    def close(self):
        """ Метод должен закрыть текущее подключение.
            (если есть несколько подключений, то закрыть и их)
        """
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


class AsyncPGConnection(AsyncConnection):
    """ Асинхронное подключение к Постгресу.

        Текущая реализация под "подключением" подразумевает "Пулл подключений"
        из библиотеки asyncpg.
    """
    def __init__(self, params: AsyncPGConnectionParams):

        super().__init__(params)

        # Храним все созданные пулы подключений
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

        self.current_connection = pool
        self.pools.append(pool)

        return pool

    async def close(self):
        """ Закрывает все пулы подключений экземпляра.
        """
        while self.pools:
            pool = self.pools.pop()
            await pool.close()

        self.current_connection = None
