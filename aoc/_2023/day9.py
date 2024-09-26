import sys
from itertools import pairwise


class History:
    def __init__(self, values: list[int]):
        self._seqs = [values]
        seq = self._seqs[0]
        while not all(x == 0 for x in seq):
            seq = [b - a for a, b in pairwise(seq)]
            self._seqs.append(seq)

    def extrapolate(self):
        self._seqs[-1].append(0)
        for i in reversed(range(0, len(self._seqs) - 1)):
            self._seqs[i].append(self._seqs[i][-1] + self._seqs[i + 1][-1])

    def __getitem__(self, index: int) -> int:
        return self._seqs[0][index]


def part1(data: str) -> int:
    _data = data.splitlines()
    histories = [History([int(x) for x in line.split()]) for line in _data]
    for history in histories:
        history.extrapolate()
    return sum(history[-1] for history in histories)


def part2(data: str) -> int:
    _data = data.splitlines()
    histories = [History([int(x) for x in line.split()[::-1]]) for line in _data]
    for history in histories:
        history.extrapolate()
    return sum(history[-1] for history in histories)


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
