import inspect

from aoc._2022.day3 import part1, part2

data = inspect.cleandoc(
    """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
)


def test_part1() -> None:
    assert part1(data) == 157


def test_part2() -> None:
    assert part2(data) == 70
