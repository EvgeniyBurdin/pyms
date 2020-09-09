import asyncio
import json
from dataclasses import asdict

from aiohttp import web

from api_exeptions import InputValidationError
from data_classes.requests import RequestDC
from data_classes.responses import ErrorResult, ResponseDC


@web.middleware
async def system_error(request, handler):

    try:
        response = await handler(request)
        return response

    except (KeyboardInterrupt, SystemExit):
        exit(-1)

    except asyncio.CancelledError:
        return {}


@web.middleware
async def json_server(request, handler):

    MAX_REPR = 200

    def repr_(val) -> str:
        val = str(val)
        return f"{val[: MAX_REPR]}..." if len(val) > MAX_REPR else val

    extra = dict(
        url=str(request.url),
        method=request.method,
        headers=dict(request.headers),
        cookies=dict(request.cookies)
    )

    # Проверка того, что получили json --------------------------------
    try:
        data = await request.json()

    except json.decoder.JSONDecodeError as error:

        error_type = type(error).__name__
        text = await request.text()

        extra["error_type"] = error_type
        extra["text"] = repr_(text)

        return web.Response(status=400, text="Wrong JSON format")

    # Проверка того, что формат запроса к серверу - корректный ---------------

    id_ = 0
    body = str(data)
    extra["body"] = repr_(body)

    try:
        request_data = RequestDC(**data)
        id_ = asdict(request_data).get('id', 0)
        error = request_data.get_errors()

        if error is not None:
            raise InputValidationError(str(error))

    except (TypeError, InputValidationError) as error:

        error_type = type(error).__name__
        msg = f"Request validation error: {error}."

        return web.json_response(
            data=asdict(ResponseDC(
                status=False,
                result=ErrorResult(error_type, msg, extra),
                id=id_
            )),
            status=400
        )

    # Выполнение запроса -----------------------------------------------------

    try:
        result = await handler(request_data.params)
        response = asdict(ResponseDC(status=True, result=result, id=id_))

    except Exception as error:

        error_type = type(error).__name__
        msg = f"Error while executing request: {error}"

        return web.json_response(
            data=asdict(ResponseDC(
                status=False,
                result=ErrorResult(error_type, msg, extra),
                id=id_
            )),
            status=500
        )

    return web.json_response(response)
