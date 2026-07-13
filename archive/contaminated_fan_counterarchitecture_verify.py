#!/usr/bin/env python3
"""Verify the finite claims in hadwiger_contaminated_fan_counterarchitecture.md."""

from itertools import combinations


parts = [("x", "y", "k")] + [(f"u{i}", f"v{i}") for i in range(1, 6)]
vertices = tuple(v for part in parts for v in part)


def edge(x: str, y: str) -> tuple[str, str]:
    return tuple(sorted((x, y)))


edges = {
    edge(x, y)
    for i, left in enumerate(parts)
    for right in parts[i + 1 :]
    for x in left
    for y in right
}
edges.remove(edge("x", "u1"))
edges.add(edge("x", "y"))


def connected_after(removal: tuple[str, ...]) -> bool:
    remaining = set(vertices) - set(removal)
    if len(remaining) <= 1:
        return True
    reached = {next(iter(remaining))}
    while True:
        expanded = reached | {
            v for v in remaining if any(edge(v, u) in edges for u in reached)
        }
        if expanded == reached:
            return reached == remaining
        reached = expanded


def connectivity() -> tuple[int, tuple[str, ...]]:
    for size in range(len(vertices)):
        for removal in combinations(vertices, size):
            if not connected_after(removal):
                return size, removal
    raise AssertionError("complete graph convention not reached")


def main() -> None:
    kappa, cut = connectivity()
    assert kappa == 10

    clique = ("x", "y", "v1", "u2", "u3", "u4", "u5")
    assert all(edge(x, y) in edges for x, y in combinations(clique, 2))

    colour = {v: i for i, part in enumerate(parts) for v in part}
    deletion_edges = edges - {edge("x", "y")}
    assert all(colour[x] != colour[y] for x, y in deletion_edges)

    paths = [("x", "v1", "k", "u1", "y")]
    paths += [("x", f"u{i}", "y") for i in range(2, 6)]
    for index, path in enumerate(paths, 1):
        assert all(edge(path[i], path[i + 1]) in deletion_edges for i in range(len(path) - 1))
        assert set(map(colour.get, path)) == {0, index}

    assert edge("x", "u1") not in edges
    print("vertices", len(vertices))
    print("connectivity", kappa, "example cut", cut)
    print("K7 clique", clique)
    print("five detours", paths)
    print("aligned x-u1-y path", False)


if __name__ == "__main__":
    main()
