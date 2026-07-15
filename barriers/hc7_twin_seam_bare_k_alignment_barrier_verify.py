#!/usr/bin/env python3
"""Verify the bounded barrier to bare common-five-set alignment."""

from itertools import combinations

import z3


PALETTE = tuple(f"p{i}" for i in range(1, 7))
COMMON = ("t", "k", "p2", "p3", "p4")


Graph = dict[str, set[str]]


def add_edge(graph: Graph, x: str, y: str) -> None:
    graph.setdefault(x, set()).add(y)
    graph.setdefault(y, set()).add(x)


def edges(graph: Graph):
    for x, y in combinations(graph, 2):
        if y in graph[x]:
            yield x, y


def host() -> Graph:
    graph: Graph = {}
    for x, y in combinations(PALETTE, 2):
        add_edge(graph, x, y)
    for vertex, indices in {
        "k": (2, 3, 4, 5, 6),
        "z": (1, 2, 3, 4, 5),
        "u": (1, 2, 3, 4),
        "d": (1, 2, 3, 4, 6),
        "t": (2, 3, 4, 6),
    }.items():
        for index in indices:
            add_edge(graph, vertex, f"p{index}")
    add_edge(graph, "z", "u")
    add_edge(graph, "d", "t")
    return graph


def assert_proper(graph: Graph, colour: dict[str, int]) -> None:
    assert set(colour) == set(graph)
    assert all(colour[x] != colour[y] for x, y in edges(graph))


def exact_partition(colour: dict[str, int]) -> set[frozenset[str]]:
    return {
        frozenset(v for v in COMMON if colour[v] == value)
        for value in {colour[v] for v in COMMON}
    }


def six_colouring(graph: Graph) -> dict[str, int] | None:
    vertices = tuple(graph)
    solver = z3.Solver()
    variables = {v: z3.Int(f"c_{i}") for i, v in enumerate(vertices)}
    for variable in variables.values():
        solver.add(1 <= variable, variable <= 6)
    for x, y in edges(graph):
        solver.add(variables[x] != variables[y])
    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return {v: model.eval(variables[v]).as_long() for v in vertices}


def has_clique_minor(graph: Graph, order: int) -> bool:
    """Exact connected branch-set encoding; unused vertices get label -1."""
    vertices = tuple(graph)
    solver = z3.Solver()
    label = {v: z3.Int(f"label_{i}") for i, v in enumerate(vertices)}
    depth = {v: z3.Int(f"depth_{i}") for i, v in enumerate(vertices)}
    root = {
        (v, bag): z3.Bool(f"root_{i}_{bag}")
        for i, v in enumerate(vertices)
        for bag in range(order)
    }
    for v in vertices:
        solver.add(-1 <= label[v], label[v] < order)
        solver.add(0 <= depth[v], depth[v] < len(vertices))
    for bag in range(order):
        solver.add(z3.PbEq([(root[v, bag], 1) for v in vertices], 1))
        for v in vertices:
            solver.add(
                z3.Implies(
                    root[v, bag], z3.And(label[v] == bag, depth[v] == 0)
                )
            )
            predecessors = [
                z3.And(label[w] == bag, depth[w] < depth[v])
                for w in graph[v]
            ]
            solver.add(
                z3.Implies(
                    z3.And(label[v] == bag, z3.Not(root[v, bag])),
                    z3.And(depth[v] > 0, z3.Or(predecessors)),
                )
            )
    for first, second in combinations(range(order), 2):
        solver.add(
            z3.Or(
                [
                    z3.Or(
                        z3.And(label[x] == first, label[y] == second),
                        z3.And(label[x] == second, label[y] == first),
                    )
                    for x, y in edges(graph)
                ]
            )
        )
    return solver.check() == z3.sat


def connected(graph: Graph, vertices: set[str]) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    frontier = list(reached)
    while frontier:
        vertex = frontier.pop()
        for neighbour in (graph[vertex] & vertices) - reached:
            reached.add(neighbour)
            frontier.append(neighbour)
    return reached == vertices


def node_connectivity(graph: Graph) -> int:
    vertices = tuple(graph)
    for size in range(len(vertices)):
        for deleted in combinations(vertices, size):
            remaining = set(vertices) - set(deleted)
            if len(remaining) >= 2 and not connected(graph, remaining):
                return size
    return len(vertices) - 1


def contract(graph: Graph, keep: str, drop: str) -> Graph:
    result = {v: set(neighbours) for v, neighbours in graph.items() if v != drop}
    result[keep].update(graph[drop] - {keep})
    for neighbour in graph[drop] - {keep}:
        result[neighbour].discard(drop)
        result[neighbour].add(keep)
    result[keep].discard(drop)
    result[keep].discard(keep)
    return result


def remove_edge(graph: Graph, x: str, y: str) -> Graph:
    result = {v: set(neighbours) for v, neighbours in graph.items()}
    result[x].remove(y)
    result[y].remove(x)
    return result


def induced_edges(graph: Graph, vertices: tuple[str, ...]) -> set[frozenset[str]]:
    chosen = set(vertices)
    return {
        frozenset((x, y))
        for x, y in edges(graph)
        if x in chosen and y in chosen
    }


def assert_rooted_model(graph: Graph) -> None:
    bags = (
        {"t"},
        {"u", "k", "p5", "p1", "p6"},
        {"p2"},
        {"p3"},
        {"p4"},
    )
    assert all(connected(graph, bag) for bag in bags)
    assert all(
        any(y in graph[x] for x in left for y in right)
        for left, right in combinations(bags, 2)
    )


def main() -> None:
    graph = host()
    first = {f"p{i}": i for i in range(1, 7)}
    first.update({"z": 6, "u": 6, "d": 5, "t": 1, "k": 1})
    graph_minus_e = remove_edge(graph, "z", "u")
    assert_proper(graph_minus_e, first)

    contracted = contract(graph, "t", "d")
    second = {f"p{i}": i for i in range(1, 7)}
    second.update({"z": 6, "u": 5, "t": 5, "k": 1})
    assert_proper(contracted, second)
    assert exact_partition(first) != exact_partition(second)

    # The K6 palette forces k=p1 and t=p5 in every contracted colouring.
    assert contracted["k"] & set(PALETTE) == set(PALETTE) - {"p1"}
    assert contracted["t"] & set(PALETTE) == set(PALETTE) - {"p5"}

    # Contracting d into t adds no edge inside COMMON.
    assert induced_edges(graph, COMMON) == induced_edges(contracted, COMMON)

    assert node_connectivity(graph) == 5
    assert six_colouring(graph) is not None
    assert not has_clique_minor(graph, 7)
    assert_rooted_model(graph)
    print("GREEN: bare K-alignment fails; rooted K5 terminal is present")


if __name__ == "__main__":
    main()
