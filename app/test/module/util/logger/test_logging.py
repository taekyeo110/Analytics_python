from app.main.modules.util.logger.logging import logging
from app.main.modules.util.data.date import now
import time


def test_logging():
    start = now()
    time.sleep(5)
    end = now()
    result = logging(None, None, 'test_account', 'test_result', 'test_media', 'test_type', 0, 0)
    print(result)
    assert result is None
