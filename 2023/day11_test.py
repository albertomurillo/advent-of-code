import inspect

from day11 import part1, part2

data = inspect.cleandoc(
    """
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....
    """
).splitlines()


def test_part1():
    assert part1(data) == 374


def test_part2():
    assert part2(data) == 82000210
