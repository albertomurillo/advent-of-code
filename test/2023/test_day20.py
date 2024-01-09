import inspect

from aoc._2023.day20 import part1

data = inspect.cleandoc(
    """
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
)


def test_part1():
    assert part1(data) == 32000000
