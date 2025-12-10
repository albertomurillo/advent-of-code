def joltage_k(bank: str, k: int) -> int:
    stack = []
    n = len(bank)
    removals = n - k
    for battery in bank:
        while stack and removals and stack[-1] < battery:
            stack.pop()
            removals -= 1
        stack.append(battery)
    if removals:
        stack = stack[:-removals]
    return int("".join(stack[:k]))


def part1(data: str) -> int:
    banks = data.splitlines()
    return sum(joltage_k(bank, 2) for bank in banks)


def part2(data: str) -> int:
    banks = data.splitlines()
    return sum(joltage_k(bank, 12) for bank in banks)
