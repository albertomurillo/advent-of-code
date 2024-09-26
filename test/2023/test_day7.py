import inspect

from aoc._2023.day7 import part1, part2

data = inspect.cleandoc(
    """
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483
    """
)


def test_part1() -> None:
    assert part1(data) == 6440


def test_part2() -> None:
    assert part2(data) == 5905
