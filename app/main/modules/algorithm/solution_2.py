import re


def solution(orders, course):
    for order in orders:
        if len(order) < 2:
            raise "order의 개수가 적습니다."
        for menu in order:
            if menu.isalpha() is False:
                raise "order가 잘못되었습니다."
    answer = []
    return answer
