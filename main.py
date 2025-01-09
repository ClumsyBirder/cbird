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

from app.api import api_router
from app.core.middleware import error_handler_middleware
from config import settings
from app.db.session import init_db


# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure Loguru
logger.add("logs/app.log", rotation="10 MB", compression="zip", level="INFO")

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# Add error handler middleware
app.middleware("http")(error_handler_middleware)

app.include_router(api_router, prefix=settings.APP_API_STR)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application")
    await init_db()

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the application")

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting the server")
    uvicorn.run(app, host="0.0.0.0", port=8000)