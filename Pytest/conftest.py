import pytest

#when module is passed under scope of fixture, then it means it will run only once before start.
#when function is passed under scope of fixture, then it means it will run every time before rning function.

''''
function = : It runs once per test function.
module = It runs once per Python file (.py file).
session = It runs once per entire test suite execution.
'''

@pytest.fixture(scope="module")
def prework():
    print("I setup browser instance")
