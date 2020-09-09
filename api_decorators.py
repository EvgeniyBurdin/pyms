"""
    Модуль для декораторов
"""
import functools
from dataclasses import dataclass

from api_exeptions import InputValidationError, OutputValidationError
from data_classes.base import ApiDC

_INPUT_ANNOTATION = '_api__input_annotation_'
_OUTPUT_ANNOTATION = '_api__output_annotation_'
_USED_API_DC = '_api__used_api_dc_'


def api_method(func):
    """
        Декоратор для api-функций (для обработчиков запросов).

        Валидирует входные и выходные данные.

        Входные данные должны приниматься в агрумент "params".

        Аннотации, для аргумента "params" и для результата
        функции - обязательны!

        Пример:
            @api_method
            async def drop(params: TableDropRequestDC) -> ChangeResponseDC:


    """
    input_annotation = func.__annotations__['params']

    @dataclass
    class InputDC(ApiDC):
        """
            Датакласс для валидации входных данных
        """
        params: input_annotation

    output_annotation = func.__annotations__['return']

    @dataclass
    class OutputDC(ApiDC):
        """
            Датакласс для валидации выходных данных
        """
        result: output_annotation

    # Добавим к функции api-атрибуты

    func.__dict__[_INPUT_ANNOTATION] = input_annotation
    func.__dict__[_OUTPUT_ANNOTATION] = output_annotation

    used_api_dc = InputDC.get_nested_validated_dc()
    used_api_dc.update(OutputDC.get_nested_validated_dc())
    func.__dict__[_USED_API_DC] = used_api_dc

    @functools.wraps(func)
    async def wrapped(params):

        input_data = InputDC(params=params)
        errors = input_data.get_errors()

        if errors is None:
            result = await func(input_data.params)
        else:
            raise InputValidationError(
                f"Error '{func.__name__}' in the incoming data: {errors}"
            )

        output_data = OutputDC(result=result)
        errors = output_data.get_errors()

        if errors is not None:
            raise OutputValidationError(
                f"Error '{func.__name__}' in the outgoing data: {errors}"
            )

        return result

    return wrapped
