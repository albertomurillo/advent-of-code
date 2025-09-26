import math
import sys

from aoc import as_matrix
from aoc.grids import Direction, E, Grid, GridPoint, N, S, W


class Forest(Grid):
    def scenic_score(self, tree: GridPoint) -> int:
        return math.prod(self.viewing_distance(tree, d) for d in (N, S, E, W))

    def viewing_distance(self, tree: GridPoint, direction: Direction) -> int:
        score = 0
        tree_h = self[tree]
        next_tree = tree.step(direction)
        while next_tree in self:
            h = self[next_tree]
            score += 1
            if h >= tree_h:
                return score
            next_tree = next_tree.step(direction)
        return score

    def visible(
        self, tree: GridPoint, direction: Direction, highest: float = math.inf
    ) -> tuple[set[GridPoint], int]:
        trees = set()
        highest_so_far = -math.inf
        while tree in self:
            h = self[tree]
            if h > highest_so_far:
                trees.add(tree)
                highest_so_far = h
            if h == highest:
                break
            tree = tree.step(direction)
        return trees, highest_so_far


def part1(data: str) -> int:
    grid = Forest(as_matrix(data))
    visible_trees = set()

    for row in range(grid.m):
        trees, highest = grid.visible(GridPoint(row, 0), E)
        visible_trees |= trees

        trees, _ = grid.visible(GridPoint(row, grid.n - 1), W, highest)
        visible_trees |= trees

    for col in range(grid.n):
        trees, highest = grid.visible(GridPoint(0, col), S)
        visible_trees |= trees

        trees, _ = grid.visible(GridPoint(grid.m - 1, col), N, highest)
        visible_trees |= trees

    return len(visible_trees)


def part2(data: str) -> int:
    grid = Forest(as_matrix(data))
    return max(grid.scenic_score(tree) for tree, _ in grid.items())


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
