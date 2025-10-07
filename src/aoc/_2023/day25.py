import sys

import matplotlib.pyplot as plt
import networkx as nx


def draw(g: nx.Graph):
    nx.draw(
        g,
        with_labels=True,
        node_color="skyblue",
        node_size=150,
        edge_color="gray",
        width=2,
    )
    plt.title("Basic NetworkX Graph Visualization")
    plt.show()


def part1(data: str) -> int:
    # Build graph
    adjacency_dict = {}
    for line in data.splitlines():
        k, v = line.split(":")
        adjacency_dict[k] = v.split()
    g = nx.Graph(adjacency_dict)

    # Cut graph
    edges = nx.minimum_edge_cut(g)
    for edge in edges:
        g.remove_edge(*edge)

    # Count size of each group
    size = 1
    for edge in edges.pop():
        nodes = set()
        for n1, n2 in nx.edge_bfs(g, edge):
            nodes.add(n1)
            nodes.add(n2)
        size *= len(nodes)

    return size


def part2(data: str) -> int:
    return 0


def main() -> None:
    data = sys.stdin.read()
    print(f"part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()
