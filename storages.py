""" Модуль для классов хранилищ данных
"""
import functools
from abc import ABC, abstractmethod

from sqlalchemy.dialects import postgresql  # noqa

from api_json_enc_dec import json_dumps
from connections import Connection


def storage_request(method):
    """ Декоратор для запроса к хранилищу
    """
    @functools.wraps(method)
    async def wrapper(self, query):

        compile_params = {}
        if self.dialect is not None:
            compile_params['dialect'] = self.dialect.dialect()

        raw_sql = query.compile(**compile_params)
        raw_sql_str = str(raw_sql)

        print('-'*40)

        for sql_param_name in raw_sql.params.keys():
            value = json_dumps(raw_sql.params[sql_param_name])
            raw_sql_str = raw_sql_str.replace(f':{sql_param_name}', value)

        print(raw_sql_str)  # Лог запроса

        try:
            result = await method(self, query)

        except Exception as error:
            print(error)  # Лог ошибки
            raise

        return result

    return wrapper


class Storage:
    """ Базовый класс хранилища данных
    """
    def __init__(self, connection: Connection):

        self.connection = connection
        self.dialect = self.get_dialect()

    def get_dialect(self):

        return None


class AsyncStorage(Storage):
    """ Базовый класс асинхронного хранилища данных
    """
    async def setup(self, _) -> None:
        """ Метод подключает хранилище для работы, а при повторном
            вызове - закрывает его.

            Добавляется в список aiohttp.web.Application.cleanup_ctx при
            старте приложения.
        """
        await self.connect()

        yield

        await self.disconnect()

    async def connect(self) -> None:
        """  Подключает хранилище
        """
        await self.connection.create()

    async def disconnect(self) -> None:
        """ Закрывает подключение к хранилищу
        """
        await self.connection.close()


class AsyncCRUDStorage(AsyncStorage, ABC):
    """ Базовый класс асинхронного хранилища данных с методами CRUD
    """
    @abstractmethod
    async def create(self, query):
        pass

    @abstractmethod
    async def read(self, query):
        pass

    @abstractmethod
    async def update(self, query):
        pass

    @abstractmethod
    async def delete(self, query):
        pass


class AsyncpgsaStore(AsyncCRUDStorage):
    """ Класс асинхронного хранилища данных Postgres с доступом при
        помощи библиотеки asyncpgsa.
    """
    def get_dialect(self):
        """ Возвращает используемый в SQLAlchemy диалект БД
        """
        return None  # postgresql

    @storage_request
    async def _execute(self, query):
        """ Запрос для любого изменения
        """
        pool = await self.connection.get()
        async with pool.acquire() as conn:
            result = await conn.execute(query)

        return result

    async def create(self, query):
        """ Запрос записи
        """
        return await self._execute(query)

    @storage_request
    async def read(self, query):
        """ Запрос чтения
        """
        pool = await self.connection.get()
        async with pool.acquire() as conn:
            rows = await conn.fetch(query)

        return [{key: value for key, value in row.items()} for row in rows]

    async def update(self, query):
        """ Запрос обновления
        """
        return await self._execute(query)

    async def delete(self, query):
        """ Запрос удаления
        """
        return await self._execute(query)
