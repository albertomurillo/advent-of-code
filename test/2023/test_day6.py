import inspect

from aoc._2023.day6 import part1, part2

data = inspect.cleandoc(
    """
    Time:      7  15   30
    Distance:  9  40  200
    """
)


def test_part1() -> None:
    assert part1(data) == 288


def test_part2() -> None:
    assert part2(data) == 71503
