from collections import deque
from itertools import pairwise
from typing import List


class History:
    def __init__(self, values: List[int]):
        self._seqs = [deque(values)]
        seq = self._seqs[0]
        while not all(x == 0 for x in seq):
            seq = deque(b - a for a, b in pairwise(seq))
            self._seqs.append(seq)

    def extrapolate(self):
        self._seqs[-1].append(0)
        for i in reversed(range(0, len(self._seqs) - 1)):
            self._seqs[i].append(self._seqs[i][-1] + self._seqs[i + 1][-1])

    def extrapolateleft(self):
        self._seqs[-1].appendleft(0)
        for i in reversed(range(0, len(self._seqs) - 1)):
            self._seqs[i].appendleft(self._seqs[i][0] - self._seqs[i + 1][0])

    def __getitem__(self, index: int) -> int:
        return self._seqs[0][index]


def part1(data: List[str]) -> int:
    histories = [History([int(x) for x in line.split()]) for line in data]
    for history in histories:
        history.extrapolate()
    return sum(history[-1] for history in histories)


def part2(data: List[str]) -> int:
    histories = [History([int(x) for x in line.split()]) for line in data]
    for history in histories:
        history.extrapolateleft()
    return sum(history[0] for history in histories)


def main():
    data = []
    with open("day9.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
