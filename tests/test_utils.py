from src.utils import add, div, mul, sub


def test_answer() -> None:
    assert add(3, 1) == 4
    assert sub(1, 2) == -1
    assert div(1, 2) == 0
    assert mul(1, 2) == 2
