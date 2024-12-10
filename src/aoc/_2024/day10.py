import sys
from functools import cached_property

from aoc import as_graph, as_grid
from aoc.grids import Grid, GridPoint


class HikingMap(Grid):
    def __init__(self, data: str) -> None:
        super().__init__(as_grid(data))
        self.graph = as_graph(self, self._is_uphill)

    def _is_uphill(self, a: GridPoint, b: GridPoint) -> bool:
        return int(self[b]) - int(self[a]) == 1

    @cached_property
    def trailheads(self) -> tuple[GridPoint]:
        return (k for k, v in self.items() if v == "0")

    def peaks(self, trailhead: GridPoint) -> list[GridPoint]:
        return [e for e in self.graph.bfs(trailhead) if self[e] == "9"]  # type: ignore

    def score(self, trailhead: GridPoint) -> int:
        return len(set(self.peaks(trailhead)))

    def rating(self, trailhead: GridPoint) -> int:
        return len(self.peaks(trailhead))


def part1(data: str) -> int:
    hiking_map = HikingMap(data)
    return sum(hiking_map.score(trailhead) for trailhead in hiking_map.trailheads)


def part2(data: str) -> int:
    hiking_map = HikingMap(data)
    return sum(hiking_map.rating(trailhead) for trailhead in hiking_map.trailheads)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
