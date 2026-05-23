import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixture_demo(setup):
    print("I will execute steps in fixturedemo method")

