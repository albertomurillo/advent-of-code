#!/usr/bin/env python3

import re
import shutil
import subprocess
import tomllib
from pathlib import Path

UV = shutil.which("uv")
assert UV is not None, "uv command not found"

PATTERN = re.compile(r"([a-z][a-z-]*).*")
FROZEN: set[str] = set()

with Path("pyproject.toml").open("rb") as fp:
    config = tomllib.load(fp)


for table, field, opt in [
    ["project", "dependencies", ""],
    ["dependency-groups", "dev", "--dev"],
]:
    deps = config.get(table, {}).get(field, [])
    deps = {m[1] for dep in deps if (m := PATTERN.match(dep))} - FROZEN
    opts = [opt] if opt else []
    if not deps:
        continue
    for command in ("remove", "add"):
        subprocess.run([UV, command, *opts, *deps], check=True)  # noqa: S603
