import inspect

from day21 import part1

data = inspect.cleandoc(
    """
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    """
).splitlines()


def test_part1():
    assert part1(data, 6) == 16
