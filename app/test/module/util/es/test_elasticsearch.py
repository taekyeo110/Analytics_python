from app.main.modules.util.data.date import now
from app.main.modules.util.es.elasticsearch import *


def test_index():
    doc = {
        'author': 'test',
        'text': 'target text2',
        'timestamp': now(),
    }
    result = index(target_index="test-index", target_id=1, body=doc)
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_get():
    result = get(target_index="test-index", target_id=1)
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_search():
    doc = {"query": {"match_all": {}}}
    result = search(target_index="test-index", body=doc)
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_refresh():
    result = refresh(target_index="test-index")
    print(f"\n{result}")
    assert isinstance(result, dict)
