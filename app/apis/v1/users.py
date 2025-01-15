# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 17:51
@Author   : wiesZheng
@Software : PyCharm
"""
from fastapi import APIRouter
from loguru import logger

router = APIRouter()

@router.post("/")
async def create_user():
    logger.info(f"Received request to create user with email")
