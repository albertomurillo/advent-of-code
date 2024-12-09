import sys
from collections import deque
from dataclasses import dataclass
from itertools import count

from more_itertools import grouper


@dataclass
class File:
    id: int
    size: int
    idx: int


@dataclass
class Hole:
    idx: int
    size: int


class Disk(list):
    def checksum(self) -> int:
        return sum(idx * id_ for idx, id_ in enumerate(self) if id_ != -1)

    def compact(self) -> None:
        left, right = 0, len(self) - 1
        while True:
            while left < right and self[left] != -1:
                left += 1
            while left < right and self[right] == -1:
                right -= 1
            if left >= right:
                break
            self[left], self[right] = self[right], self[left]

    def defrag(self) -> None:
        files, holes = self.scan()

        tmp = deque()
        while files and holes:
            while files and holes:
                file = files.pop()
                hole = holes.popleft()

                if hole.idx > file.idx:
                    files.append(file)
                    continue

                if hole.size >= file.size:
                    self.swap(hole.idx, file.idx, file.size)
                    hole.idx += file.size
                    hole.size -= file.size
                    if hole.size > 0:
                        holes.appendleft(hole)
                    holes, tmp = tmp + holes, deque()
                    continue

                tmp.append(hole)
                if holes:
                    files.append(file)

            holes, tmp = tmp, deque()

    def scan(self) -> tuple[deque[File], deque[Hole]]:
        files: deque[File] = deque()
        holes: deque[Hole] = deque()

        idx = id_ = size = 0
        c_id = -2
        for idx, id_ in enumerate(self):
            if c_id == id_:
                size += 1
                continue

            if c_id == -2:
                pass
            elif c_id == -1:
                holes.append(Hole(idx - size, size))
            else:
                files.append(File(c_id, size, idx - size))
            c_id = id_
            size = 1

        if c_id != -1:
            files.append(File(c_id, size, idx - size + 1))

        return files, holes

    def swap(self, idx1: int, idx2: int, size: int) -> None:
        self[idx1 : idx1 + size], self[idx2 : idx2 + size] = (
            self[idx2 : idx2 + size],
            self[idx1 : idx1 + size],
        )


def parse_input(data: str) -> Disk:
    disk = Disk()
    file_id = count()
    for file_size, hole_size in grouper(
        map(int, data.strip()), 2, incomplete="fill", fillvalue=0
    ):
        id_ = next(file_id)
        disk.extend(id_ for _ in range(file_size))
        disk.extend(-1 for _ in range(hole_size))
    return disk


def part1(data: str) -> int:
    disk = parse_input(data)
    disk.compact()
    return disk.checksum()


def part2(data: str) -> int:
    disk = parse_input(data)
    disk.defrag()
    return disk.checksum()


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
