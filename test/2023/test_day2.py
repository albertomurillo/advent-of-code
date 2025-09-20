import inspect

import pytest

from aoc._2023.day2 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 8

    def test_part2(self) -> None:
        assert part2(data) == 2286


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 2)) == 2061

    def test_part2(self) -> None:
        assert part2(read_input(2023, 2)) == 72596
