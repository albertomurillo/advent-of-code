from __future__ import annotations

import heapq
from collections import defaultdict
from typing import Any, Protocol, Tuple


class PriorityQueue(Protocol):
    def push(self, key: Any, value: Any) -> None:
        ...

    def pop(self) -> Tuple[Any, Any]:
        ...

    def peek(self) -> Tuple[Any, Any]:
        ...

    def __bool__(self) -> bool:
        ...


class MinHeap:
    def __init__(self):
        self._q = []

    def push(self, key: Any, value: Any) -> None:
        heapq.heappush(self._q, (key, value))

    def pop(self) -> Tuple[Any, Any]:
        return heapq.heappop(self._q)

    def peek(self) -> Tuple[Any, Any]:
        return self._q[0]

    def __bool__(self) -> bool:
        return bool(self._q)


class BucketQueue:
    """https://en.wikipedia.org/wiki/Bucket_queue"""

    def __init__(self):
        self._q: dict[Any, list] = defaultdict(list)

    def push(self, key: Any, value: Any) -> None:
        self._q[key].append(value)

    def pop(self) -> Tuple[Any, Any]:
        key = min(self._q)
        val = self._q[key].pop()
        if not self._q[key]:
            del self._q[key]
        return key, val

    def peek(self) -> Tuple[Any, Any]:
        key = min(self._q)
        return key, self._q[key][-1]

    def __bool__(self) -> bool:
        return bool(self._q)
