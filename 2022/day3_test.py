import inspect

from day3 import part1, part2

data = inspect.cleandoc(
    """
    vJrwpWtwJgWrhcsFMMfFFhFp
    jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
    PmmdzqPrVvPwwTWBwg
    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
    ttgJtRGJQctTZtZT
    CrZsJsPPZsGzwwsLwLmpwMDw
    """
).splitlines()


def test_part1():
    assert part1(data) == 157


def test_part2():
    assert part2(data) == 70
