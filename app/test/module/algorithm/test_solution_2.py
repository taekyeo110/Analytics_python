from app.main.modules.algorithm.solution_2 import solution


def test_solution_1():
    result = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    print(result)
    assert result == ["AC", "ACDE", "BCFG", "CDE"]


def test_solution_2():
    result = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
    print(result)
    assert result == ["ACD", "AD", "ADE", "CD", "XYZ"]


def test_solution_3():
    result = solution(["XYZ", "XWY", "WXA"], [2,3,4])
    print(result)
    assert result == ["WX", "XY"]
