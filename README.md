# narou_api

 unofficial syosetu.com api library

## Installing

Install and update using pip

```
pip install -U narou-api
```

## A Simple Example

```python
import narou_api

r = narou_api.get(st=1, lim=5, order="new")
print(r.text)
```

CLI

```bash
narou_api get st=1 lim=5 order=new
```

|Function|Description|
|---|----|
|get|[なろう小説API](https://dev.syosetu.com/man/api/)|
|get_rank|[なろう小説ランキングAPI](https://dev.syosetu.com/man/rankapi/)|
|get_rankin|[なろう殿堂入りAPI](https://dev.syosetu.com/man/rankinapi/)|
|get_user|[なろうユーザ検索API](https://dev.syosetu.com/man/userapi/)|
|getx|[なろうR18小説API](https://dev.syosetu.com/xman/api/)|


## Links

- Official API Documet: https://dev.syosetu.com/man/api/
- PyPI Releases: https://pypi.org/project/narou-api/
