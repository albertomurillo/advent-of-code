import inspect

from aoc._2022.day1 import part1, part2

data = inspect.cleandoc(
    """
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """
)


def test_part1() -> None:
    assert part1(data) == 24000


def test_part2() -> None:
    assert part2(data) == 45000
