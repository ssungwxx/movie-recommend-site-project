import pytest


def func(x):
    return x + 1


@pytest.mark.test_id(1)
def test_answer():
    assert func(3) == 4


@pytest.mark.test_id(2)
def test_function():
    assert True
