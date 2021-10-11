from mysql.connector import Error

from app.main.modules.util.logger.store import *


def test_log_job():
    result = log_job('test title', 12, 10, 10)
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_log_request():
    result = log_request('GET', 'http://localhost', 200, 0.1, {"dict": "dict"})
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_log_mysql_error():
    try:
        raise Error(msg='test message', errno=100, sqlstate='test sqlstate')
    except Error as e:
        result = log_mysql_error(e.msg, e.errno, e.sqlstate)
        print(f"\n{result}")
    assert isinstance(result, dict)


def test_log_send_mail():
    doc = {
        "send_from": "send_from",
        "send_to": ["send_to"],
        "subject": "subject",
        "text": "text",
        "html": "html",
        "files": ["files"],
    }
    result = log_send_mail(**doc)
    print(f"\n{result}")
    assert isinstance(result, dict)
