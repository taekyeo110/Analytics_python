from app.main.modules.util.data.data_type import *


def test_convert_data_type():
    result = check_data_type([
        'haha',
        123123123123123,
        1561231,
        ['ha', 1, 'hahaha'],
        {'ha': 1, },
        ('yeah', 3),
        None,
        1.52,
        True,
        False,
        0,
        1,
    ])
    print(result)
    assert isinstance(result, tuple)


def test_check_data_type_before_create_table():
    result = check_data_type_before_create_table(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
        [
            'haha',
            123123123123123,
            1561231,
            ['ha', 1, 'hahaha'],
            {'ha': 1, },
            ('yeah', 3),
            None,
            1.52,
            True,
            False,
            0,
            1,
        ]
    )
    print(result)
    assert isinstance(result, list)


def test_convert_data_type_when_already_create_table():
    result = convert_data_type_when_already_create_table(
        'hermes',
        'convert_data_type',
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
        [
            'haha',
            123123123123123,
            1561231,
            ['ha', 1, 'hahaha'],
            {'ha': 1, },
            ('yeah', 3),
            None,
            1.52,
            True,
            False,
            0,
            1,
        ]
    )
    print(result)
    assert result == "Complete"
