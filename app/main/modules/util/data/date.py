import copy
from typing import Callable
from datetime import date, datetime, timedelta
import time


def now():
    """
            utc 기준 현 시각 리턴
    """
    return datetime.utcnow()


def now_time():
    """
            현재 시간 리턴
    """
    return time.time()


def today():
    """
            오늘 날짜 리턴
    """
    return date.today()


def get_date(date_string):
    """
            오늘 날짜를 string으로 받아 datetime 형태로 리턴
    """
    return datetime.strptime(date_string, "%Y-%m-%d").date()


def get_date_format(date_string, format_to="%Y-%m-%d", format_from="%Y-%m-%d"):
    """
            string 혹은 date 타입을 datetime 타입으로 변경
    """
    if isinstance(date_string, date):
        return date_string.strftime(format_to)
    else:
        return datetime.strptime(date_string, format_from).strftime(format_to)


def get_date_list(start_date: date, end_date: date):
    """
            start date ~ end date의 날짜들을 리스트로 변경하여 리턴
    """
    date_list = []
    while start_date <= end_date:
        date_list.append(copy.deepcopy(start_date))
        start_date = add_days(start_date, 1)
    return date_list


def add_days(target_date: date, day_count: int):
    """
            날짜에 원하는 값만큼 날짜 더하기
    """
    return target_date + timedelta(days=day_count)


def calculate_days(start_date: date, end_date: date):
    """
            두 날짜 사이의 기간 계산
    """
    return (end_date - start_date).days


def calculate_seconds(start_date: date, end_date: date):
    """
            두 시간의 시간초 차이를 계산
    """
    return (end_date - start_date).seconds


def loop_days(start_date: date, end_date: date, callback: Callable):
    """
            start_date ~ end_date 만큼의 기간동안 루프를 돌며 callback에 정의된 함수 실행
    """
    while start_date <= end_date:
        print(f"loop_days: {start_date}")
        callback(start_date)
        start_date = add_days(start_date, 1)


def calculate_loop_time_by_period(period: int, standard_period: int):
    """
            파라미터로 들어온 기간에 대해 지정한 기간으로 나누어 기간 실행 횟수, 남은 기간을 리턴
                -> 긴 기간의 파라미터가 들어왔을 경우
                -> 기준 기간보다 적은 수의 기간이 파라미터로 들어왔을 경우
                -> 기간이 없을 경우
    """
    loop_times = 0
    is_remain = False
    remain = 0
    if period > standard_period:
        if period % standard_period == 0:
            if period / standard_period == 0:
                loop_times = 0
            elif period / standard_period >= 1:
                loop_times = int(period / standard_period)
        elif period % standard_period != 0:
            if period / standard_period == 0:
                loop_times = 1
            elif period / standard_period >= 1:
                loop_times = int(period / standard_period) + 1
                is_remain = True
                remain = period % standard_period
    elif period < standard_period:
        loop_times = 1
        is_remain = True
        remain = period
    elif period == standard_period:
        loop_times = 1
        is_remain = False
        remain = 0
    return loop_times, is_remain, remain
