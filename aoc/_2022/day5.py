import sys
from typing import List

from aoc import as_parts


class CrateMover9000:
    def parse_drawing(self, drawing: List[str]):
        self.stacks = [[] for _ in drawing[-1].split()]
        columns = list(range(1, len(self.stacks) * 4, 4))

        for i in reversed(range(len(drawing) - 1)):
            line = drawing[i]
            for column in (c for c in columns if c < len(line)):
                if "A" <= line[column] <= "Z":
                    self.stacks[columns.index(column)].append(line[column])

    def apply_procedure(self, procedure: List[str]):
        for step in procedure:
            amount, source, dest = map(int, step.split()[1::2])
            for _ in range(amount):
                self.stacks[dest - 1].append(self.stacks[source - 1].pop())

    def top_crates(self) -> List[str]:
        return [stack[-1] for stack in self.stacks]


class CrateMover9001(CrateMover9000):
    def apply_procedure(self, procedure: List[str]):
        for step in procedure:
            amount, source, dest = map(int, step.split()[1::2])
            self.stacks[dest - 1].extend(self.stacks[source - 1][-amount:])
            self.stacks[source - 1] = self.stacks[source - 1][:-amount]


def part1(data: str) -> str:
    drawing, procedure = as_parts(data)
    crane = CrateMover9000()
    crane.parse_drawing(drawing.splitlines())
    crane.apply_procedure(procedure.splitlines())
    return "".join(crane.top_crates())


def part2(data: str) -> str:
    drawing, procedure = as_parts(data)
    crane = CrateMover9001()
    crane.parse_drawing(drawing.splitlines())
    crane.apply_procedure(procedure.splitlines())
    return "".join(crane.top_crates())


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
