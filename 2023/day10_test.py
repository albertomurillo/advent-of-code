import inspect

from day10 import part1


def test_part1():
    data = inspect.cleandoc(
        """
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        """
    ).splitlines()
    assert part1(data) == 8
