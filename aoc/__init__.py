from typing import List


def as_matrix(data: str) -> List[List[str]]:
    return [list(x) for x in data.splitlines()]
