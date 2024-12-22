import inspect

from aoc._2024.day8 import part1, part2

data = inspect.cleandoc(
    """
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
)


def test_part1() -> None:
    assert part1(data) == 14


def test_part2() -> None:
    assert part2(data) == 34