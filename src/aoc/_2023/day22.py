from __future__ import annotations

import sys
from collections import deque
from contextlib import contextmanager
from dataclasses import dataclass

SPACE: dict[Cube, Brick] = {}


@contextmanager
def forked_space():  # noqa: ANN202
    global SPACE  # noqa: PLW0603
    space = SPACE.copy()
    try:
        yield
    finally:
        SPACE = space


@dataclass(unsafe_hash=True)
class Cube:
    x: int
    y: int
    z: int

    @property
    def is_on_ground(self) -> bool:
        return self.z == 1

    @property
    def above(self) -> Cube:
        return Cube(self.x, self.y, self.z + 1)

    @property
    def below(self) -> Cube:
        return Cube(self.x, self.y, self.z - 1)


@dataclass(unsafe_hash=True)
class Brick:
    p1: Cube
    p2: Cube

    @property
    def lowest_z(self) -> int:
        return min(self.p1.z, self.p2.z)

    @property
    def cubes(self) -> list[Cube]:
        if self.p1.x != self.p2.x:
            a, b = sorted((self.p1.x, self.p2.x))
            return [Cube(n, self.p1.y, self.p1.z) for n in range(a, b + 1)]
        if self.p1.y != self.p2.y:
            a, b = sorted((self.p1.y, self.p2.y))
            return [Cube(self.p1.x, n, self.p1.z) for n in range(a, b + 1)]
        if self.p1.z != self.p2.z:
            a, b = sorted((self.p1.z, self.p2.z))
            return [Cube(self.p1.x, self.p1.y, n) for n in range(a, b + 1)]
        if self.p1 == self.p2:
            return [self.p1]
        raise ValueError(self.p1, self.p2)

    @property
    def bottom_cubes(self) -> list[Cube]:
        return [cube for cube in self.cubes if cube.z == self.lowest_z]

    @property
    def bricks_above(self) -> list[Brick]:
        return list({SPACE[cube.above] for cube in self.cubes if cube.above in SPACE})

    @property
    def can_fall(self) -> bool:
        for cube in self.bottom_cubes:
            if cube.is_on_ground:
                return False
            if cube.below in SPACE:
                return False
        return True

    def fall(self) -> None:
        while self.can_fall:
            self.p1.z -= 1
            self.p2.z -= 1
        self.materialize()

    def materialize(self) -> None:
        for cube in self.cubes:
            SPACE[cube] = self

    def disintegrate(self) -> None:
        for cube in self.cubes:
            del SPACE[cube]

    @property
    def supported_bricks(self) -> list[Brick]:
        self.disintegrate()
        bricks = [brick for brick in self.bricks_above if brick.can_fall]
        self.materialize()
        return bricks

    @property
    def falling_bricks(self) -> int:
        return len(self.supported_bricks)

    @property
    @forked_space()
    def falling_bricks_chain_reaction(self) -> int:
        q: deque[Brick] = deque()
        q.append(self)
        count = -1
        while q:
            count += 1
            brick = q.popleft()
            q.extend(brick.supported_bricks)
            brick.disintegrate()

        return count

    def __lt__(self, other: Brick) -> bool:
        return self.lowest_z < other.lowest_z


def parse_bricks(data: str) -> list[Brick]:
    bricks: list[Brick] = []
    for line in data.splitlines():
        end1, end2 = line.split("~")
        x1, y1, z1 = map(int, end1.split(","))
        x2, y2, z2 = map(int, end2.split(","))
        bricks.append(Brick(Cube(x1, y1, z1), Cube(x2, y2, z2)))
    return sorted(bricks)


@forked_space()
def part1(data: str) -> int:
    bricks = parse_bricks(data)
    for brick in bricks:
        brick.fall()
    return sum(not brick.falling_bricks for brick in bricks)


@forked_space()
def part2(data: str) -> int:
    bricks = parse_bricks(data)
    for brick in bricks:
        brick.fall()
    return sum(brick.falling_bricks_chain_reaction for brick in bricks)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
