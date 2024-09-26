from __future__ import annotations

import heapq
from collections import defaultdict
from collections.abc import Hashable
from typing import Any, Protocol

Key = Hashable


class PriorityQueue(Protocol):
    def push(self, key: Key, value: Any) -> None:
        pass

    def pop(self) -> tuple[Key, Any]:
        pass

    def __bool__(self) -> bool:
        pass


class MinHeap:
    def __init__(self) -> None:
        self._q = []

    def push(self, key: Key, value: Any) -> None:
        heapq.heappush(self._q, (key, value))

    def pop(self) -> tuple[Key, Any]:
        return heapq.heappop(self._q)

    def __bool__(self) -> bool:
        return bool(self._q)


class BucketQueue:
    """https://en.wikipedia.org/wiki/Bucket_queue"""

    def __init__(self) -> None:
        self._q: dict[Key, list] = defaultdict(list)

    def push(self, key: Key, value: Any) -> None:
        self._q[key].append(value)

    def pop(self) -> tuple[Key, Any]:
        key = min(self._q)
        val = self._q[key].pop()
        if not self._q[key]:
            del self._q[key]
        return key, val

    def __bool__(self) -> bool:
        return bool(self._q)
