import pytest

from roll import Roll


@pytest.fixture(scope="module")
def rolls():
    print("Setting up")
    pass

def test_get_random():
    pass

def test_choose():
    roll = Roll()
    choice = roll.choose()
    assert choice == "Rock"