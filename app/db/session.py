# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 14:38
@Author   : wiesZheng
@Software : PyCharm
"""
from typing import AsyncGenerator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


from config import settings
from loguru import logger

async_database_url = URL.create(
    settings.MYSQL_PROTOCOL,
    settings.MYSQL_USERNAME,
    settings.MYSQL_PASSWORD,
    settings.MYSQL_HOST,
    settings.MYSQL_PORT,
    settings.MYSQL_DATABASE,
    {"charset": "utf8mb4"},
)

async_engine = create_async_engine(
    async_database_url,
    echo=settings.MYSQL_ECHO,
    max_overflow=settings.MYSQL_MAX_OVERFLOW,
    pool_size=settings.MYSQL_POOL_SIZE,
    pool_recycle=settings.MYSQL_POOL_RECYCLE,
    pool_timeout=settings.MYSQL_POOL_TIMEOUT,
)

async_session_maker = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, autocommit=False, expire_on_commit=False
)



async def generate_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    生成数据库会话
    """
    async with async_session_maker() as session:
        logger.debug("Database session created")
        try:
            yield session
        finally:
            await session.close()
            logger.debug("Database session closed")
