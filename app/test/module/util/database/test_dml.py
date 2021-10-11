from app.main.modules.util.mysql import *


def test_select():
    result = select('SELECT * FROM insert_test LIMIT 1000')
    print(f"\nTEST Result: {result}")
    assert isinstance(result, list)


def test_insert():
    column_list = ('column_2', 'column_3', 'column_4', 'column_5', 'column_6')
    data = [
        ('h', 'i', 'j', 'k', 'l'),
        ('h', 'i', 'j', 'k', 'l'),
        ('h', 'i', 'j', 'k', 'l'),
        ('h', 'i', 'j', 'k', 'l'),
        ('h', 'i', 'j', 'k', 'l')
    ]
    result = insert('insert_test', column_list, data)
    print(f"\nTEST Result: {result}")
    assert result == 'Complete'


def test_insert_many_data():
    array_data = []
    column_list = ('column_2', 'column_3', 'column_4', 'column_5', 'column_6')
    for count in range(500000):
        array_data.append(('h', 'i', 'j', 'k', 'l'))
    result = insert('insert_test', column_list, array_data)
    print(f"\nTEST Result: {result}")
    assert result == 'Complete'


def test_update():
    key_column = 'column_1'
    target_columns = ('column_2', 'column_3', 'column_4', 'column_5', 'column_6')
    data = [
        {
            "key": 775226,
            "value": ('수정된 h', '수정된 i', '수정된 j', '수정된 k', '수정된 l')
        },
        {
            "key": 775225,
            "value": ('수정된 h', '수정된 i', '수정된 j', '수정된 k', '수정된 l')
        },
        {
            "key": 775224,
            "value": ('수정된 h', '수정된 i', '수정된 j', '수정된 k', '수정된 l')
        },
    ]
    result = update('insert_test', key_column, target_columns, data)
    print(f"\nTEST Result: {result}")
    assert result == 'Complete'


def test_delete():
    key_column = 'column_1'
    key_list = [775223, 775222, 775221]
    result = delete('insert_test', key_column, key_list)
    print(f"\nTEST Result: {result}")
    assert result == 'Complete'
