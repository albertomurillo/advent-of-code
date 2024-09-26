import math
import re
import sys
from itertools import cycle


class Map:
    def __init__(self, data: list[str]) -> None:
        self.directions = data[0]

        self.nodes: dict[str, dict[str, str]] = {}
        pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
        for element in data[2:]:
            match = pattern.match(element)
            assert match, "Invalid data"
            node, left, right = match.groups()
            self.nodes[node] = {"L": left, "R": right}

    def steps_to_destination_suffix(self, start_node: str, end_node_suffix: str) -> int:
        node = start_node
        for steps, direction in enumerate(cycle(self.directions)):
            if node.endswith(end_node_suffix):
                return steps
            node = self.nodes[node][direction]
        raise RuntimeError


def part1(data: str) -> int:
    map_ = Map(data.splitlines())
    return map_.steps_to_destination_suffix("AAA", "ZZZ")


def part2(data: str) -> int:
    # Examining the input data we can find that:
    # 1) For each A node, there is only one path to only one Z node
    # 2) After a Z node is reached at x steps:
    #    The cycle repeats reaching the same Z node at 2x steps
    #
    # The least common multiple is the point where all cycles meet
    # https://en.wikipedia.org/wiki/Least_common_multiple

    map_ = Map(data.splitlines())
    nodes = (node for node in map_.nodes if node.endswith("A"))
    steps = [map_.steps_to_destination_suffix(node, "Z") for node in nodes]
    return math.lcm(*steps)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
