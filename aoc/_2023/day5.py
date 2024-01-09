from __future__ import annotations

from collections import OrderedDict
from dataclasses import dataclass
from typing import List, Optional

from aoc import Range


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
    def __init__(self, data: List[str]):
        self.maps: OrderedDict[str, List[AlmanacMap]] = OrderedDict(
            (
                ("seed-to-soil", []),
                ("soil-to-fertilizer", []),
                ("fertilizer-to-water", []),
                ("water-to-light", []),
                ("light-to-temperature", []),
                ("temperature-to-humidity", []),
                ("humidity-to-location", []),
            )
        )

        map_ = None
        for line in data[1:]:
            if not line:
                map_ = None
                continue

            if map_ is None:
                map_ = self.maps[line.split(" map:")[0]]
                continue

            dest, src, size = (int(x) for x in line.split())
            map_.append(
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
    almanac = Almanac(data.splitlines())
    seeds = [int(x) for x in data.splitlines()[0].split(": ")[1].split()]
    return min(almanac.seed_to_location(seed) for seed in seeds)


def part2(data: str) -> int:
    almanac = Almanac(data.splitlines())

    seed_ranges: List[Range] = []
    range_data = data.splitlines()[0].split(": ")[1].split()
    for i in range(0, len(range_data), 2):
        start = int(range_data[i])
        size = int(range_data[i + 1])
        seed_ranges.append(Range(start, start + size))

    location_ranges: List[Range] = []
    for seed_range in seed_ranges:
        location_ranges.extend(almanac.seeds_to_locations(seed_range))

    return min(location_ranges).start


def main():
    with open("day5.txt", encoding="utf-8") as f:
        data = f.read()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
