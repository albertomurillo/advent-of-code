from aoc._2024.day11 import part1, part2

data = "125 17"


def test_part1() -> None:
    assert part1(data, 6) == 22
    assert part1(data, 25) == 55312


def test_part2() -> None:
    assert part2(data, 6) == 22
    assert part2(data, 25) == 55312
    assert part2(data, 75) == 65601038650482
