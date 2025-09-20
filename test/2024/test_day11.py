import pytest

from aoc._2024.day11 import part1, part2
from test import read_input

data = "125 17"


class TestFast:
    def test_part1(self) -> None:
        assert part1(data, 6) == 22
        assert part1(data, 25) == 55312

    def test_part2(self) -> None:
        assert part2(data, 6) == 22
        assert part2(data, 25) == 55312
        assert part2(data, 75) == 65601038650482


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 11), 6) == 76

    def test_part2(self) -> None:
        assert part2(read_input(2024, 11), 6) == 76
