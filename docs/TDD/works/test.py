import main
import pytest

def test_case0():
        # ID는 존재, PW는 일치
        assert main.Login('test1', 'test1234') == True
        pass

def test_case1():
        # ID 는 공란 
        assert main.Login('', 'test1234') == main.FIRST_CASE_RESULT
        pass

def test_case2():
        # ID는 존재, PW는 불일치
        assert main.Login('test1', '1234') == main.SECOND_CASE_RESULT
        pass

def test_case3():
        # ID는 미존재, PW는 공란
        assert main.Login('testtest','') == main.THIRD_CASE_RESULT
        pass

def test_case4():
        # ID는 미존재, PW는 값 있음
        assert main.Login('testtest','1234') == main.FOURTH_CASE_RESULT
        pass

def test_case5():
        # ID는 존재, PW는 공란
        assert main.Login('test1','') == main.FIFTH_CASE_RESULT
        pass

