# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/14
@Author   : shweZheng
@Software : PyCharm
"""
from loguru import logger
from sqlalchemy.orm import declarative_base

from app.db import async_engine

Base = declarative_base()


async def init_db() -> None:
    """
    初始化数据库
    :return:
    """
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise