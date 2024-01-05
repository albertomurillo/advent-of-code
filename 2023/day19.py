from __future__ import annotations

import math
import operator
import re
from copy import copy
from dataclasses import dataclass
from typing import List, Tuple


class PartRange(dict[str, range]):
    @property
    def combinations(self) -> int:
        return math.prod((len(x) for x in self.values()))


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
    rules: List[Rule]
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

    def accept_range(self, r: PartRange) -> List[PartRange]:
        accepted: List[PartRange] = []

        q = [("in", r)]
        while q:
            wn, r = q.pop()
            w = self[wn]

            if w.name == "A":
                accepted.append(r)
                continue

            if w.name == "R":
                continue

            for rule in w.rules:
                if (rule.op == "<" and rule.value - 1 not in r[rule.field]) or (
                    rule.op == ">" and rule.value + 1 not in r[rule.field]
                ):
                    continue

                r1, r2 = self._bisect_range(r[rule.field], rule.value, rule.op)
                if rule.op == ">":
                    r1, r2 = r2, r1
                if r1:
                    r[rule.field] = r1
                    q.append((rule.dest, copy(r)))
                if r2:
                    r[rule.field] = r2
                    q.append((w.name, copy(r)))
                break
            else:
                q.append((w.default, copy(r)))

        return accepted

    def _bisect_range(self, r: range, value: int, op: str) -> Tuple[range, range]:
        if op == "<":
            if value <= r.start:
                return (range(0, 0), r)
            if value >= r.stop:
                return (r, range(0, 0))
            return (range(r.start, value), range(value, r.stop))

        if value < r.start:
            return (range(0, 0), r)
        if value >= r.stop - 1:
            return (r, range(0, 0))
        return (range(r.start, value + 1), range(value + 1, r.stop))


def parse_input(data: str) -> Tuple[Workflows, List[Part]]:
    w, p = data.split("\n\n")

    workflows = Workflows()
    for workflow in w.splitlines():
        w = parse_workflow(workflow)
        workflows[w.name] = w
    workflows["A"] = Workflow(name="A", rules=[], default="A")
    workflows["R"] = Workflow(name="R", rules=[], default="R")

    parts = [parse_part(p) for p in p.splitlines()]

    return workflows, parts


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
    ranges = workflows.accept_range(PartRange({k: range(1, 4001) for k in "xmas"}))
    return sum(r.combinations for r in ranges)


def main():
    with open("day19.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
