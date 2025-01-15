# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/15 15:54
@Author   : wiesZheng
@Software : PyCharm
"""
import aiohttp
from typing import Optional, Dict, Any, Union

class AsyncHttpClient:
    """
    异步http客户端，提供异步HTTP请求功能
    """
    def __init__(self):
        """初始化异步HTTP客户端"""
        self._session = None
        self._timeout = 30  # 默认超时时间30秒

    async def __aenter__(self):
        """异步上下文管理器入口"""
        import aiohttp
        if self._session is None:
            self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        if self._session:
            await self._session.close()
            self._session = None

    async def get(self, url: str, params: dict = None, headers: dict = None) -> dict:
        """
        执行异步GET请求
        :param url: 请求URL
        :param params: URL参数
        :param headers: 请求头
        :return: 响应数据
        """
        async with self._session.get(url, params=params, headers=headers, timeout=self._timeout) as response:
            return await response.json()

    async def post(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        """
        执行异步POST请求
        :param url: 请求URL
        :param data: 表单数据
        :param json: JSON数据
        :param headers: 请求头
        :return: 响应数据
        """
        async with self._session.post(url, data=data, json=json, headers=headers, timeout=self._timeout) as response:
            return await response.json()

    async def put(self, url: str, data: dict = None, json: dict = None, headers: dict = None) -> dict:
        """
        执行异步PUT请求
        :param url: 请求URL
        :param data: 表单数据
        :param json: JSON数据
        :param headers: 请求头
        :return: 响应数据
        """
        async with self._session.put(url, data=data, json=json, headers=headers, timeout=self._timeout) as response:
            return await response.json()

    async def delete(self, url: str, headers: dict = None) -> dict:
        """
        执行异步DELETE请求
        :param url: 请求URL
        :param headers: 请求头
        :return: 响应数据
        """
        async with self._session.delete(url, headers=headers, timeout=self._timeout) as response:
            return await response.json()

    def set_timeout(self, timeout: int):
        """
        设置请求超时时间
        :param timeout: 超时时间（秒）
        """
        self._timeout = timeout


async def main():
    async with AsyncHttpClient() as client:
        # GET请求
        response = await client.get('https://api.example.com/data')

        # POST请求
        data = {'name': 'test'}
        response = await client.post('https://api.example.com/create', json=data)

        # 设置超时时间
        client.set_timeout(60)
        response = await client.get('https://api.example.com/slow-endpoint')