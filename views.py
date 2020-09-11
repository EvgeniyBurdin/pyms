from api_decorators import api_method
from data_classes.requests import SimpleParams
from data_classes.responses import SimpleResult
from service import pg_storage
from tables import people as people_table


@api_method
async def simple(params: SimpleParams) -> SimpleResult:
    """
        Простой апи-метод (для примера).
    """
    query = params.query

    connection = pg_storage.get_connection()
    query = people_table.select().where(people_table.c.name == 'Ivan')

    async with connection.acquire() as conn:
        row = await conn.fetch(query)

    message = str(row)

    return SimpleResult(message=message)
