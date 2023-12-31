from __future__ import annotations

from typing import List


class Shape:
    def __init__(self, val: int):
        self.score = val
        self.beats = None
        self.beaten_by = None

    def play(self, other: Shape) -> int:
        if self.beats == other:
            return self.score + 6
        if self == other:
            return self.score + 3
        return self.score


ROCK = Shape(1)
PAPER = Shape(2)
SCISSOR = Shape(3)
ROCK.beats = SCISSOR
ROCK.beaten_by = PAPER
PAPER.beats = ROCK
PAPER.beaten_by = SCISSOR
SCISSOR.beats = PAPER
SCISSOR.beaten_by = ROCK


def part1(data: List[str]) -> int:
    score = 0

    shapes = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSOR,
        "X": ROCK,
        "Y": PAPER,
        "Z": SCISSOR,
    }

    for line in data:
        opponent, me = line.split()
        opponent = shapes[opponent]
        me = shapes[me]
        score += me.play(opponent)

    return score


def part2(data: List[str]) -> int:
    score = 0

    shapes = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSOR,
    }

    actions = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN",
    }

    for line in data:
        opponent, action = line.split()
        opponent = shapes[opponent]
        action = actions[action]
        if action == "DRAW":
            me = opponent
        elif action == "LOSE":
            me = opponent.beats
        else:  # action == "WIN"
            me = opponent.beaten_by
        score += me.play(opponent)

    return score


def main():
    with open("day2.txt", encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
