import inspect

import pytest

from aoc._2023.day23 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    #.#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#...#
    #####################.#
    """
)


class TestFast:
    def test_part1(self) -> None:
        assert part1(data) == 94

    def test_part2(self) -> None:
        assert part2(data) == 154


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2023, 23)) == 2086

    def test_part2(self) -> None:
        assert part2(read_input(2023, 23)) == 6526
