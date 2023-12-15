from collections import defaultdict
from itertools import repeat
from typing import Dict, List, Tuple


class SpringConditions:
    def __init__(self, data: List[str], folded_in_parts: int = 1):
        self.records: List[Tuple[List[str], List[int]]] = []
        for line in data:
            s, g = line.split()
            springs = list("?".join(repeat(s, folded_in_parts)))
            groups = [int(x) for x in ",".join(repeat(g, folded_in_parts)).split(",")]
            self.records.append((springs, groups))

    def matches(self, springs: List[str], groups: List[int]) -> int:
        # First I solved it with backtracking and failed to solve p2
        # with memoization.
        #
        # Decided to study the fast regular expression approach from this post
        # https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd3rclt
        # https://swtch.com/~rsc/regexp/regexp1.html
        # https://research.swtch.com/glob
        matches = 0

        cstates: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
        nstates: Dict[Tuple[int, int, int, int], int] = defaultdict(int)
        cstates[(0, 0, 0, 0)] = 1

        while len(cstates) > 0:
            for state, num in cstates.items():
                # si = springs index
                # gi = groups index
                # cc = current count
                # expdot = expecting a dot
                si, gi, cc, expdot = state

                if si == len(springs) and gi == len(groups):
                    matches += num

                if si == len(springs):
                    continue

                if (springs[si] in "#?") and gi < len(groups) and expdot == 0:
                    if springs[si] == "?" and cc == 0:
                        nstates[(si + 1, gi, cc, expdot)] += num
                    cc += 1
                    if cc == groups[gi]:
                        gi += 1
                        cc = 0
                        expdot = 1
                    nstates[(si + 1, gi, cc, expdot)] += num
                    continue

                if (springs[si] in ".?") and cc == 0:
                    expdot = 0
                    nstates[(si + 1, gi, cc, expdot)] += num

            cstates, nstates = nstates, cstates
            nstates.clear()

        return matches


def part1(data: List[str]):
    scr = SpringConditions(data)
    return sum(scr.matches(springs, groups) for springs, groups in scr.records)


def part2(data: List[str]) -> int:
    scr = SpringConditions(data, 5)
    return sum(scr.matches(springs, groups) for springs, groups in scr.records)


def main():
    with open("day12.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
