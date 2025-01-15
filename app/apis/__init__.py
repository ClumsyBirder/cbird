# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 12:47
@Author   : wiesZheng
@Software : PyCharm
"""
from fastapi import APIRouter, FastAPI
from app.apis.v1 import users
from config import settings

api_router = APIRouter()

[
    api_router.include_router(router, prefix=prefix, tags=[tag])
    for router, prefix, tag in [
        (users.router, "/system/users", "System users"),
    ]
]



def init_router(_app:FastAPI):
    """
    注册路由
    """
    _app.include_router(api_router, prefix=settings.APP_API_STR)
