#Any pytest file should start with "test_"
#pytest name should start with test.
#Any code should be wrapped in method only.
# -k stand for method names execution , -s logs in output , -v stands for more info metadata
# we can run specific file with py.test <filename>
import pytest


@pytest.mark.smoke
def test_FirstProgram():
    print("Hello")

def test_addition():
    x =10
    y= 20
    assert x+y==30

def test_string_match():
    name="playwright"
    assert  "pytest" in name

def test_subtraction():
    a=50
    b=90
    assert b-a==100

def TC_01():
    a=40
    b=60
    assert a+20==b , "Addition do not match"
