import pytest

from aoc._2024.day3 import part1, part2
from test import read_input


class TestFast:
    def test_part1(self) -> None:
        data = "xmul(2,4)%&mul[3,7]!@^don't_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        assert part1(data) == 161

    def test_part2(self) -> None:
        data = (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        assert part2(data) == 48


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2024, 3)) == 183788984

    def test_part2(self) -> None:
        assert part2(read_input(2024, 3)) == 62098619
