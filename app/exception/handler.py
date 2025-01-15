# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/14
@Author   : shweZheng
@Software : PyCharm
"""
from fastapi import Request, FastAPI
from loguru import logger
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse


def init_exception_handlers(_app: FastAPI) -> None:
    """
    初始化异常处理器
    :param _app:
    :return:
    """

    @_app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.warning(
            f"Http请求异常\n"
            f"Method:{request.method}\n"
            f"URL:{request.url}\n"
            f"Headers:{request.headers}\n"
            f"Code:{exc.status_code}\n"
            f"Message:{exc.detail}\n"
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )
