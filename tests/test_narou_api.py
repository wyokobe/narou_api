import narou_api


def test_get():
    r = narou_api.get()
    assert r.status_code == 200


def test_get_with_kwargs():
    r = narou_api.get(out="json", st=1, lim=1, order="hyoka")
    assert r.status_code == 200
