import pytest

from aoc._2023.day15 import part1, part2
from test import read_input

DATA = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


class TestFast:
    def test_part1(self) -> None:
        assert part1(DATA) == 1320

    def test_part2(self) -> None:
        assert part2(DATA) == 145


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 15)) == 517551

    def test_part2(self) -> None:
        assert part2(read_input(2023, 15)) == 286097
