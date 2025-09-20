import inspect

import pytest

from aoc._2023.day20 import part1
from test import read_input

data = inspect.cleandoc(
    """
    broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 32000000


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 20)) == 739960225
