import operator
import re
import sys
from collections.abc import Callable

Operator = Callable[[int, int], int]


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def can_solve(target: int, nums: list[int], operators: list[Operator]) -> bool:
    def backtrack(acc: int, nums: list[int]) -> bool:
        if not nums:
            return acc == target
        if acc > target:
            return False
        return any(backtrack(op(acc, nums[0]), nums[1:]) for op in operators)

    return backtrack(0, nums)


def parse_input(data: str) -> list[tuple[int, list[int]]]:
    pattern = re.compile(r"\d+")
    equations = (map(int, pattern.findall(line)) for line in data.splitlines())
    return ((k, v) for k, *v in (equations))


def part1(data: str) -> int:
    equations = parse_input(data)
    opeators = [operator.mul, operator.add]
    return sum(val for val, nums in equations if can_solve(val, nums, opeators))


def part2(data: str) -> int:
    equations = parse_input(data)
    opeators = [concat, operator.mul, operator.add]
    return sum(val for val, nums in equations if can_solve(val, nums, opeators))


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
