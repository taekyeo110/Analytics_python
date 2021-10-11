from apscheduler.schedulers.background import BackgroundScheduler
from typing import Callable

scheduler = BackgroundScheduler()
scheduler.start()


def add_job(title: str, hour, minute, second, func: Callable = print, args: tuple = (), day_of_week: str = None):
    """
        스케쥴 작업 추가 함수
    """
    print(f"Job {title} Added({day_of_week if day_of_week is not None else 'everday'}, {hour}:{minute}:{second})")
    return scheduler.add_job(
        trigger='cron',
        day_of_week=day_of_week,
        id=title,
        hour=hour,
        minute=minute,
        second=second,
        func=func,
        args=args
    )


def remove_job(title: str):
    """
        스케쥴 작업 제거 함수
    """
    scheduler.remove_job(title)
    return 'Complete'


def get_jobs():
    """
        스케쥴 작업 목록 조회 함수
    """
    return scheduler.get_jobs()
