def flat_list(list_by_list: list):
    """
            리스트 평탄화
            라이브러리 사용 가능하나, 안전한 유지보수를 위해 최대한 라이브러리 사용 지양
    """
    final_list = []
    for list_num in list_by_list:
        final_list.extend(list_num)
    return final_list