import inspect

from aoc._2024.day10 import part1, part2

data = inspect.cleandoc(
    """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """
)


def test_part1() -> None:
    assert part1(data) == 36


def test_part2() -> None:
    assert part2(data) == 81
