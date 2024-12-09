from aoc._2024.day9 import part1, part2

data = "2333133121414131402"


def test_part1() -> None:
    assert part1(data) == 1928


def test_part2() -> None:
    assert part2(data) == 2858
