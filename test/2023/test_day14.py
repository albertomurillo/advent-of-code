import inspect

from aoc._2023.day14 import part1, part2

data = inspect.cleandoc(
    """
    O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#....
    """
)


def test_part1():
    assert part1(data) == 136


def test_part2():
    assert part2(data) == 64
