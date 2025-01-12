# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 12:47
@Author   : wiesZheng
@Software : PyCharm
"""
from fastapi import APIRouter
from app.api.v1 import users

api_router = APIRouter()

[
    api_router.include_router(router, prefix=prefix, tags=[tag])
    for router, prefix, tag in [
        (users.router, "/system/users", "System users"),
    ]
]
