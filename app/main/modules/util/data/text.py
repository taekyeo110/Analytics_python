import re


def wrap_quote(text: str, quote: str):
    """
            text 양 옆에 quote 붙이기
            ex. 'text' "text" `text`
    """
    return f"{quote}{text}{quote}"


def camel_to_snake(name: str):
    """
            문자 표기법
            카멜(자바식) -> 스네이크(파이썬식)
    """
    name = re.sub('[^_A-Za-z0-9]+', '', name)
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name) \
        .lower() \
        .replace(" ", "_") \
        .replace("__", "_")


def single_quote_to_duoble_quote(text: str):
    """
            작은 따옴표 -> 큰 따옴표
    """
    return text.replace("'", "\"")


def insert_unicode_in_text(text: str, unicode: str, locate: list):
    """
            전화번호에 - 넣듯이,
            텍스트를 받은 후 원하는 위치에 원하는 특수문자 삽입
    """
    text_list = list(text)
    for count in locate:
        text_list.insert(count, unicode)
    return "".join(text_list)


def remove_double_bars(data_list: list):
    """
            빈 값을 --로 표현하는 경우 삭제
    """
    return [None if data == ' --' or '--' in data else data for data in data_list]
