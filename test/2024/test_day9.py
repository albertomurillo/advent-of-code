import pytest

from aoc._2024.day9 import part1, part2
from test import read_input

data = "2333133121414131402"


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 1928

    def test_part2(self) -> None:
        assert part2(data) == 2858


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 9)) == 6340197768906

    def test_part2(self) -> None:
        assert part2(read_input(2024, 9)) == 6363913128533
