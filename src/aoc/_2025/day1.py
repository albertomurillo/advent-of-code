def get_rotations(data: str) -> list[int]:
    result = []
    for line in data.strip().split("\n"):
        direction = line[0]
        amount = int(line[1:])
        if direction == "L":
            result.append(-amount)
        else:
            result.append(amount)
    return result


def part1(data: str) -> int:
    dial = 50
    count = 0
    rotations = get_rotations(data)
    for rotation in rotations:
        dial = (dial + rotation) % 100
        count += dial == 0
    return count


def part2(data: str) -> int:
    dial = 50
    count = 0
    rotations = get_rotations(data)
    for rotation in rotations:
        # count full rotations first
        full, partial = divmod(abs(rotation), 100)
        count += full

        # calculate next dial position with the partial rotation
        next_dial = dial + (partial if rotation > 0 else -partial)

        # if we start at 0, we can't cross zero with a partial rotation
        if dial == 0:
            dial = next_dial % 100
            continue

        # check if we cross zero with the partial rotation
        if (rotation < 0 and next_dial <= 0) or (rotation > 0 and next_dial >= 100):
            count += 1

        dial = next_dial % 100

    return count
