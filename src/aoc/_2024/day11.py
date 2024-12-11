import sys
from collections import deque
from functools import cache


@cache
def transform(stone: int) -> list[int]:
    s = str(stone)
    if s == "0":
        return [1]

    idx, mod = divmod(len(s), 2)
    if mod == 0:
        return [int(s[0:idx]), int(s[idx:])]

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
