from api_decorators import api_method
from data_classes.requests import SimpleParams
from data_classes.responses import SimpleResult
from service import pg_storage


@api_method
async def simple(params: SimpleParams) -> SimpleResult:
    """
        Простой апи-метод (для примера).
    """
    query = params.query
    await pg_storage.fetch()

    message = "All ok!" if query == "How are you?" else "What do you want?"

    return SimpleResult(message=message)
