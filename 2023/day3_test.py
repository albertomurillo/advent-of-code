import inspect

from day3 import part1, part2

data = inspect.cleandoc(
    """
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    """
).splitlines()


def test_part1():
    assert part1(data) == 4361


def test_part2():
    assert part2(data) == 467835
