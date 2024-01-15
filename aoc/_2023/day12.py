import sys
from collections import defaultdict
from itertools import repeat
from typing import Dict, List, Tuple


class SpringConditions:
    def __init__(self, data: List[str], folded_in_parts: int = 1):
        self.records: List[Tuple[str, List[int]]] = []
        for line in data:
            s, g = line.split()
            springs = "?".join(repeat(s, folded_in_parts))
            groups = [int(x) for x in ",".join(repeat(g, folded_in_parts)).split(",")]
            self.records.append((springs, groups))

    def matches(self, springs: str, groups: List[int]) -> int:
        # Based on https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd3rclt

        nstates: Dict[Tuple[int, int, bool], int] = defaultdict(int)
        cstates: Dict[Tuple[int, int, bool], int] = defaultdict(int)
        cstates[(0, 0, False)] = 1

        len_groups = len(groups)

        for spring in springs:
            for (gi, cc, want_dot), seen in cstates.items():
                if spring in ".?" and cc == 0:
                    nstates[(gi, 0, False)] += seen

                if spring in "#?" and gi < len_groups and not want_dot:
                    cc += 1
                    if cc == groups[gi]:
                        nstates[(gi + 1, 0, True)] += seen
                    else:
                        nstates[(gi, cc, False)] += seen

            cstates, nstates = nstates, cstates
            nstates.clear()

        return sum(v for (gi, _, _), v in cstates.items() if gi == len_groups)


def part1(data: str):
    scr = SpringConditions(data.splitlines())
    return sum(scr.matches(springs, groups) for springs, groups in scr.records)


def part2(data: str) -> int:
    scr = SpringConditions(data.splitlines(), 5)
    return sum(scr.matches(springs, groups) for springs, groups in scr.records)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
