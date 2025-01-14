# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/14
@Author   : shweZheng
@Software : PyCharm
"""
from pydantic import BaseModel
from typing import Optional, Dict


class TestCaseBase(BaseModel):
    name: str
    description: Optional[str] = None
    url: str
    method: str
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict] = None
    expected_status: Optional[int] = None
    expected_response: Optional[Dict] = None


class TestCaseCreate(TestCaseBase):
    pass


class TestCaseUpdate(TestCaseBase):
    pass


class TestCaseInDBBase(TestCaseBase):
    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True


class TestCase(TestCaseInDBBase):
    pass
