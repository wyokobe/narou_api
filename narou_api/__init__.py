import sys

import requests


def get(**kwargs):
    """
    なろう小説APIを実行
    @see https://dev.syosetu.com/man/api/
    """
    is_first_loop = True
    url = "https://api.syosetu.com/novelapi/api/"
    for k, v in kwargs.items():
        if is_first_loop:
            url += "?"
            is_first_loop = False
        else:
            url += "&"
        url += k + "=" + v

    return requests.get(url)


def main() -> None:
    r = get(**dict(arg.split('=') for arg in sys.argv[1:]))
    print(r.text)
