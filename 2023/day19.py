import math
import operator
import re
from copy import copy
from dataclasses import dataclass
from typing import Dict, List, Tuple

Part = Dict[str, int]


@dataclass
class Workflow:
    name: str
    rules: List[str]
    default: str


def parse_input(data: str) -> Tuple[Dict[str, Workflow], List[Part]]:
    w, p = data.split("\n\n")

    workflows = {}
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
        rules=m.group(2).split(","),
        default=m.group(3),
    )


def parse_part(data: str) -> Part:
    pattern = re.compile(r"^{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}$")
    m = pattern.match(data)
    return {
        "x": int(m.group(1)),
        "m": int(m.group(2)),
        "a": int(m.group(3)),
        "s": int(m.group(4)),
    }


def parse_rule(data: str) -> Tuple[str, callable, int, str]:
    operators = {"<": operator.lt, ">": operator.gt}
    pattern = re.compile(r"([xmas])([<>])(\d+):(\w+)")
    m = pattern.match(data)
    return (m.group(1), operators[m.group(2)], int(m.group(3)), m.group(4))


def process_part(part: Part, workflows: Dict[str, Workflow]) -> int:
    workflow = workflows["in"]

    while workflow.name not in ["A", "R"]:
        for rule in workflow.rules:
            field, op, value, next_workflow = parse_rule(rule)
            if op(part[field], value):
                workflow = workflows[next_workflow]
                break
        else:
            workflow = workflows[workflow.default]

    if workflow.name == "A":
        return sum(x for x in part.values())

    return 0


def bisect_range(r: range, value: int, op: operator) -> Tuple[range, range]:
    if op == operator.lt:
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


def part1(data: str) -> int:
    workflows, parts = parse_input(data)
    return sum(process_part(p, workflows) for p in parts)


def part2(data: str) -> int:
    workflows, _ = parse_input(data)

    def process_ranges(workflow_name: str, r: Dict[str, range]) -> None:
        nonlocal accepted

        w = workflows[workflow_name]
        if w.name == "A":
            accepted.append(r)
            return
        if w.name == "R":
            return
        for rule in w.rules:
            field, op, value, next_workflow = parse_rule(rule)
            if (op == operator.lt and value - 1 not in r[field]) or (
                op == operator.gt and value + 1 not in r[field]
            ):
                continue

            r1, r2 = bisect_range(r[field], value, op)
            if op == operator.gt:
                r1, r2 = r2, r1
            if r1:
                r[field] = r1
                q.append((next_workflow, copy(r)))
            if r2:
                r[field] = r2
                q.append((w.name, copy(r)))
            break
        else:
            q.append((w.default, copy(r)))

    ranges = {k: range(1, 4001) for k in "xmas"}
    accepted: List[Dict[str, range]] = []
    q = [("in", ranges)]

    while q:
        wf, r = q.pop()
        process_ranges(wf, r)

    return sum(math.prod([len(x) for x in a.values()]) for a in accepted)


def main():
    with open("day19.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
