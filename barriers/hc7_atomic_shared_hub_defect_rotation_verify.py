#!/usr/bin/env python3
"""Verify the atomic shared-hub defect-rotation barrier.

The host is the 13-vertex sparse four-anchor augmentation of an ``H_0``
subdivision described in the companion note.  The checker independently

* exhausts all spanning seven-bag clique-minor models;
* validates the displayed atomic strong ``K_7`` immersion;
* exhausts every choice of seven branch vertices and every possible atomic
  strong immersion on those branches; and
* validates the exact rotated eight-bag quotient.

Run from the repository root with

    .venv/bin/python -B barriers/hc7_atomic_shared_hub_defect_rotation_verify.py

Expected final line:

    rotated_strong_lifts: collision_f=no collision_g=no
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from typing import Hashable

import networkx as nx


Node = Hashable
CORE_BRANCHES = tuple("abcdefg")
VERTICES = CORE_BRANCHES + ("x", "h", "p_ac", "p_bd", "p_ad", "p_bc")
DEFECTS = {frozenset(("a", "b")), frozenset(("c", "d"))}


def build_host() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(VERTICES)
    graph.add_edges_from(
        (u, v)
        for u, v in combinations(CORE_BRANCHES, 2)
        if frozenset((u, v)) not in DEFECTS
    )
    graph.add_edges_from(("x", z) for z in "abcd")

    for u, v, middle in (
        ("a", "c", "p_ac"),
        ("b", "d", "p_bd"),
        ("a", "d", "p_ad"),
        ("b", "c", "p_bc"),
    ):
        graph.remove_edge(u, v)
        graph.add_edges_from(((u, middle), (middle, v)))

    graph.add_edges_from(
        (("f", "p_ac"), ("f", "p_bd"), ("g", "p_ad"), ("g", "p_bc"))
    )
    graph.remove_edge("f", "g")
    graph.add_edges_from(
        (("f", "h"), ("h", "g"), ("e", "h"), ("h", "x"))
    )
    assert tuple(graph) == VERTICES
    assert len(graph) == 13 and graph.number_of_edges() == 34
    return graph


def spanning_k7_model(graph: nx.Graph) -> tuple[frozenset[Node], ...] | None:
    """Return an exact spanning ``K_7`` model, or certify that none exists."""

    vertices = tuple(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    rows = [0] * len(vertices)
    for u, v in graph.edges:
        left, right = index[u], index[v]
        rows[left] |= 1 << right
        rows[right] |= 1 << left

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            old_reached = reached
            pending = reached
            while pending:
                bit = pending & -pending
                pending ^= bit
                reached |= rows[bit.bit_length() - 1] & mask
            if reached == old_reached:
                return reached == mask

    blocks: list[list[int]] = []

    def search(position: int) -> tuple[frozenset[Node], ...] | None:
        if position == len(vertices):
            if len(blocks) != 7:
                return None
            masks = tuple(sum(1 << vertex for vertex in block) for block in blocks)
            if not all(connected(mask) for mask in masks):
                return None
            for left, right in combinations(range(7), 2):
                neighbourhood = 0
                pending = masks[left]
                while pending:
                    bit = pending & -pending
                    pending ^= bit
                    neighbourhood |= rows[bit.bit_length() - 1]
                if not neighbourhood & masks[right]:
                    return None
            return tuple(
                frozenset(vertices[vertex] for vertex in block) for block in blocks
            )

        if len(blocks) + len(vertices) - position < 7:
            return None
        for block in blocks:
            block.append(position)
            model = search(position + 1)
            block.pop()
            if model is not None:
                return model
        if len(blocks) < 7:
            blocks.append([position])
            model = search(position + 1)
            blocks.pop()
            if model is not None:
                return model
        return None

    return search(0)


def original_routes() -> dict[frozenset[str], tuple[str, ...]]:
    routes: dict[frozenset[str], tuple[str, ...]] = {}
    subdivisions = {
        frozenset(("a", "c")): "p_ac",
        frozenset(("b", "d")): "p_bd",
        frozenset(("a", "d")): "p_ad",
        frozenset(("b", "c")): "p_bc",
        frozenset(("f", "g")): "h",
    }
    for u, v in combinations(CORE_BRANCHES, 2):
        demand = frozenset((u, v))
        if demand == frozenset(("a", "b")):
            routes[demand] = (u, "x", v)
        elif demand == frozenset(("c", "d")):
            routes[demand] = (u, "x", v)
        elif demand in subdivisions:
            routes[demand] = (u, subdivisions[demand], v)
        else:
            routes[demand] = (u, v)
    return routes


def validate_atomic_immersion(
    graph: nx.Graph,
    branches: tuple[str, ...],
    routes: dict[frozenset[str], tuple[str, ...]],
) -> tuple[str, tuple[str, str], int]:
    assert set(routes) == {frozenset(pair) for pair in combinations(branches, 2)}
    used_edges: set[frozenset[str]] = set()
    transit: dict[str, list[frozenset[str]]] = {vertex: [] for vertex in graph}
    length = 0
    for demand, path in routes.items():
        assert frozenset((path[0], path[-1])) == demand
        assert len(path) == len(set(path))
        assert all(graph.has_edge(u, v) for u, v in zip(path, path[1:]))
        assert not (set(path[1:-1]) & set(branches))
        length += len(path) - 1
        for u, v in zip(path, path[1:]):
            edge = frozenset((u, v))
            assert edge not in used_edges
            used_edges.add(edge)
        for vertex in path[1:-1]:
            transit[vertex].append(demand)

    collisions = {vertex: demands for vertex, demands in transit.items() if len(demands) > 1}
    assert len(collisions) == 1
    collision, demands = next(iter(collisions.items()))
    assert len(demands) == 2
    labels = tuple(sorted("".join(sorted(demand)) for demand in demands))
    return collision, labels, length


Path = tuple[int, int, int, tuple[str, ...]]


def path_candidates(
    graph: nx.Graph,
    branches: tuple[str, ...],
    source: str,
    target: str,
    edge_index: dict[tuple[str, str], int],
    vertex_index: dict[str, int],
) -> tuple[Path, ...]:
    """Enumerate every simple branch-avoiding path for one demand."""

    branch_set = set(branches)
    candidates: list[Path] = []

    def visit(current: str, path: list[str], used: set[str]) -> None:
        for neighbour in sorted(graph[current]):
            if neighbour == target:
                sequence = tuple(path + [target])
                edge_mask = 0
                for u, v in zip(sequence, sequence[1:]):
                    edge_mask |= 1 << edge_index[tuple(sorted((u, v)))]
                internal = sequence[1:-1]
                vertex_mask = sum(1 << vertex_index[z] for z in internal)
                candidates.append((len(internal), edge_mask, vertex_mask, sequence))
                continue
            if neighbour in used or neighbour in branch_set:
                continue
            # There are six nonbranches.  An atomic immersion can use each
            # at most once, except its unique collision vertex twice.
            if len(path) - 1 == 6:
                continue
            used.add(neighbour)
            path.append(neighbour)
            visit(neighbour, path, used)
            path.pop()
            used.remove(neighbour)

    visit(source, [source], {source})
    return tuple(sorted(candidates, key=lambda candidate: (candidate[0], candidate[3])))


def candidates_for_branches(
    graph: nx.Graph,
    branches: tuple[str, ...],
    edge_index: dict[tuple[str, str], int],
    vertex_index: dict[str, int],
) -> dict[tuple[str, str], tuple[Path, ...]]:
    return {
        demand: path_candidates(
            graph, branches, demand[0], demand[1], edge_index, vertex_index
        )
        for demand in combinations(branches, 2)
    }


def find_atomic_routes(
    graph: nx.Graph,
    candidates: dict[tuple[str, str], tuple[Path, ...]],
    vertex_index: dict[str, int],
    excess_limit: int,
) -> dict[tuple[str, str], tuple[str, ...]] | None:
    """Find an atomic strong immersion within a total route-excess limit."""

    vertices = tuple(graph)
    seen: set[tuple[tuple[tuple[str, str], ...], int, tuple[int, ...], int]] = set()

    def search(
        remaining: tuple[tuple[str, str], ...],
        used_edges: int,
        usage: tuple[int, ...],
        excess: int,
        chosen: dict[tuple[str, str], tuple[str, ...]],
    ) -> dict[tuple[str, str], tuple[str, ...]] | None:
        if not remaining:
            if sum(max(0, count - 1) for count in usage) == 1:
                return chosen.copy()
            return None

        state = (remaining, used_edges, usage, excess)
        if state in seen:
            return None
        seen.add(state)

        selected: tuple[str, str] | None = None
        feasible: list[tuple[Path, tuple[int, ...]]] | None = None
        for demand in remaining:
            demand_options: list[tuple[Path, tuple[int, ...]]] = []
            for candidate in candidates[demand]:
                path_excess, edge_mask, vertex_mask, _ = candidate
                if excess + path_excess > excess_limit or edge_mask & used_edges:
                    continue
                next_usage = list(usage)
                for vertex in vertices:
                    if vertex_mask & (1 << vertex_index[vertex]):
                        next_usage[vertex_index[vertex]] += 1
                if max(next_usage) > 2:
                    continue
                if sum(max(0, count - 1) for count in next_usage) > 1:
                    continue
                demand_options.append((candidate, tuple(next_usage)))
            if not demand_options:
                return None
            if feasible is None or len(demand_options) < len(feasible):
                selected, feasible = demand, demand_options

        assert selected is not None and feasible is not None
        next_remaining = tuple(demand for demand in remaining if demand != selected)
        for candidate, next_usage in feasible:
            path_excess, edge_mask, _, sequence = candidate
            chosen[selected] = sequence
            answer = search(
                next_remaining,
                used_edges | edge_mask,
                next_usage,
                excess + path_excess,
                chosen,
            )
            if answer is not None:
                return answer
            del chosen[selected]
        return None

    return search(tuple(candidates), 0, (0,) * len(graph), 0, {})


def all_atomic_routes(
    graph: nx.Graph,
    candidates: dict[tuple[str, str], tuple[Path, ...]],
    vertex_index: dict[str, int],
    excess_limit: int,
) -> list[dict[tuple[str, str], tuple[str, ...]]]:
    """Enumerate solutions after ``find_atomic_routes`` identifies a branch set."""

    vertices = tuple(graph)
    solutions: list[dict[tuple[str, str], tuple[str, ...]]] = []

    def search(
        remaining: tuple[tuple[str, str], ...],
        used_edges: int,
        usage: tuple[int, ...],
        excess: int,
        chosen: dict[tuple[str, str], tuple[str, ...]],
    ) -> None:
        if not remaining:
            if sum(max(0, count - 1) for count in usage) == 1:
                solutions.append(chosen.copy())
            return

        selected: tuple[str, str] | None = None
        feasible: list[tuple[Path, tuple[int, ...]]] | None = None
        for demand in remaining:
            demand_options: list[tuple[Path, tuple[int, ...]]] = []
            for candidate in candidates[demand]:
                path_excess, edge_mask, vertex_mask, _ = candidate
                if excess + path_excess > excess_limit or edge_mask & used_edges:
                    continue
                next_usage = list(usage)
                for vertex in vertices:
                    if vertex_mask & (1 << vertex_index[vertex]):
                        next_usage[vertex_index[vertex]] += 1
                if max(next_usage) > 2:
                    continue
                if sum(max(0, count - 1) for count in next_usage) > 1:
                    continue
                demand_options.append((candidate, tuple(next_usage)))
            if not demand_options:
                return
            if feasible is None or len(demand_options) < len(feasible):
                selected, feasible = demand, demand_options

        assert selected is not None and feasible is not None
        next_remaining = tuple(demand for demand in remaining if demand != selected)
        for candidate, next_usage in feasible:
            path_excess, edge_mask, _, sequence = candidate
            chosen[selected] = sequence
            search(
                next_remaining,
                used_edges | edge_mask,
                next_usage,
                excess + path_excess,
                chosen,
            )
            del chosen[selected]

    search(tuple(candidates), 0, (0,) * len(graph), 0, {})
    return solutions


def validate_rotated_partition(graph: nx.Graph) -> None:
    bags = {
        "X": {"x", "h"},
        "e": {"e"},
        "a": {"a", "p_ac", "p_ad"},
        "b": {"b", "p_bd", "p_bc"},
        "c": {"c"},
        "d": {"d"},
        "f": {"f"},
        "g": {"g"},
    }
    assert set().union(*bags.values()) == set(graph)
    assert sum(map(len, bags.values())) == len(graph)
    assert all(nx.is_connected(graph.subgraph(bag)) for bag in bags.values())
    missing = set()
    for left, right in combinations(bags, 2):
        if not any(graph.has_edge(u, v) for u in bags[left] for v in bags[right]):
            missing.add(frozenset((left, right)))
    assert missing == {
        frozenset(("a", "b")),
        frozenset(("c", "d")),
        frozenset(("f", "g")),
    }


def collision_signature(
    graph: nx.Graph,
    routes: dict[tuple[str, str], tuple[str, ...]],
) -> tuple[str, tuple[str, str]]:
    usage: dict[str, list[str]] = {vertex: [] for vertex in graph}
    for demand, path in routes.items():
        for vertex in path[1:-1]:
            usage[vertex].append("".join(demand))
    collisions = {vertex: demands for vertex, demands in usage.items() if len(demands) == 2}
    assert len(collisions) == 1
    vertex, demands = next(iter(collisions.items()))
    return vertex, tuple(sorted(demands))


def main() -> None:
    graph = build_host()
    assert nx.node_connectivity(graph) == 3
    assert spanning_k7_model(graph) is None

    collision, collision_demands, length = validate_atomic_immersion(
        graph, CORE_BRANCHES, original_routes()
    )
    assert (collision, collision_demands, length) == ("x", ("ab", "cd"), 28)
    validate_rotated_partition(graph)

    edge_index = {
        edge: position
        for position, edge in enumerate(
            sorted(tuple(sorted((u, v))) for u, v in graph.edges)
        )
    }
    vertex_index = {vertex: position for position, vertex in enumerate(graph)}

    shorter: list[tuple[str, ...]] = []
    supporting: list[
        tuple[
            tuple[str, ...],
            dict[tuple[str, str], tuple[Path, ...]],
        ]
    ] = []
    branch_set_count = 0
    for branches in combinations(tuple(graph), 7):
        branch_set_count += 1
        candidates = candidates_for_branches(graph, branches, edge_index, vertex_index)
        if find_atomic_routes(graph, candidates, vertex_index, 6) is not None:
            shorter.append(branches)
        if find_atomic_routes(graph, candidates, vertex_index, 7) is not None:
            supporting.append((branches, candidates))

    assert branch_set_count == 1716
    assert shorter == []
    assert [branches for branches, _ in supporting] == [CORE_BRANCHES]
    all_solutions = all_atomic_routes(graph, supporting[0][1], vertex_index, 7)
    assert len(all_solutions) == 1
    expected_routes = {
        tuple(sorted(demand)): route for demand, route in original_routes().items()
    }
    assert all_solutions[0] == expected_routes
    assert collision_signature(graph, all_solutions[0]) == ("x", ("ab", "cd"))

    collision_f_branches = tuple("abcdegx")
    collision_g_branches = tuple("abcdefx")
    assert collision_f_branches not in [branches for branches, _ in supporting]
    assert collision_g_branches not in [branches for branches, _ in supporting]

    print("GREEN atomic shared-hub defect-rotation barrier")
    print("host: vertices=13 edges=34 connectivity=3 K7_minor=no")
    print("original: potential=(1,0,0,28) collision=x demands=ab,cd")
    print("rotated_partition: defects=ab,cd,fg bag_X={x,h}")
    print("atomic_search: branch_sets=1716 L<=27=0 L=28=1")
    print("minimum_witness: branches=abcdefg collision=x demands=ab,cd")
    print("rotated_strong_lifts: collision_f=no collision_g=no")


if __name__ == "__main__":
    main()
