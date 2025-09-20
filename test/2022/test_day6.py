import pytest

from aoc._2022.day6 import part1, part2
from test import read_input


class TestFast:
    @pytest.mark.parametrize(
        ("data", "want"),
        [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ],
    )
    def test_part1(self, data: str, want: int) -> None:
        got = part1(data)
        assert got == want

    @pytest.mark.parametrize(
        ("data", "want"),
        [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        ],
    )
    def test_part2(self, data: str, want: int) -> None:
        got = part2(data)
        assert got == want


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 6)) == 1093

    def test_part2(self) -> None:
        assert part2(read_input(2022, 6)) == 3534
