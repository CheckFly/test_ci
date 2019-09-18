from test_ci import addition


def test_addition():
    assert addition(1, 1) == 2
    assert addition(-1, -1) == -2
    assert addition(-1, 1) == 0
    assert addition(1, -1) == 0
