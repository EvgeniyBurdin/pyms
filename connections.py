""" Модуль для классов подключений.
"""
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
        self.current_connection = await self._create(params or self.params)

        return self.current_connection

    async def close(self) -> None:
        """ Метод закрываект подключение.
        """
        await self._close()
        self.current_connection = None

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
class AsyncPGConnectionParams(ConnectionParams):
    """ Дополнительные параметры для асинхронного подключения к Postgres.
    """
    db: str
    user: str
    password: str
    min_size: int = 5
    max_size: int = 10


class AsyncPGConnection(AsyncConnection):
    """ Асинхронное подключение к Postgres.

        Текущая реализация под "подключением" подразумевает "Пулл подключений"
        из библиотеки asyncpg.
    """
    def __init__(self, params: AsyncPGConnectionParams):

        super().__init__(params)

        # Храним все созданные пуллы подключений, чтобы потом корректно
        # закрыть их.
        self.pools = []

    async def _create(self, params: AsyncPGConnectionParams = None
                      ) -> asyncpg.pool.Pool:
        """ Создает и возвращает новый пулл подключений к Postgres.

            Созданный пулл добавляется в список пуллов экземпляра.
        """

        if isinstance(params, AsyncPGConnectionParams):
            params = asdict(params)

        try:
            database = params.pop('db')
            params['database'] = database

        except Exception:
            raise DatabaseSettingsError(f"Incorrect DB settings: {params}.")

        pool = await asyncpgsa.create_pool(**params)

        self.pools.append(pool)

        return pool

    async def _close(self) -> None:
        """ Закрывает все пуллы подключений экземпляра.
        """
        while self.pools:
            pool = self.pools.pop()
            await pool.close()
