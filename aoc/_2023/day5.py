from __future__ import annotations

import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Optional

from aoc import as_parts
from aoc.ranges import Range


@dataclass
class AlmanacMap:
    source: Range
    dest: Range

    def to_dest(self, source: int) -> Optional[int]:
        if source not in self.source:
            return None
        return self.dest.start + self.source.offset(source)

    def to_dest_range(self, source: Range) -> Optional[Range]:
        return Range(
            self.dest.start + self.source.offset(source.start),
            self.dest.start + self.source.offset(source.stop),
        )


class Almanac:
    def __init__(self, maps: List[str]):
        self.maps = defaultdict(list)
        for map_ in maps:
            header, *lines = map_.splitlines()
            name = header.split()[0]
            for line in lines:
                dest, src, size = (int(x) for x in line.split())
                self.maps[name].append(
                    AlmanacMap(
                        source=Range(src, src + size),
                        dest=Range(dest, dest + size),
                    )
                )

    def seed_to_location(self, seed: int) -> int:
        source = seed
        for maps in self.maps.values():
            source = self.lookup(maps, source)
        return source

    def seeds_to_locations(self, seeds: Range) -> List[Range]:
        unprocessed = [seeds]
        for maps in self.maps.values():
            matched = []
            for map_ in maps:
                unmatched = []
                while unprocessed:
                    source_range = unprocessed.pop()
                    before, intersection, after = source_range.intersection(map_.source)
                    if before:
                        unmatched.append(before)
                    if intersection:
                        matched.append(map_.to_dest_range(intersection))
                    if after:
                        unmatched.append(after)
                unprocessed = unmatched
            unprocessed = matched + unmatched
        return unprocessed

    def lookup(self, maps: List[AlmanacMap], source: int) -> int:
        for map_ in maps:
            dest = map_.to_dest(source)
            if dest is not None:
                return dest
        return source


def part1(data: str) -> int:
    seed_data, *map_data = as_parts(data)
    seeds = [int(x) for x in seed_data.split()[1:]]
    almanac = Almanac(map_data)
    return min(almanac.seed_to_location(seed) for seed in seeds)


def part2(data: str) -> int:
    seed_data, *map_data = as_parts(data)
    almanac = Almanac(map_data)

    seed_ranges: List[Range] = []
    range_data = [int(x) for x in seed_data.split()[1:]]
    for i in range(0, len(range_data), 2):
        start = range_data[i]
        size = range_data[i + 1]
        seed_ranges.append(Range(start, start + size))

    location_ranges: List[Range] = []
    for seed_range in seed_ranges:
        location_ranges.extend(almanac.seeds_to_locations(seed_range))

    return min(location_ranges).start


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
