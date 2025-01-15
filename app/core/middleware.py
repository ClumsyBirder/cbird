# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/9 17:38
@Author   : wiesZheng
@Software : PyCharm
"""
from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from loguru import logger

from app.exception.errors import AppException


async def error_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except AppException as e:
        logger.error(f"Application error: {e.error_code} - {str(e)}")
        return JSONResponse(
            status_code=e.status_code,
            content={"error_code": e.error_code, "detail": str(e)}
        )
    except StarletteHTTPException as e:
        logger.error(f"HTTP error: {e.status_code} - {str(e.detail)}")
        return JSONResponse(
            status_code=e.status_code,
            content={"error_code": "HTTP_ERROR", "detail": str(e.detail)}
        )
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error_code": "DATABASE_ERROR", "detail": "An error occurred while processing your request."}
        )
    except Exception as e:
        logger.exception(f"Unexpected error: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error_code": "INTERNAL_SERVER_ERROR", "detail": "An unexpected error occurred."}
        )
