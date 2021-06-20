import sys

import requests


def get(timeout=30.0, **kwargs):
    """
    なろう小説API
    @see https://dev.syosetu.com/man/api/
    """
    url = "https://api.syosetu.com/novelapi/api/"
    return exec_get(url, float(timeout), **kwargs)


def get_rank(timeout=30.0, **kwargs):
    """
    なろう小説ランキングAPI
    @see https://dev.syosetu.com/man/rankapi/
    """
    url = "https://api.syosetu.com/rank/rankget/"
    return exec_get(url, float(timeout), **kwargs)


def get_rankin(timeout=30.0, **kwargs):
    """
    なろう殿堂入りAPI
    @see https://dev.syosetu.com/man/rankinapi/
    """
    url = "https://api.syosetu.com/rank/rankin/"
    return exec_get(url, float(timeout), **kwargs)


def get_user(timeout=30.0, **kwargs):
    """
    なろうユーザ検索API
    @see https://dev.syosetu.com/man/userapi/
    """
    url = "https://api.syosetu.com/userapi/api/"
    return exec_get(url, float(timeout), **kwargs)


def getx(timeout=30.0, **kwargs):
    """
    なろうR18小説API
    @see https://dev.syosetu.com/xman/api/
    """
    url = "https://api.syosetu.com/novel18api/api/"
    return exec_get(url, float(timeout), **kwargs)


def exec_get(url, timeout=30.0, **kwargs):
    """共通GETエクゼキューター"""
    is_first_loop = True
    for k, v in kwargs.items():
        if is_first_loop:
            url += "?"
            is_first_loop = False
        else:
            url += "&"
        url += f"{k}={v}"

    return requests.get(url, timeout=timeout)


commands = locals()


def main() -> None:
    if sys.argv[1] in commands:
        func = commands[sys.argv[1]]
        r = func(**dict(arg.split('=') for arg in sys.argv[2:]))
        print(r.text)
