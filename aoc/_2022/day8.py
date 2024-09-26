import math
import sys

from aoc import as_matrix
from aoc.grids import Direction, E, Grid, GridPoint, N, S, W


class Forest(Grid):
    def scenic_score(self, tree: GridPoint) -> int:
        return math.prod(self.viewing_distance(tree, d) for d in (N, S, E, W))

    def viewing_distance(self, tree: GridPoint, direction: Direction) -> int:
        score = 0
        tree_h = int(self[tree])
        next_tree = tree.step(direction)
        while next_tree in self:
            h = int(self[next_tree])
            score += 1
            if h >= tree_h:
                return score
            next_tree = next_tree.step(direction)
        return score

    def visible(self, tree: GridPoint, direction: Direction) -> set[GridPoint]:
        trees = set()
        shortest = -math.inf
        while tree in self:
            h = int(self[tree])
            if h > shortest:
                trees.add(tree)
                shortest = h
            tree = tree.step(direction)
        return trees


def part1(data: str) -> int:
    grid = Forest(Grid(as_matrix(data)))
    trees = set()

    for row in range(grid.m):
        trees |= grid.visible(GridPoint(row, 0), E)
        trees |= grid.visible(GridPoint(row, grid.n - 1), W)

    for col in range(grid.n):
        trees |= grid.visible(GridPoint(0, col), S)
        trees |= grid.visible(GridPoint(grid.m - 1, col), N)

    return len(trees)


def part2(data: str) -> int:
    grid = Forest(Grid(as_matrix(data)))
    return max(grid.scenic_score(tree) for tree, _ in grid.items())


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
