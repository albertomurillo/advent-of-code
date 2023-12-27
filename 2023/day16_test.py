import inspect

from day16 import part1, part2

data = inspect.cleandoc(
    """
    .|...\\....
    |.-.\\.....
    .....|-...
    ........|.
    ..........
    .........\\
    ..../.\\\\..
    .-.-/..|..
    .|....-|.\\
    ..//.|....
    """
).splitlines()


def test_part1():
    assert part1(data) == 46


def test_part2():
    assert part2(data) == 51
