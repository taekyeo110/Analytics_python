import re


def transfer_lower_alphabet(input_id):
    """
            1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    """
    return input_id.lower()


def remove_unicode(input_id):
    """
            2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    """
    return re.sub("[^A-Za-z0-9._-]", "", input_id)


def remove_duplicated_dot(input_id):
    """
            3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    """
    return re.sub('(([.])\\2+)', '.', input_id)


def remove_side_dot(input_id):
    """
            4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    """
    return input_id.strip('.')


def confirm_blank_id(input_id):
    """
            5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    """
    return 'a' if len(input_id) == 0 else input_id


def detect_bigger_than_16(input_id):
    """
            6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
                 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    """
    return input_id[:15].rstrip('.') if len(input_id) >= 16 else input_id


def attach_str_to_smaller_than_2_str_until_3(input_id):
    """
            7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    """
    if len(input_id) <= 2:
        while len(input_id) < 3:
            input_id += input_id[-1]
    return input_id


def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3 - len(st))])
    return st
    # print("\n ---------결과------------")
    # id_1 = transfer_lower_alphabet(new_id)
    # print(f"첫번째 함수 결과값 : {id_1}")
    # id_2 = remove_unicode(id_1)
    # print(f"두번째 함수 결과값 : {id_2}")
    # id_3 = remove_duplicated_dot(id_2)
    # print(f"세번째 함수 결과값 : {id_3}")
    # id_4 = remove_side_dot(id_3)
    # print(f"네번째 함수 결과값 : {id_4}")
    # id_5 = confirm_blank_id(id_4)
    # print(f"다섯번째 함수 결과값 : {id_5}")
    # id_6 = detect_bigger_than_16(id_5)
    # print(f"여섯째 함수 결과값 : {id_6}")
    # id_7 = attach_str_to_smaller_than_2_str_until_3(id_6)
    # print(f"일곱번째 함수 결과값 : {id_7}")
    # answer = id_7
    # return answer
