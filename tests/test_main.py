# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/14
@Author   : shweZheng
@Software : PyCharm
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_create_test_case():
    response = client.post(
        "/test-cases/",
        json={"name": "Test Case 1", "url": "http://example.com", "method": "GET"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Case 1"
    assert "id" in data

def test_read_test_cases():
    response = client.get("/test-cases/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)