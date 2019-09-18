import pytest
from test_ci import addition


def test_addition():
    assert addition(1, 1) == 2
    assert addition(-1, -1) == -2
    assert addition(-1, 1) == 0
    assert addition(1, -1) == 0

if __name__ == "__main__"
    test_addition()