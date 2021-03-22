import sys

import requests


def get(**kwargs):
    """
    なろう小説API
    @see https://dev.syosetu.com/man/api/
    """
    url = "https://api.syosetu.com/novelapi/api/"
    return exec_get(url, **kwargs)


def get_rank(**kwargs):
    """
    なろう小説ランキングAPI
    @see https://dev.syosetu.com/man/rankapi/
    """
    url = "https://api.syosetu.com/rank/rankget/"
    return exec_get(url, **kwargs)


def get_rankin(**kwargs):
    """
    なろう殿堂入りAPI
    @see https://dev.syosetu.com/man/rankinapi/
    """
    url = "https://api.syosetu.com/rank/rankin/"
    return exec_get(url, **kwargs)


def get_user(**kwargs):
    """
    なろうユーザ検索API
    @see https://dev.syosetu.com/man/userapi/
    """
    url = "https://api.syosetu.com/userapi/api/"
    return exec_get(url, **kwargs)


def getx(**kwargs):
    """
    なろうR18小説API
    @see https://dev.syosetu.com/xman/api/
    """
    url = "https://api.syosetu.com/novel18api/api/"
    return exec_get(url, **kwargs)


def exec_get(url, **kwargs):
    """共通GETエクゼキューター"""
    is_first_loop = True
    for k, v in kwargs.items():
        if is_first_loop:
            url += "?"
            is_first_loop = False
        else:
            url += "&"
        url += f"{k}={v}"

    return requests.get(url)


commands = locals()


def main() -> None:
    if sys.argv[1] in commands:
        func = commands[sys.argv[1]]
        r = func(**dict(arg.split('=') for arg in sys.argv[2:]))
        print(r.text)
