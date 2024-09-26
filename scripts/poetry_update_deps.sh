#!/bin/bash
set -e

deps=$(sed -n '/\[tool.poetry.group.dev.dependencies\]/,/^$/s/\(^.*\) = .*/\1/p' pyproject.toml)
for dep in $deps; do
    poetry add --group dev "${dep}@latest"
done
