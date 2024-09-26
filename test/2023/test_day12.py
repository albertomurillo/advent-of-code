import inspect

from aoc._2023.day12 import part1, part2

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


def test_part1() -> None:
    assert part1(data) == 21


def test_part2() -> None:
    assert part2(data) == 525152
