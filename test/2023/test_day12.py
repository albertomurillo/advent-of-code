import inspect

import pytest

from aoc._2023.day12 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    ???.### 1,1,3
    .??..??...?##. 1,1,3
    ?#?#?#?#?#?#?#? 1,3,1,6
    ????.#...#... 4,1,1
    ????.######..#####. 1,6,5
    ?###???????? 3,2,1
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 21

    def test_part2(self) -> None:
        assert part2(data) == 525152


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 12)) == 7084

    def test_part2(self) -> None:
        assert part2(read_input(2023, 12)) == 8414003326821
