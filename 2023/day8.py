import math
import re
from itertools import cycle
from typing import Dict, List, Set


class Map:
    def __init__(self, data: List[str]):
        self.directions = data[0]

        self.map: Dict[str, Dict[str, str]] = {}
        for element in data[2:]:
            pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
            node, left, right = pattern.match(element).groups()
            self.map[node] = {"L": left, "R": right}

    @property
    def nodes(self) -> Set[str]:
        return self.map.keys()

    def steps_to_destination_suffix(self, start_node: str, end_node_suffix: str) -> int:
        node = start_node
        for steps, direction in enumerate(cycle(self.directions)):
            if node.endswith(end_node_suffix):
                return steps
            node = self.map[node][direction]
        raise RuntimeError


def part1(data: List[str]) -> int:
    map_ = Map(data)
    return map_.steps_to_destination_suffix("AAA", "ZZZ")


def part2(data: List[str]) -> int:
    # Examining the input data we can find that:
    # 1) For each A node, there is only one path to only one Z node
    # 2) After a Z node is reached at x steps:
    #    The cycle repeats reaching the same Z node at 2x steps
    #
    # The least common multiple is the point where all cycles meet
    # https://en.wikipedia.org/wiki/Least_common_multiple

    map_ = Map(data)
    nodes = (node for node in map_.nodes if node.endswith("A"))
    steps = [map_.steps_to_destination_suffix(node, "Z") for node in nodes]
    return math.lcm(*steps)


def main():
    with open("day8.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
