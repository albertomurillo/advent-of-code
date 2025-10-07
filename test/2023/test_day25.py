import inspect

import pytest

from aoc._2023.day25 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    jqt: rhn xhk nvd
    rsh: frs pzl lsr
    xhk: hfx
    cmg: qnr nvd lhk bvb
    rhn: xhk bvb hfx
    bvb: xhk hfx
    pzl: lsr hfx nvd
    qnr: nvd
    ntq: jqt hfx bvb xhk
    nvd: lhk
    lsr: lhk
    rzs: qnr cmg lsr rsh
    frs: qnr lhk lsr
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 54

    def test_part2(self) -> None:
        assert part2(data) == 0


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 25)) == 552682

    # def test_part2(self) -> None:
    #     assert part2(read_input(2023, 25)) == 0
