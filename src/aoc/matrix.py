from __future__ import annotations

type Direction = tuple[int, int]

N: Direction = (-1, 0)
S: Direction = (1, 0)
E: Direction = (0, 1)
W: Direction = (0, -1)


class Matrix:
    def __init__(self, data: list[list[int]] | None = None) -> None:
        self.data = data if data else []

    def from_str(self, data: str) -> None:
        self.data = [[int(x) for x in line] for line in data.splitlines()]

    def from_zeros(self, m: int, n: int = 0) -> Matrix:
        self.data = [[0 for _ in range(m)] for _ in range(n)]

    @property
    def shape(self) -> tuple[int, int]:
        return self.m, self.n

    @property
    def m(self) -> int:
        return len(self.data[0])

    @property
    def n(self) -> int:
        return len(self.data)

    def __getitem__(self, key: int) -> list[int]:
        return self.data[key]

    def __str___(self) -> str:
        return "\n".join(str(row) for row in self.data)
