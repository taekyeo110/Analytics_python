from app.main.modules.util.network.request import get


def test_request():
    result = get('http://athenaapi.artience.com/api/v1/user/token')
    assert isinstance(result, dict)
