from day15 import part1, part2

DATA = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_part1():
    assert part1(DATA) == 1320


def test_part2():
    assert part2(DATA) == 145
