import math
import re
import sys


def part1(data: str) -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    instructions = pattern.findall(data)
    return sum(math.prod(map(int, operands)) for operands in instructions)


def part2(data: str) -> int:
    pattern = re.compile(r"(mul|do|don't)\((\d+)?,?(\d+)?\)")
    instructions = pattern.findall(data)
    res = 0
    enabled = True
    for instruction, *operands in instructions:
        match instruction:
            case "do":
                enabled = True
            case "don't":
                enabled = False
            case _:
                res += enabled * math.prod(map(int, (op for op in operands if op)))
    return res


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
