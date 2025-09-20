import inspect

import pytest

from aoc._2023.day16 import part1, part2
from test import read_input

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
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 46

    def test_part2(self) -> None:
        assert part2(data) == 51


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 16)) == 7728

    def test_part2(self) -> None:
        assert part2(read_input(2023, 16)) == 8061
