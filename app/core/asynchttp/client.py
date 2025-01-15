# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/1/7
@Author   : shweZheng
@Software : PyCharm
"""
import time
import aiohttp
from datetime import timedelta
from typing import Optional, Dict, Union, Any
from loguru import logger
from aiohttp import ClientResponse

from enum import Enum


class HttpMethod(Enum):
    """HTTP请求方法枚举"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class AsyncHttpClient:
    """
    异步http客户端
    """

    def __init__(self, base_url: str = "", timeout=timedelta(seconds=10), headers: Optional[Dict] = None, **kwargs):
        """
        初始化异步HTTP客户端
        :param base_url: 基础URL
        :param timeout: 超时时间(秒)
        :param kwargs: 其他参数
        """
        self._session: Optional[aiohttp.ClientSession] = None
        self._timeout = aiohttp.ClientTimeout(timeout.total_seconds())
        self._base_url = base_url
        self._headers = headers or {}
        self.kwargs = kwargs

    async def __aenter__(self):
        """支持异步上下文管理器"""
        if self._session is None:
            self._session = aiohttp.ClientSession(headers=self._headers, timeout=self._timeout, **self.kwargs)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """关闭会话"""
        if self._session:
            await self._session.close()
            self._session = None

    def _build_url(self, url: str) -> str:
        """构建完整的URL"""
        return f"{self._base_url}{url}" if self._base_url else url

    async def request(
            self,
            method: HttpMethod,
            url: str,
            params: Optional[Dict] = None,
            data: Optional[Dict] = None,
            timeout: Optional[timedelta] = None,
            headers: Optional[Dict] = None,
            **kwargs
    ) -> ClientResponse:
        """
        发送HTTP请求
        :param method: HTTP方法，支持字符串或HttpMethod枚举
        :param url: 请求URL
        :param params: 请求查询参数
        :param data: 表单数据
        :param timeout: 超时时间(秒)
        :param headers: 请求头
        :param kwargs: 其他请求参数
        :return: 响应数据
        """
        if isinstance(method, str):
            method = method.upper()
            if method not in HttpMethod._member_names_:
                raise ValueError(f"Invalid HTTP method: {method}")
            http_method = method
        elif isinstance(method, HttpMethod):
            http_method = method.value
        else:
            raise ValueError(f"Invalid HTTP method type: {type(method)}")

        timeout = timeout or self._timeout
        if isinstance(timeout, timedelta):
            timeout = aiohttp.ClientTimeout(timeout.total_seconds())

        url = self._build_url(url)
        headers = headers or {}
        headers.update(self._headers)

        logger.info(f"Sending {http_method} request to {url}")
        logger.debug(f"Request params: {params}")
        logger.debug(f"Request data: {data}")
        logger.debug(f"Request headers: {headers}")

        start_time = time.time()
        try:
            response = await self._session.request(http_method, url, params=params, data=data, timeout=timeout,
                                                   headers=headers,
                                                   **kwargs)
            elapsed_time = time.time() - start_time
            logger.info(f"Received response from {url}, status: {response.status}, time: {elapsed_time:.3f}s")
            return response
        except Exception as e:
            elapsed_time = time.time() - start_time
            logger.error(f"Request failed: {str(e)}, time: {elapsed_time:.3f}s")
            raise

    async def get(
            self,
            url: str,
            params: Optional[Dict] = None,
            timeout: Optional[timedelta] = None,
            **kwargs
    ) -> ClientResponse:
        """
        发送GET请求
        :param url: 请求URL
        :param params: URL参数
        :param timeout: 超时时间(秒)
        :param kwargs: 其他请求参数
        :return: 响应数据
        """
        return await self.request(HttpMethod.GET, url, params=params, timeout=timeout, **kwargs)

    async def post(
            self,
            url: str,
            data: Optional[Union[Dict, str]] = None,
            json_data: Optional[Dict] = None,
            timeout: Optional[timedelta] = None,
            **kwargs
    ) -> ClientResponse:
        """
        发送POST请求
        :param url: 请求URL
        :param data: 表单数据
        :param json_data: JSON数据
        :param timeout: 超时时间(秒)
        :param kwargs: 其他请求参数
        :return: 响应数据
        """
        return await self.request(HttpMethod.POST, url, data=data, json=json_data, timeout=timeout, **kwargs)

    async def put(
            self,
            url: str,
            data: Optional[Union[Dict, str]] = None,
            json_data: Optional[Dict] = None,
            timeout: Optional[timedelta] = None,
            **kwargs
    ) -> ClientResponse:
        """
        发送PUT请求
        :param url: 请求URL
        :param data: 表单数据
        :param json_data: JSON数据
        :param timeout: 超时时间(秒)
        :param kwargs: 其他请求参数
        :return: 响应数据
        """
        return await self.request(HttpMethod.PUT, url, data=data, json=json_data, timeout=timeout, **kwargs)

    async def delete(
            self,
            url: str,
            data: Optional[Union[Dict, str]] = None,
            json_data: Optional[Dict] = None,
            timeout: Optional[timedelta] = None,
            **kwargs
    ) -> ClientResponse:
        """
        发送DELETE请求
        :param url: 请求URL
        :param data: 表单数据
        :param json_data: JSON数据
        :param timeout: 超时时间(秒)
        :param kwargs: 其他请求参数
        :return: 响应数据
        """
        return await self.request(HttpMethod.DELETE, url, data=data, json=json_data, timeout=timeout, **kwargs)


async def main():
    async with AsyncHttpClient() as client:
        # GET请求
        response = await client.get('https://api.example.com/data')

        # POST请求
        data = {'name': 'test'}
        response = await client.post('https://api.example.com/create', json=data)

        response = await client.get('https://api.example.com/slow-endpoint')
