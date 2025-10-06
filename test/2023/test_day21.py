import inspect

import pytest

from aoc._2023.day21 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    ...........
    .....###.#.
    .###.##..#.
    ..#.#...#..
    ....#.#....
    .##..S####.
    .##..#...#.
    .......##..
    .##.#.####.
    .##..##.##.
    ...........
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data, 6) == 16

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        ("steps", "plots"),
        [
            (6, 16),
            (10, 50),
            (50, 1594),
            (100, 6536),
            (500, 167004),
            (1000, 668697),
            (5000, 16733044),
        ],
    )
    def test_part2(self, steps: int, plots: int) -> None:
        assert part2(data, steps) == plots


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 21), 64) == 3578

    def test_part2(self) -> None:
        assert part2(read_input(2023, 21), 26501365) == 594115391548176
