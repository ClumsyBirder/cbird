# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/14
@Author   : shweZheng
@Software : PyCharm
"""
from datetime import datetime, UTC
from sqlalchemy import Integer, Column, String, JSON, TIMESTAMP

from app.models import Base


class TestCase(Base):
    """
    测试用例表
    """
    __tablename__ = "test_case"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    url = Column(String, index=True)
    method = Column(String, index=True)
    headers = Column(JSON)
    body = Column(JSON)
    expected_status = Column(Integer)
    expected_response = Column(JSON)
    created_at = Column(TIMESTAMP, default=datetime.now(UTC))
    updated_at = Column(TIMESTAMP, default=datetime.now(UTC), onupdate=datetime.now(UTC))
