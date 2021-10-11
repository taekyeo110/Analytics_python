import time

import aiohttp
import requests
from app.main.modules.util.logger.store import log_request

type_functions = {
    'url': lambda res: res.url,
    'json': lambda res: res.json(),
    'raw': lambda res: res
}


async def get_async(url: str, params: dict = {}):
    """
        Get 요청 함수 (비동기)
            -> flask 자체에서 비동기를 지원하기 떄문에 미사용
    """
    async with aiohttp.ClientSession() as session:
        start = time.time()
        async with session.get(url, params=params) as response:
            end = time.time()
            # log_request('GET', url, response.status, end - start, dict(response.headers))
            if response.status == 200:
                data = response.json()
                return data
            else:
                print(f"\n{response.status} Error / {response.content}")


def get(url: str, params: dict = {}, headers: dict = {}, return_type: str = 'json'):
    """
        Get 요청 함수
    """
    response = requests.get(url, params, headers=headers)
    # log_request('GET', url, response.status_code, response.elapsed.total_seconds(), dict(response.headers))
    if response.status_code == 200:
        return type_functions[return_type](response)
    else:
        print(f"\n{response.status_code} Error / {response.content}")


def post(url: str, body: dict = {}, headers: dict = {}, json=False, return_type: str = 'json'):
    """
        Post 요청 함수
    """
    response = requests.post(url, data=body, headers=headers) \
        if not json \
        else requests.post(url, json=body, headers=headers)
    # log_request('POST', url, response.status_code, response.elapsed.total_seconds(), dict(response.headers))
    if response.status_code == 200:
        return type_functions[return_type](response)
    else:
        print(f"\n{response.status_code} Error / {response.content}")
        raise Exception(response.status_code)
