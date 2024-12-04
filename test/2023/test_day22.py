import inspect

from aoc._2023.day22 import part1, part2

data = inspect.cleandoc(
    """
    1,0,1~1,2,1
    0,0,2~2,0,2
    0,2,3~2,2,3
    0,0,4~0,2,4
    2,0,5~2,2,5
    0,1,6~2,1,6
    1,1,8~1,1,9
    """
)


def test_part1() -> None:
    assert part1(data) == 5


def test_part2() -> None:
    assert part2(data) == 7


# 593 too high
