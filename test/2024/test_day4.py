import inspect

from aoc._2024.day4 import part1, part2

data = inspect.cleandoc(
    """
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
    """
)


def test_part1() -> None:
    assert part1(data) == 18


def test_part2() -> None:
    assert part2(data) == 9
