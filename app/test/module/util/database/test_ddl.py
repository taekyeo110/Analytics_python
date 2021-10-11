from app.main.modules.util.mysql import *


def test_create_table():
    execute('DROP TABLE IF EXISTS test_table')
    result = create_table('test_table', [get_column_definition('test', 'int', 'null')])
    print(f"\n{result}")
    assert result == 'Complete'


def test_add_column():
    result = add_column('test_table', get_column_definition('test_col', 'int', 'null'))
    print(f"\n{result}")
    assert result == 'Complete'


def test_add_index():
    result = add_index('test_table', 'test_col_index', ['test_col'])
    print(f"\n{result}")
    assert result == 'Complete'


def test_describe_table_true():
    result = describe_table('report', 'insert_test2')
    print(f"\n{result}")
    assert isinstance(result, dict)


def test_describe_table_false():
    result = describe_table('report', 'test_table')
    print(f"\n{result}")
    assert result == False


def test_create_data_table():
    result = create_data_table(
        table_name='google_ads_account',
        columns=['name', 'customer_id', 'can_manage_clients', 'currency_code', 'date_time_zone', 'test_account', 'account_labels', 'exclude_hidden_accounts']
    )
    print(f"\n{result}")
    assert True
