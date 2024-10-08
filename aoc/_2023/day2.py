import sys
from dataclasses import dataclass


@dataclass
class Cubes:
    blue: int = 0
    green: int = 0
    red: int = 0

    @property
    def power(self) -> int:
        return self.blue * self.green * self.red


@dataclass
class Game:
    id: int
    hands: list[Cubes]

    def is_possible_with_bag(self, bag: Cubes) -> bool:
        for hand in self.hands:
            if hand.blue > bag.blue or hand.green > bag.green or hand.red > bag.red:
                return False
        return True


def parse_game(data: str) -> Game:
    game_data, hands_data = data.split(":")
    _, game_id = game_data.split()

    hands = [parse_hand(hand_data) for hand_data in hands_data.split(";")]
    return Game(id=int(game_id), hands=hands)


def parse_hand(data: str) -> Cubes:
    cubes = Cubes()
    for cube_data in data.split(","):
        count, color = cube_data.split()
        setattr(cubes, color, int(count))
    return cubes


def part1(data: str) -> int:
    bag = Cubes(blue=14, green=13, red=12)
    games = (parse_game(line) for line in data.splitlines())
    return sum(game.id for game in games if game.is_possible_with_bag(bag))


def part2(data: str) -> int:
    games = (parse_game(line) for line in data.splitlines())
    cubes = (
        Cubes(
            blue=max(hand.blue for hand in game.hands),
            green=max(hand.green for hand in game.hands),
            red=max(hand.red for hand in game.hands),
        )
        for game in games
    )
    return sum(cube.power for cube in cubes)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
