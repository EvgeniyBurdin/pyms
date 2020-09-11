from api_decorators import api_method
from data_classes.requests import SimpleParams
from data_classes.responses import SimpleResult
from service import pg_storage
from tables import tasks_table


@api_method
async def simple(params: SimpleParams) -> SimpleResult:
    """
        Простой апи-метод (для примера).
    """
    query = params.query

    connection = pg_storage.get_connection()
    query = tasks_table.select().where(tasks_table.c.name == 'Ivan')

    async with connection.acquire() as conn:
        row = await conn.fetchrow(query)

    message = str(row)

    return SimpleResult(message=message)
