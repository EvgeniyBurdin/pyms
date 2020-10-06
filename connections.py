""" Модуль для классов подключений.
"""
import json
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any

import asyncpg
import asyncpgsa

from settings import DatabaseSettingsError


# ----------------------------------------------------------------------------

@dataclass
class ConnectionParams:
    """ Основные параметры подключения.
    """
    host: str
    port: str


class Connection:

    def __init__(self, params: ConnectionParams):

        self.params = params
        self.current = None


class AsyncConnection(Connection, ABC):
    """ Класс асинхронного подключения.
    """
    async def get(self) -> Any:
        """ Возвращает текущее подключение.
        """
        return self.current or await self.create()

    async def setup(self, _) -> None:
        """ Метод создает подключение а при повторном вызове - закрывает его.

            (используется для добавления в список
             aiohttp.web.Application.cleanup_ctx при старте приложения)
        """
        await self.create()

        yield

        await self.close()

    async def create(self, params: ConnectionParams = None) -> Any:
        """ Метод создает подключение и возвращает его.
        """
        self.current = await self._create(params or self.params)

        return self.current

    async def close(self) -> None:
        """ Метод закрываект подключение.
        """
        await self._close()
        self.current = None

    @abstractmethod
    async def _create(self, params: ConnectionParams) -> Any:
        """ Метод должен создать подключение и вернуть его.
        """
        pass

    @abstractmethod
    async def _close(self) -> None:
        """ Метод должен закрыть текущее подключение.
            (если есть несколько подключений, то закрыть и их)
        """
        pass


# ----------------------------------------------------------------------------

@dataclass
class AsyncpgConnectionParams(ConnectionParams):
    """ Дополнительные параметры для асинхронного подключения к Postgres.
    """
    db: str
    user: str
    password: str
    min_size: int = 5
    max_size: int = 1000


class AsyncpgConnection(AsyncConnection):
    """ Асинхронное подключение к Postgres c помощью библиотеки asyncpg.
    """
    def __init__(self, params: AsyncpgConnectionParams):

        super().__init__(params)

        # Храним все созданные пулы подключений, чтобы потом корректно
        # закрыть их.
        self.pools = []

    async def connection_init(self, connection) -> None:
        """ Устанавливает параметры у каждого созданного в пуле подключения.
            (вызывается самим пулом, после создания подключения)
        """
        await connection.set_type_codec(
            'jsonb',
            encoder=str, decoder=json.loads, schema='pg_catalog'
        )

    async def create_pool(self, **params) -> asyncpg.pool.Pool:
        """ Возвращает пул подключений.
        """
        return await asyncpg.create_pool(**params)

    async def _create(self, params: AsyncpgConnectionParams = None
                      ) -> asyncpg.pool.Pool:
        """ Создает и возвращает новый пул подключений к Postgres.

            Созданный пул добавляется в список пулов экземпляра.
        """
        if isinstance(params, AsyncpgConnectionParams):
            params = asdict(params)

        try:
            database = params.pop('db')

        except Exception:
            raise DatabaseSettingsError(f"Incorrect DB settings: {params}.")

        params['database'] = database
        params['init'] = self.connection_init

        pool = await self.create_pool(**params)

        self.pools.append(pool)

        return pool

    async def _close(self) -> None:
        """ Закрывает все пулы подключений экземпляра.
        """
        while self.pools:
            pool = self.pools.pop()
            await pool.close()


class AsyncpgsaConnection(AsyncpgConnection):
    """ Асинхронное подключение к Postgres c помощью библиотеки asyncpgsa.
    """
    async def create_pool(self, **params) -> asyncpg.pool.Pool:
        """ Возвращает пул подключений.
        """
        return await asyncpgsa.create_pool(**params)
