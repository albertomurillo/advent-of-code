import sys
from functools import partial

from aoc import as_ints, as_lines, as_parts

Rule = tuple[int, int]
Update = list[int]


def is_in_order(update: Update, rules: list[Rule]) -> bool:
    for a, b in rules:
        if not (a in update and b in update):
            continue
        if update.index(a) > update.index(b):
            return False
    return True


def bubble_sort(update: Update, rules: list[Rule]) -> None:
    for n in reversed(range(len(update))):
        i, j = 0, 1
        swapped = False
        while j <= n:
            if not is_in_order(update[i : j + 1], rules):
                update[i], update[j] = update[j], update[i]
                swapped = True
            i, j = j, j + 1
        if swapped is False:
            return


def parse_input(data: str) -> tuple[list[Rule], list[Update]]:
    p1, p2 = as_lines(as_parts(data))
    rules = [as_ints(line.split("|")) for line in p1]
    updates = [as_ints(line.split(",")) for line in p2]
    return rules, updates


def part1(data: str) -> int:
    rules, updates = parse_input(data)
    good_updates = [x for x in updates if is_in_order(x, rules)]
    return sum(x[len(x) // 2] for x in good_updates)


def part2(data: str) -> int:
    rules, updates = parse_input(data)
    bad_updates = [x for x in updates if not is_in_order(x, rules)]
    list(map(partial(bubble_sort, rules=rules), bad_updates))
    return sum(x[len(x) // 2] for x in bad_updates)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
