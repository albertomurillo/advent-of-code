import inspect

from aoc._2022.day8 import part1, part2

data = inspect.cleandoc(
    """
    30373
    25512
    65332
    33549
    35390
    """
)


def test_part1() -> None:
    got = part1(data)
    assert got == 21


def test_part2() -> None:
    got = part2(data)
    assert got == 8
