import inspect

import pytest

from aoc._2022.day7 import part1, part2
from test import read_input

data = inspect.cleandoc(
    """
    $ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k
"""
)


class TestFast:
    def test_part1(self) -> None:
        got = part1(data)
        assert got == 95437

    def test_part2(self) -> None:
        got = part2(data)
        assert got == 24933642


@pytest.mark.slow
class TestSlow:
    def test_part1(self) -> None:
        assert part1(read_input(2022, 7)) == 1770595

    def test_part2(self) -> None:
        assert part2(read_input(2022, 7)) == 2195372
