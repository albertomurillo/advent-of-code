from __future__ import annotations

import math
import operator
import re
import sys
from copy import copy
from dataclasses import dataclass

from aoc import as_parts
from aoc.ranges import Range


class PartRange(dict[str, Range]):
    @property
    def combinations(self) -> int:
        return math.prod(len(x) for x in self.values())


class Part(dict):
    @property
    def rating(self) -> int:
        return sum(x for x in self.values())


@dataclass
class Rule:
    field: str
    op: str
    value: int
    dest: str

    def eval(self, part: Part) -> bool:
        ops = {"<": operator.lt, ">": operator.gt}
        return ops[self.op](part[self.field], self.value)


@dataclass
class Workflow:
    name: str
    rules: list[Rule]
    default: str


class Workflows(dict[str, Workflow]):
    def accept_part(self, part: Part) -> bool:
        workflow = self["in"]

        while workflow.name not in ["A", "R"]:
            for rule in workflow.rules:
                if rule.eval(part):
                    workflow = self[rule.dest]
                    break
            else:
                workflow = self[workflow.default]

        return workflow.name == "A"

    def accept_range(self, pr: PartRange) -> list[PartRange]:
        accepted: list[PartRange] = []

        q = [("in", pr)]
        while q:
            workflow_name, pr = q.pop()
            workflow = self[workflow_name]

            if workflow.name == "A":
                accepted.append(pr)
                continue

            if workflow.name == "R":
                continue

            for rule in workflow.rules:
                value = rule.value

                if (rule.op == "<" and value - 1 not in pr[rule.field]) or (
                    rule.op == ">" and value + 1 not in pr[rule.field]
                ):
                    continue

                if rule.op == "<":
                    r1, _, r2 = pr[rule.field].intersection(Range(value, value))
                else:
                    r2, _, r1 = pr[rule.field].intersection(Range(value + 1, value + 1))

                pr[rule.field] = r1
                q.append((rule.dest, copy(pr)))

                pr[rule.field] = r2
                q.append((workflow.name, copy(pr)))

                break
            else:
                q.append((workflow.default, copy(pr)))

        return accepted


def parse_input(data: str) -> tuple[Workflows, list[Part]]:
    p1, p2 = as_parts(data)

    workflows = {(w := parse_workflow(line)).name: w for line in p1.splitlines()}
    workflows["A"] = Workflow(name="A", rules=[], default="A")
    workflows["R"] = Workflow(name="R", rules=[], default="R")

    parts = [parse_part(line) for line in p2.splitlines()]

    return Workflows(workflows), parts


def parse_workflow(data: str) -> Workflow:
    pattern = re.compile(r"(\w+){(.+),(\w+)}")
    m = pattern.match(data)
    return Workflow(
        name=m.group(1),
        rules=[parse_rule(x) for x in m.group(2).split(",")],
        default=m.group(3),
    )


def parse_rule(data: str) -> Rule:
    pattern = re.compile(r"([xmas])([<>])(\d+):(\w+)")
    m = pattern.match(data)
    return Rule(field=m.group(1), op=m.group(2), value=int(m.group(3)), dest=m.group(4))


def parse_part(data: str) -> Part:
    pattern = re.compile(r"^{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}$")
    m = pattern.match(data)
    return Part(
        [
            ("x", int(m.group(1))),
            ("m", int(m.group(2))),
            ("a", int(m.group(3))),
            ("s", int(m.group(4))),
        ]
    )


def part1(data: str) -> int:
    workflows, parts = parse_input(data)
    return sum(p.rating for p in parts if workflows.accept_part(p))


def part2(data: str) -> int:
    workflows, _ = parse_input(data)
    ranges = workflows.accept_range(PartRange({k: Range(1, 4001) for k in "xmas"}))
    return sum(r.combinations for r in ranges)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
