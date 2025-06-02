import pytest

from solution import strict


@pytest.fixture(scope='module')
def sum_two():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    return sum_two


def test_result(sum_two):
    assert sum_two(5, 10) == 15


def test_error_calling(sum_two):
    assert sum_two(1, 2) == 3
    with pytest.raises(TypeError):
        sum_two(1, 2.4)
