from api_decorators import api_method
from data_classes.requests import SimpleParams
from data_classes.responses import SimpleResult


@api_method
async def simple(params: SimpleParams) -> SimpleResult:
    """
        Простой апи-метод (для примера).
    """
    query = params.query

    message = "All ok!" if query == "How are you?" else "What do you want?"

    return SimpleResult(message=message)
