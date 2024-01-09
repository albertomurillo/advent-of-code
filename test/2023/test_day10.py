import inspect

import pytest

from aoc._2023.day10 import PipeMaze, part1, part2_raycasting, part2_shoelace


@pytest.fixture(name="maze_1")
def fixture_maze_1():
    return inspect.cleandoc(
        """
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        """
    ).splitlines()


@pytest.fixture(name="maze_2")
def fixture_maze_2():
    return inspect.cleandoc(
        """
        FF7FSF7F7F7F7F7F---7
        L|LJ||||||||||||F--J
        FL-7LJLJ||||||LJL-77
        F--JF--7||LJLJ7F7FJ-
        L---JF-JLJ.||-FJLJJ7
        |F|F-JF---7F7-L7L|7|
        |FFJF7L7F-JF7|JL---7
        7-L-JL7||F7|L7F-7F7|
        L.L7LFJ|||||FJL7||LJ
        L7JLJL-JLJLJL--JLJ.L
        """
    ).splitlines()


def test_part1(maze_1):
    maze = PipeMaze([list(line) for line in maze_1])
    assert part1(maze) == 8


def test_part2(maze_2):
    maze = PipeMaze([list(line) for line in maze_2])
    assert part2_raycasting(maze) == 10


def test_part2_shoelace(maze_2):
    maze = PipeMaze([list(line) for line in maze_2])
    assert part2_shoelace(maze) == 10
