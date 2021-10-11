from app.main.modules.algorithm.solution_1 import transfer_lower_alphabet, remove_unicode, remove_duplicated_dot, \
    remove_side_dot, confirm_blank_id, detect_bigger_than_16, attach_str_to_smaller_than_2_str_until_3, solution

# NEW_ID = ''


def test_transfer_lower_alphabet():
    NEW_ID = "...!@BaT#*..y.abcdefghijklm"
    result = transfer_lower_alphabet(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_remove_unicode():
    NEW_ID = "...!@bat#*..y.abcdefghijklm"
    result = remove_unicode(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_remove_duplicated_dot():
    NEW_ID = "...bat..y.abcdefghijklm"
    result = remove_duplicated_dot(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_remove_side_dot():
    NEW_ID = ".bat.y.abcdefghijklm"
    result = remove_side_dot(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_confirm_blanck_id():
    NEW_ID = "bat.y.abcdefghijklm"
    NEW_ID = ''
    result = confirm_blank_id(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_detect_bigger_than_16():
    NEW_ID = "bat.y.abcdefghijklm"
    result = detect_bigger_than_16(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_attach_str_to_smaller_than_2_str_until_3():
    NEW_ID = "bat.y.abcdefghi"
    NEW_ID = "a"
    result = attach_str_to_smaller_than_2_str_until_3(NEW_ID)
    print(result)
    assert isinstance(result, str)


def test_solution():
    NEW_ID = "...!@BaT#*..y.abcdefghijklm"
    result = solution(NEW_ID)
    print(f"최종 결과값 : {result}")
    # 결과값 : "bat.y.abcdefghi"
    assert result == "bat.y.abcdefghi"
