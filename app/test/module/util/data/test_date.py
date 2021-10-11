from app.main.modules.util.data.date import *


def test_now():
    result = now()
    print(f"\n{result}")
    assert isinstance(result, date)


def test_now_time():
    result = now_time()
    time.sleep(5)
    result_2 = now_time()
    result_3 = result_2 - result
    print(f"\n{result_3}")
    assert isinstance(result, date)


def test_today():
    result = today()
    print(f"\n{result}")
    assert isinstance(result, date)


def test_get_date():
    result = get_date('2021-01-01')
    print(f"\n{result}")
    assert isinstance(result, date)


def test_get_date_format():
    result = get_date_format('2021-01-01', "%Y%m%d")
    print(f"\n{result}")
    assert isinstance(result, str)


def test_get_date_list():
    start_date = add_days(today(), -10)
    end_date = add_days(today(), 10)
    date_list = get_date_list(start_date, end_date)
    print(f"\n{date_list}")
    assert isinstance(date_list, list)


def test_add_days():
    result = add_days(today(), -10)
    print(f"\n{result}")
    assert isinstance(result, date)


def test_calculate_days():
    result = calculate_days(today(), add_days(today(), 1))
    print(f"\n{result}")
    assert isinstance(result, int)


def test_calculate_seconds():
    result = calculate_seconds(today(), add_days(today(), 1))
    print(f"\n{result}")
    assert isinstance(result, int)


def test_day_loop():
    start_date = add_days(today(), -10)
    end_date = add_days(today(), 10)
    loop_days(start_date, end_date, lambda x: print(x))
    assert True


def test_calculate_loop_time_by_period():
    result = calculate_loop_time_by_period(6,5)
    print(result)
    assert isinstance(result, tuple)