import inspect

from aoc._2024.day2 import part1, part2

data = inspect.cleandoc(
    """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
)


def test_part1() -> None:
    assert part1(data) == 2


def test_part2() -> None:
    assert part2(data) == 4
