def invalid_ids(start: int, end: int, repetitions: int) -> set[int]:
    ids = set()
    start_str = str(start)
    end_str = str(end)
    num = (
        start_str[: len(start_str) // repetitions]
        or end_str[: len(end_str) // repetitions]
    )
    while True:
        invalid_id = int(num * repetitions)
        if invalid_id > end:
            break
        if invalid_id >= start:
            ids.add(invalid_id)
        num = str(int(num) + 1)
    return ids


def get_ranges(data: str) -> list[tuple[int, int]]:
    ranges = data.strip().split(",")
    ranges = [r.split("-") for r in ranges]
    return [(int(r[0]), int(r[1])) for r in ranges]


def part1(data: str) -> int:
    s = set()
    for start, end in get_ranges(data):
        s |= invalid_ids(start, end, 2)
    return sum(s)


def part2(data: str) -> int:
    s = set()
    for start, end in get_ranges(data):
        for rep in range(2, len(str(end)) + 1):
            s |= invalid_ids(start, end, rep)
    return sum(s)
