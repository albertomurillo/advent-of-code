import inspect

from aoc._2023.day21 import part1

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
)


def test_part1() -> None:
    assert part1(data, 6) == 16
