""" Модуль абстрактного клиента для запросов данных у других сервисов.
"""
from abc import ABC, abstractmethod


class Client(ABC):

    @abstractmethod
    def _get_request_template(self) -> dict:
        """ Возвращает экземпляр датакласса для запроса к другому сервису.
        """
        return {}

    @abstractmethod
    def _post(self) -> dict:
        """ Выполняет POST запрос и возвращает результат.
        """
        pass

    @abstractmethod
    def _decode_response(self, raw_response: dict) -> dict:
        """ Декодирует сырой ответ от другого сервиса.
            Возвращает датакласс с результатом из запроса.
        """
        pass

    def post(self, params: dict) -> dict:
        """ Выполняет запрос к другому сервису.
        """
        request = self._get_request_template()
        request.params = params

        raw_response = self._post(request)

        response = self._decode_response(raw_response)

        return response
