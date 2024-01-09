from collections import OrderedDict


def hash_(s: str) -> int:
    total = 0
    for c in s:
        _, total = divmod(((total + ord(c)) * 17), 256)
    return total


def part1(data: str):
    return sum(hash_(step) for step in data.split(","))


def part2(data: str):
    boxes = [OrderedDict() for _ in range(256)]

    for step in data.split(","):
        if step.endswith("-"):
            box, _ = step.split("-")
            if box in boxes[hash_(box)]:
                del boxes[hash_(box)][box]

        if "=" in step:
            box, value = step.split("=")
            boxes[hash_(box)][box] = value

    total = 0
    for i, box in enumerate(boxes, start=1):
        for j, (_, val) in enumerate(box.items(), start=1):
            total += i * j * int(val)

    return total


def main():
    with open("day15.txt", encoding="utf-8") as f:
        data = f.read().strip()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
