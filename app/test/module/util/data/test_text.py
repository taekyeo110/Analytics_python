from app.main.modules.util.data.text import *


def test_wrap_quote():
    result = wrap_quote('ohhhh', '`')
    print(f"\n{result}")
    assert isinstance(result, str)


def test_camel_to_snake():
    camel_list = ['Customer ID', 'Account', 'Ad', 'Headline 1', 'Headline 2', 'Short headline', 'Long headline']
    result = [camel_to_snake(camel) for camel in camel_list]
    print(f"\n{result}")
    assert isinstance(result, list)


def test_single_quote_to_duoble_quote():
    result = single_quote_to_duoble_quote("'fkfds'sdf'dg")
    print(result)
    assert isinstance(result, str)


def test_insert_unicode_in_text():
    result = insert_unicode_in_text('4173235612','-',[3,7])
    print(result)
    assert isinstance(result,str)
