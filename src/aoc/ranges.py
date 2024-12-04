from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Range:
    start: int
    stop: int

    def overlaps(self, other: Range) -> bool:
        return max(self, other).start <= min(self, other).stop

    def fully_overlaps(self, other: Range) -> bool:
        return (self.start <= other.start <= other.stop <= self.stop) or (
            other.start <= self.start <= self.stop <= other.stop
        )

    def intersection(self, other: Range) -> tuple[Range, Range, Range]:
        if self.start > other.stop:
            return (Range(0, 0), Range(0, 0), self)

        if self.stop < other.start:
            return (self, Range(0, 0), Range(0, 0))

        before = Range(0, 0)
        if self.start < other.start:
            before = Range(self.start, other.start)

        inter = Range(max(self.start, other.start), min(self.stop, other.stop))

        after = Range(0, 0)
        if self.stop > other.stop:
            after = Range(other.stop, self.stop)

        return (before, inter, after)

    def offset(self, item: int) -> int:
        return item - self.start

    def __bool__(self) -> bool:
        return bool(len(self))

    def __contains__(self, item: int) -> bool:
        return self.start <= item < self.stop

    def __len__(self) -> int:
        return self.stop - self.start
