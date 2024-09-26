import inspect

from aoc._2022.day5 import part1, part2

data = inspect.cleandoc(
    """
        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    """
)


def test_part1() -> None:
    assert part1(data) == "CMZ"


def test_part2() -> None:
    assert part2(data) == "MCD"
