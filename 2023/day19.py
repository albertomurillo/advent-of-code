import operator
import re
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
            field, op, amount, next_workflow = parse_rule(rule)
            if op(part[field], amount):
                workflow = workflows[next_workflow]
                break
        else:
            workflow = workflows[workflow.default]

    if workflow.name == "A":
        return sum(x for x in part.values())

    return 0


def part1(data: str) -> int:
    workflows, parts = parse_input(data)
    return sum(process_part(p, workflows) for p in parts)


def main():
    with open("day19.txt", encoding="utf-8") as f:
        data = f.read()

    print(part1(data))


if __name__ == "__main__":
    main()
