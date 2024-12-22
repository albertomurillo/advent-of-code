import math
import sys
from collections import deque
from functools import cache


@cache
def transform(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_len = int(math.log10(stone)) + 1
    if stone_len % 2 == 0:
        p = 10 ** (stone_len / 2)
        return list(map(int, divmod(stone, p)))

    return [stone * 2024]


def part1(data: str, blinks: int) -> int:
    def blink(stones: deque) -> deque:
        q = deque()
        while stones:
            stone = stones.popleft()
            q.extend(transform(stone))
        return q

    stones = deque(map(int, data.split()))
    for _ in range(blinks):
        stones = blink(stones)
    return len(stones)


def part2(data: str, blinks: int) -> int:
    @cache
    def dfs(stone: int, blinks: int) -> int:
        if blinks == 0:
            return 1
        return sum(dfs(stone, blinks - 1) for stone in transform(stone))

    stones = map(int, data.split())
    return sum(dfs(stone, blinks) for stone in stones)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data,25)}")
    print(f"part 2: {part2(data,75)}")


if __name__ == "__main__":
    main()
