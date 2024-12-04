import math
import sys
from collections import deque
from dataclasses import dataclass, field
from itertools import count


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

    def push(self, item: tuple[str, str, bool]) -> None:
        _, _, pulse = item
        if pulse:
            self._high_pulses += 1
        else:
            self._low_pulses += 1
        self._q.append(item)

    def pop(self) -> tuple[str, str, bool]:
        return self._q.popleft()

    def __len__(self) -> int:
        return len(self._q)

    def __bool__(self) -> bool:
        return bool(len(self))


@dataclass
class Module:
    name: str
    modules: list[str] = field(default_factory=list)
    pulse: bool = field(default=False)

    def send(self, q: Queue) -> None:
        for receiver in self.modules:
            q.push((self.name, receiver, self.pulse))

    def receive(self, q: Queue, sender: str, pulse: bool) -> None:
        pass


@dataclass
class FlipFlop(Module):
    def receive(self, q: Queue, sender: str, pulse: bool) -> None:
        if pulse:
            return

        self.pulse = not self.pulse
        self.send(q)


@dataclass
class Conjuction(Module):
    low: set[str] = field(default_factory=set)
    high: set[str] = field(default_factory=set)

    def add_input(self, module: str) -> None:
        self.low.add(module)

    def receive(self, q: Queue, sender: str, pulse: bool) -> None:
        if pulse:
            self.low.discard(sender)
            self.high.add(sender)
        else:
            self.high.discard(sender)
            self.low.add(sender)

        self.pulse = bool(self.low)
        self.send(q)


@dataclass
class Broadcaster(Module):
    def receive(self, q: Queue, sender: str, pulse: bool) -> None:
        self.pulse = pulse
        self.send(q)


@dataclass
class Button(Module):
    def push(self, q: Queue) -> None:
        self.send(q)


def parse_input(data: list[str]) -> dict[str, Module]:
    module_map: dict[str, Module] = {}

    # First pass
    for line in data:
        name, d = line.split(" -> ")
        destinations = d.split(", ")

        if name.startswith("%"):
            module_map[name[1:]] = FlipFlop(name[1:], destinations)

        elif name.startswith("&"):
            module_map[name[1:]] = Conjuction(name[1:], destinations)

        elif name == "broadcaster":
            module_map[name] = Broadcaster(name, destinations)

    # Second Passs
    for line in data:
        name, d = line.split(" -> ")
        destinations = d.split(", ")

        if name[0] in "%&":
            name = name[1:]

        for destination in destinations:
            m = module_map.get(destination)
            if isinstance(m, Conjuction):
                m.add_input(name)

    return module_map


def part1(data: str) -> int:
    modules = parse_input(data.splitlines())
    button = Button("button", ["broadcaster"])
    q = Queue()

    for _ in range(1000):
        button.push(q)
        while q:
            sender, receiver, pulse = q.pop()
            if receiver not in modules:
                continue
            modules[receiver].receive(q, sender, pulse)

    return q.high_pulses * q.low_pulses


def part2(data: str) -> int:
    modules = parse_input(data.splitlines())
    button = Button("button", ["broadcaster"])
    q = Queue()

    # Assumption 1: There is only 1 parent for rx
    rx_parents = [k for k, v in modules.items() if "rx" in v.modules]
    assert len(rx_parents) == 1
    rx_parent = rx_parents[0]

    # Assumption 2: The rx_parent is a conjunction
    assert isinstance(modules[rx_parent], Conjuction)

    # Assumption 3: The rx_grand_parents signal high in regular intervals / cycles
    rx_grand_parents = {k for k, v in modules.items() if rx_parent in v.modules}
    cycles = []

    for pushes in count(1):
        button.push(q)
        while q:
            sender, receiver, pulse = q.pop()
            if receiver not in modules:
                continue
            modules[receiver].receive(q, sender, pulse)

            if receiver in rx_grand_parents and modules[receiver].pulse:
                cycles.append(pushes)
                rx_grand_parents.remove(receiver)

        if not rx_grand_parents:
            break

    return math.lcm(*cycles)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
