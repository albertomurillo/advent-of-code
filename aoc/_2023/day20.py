import sys
from collections import deque
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple


@dataclass
class Queue:
    _q: deque = field(default_factory=deque)
    _low_pulses: int = 0
    _high_pulses: int = 0

    @property
    def low_pulses(self) -> int:
        return self._low_pulses

    @property
    def high_pulses(self) -> int:
        return self._high_pulses

    def append(self, item: Tuple[str, str, bool]) -> None:
        _, _, pulse = item
        if pulse:
            self._high_pulses += 1
        else:
            self._low_pulses += 1
        self._q.append(item)

    def pop(self) -> Tuple[str, str, bool]:
        return self._q.popleft()

    def __len__(self) -> int:
        return len(self._q)

    def __bool__(self) -> bool:
        return bool(len(self))


@dataclass
class Module:
    name: str
    modules: List[str] = field(default_factory=list)

    def send(self, q: Queue, pulse: bool):
        for receiver in self.modules:
            q.append((self.name, receiver, pulse))

    def receive(self, q: Queue, sender: str, pulse: bool):
        pass


@dataclass
class FlipFlop(Module):
    _state: bool = field(default=False)

    def receive(self, q: Queue, sender: str, pulse: bool):
        if pulse:
            return

        self._state = not self._state
        self.send(q, self._state)


@dataclass
class Conjuction(Module):
    low: Set[str] = field(default_factory=set)
    high: Set[str] = field(default_factory=set)

    def add_input(self, module: str) -> None:
        self.low.add(module)

    def receive(self, q: Queue, sender: str, pulse: bool):
        if pulse:
            self.low.discard(sender)
            self.high.add(sender)
        else:
            self.high.discard(sender)
            self.low.add(sender)

        self.send(q, bool(self.low))


@dataclass
class Broadcaster(Module):
    def receive(self, q: Queue, sender: str, pulse: bool):
        self.send(q, pulse)


@dataclass
class Button(Module):
    pass


def parse_input(data: List[str]) -> Dict[str, Module]:
    module_map: Dict[str, Module] = {}

    # First pass
    for line in data:
        name, destination = line.split(" -> ")
        if name.startswith("%"):
            module_map[name[1:]] = FlipFlop(name[1:])
        elif name.startswith("&"):
            module_map[name[1:]] = Conjuction(name[1:])
        elif name == "broadcaster":
            module_map[name] = Broadcaster(name)

    # Second Passs
    for line in data:
        name, destination = line.split(" -> ")
        if name[0] in "%&":
            name = name[1:]
        modules = destination.split(", ")
        module_map[name].modules = modules
        for module in (
            x for x in modules if isinstance(module_map.get(x, None), Conjuction)
        ):
            module_map[module].add_input(name)

    return module_map


def part1(data: str) -> int:
    modules = parse_input(data.splitlines())
    button = Button("button", ["broadcaster"])
    q = Queue()

    for _ in range(1000):
        button.send(q, pulse=False)
        while q:
            sender, receiver, pulse = q.pop()
            if receiver not in modules:
                continue
            modules[receiver].receive(q, sender, pulse)

    return q.high_pulses * q.low_pulses


def main():
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")


if __name__ == "__main__":
    main()
