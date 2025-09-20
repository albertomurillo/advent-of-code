from pathlib import Path


def read_input(year: int, day: int) -> str:
    """Return the contents of the real input file for the given year and day.

    This helper is intended for tests and locates files under the repository's
    `inputs/<year>/day<day>.txt` path.
    """

    path = Path(__file__).resolve().parents[1] / "inputs" / str(year) / f"day{day}.txt"
    return path.read_text(encoding="utf8")
