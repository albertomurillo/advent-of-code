from dataclasses import dataclass
from typing import Dict, List, Optional
import itertools


@dataclass
class AlmanacMap:
    destination: int
    source: int
    size: int

    def dest_from_source(self, source: int) -> Optional[int]:
        start = self.source
        end = self.source + self.size
        if start <= source <= end:
            return self.destination + (source - self.source)
        return None

    def source_from_dest(self, dest: int) -> Optional[int]:
        start = self.destination
        end = self.destination + self.size
        if start <= dest <= end:
            return self.source + (dest - self.destination)
        return None


class Almanac:
    def __init__(self, data: List[str]):
        self.seed_to_soil: List[AlmanacMap] = []
        self.soil_to_fertilizer: List[AlmanacMap] = []
        self.fertilizer_to_water: List[AlmanacMap] = []
        self.water_to_light: List[AlmanacMap] = []
        self.light_to_temperature: List[AlmanacMap] = []
        self.temperature_to_humidity: List[AlmanacMap] = []
        self.humidity_to_location: List[AlmanacMap] = []

        src_to_dest_map_list = None
        src_to_dest_map_lists: Dict[str, List[AlmanacMap]] = {
            "seed-to-soil map": self.seed_to_soil,
            "soil-to-fertilizer map": self.soil_to_fertilizer,
            "fertilizer-to-water map": self.fertilizer_to_water,
            "water-to-light map": self.water_to_light,
            "light-to-temperature map": self.light_to_temperature,
            "temperature-to-humidity map": self.temperature_to_humidity,
            "humidity-to-location map": self.humidity_to_location,
        }

        for line in data[1:]:
            if not line:
                src_to_dest_map_list = None
                continue

            if src_to_dest_map_list is None:
                src_to_dest_map_list = src_to_dest_map_lists[line.split(":")[0]]
                continue

            dest, src, size = (int(x) for x in line.split())
            src_to_dest_map_list.append(AlmanacMap(dest, src, size))

    def seed_to_location(self, seed: int) -> int:
        soil = self.find_dest_in_maps(self.seed_to_soil, seed)
        fertilizer = self.find_dest_in_maps(self.soil_to_fertilizer, soil)
        water = self.find_dest_in_maps(self.fertilizer_to_water, fertilizer)
        light = self.find_dest_in_maps(self.water_to_light, water)
        temp = self.find_dest_in_maps(self.light_to_temperature, light)
        humidity = self.find_dest_in_maps(self.temperature_to_humidity, temp)
        loc = self.find_dest_in_maps(self.humidity_to_location, humidity)
        return loc

    def location_to_seed(self, loc: int) -> int:
        humidity = self.find_source_in_maps(self.humidity_to_location, loc)
        temp = self.find_source_in_maps(self.temperature_to_humidity, humidity)
        light = self.find_source_in_maps(self.light_to_temperature, temp)
        water = self.find_source_in_maps(self.water_to_light, light)
        fertilizer = self.find_source_in_maps(self.fertilizer_to_water, water)
        soil = self.find_source_in_maps(self.soil_to_fertilizer, fertilizer)
        seed = self.find_source_in_maps(self.seed_to_soil, soil)
        return seed

    def find_dest_in_maps(self, maps: List[AlmanacMap], source: int) -> int:
        for m in maps:
            dest = m.dest_from_source(source)
            if dest is not None:
                return dest
        return source

    def find_source_in_maps(self, maps: List[AlmanacMap], dest: int) -> int:
        for m in maps:
            source = m.source_from_dest(dest)
            if source is not None:
                return source
        return dest


def part1(data: List[str]) -> int:
    almanac = Almanac(data)
    seeds = [int(x) for x in data[0].split(": ")[1].split()]
    return min(almanac.seed_to_location(seed) for seed in seeds)


def part2(data: List[str]) -> int:
    almanac = Almanac(data)

    seed_ranges = []
    range_data = data[0].split(": ")[1].split()
    for i in range(0, len(range_data), 2):
        start = int(range_data[i])
        size = int(range_data[i + 1])
        seed_ranges.append(range(start, start + size))
    seed_ranges.sort(key=lambda x: x.start)

    # Brute force :(
    # python3 day5.py  122.10s user 0.05s system 98% cpu 2:03.41 total
    for location in itertools.count():
        seed = almanac.location_to_seed(location)
        for seed_range in seed_ranges:
            if seed in seed_range:
                return location


def main():
    with open("day5.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
