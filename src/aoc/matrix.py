from __future__ import annotations


class Matrix:
    def __init__(self, data: list[list[int]]) -> None:
        self.data = data

    @staticmethod
    def from_str(data: str) -> Matrix:
        return Matrix([[int(x) for x in line] for line in data.splitlines()])

    @staticmethod
    def zeros(m: int, n: int = 0) -> Matrix:
        return Matrix([[0 for _ in range(m)] for _ in range(n)])

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
