# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 12:45
@Author   : wiesZheng
@Software : PyCharm
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.models import init_db
from config import settings


@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.success(settings.BANNER)
    logger.info("Starting up the application")
    await init_db()
    yield
    logger.info("Shutting down the application")