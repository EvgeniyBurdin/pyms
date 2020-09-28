""" Обработчики запросов.
"""
from api_decorators import api_method
from data_classes.requests import Params
from data_classes.responses import Result
from service import methods


@api_method
async def main(params: Params) -> Result:
    """
    """
    method = methods[params.method]

    rows = await method(params)

    return Result(method=params.method, length=len(rows), rows=rows)
