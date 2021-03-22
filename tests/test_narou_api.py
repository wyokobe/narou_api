import narou_api


def test_get():
    r = narou_api.get()
    print(r.text)
    assert r.status_code == 200


def test_get_rank():
    r = narou_api.get_rank()
    print(r.text)
    assert r.status_code == 200


def test_get_rankin():
    r = narou_api.get_rankin()
    print(r.text)
    assert r.status_code == 200


def test_get_user():
    r = narou_api.get_user()
    print(r.text)
    assert r.status_code == 200


def test_getx():
    r = narou_api.getx()
    print(r.text)
    assert r.status_code == 200


def test_get_with_kwargs():
    r = narou_api.get(out="json", st=1, lim=1, order="hyoka")
    print(r.text)
    assert r.status_code == 200
