""" Модуль абстрактного клиента для запросов данных у других сервисов.
"""
from abc import ABC, abstractmethod
from typing import Any

from data_classes.data import DataDC
from data_classes.requests import RequestDC
from data_classes.responses import ResponseDC


class Client(ABC):

    @abstractmethod
    def _get_request_template(self) -> RequestDC:
        """ Возвращает экземпляр датакласса для запроса к другому сервису.
        """
        return RequestDC()

    @abstractmethod
    def _post(self) -> Any:
        """ Выполняет POST запрос и возвращает результат.
        """
        pass

    @abstractmethod
    def _decode_response(self, raw_response: Any) -> ResponseDC:
        """ Декодирует сырой ответ от другого сервиса.
            Возвращает датакласс с результатом из запроса.
        """
        pass

    def post(self, params: DataDC) -> DataDC:
        """ Выполняет запрос к другому сервису.
        """
        request = self._get_request_template()
        request.params = params

        raw_response = self._post(request)

        response = self._decode_response(raw_response)

        return response
