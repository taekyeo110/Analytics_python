from app.main.modules.util.mysql import *


def test_fetch():
    result = fetch(['SELECT * FROM insert_test LIMIT 1000'])
    print(f"\nTEST Result: {result}")
    assert isinstance(result, list)


def test_fetch_prepared_statement():
    result = fetch(['SELECT * FROM insert_test WHERE column_1 = %s'], (1,))
    print(f"\nTEST Result: {result}")
    assert isinstance(result, list)


def test_execute():
    execute('CREATE TABLE test_table_temp(test int null)')
    result = execute('DROP TABLE test_table_temp')
    print(f"\nTEST Result: {result}")
    assert result == 'Complete'


def test_call_procedure():
    start_date = '2021-03-19'
    end_date = '2021-03-22'
    result = call_procedure('Raw_GMC_SEM_Media', [start_date, end_date], False, 'report')
    print(result)
    assert True
