import re


def part1(data: str) -> int:
    result = 0
    for line in data.splitlines():
        c = next((x for x in line if x.isnumeric()))
        result += int(c) * 10

        c = next((x for x in reversed(line) if x.isnumeric()))
        result += int(c)

    return result


def part2(data: str) -> int:
    values = {
        # Forward values
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        # Backward values
        "eno": 1,
        "owt": 2,
        "eerht": 3,
        "ruof": 4,
        "evif": 5,
        "xis": 6,
        "neves": 7,
        "thgie": 8,
        "enin": 9,
        # Numeric values
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    forward_pattern = "one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"
    backward_pattern = "9|8|7|6|5|4|3|2|1|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno"
    result = 0
    for line in data.splitlines():
        m = re.search(forward_pattern, line)
        result += values[m[0]] * 10

        m = re.search(backward_pattern, line[::-1])
        result += values[m[0]]

    return result


def main():
    with open("day1.txt", encoding="utf-8") as f:
        data = f.read()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
