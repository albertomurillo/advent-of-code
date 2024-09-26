import sys
from typing import Any


class FileSystem(dict):
    def size(self) -> tuple[int, list[tuple[str, int]]]:
        def helper(
            name: str, root: dict[str, int | dict], results: list[tuple[str, int]]
        ) -> tuple[int, list[tuple[str, int]]]:
            leafs = (v for v in root.values() if isinstance(v, int))
            childs = ((k, v) for k, v in root.items() if isinstance(v, dict))
            result = sum(leafs)

            for k, v in childs:
                size, results = helper(k, v, results)
                result += size

            results.append((name, result))
            return result, results

        return helper("/", self["/"], [])


def parse_fs(data: str) -> FileSystem:
    tree: dict[str, Any] = {"/": {}}
    stack = []
    cwd = tree
    _ls = False

    for line in data.splitlines():
        tokens = line.split()

        if tokens[0] == "$":
            _ls = False

            match tokens[1]:
                case "cd":
                    name = tokens[2]
                    if name == "..":
                        cwd = stack.pop()
                    else:
                        stack.append(cwd)
                        cwd = cwd[name]
                case "ls":
                    _ls = True

        elif _ls:
            is_dir = tokens[0] == "dir"
            size = 0 if is_dir else int(tokens[0])
            name = tokens[1]
            cwd[name] = {} if is_dir else size

    return FileSystem(tree)


def part1(data: str) -> int:
    fs = parse_fs(data)
    _, directories = fs.size()
    return sum(size for _, size in directories if size <= 100_000)


def part2(data: str) -> int:
    fs = parse_fs(data)
    fs_size = 70_000_000
    fs_need = 30_000_000
    fs_used, directories = fs.size()
    fs_free = fs_size - fs_used

    return min(size for _, size in directories if fs_free + size >= fs_need)


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
