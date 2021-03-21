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

r = narou_api.get(out="json", st=1, lim=500, order="quarterpoint")
print(r.text)
```

CLI

```bash
narou_api out=json st=1 lim=500 order=quarterpoint
```

## Links

- Official API Documet: https://dev.syosetu.com/man/api/
- PyPI Releases: https://pypi.org/project/narou-api/
