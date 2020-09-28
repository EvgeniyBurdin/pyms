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
    method_name = f"{params.component}.{params.query.method}"
    method = methods[method_name]
    print(method)

    rows = await method(params.query)

    return Result(method=method_name, length=len(rows), rows=rows)
