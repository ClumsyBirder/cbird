# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 14:59
@Author   : wiesZheng
@Software : PyCharm
"""
import os
from fastapi import FastAPI
from loguru import logger
from starlette.staticfiles import StaticFiles

from app import lifespan
from app.api import api_router
from app.core.middleware import error_handler_middleware
from app.utils.openapi import get_stoplight_ui_html
from config import settings, ROOT


description = """
    \n\n![](https://i.ibb.co/v3Yt03v/todo-api-background.png)\n\n ## \U0001f4ab Overview\n\nTo Do API provides a simple way
    for people to manage their tasks and plan their day. This API can be used to create mobile and web applications.This
    API is documented using **OpenAPI 3.0**. The implementation lives in this [GitHub
    repo](https://github.com/stoplight-qa/studio-demo/blob/main/reference/todos/todo.v1.yaml).
    \n\n ### \U0001f9f0 Cross-Origin Resource Sharing\n\nThis API features Cross-Origin Resource Sharing (CORS) implemented in compliance
    with  [W3C spec](https://www.w3.org/TR/cors/). CORS support is necessary to make calls from the request maker within
    the API docs.\n\n### \U0001f3c1 Trying out your own API Specification\nElements can be used to generate API docs for
    any OpenAPI document. Replace this OpenAPI with a URL to your own OpenAPI document to get started. 
"""


def mount_static_files(_app: FastAPI) -> None:
    """挂载静态文件目录到应用。"""
    _app.mount(
        "/static", StaticFiles(directory=os.path.join(ROOT, "static")), name="static"
    )

def configure_docs(_app: FastAPI) -> None:
    @_app.get("/openapi", include_in_schema=False)
    async def api_documentation():
        """Add stoplight elements api doc. https://dev.to/amal/replacing-fastapis-default-api-docs-with-elements-391d"""
        return get_stoplight_ui_html(
            openapi_url="/openapi.json",
            title=settings.APP_NAME + " - OpenApi",
            logo="/static/logo.svg",
            stoplight_elements_favicon_url="/static/logo.svg",
        )


def create_app() -> FastAPI:
    """
    应用工厂函数，用于初始化和配置FastAPI应用。
    """
    # init_logging(settings.LOGGING_CONF)

    _app = FastAPI(
        title=settings.APP_NAME,
        description=description,
        version=settings.APP_VERSION,
        docs_url=None,
        redoc_url=None,
        lifespan=lifespan,
    )
    mount_static_files(_app)

    _app.middleware("http")(error_handler_middleware)
    _app.include_router(api_router, prefix=settings.APP_API_STR)
    configure_docs(_app)

    return _app


app = create_app()
