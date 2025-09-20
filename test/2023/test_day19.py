import inspect

import pytest

from aoc._2023.day19 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    px{a<2006:qkq,m>2090:A,rfg}
    pv{a>1716:R,A}
    lnx{m>1548:A,A}
    rfg{s<537:gd,x>2440:R,A}
    qs{s>3448:A,lnx}
    qkq{x<1416:A,crn}
    crn{x>2662:A,R}
    in{s<1351:px,qqz}
    qqz{s>2770:qs,m<1801:hdj,R}
    gd{a>3333:R,R}
    hdj{m>838:A,pv}

    {x=787,m=2655,a=1222,s=2876}
    {x=1679,m=44,a=2067,s=496}
    {x=2036,m=264,a=79,s=2244}
    {x=2461,m=1339,a=466,s=291}
    {x=2127,m=1623,a=2188,s=1013}
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 19114

    def test_part2(self) -> None:
        assert part2(data) == 167409079868000


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 19)) == 319295

    def test_part2(self) -> None:
        assert part2(read_input(2023, 19)) == 110807725108076
