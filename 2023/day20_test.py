import inspect

from day20 import part1

data = inspect.cleandoc(
    """
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
).splitlines()


def test_part1():
    assert part1(data) == 32000000
