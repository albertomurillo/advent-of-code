from typing import List


class CrateMover9000:
    def __init__(self, data: str):
        self.parse_drawing(data)
        self.parse_procedure(data)

    def parse_drawing(self, data: str):
        drawing = data.split("\n\n")[0].splitlines()
        self.stacks = [[] for _ in drawing[-1].split()]
        columns = list(range(1, len(self.stacks) * 4, 4))

        for i in reversed(range(len(drawing) - 1)):
            line = drawing[i]
            for column in (c for c in columns if c < len(line)):
                if "A" <= line[column] <= "Z":
                    self.stacks[columns.index(column)].append(line[column])

    def parse_procedure(self, data: str):
        self.moves = []
        moves = data.split("\n\n")[1].splitlines()
        for move in moves:
            _, amount, _, source, _, dest = move.split()
            self.moves.append((int(amount), int(source), int(dest)))

    def apply_procedure(self):
        for amount, source, dest in self.moves:
            for _ in range(amount):
                self.stacks[dest - 1].append(self.stacks[source - 1].pop())

    def top_crates(self) -> List[str]:
        return [stack[-1] for stack in self.stacks]


class CrateMover9001(CrateMover9000):
    def apply_procedure(self):
        for amount, source, dest in self.moves:
            self.stacks[dest - 1].extend(self.stacks[source - 1][-amount:])
            self.stacks[source - 1] = self.stacks[source - 1][:-amount]


def part1(data: str) -> str:
    crane = CrateMover9000(data)
    crane.apply_procedure()
    return "".join(crane.top_crates())


def part2(data: str) -> str:
    crane = CrateMover9001(data)
    crane.apply_procedure()
    return "".join(crane.top_crates())


def main():
    with open("day5.txt", encoding="utf-8") as f:
        data = f.read()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
