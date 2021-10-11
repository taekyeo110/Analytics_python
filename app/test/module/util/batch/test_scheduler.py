from app.main.modules.util.batch.scheduler import *
from datetime import datetime
import time

now = datetime.utcnow()


def test_scheduler():
    """
        스케쥴 작업 테스트(특성상 모든 함수 한곳에 포함)
    """

    def func(sec):
        print(f"In job function => Sec: {sec} Now: {now}")

    # 초당 작업 추가
    for sec in range(60):
        add_job(
            title=f"{sec} test",
            hour=None,
            minute=None,
            second=sec,
            func=func,
            args=(sec,)
        )

    # 짝수 제거
    for sec in range(60):
        if sec % 2 == 0:
            remove_job(f"{sec} test")

    # 남은 작업 조회
    jobs = get_jobs()
    print(jobs)

    count = 0
    while count < 30:
        print(f"{count} {datetime.utcnow()}")
        count += 1
        time.sleep(1)

    assert True
