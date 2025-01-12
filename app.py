# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/11
@Author   : shweZheng
@Software : PyCharm
"""
import uvicorn
from loguru import logger

from config import settings

if __name__ == "__main__":
    logger.info("Starting the server")
    uvicorn.run(
        app="main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_RELOAD,
        forwarded_allow_ips="*",
        access_log=True,
    )
