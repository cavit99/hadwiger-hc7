#!/usr/bin/env python3
"""Search larger two-sum hosts for a simultaneous C6 portal state.

This is an exploratory exact SMT search.  Each host is obtained by gluing
two 3-connected planar graphs along an edge pq and deleting pq.  Portal
classes are arbitrary nonempty vertex subsets, constrained to have an SDR.
The exact connected-carrier definition is used for all linkage predicates.
"""

from __future__ import annotations

import itertools
import subprocess
from functools import lru_cache

import networkx as nx


def disj(parts: list[str]) -> str:
    if not parts:
        return "false"
    if len(parts) == 1:
        return parts[0]
    return f"(or {' '.join(parts)})"


def conj(parts: list[str]) -> str:
    if not parts:
        return "true"
    if len(parts) == 1:
        return parts[0]
    return f"(and {' '.join(parts)})"


def wheel_torso(order: int, tag: str) -> tuple[nx.Graph, str, str]:
    """A labelled wheel with a designated rim edge pq."""
    assert order >= 4
    graph = nx.Graph()
    p, q, hub = "p", "q", f"{tag}h"
    middle = [f"{tag}r{i}" for i in range(order - 3)]
    rim = [p, *middle, q]
    graph.add_edges_from(zip(rim, rim[1:]))
    graph.add_edge(q, p)
    graph.add_edges_from((hub, vertex) for vertex in rim)
    return graph, p, q


def prism_torso(tag: str) -> tuple[nx.Graph, str, str]:
    graph = nx.circular_ladder_graph(3)
    mapping = {vertex: f"{tag}{vertex}" for vertex in graph}
    graph = nx.relabel_nodes(graph, mapping)
    p, q = mapping[0], mapping[1]
    graph = nx.relabel_nodes(graph, {p: "p", q: "q"})
    return graph, "p", "q"


def complete_torso(order: int, tag: str) -> tuple[nx.Graph, str, str]:
    graph = nx.complete_graph(order)
    mapping = {0: "p", 1: "q", **{i: f"{tag}{i}" for i in range(2, order)}}
    return nx.relabel_nodes(graph, mapping), "p", "q"


def two_sum(first: nx.Graph, second: nx.Graph) -> nx.Graph:
    graph = nx.compose(first, second)
    graph.remove_edge("p", "q")
    assert nx.node_connectivity(graph) == 2
    return graph


class Encoding:
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.vertices = tuple(graph)
        self.order = len(self.vertices)
        self.connected = tuple(
            mask for mask in range(1, 1 << self.order)
            if nx.is_connected(graph.subgraph(
                self.vertices[i] for i in range(self.order) if mask >> i & 1
            ))
        )
        self.disjoint = tuple(
            (x, y) for x in self.connected for y in self.connected if not x & y
        )

    def meets(self, label: int, mask: int) -> str:
        return disj([f"x_{label}_{i}" for i in range(self.order) if mask >> i & 1])

    def carries(self, edge: tuple[int, int], mask: int) -> str:
        return conj([self.meets(edge[0], mask), self.meets(edge[1], mask)])

    def linkage(self, edge1: tuple[int, int], edge2: tuple[int, int]) -> str:
        return disj([
            conj([self.carries(edge1, x), self.carries(edge2, y)])
            for x, y in self.disjoint
        ])

    def formula(self, opposite_pairs: tuple[int, int], *,
                min_left_reps: int = 0, min_right_reps: int = 0) -> str:
        lines = ["(set-logic QF_LIA)"]
        for label in range(6):
            for i in range(self.order):
                lines.append(f"(declare-fun x_{label}_{i} () Bool)")
            lines.append(f"(declare-fun r_{label} () Int)")
            lines.append(f"(assert (and (<= 0 r_{label}) (< r_{label} {self.order})))")
            lines.append("(assert " + disj([
                f"(and (= r_{label} {i}) x_{label}_{i})" for i in range(self.order)
            ]) + ")")
        lines.append("(assert (distinct " + " ".join(f"r_{i}" for i in range(6)) + "))")
        for prefix, minimum in (("L", min_left_reps), ("R", min_right_reps)):
            indices = [i for i, vertex in enumerate(self.vertices)
                       if str(vertex).startswith(prefix)]
            if minimum:
                terms = [f"(ite {disj([f'(= r_{label} {i})' for i in indices])} 1 0)"
                         for label in range(6)]
                lines.append(f"(assert (>= (+ {' '.join(terms)}) {minimum}))")
        for i in range(3):
            lines.append("(assert (not " + self.linkage(
                (i, (i + 1) % 6), ((i + 3) % 6, (i + 4) % 6)
            ) + "))")
        for pair in opposite_pairs:
            for frame in (pair, pair + 3):
                lines.append("(assert " + self.linkage(
                    ((frame - 2) % 6, (frame - 1) % 6),
                    ((frame + 2) % 6, (frame + 3) % 6),
                ) + ")")
        lines.extend(("(check-sat)", "(get-model)"))
        return "\n".join(lines)


def solve(formula: str, timeout: int = 240) -> str:
    result = subprocess.run(
        ("z3", "-in"), input=formula, text=True, capture_output=True,
        timeout=timeout, check=False,
    )
    if result.stderr:
        print("z3 stderr", result.stderr, flush=True)
    return result.stdout


def main() -> None:
    torso_builders = []
    for order in range(4, 8):
        torso_builders.append((f"W{order}", lambda tag, n=order: wheel_torso(n, tag)))
    for order in range(4, 7):
        torso_builders.append((f"K{order}", lambda tag, n=order: complete_torso(n, tag)))
    torso_builders.append(("P6", prism_torso))

    for (name1, build1), (name2, build2) in itertools.combinations_with_replacement(torso_builders, 2):
        first, _, _ = build1("L")
        second, _, _ = build2("R")
        graph = two_sum(first, second)
        if len(graph) > 10:
            continue
        encoding = Encoding(graph)
        print(name1, name2, "order", len(graph), "connected", len(encoding.connected),
              "pairs", len(encoding.disjoint), flush=True)
        for owned in itertools.combinations(range(3), 2):
            output = solve(encoding.formula(owned, min_left_reps=2,
                                             min_right_reps=2))
            status = output.splitlines()[0]
            print(" ", owned, status, flush=True)
            if status == "sat":
                print(output)
                return


def singleton_linkage_table(graph: nx.Graph, vertices: tuple[str, ...]):
    """Exact two prescribed disjoint path table for four distinct roots."""
    connected = tuple(
        mask for mask in range(1, 1 << len(vertices))
        if nx.is_connected(graph.subgraph(
            vertices[i] for i in range(len(vertices)) if mask >> i & 1
        ))
    )
    carriers: dict[tuple[int, int], tuple[int, ...]] = {}
    for a, b in itertools.combinations(range(len(vertices)), 2):
        carriers[a, b] = tuple(
            mask for mask in connected if mask >> a & 1 and mask >> b & 1
        )

    @lru_cache(maxsize=None)
    def linked(a: int, b: int, c: int, d: int) -> bool:
        edge1 = tuple(sorted((a, b)))
        edge2 = tuple(sorted((c, d)))
        return any(not (x & y) for x in carriers[edge1] for y in carriers[edge2])

    return linked


def singleton_search() -> None:
    torso_builders = []
    for order in range(4, 9):
        torso_builders.append((f"W{order}", lambda tag, n=order: wheel_torso(n, tag)))
    for order in range(4, 8):
        torso_builders.append((f"K{order}", lambda tag, n=order: complete_torso(n, tag)))
    torso_builders.append(("P6", prism_torso))
    for (name1, build1), (name2, build2) in itertools.combinations_with_replacement(torso_builders, 2):
        first, _, _ = build1("L")
        second, _, _ = build2("R")
        graph = two_sum(first, second)
        if len(graph) > 11:
            continue
        vertices = tuple(graph)
        left = {i for i, vertex in enumerate(vertices) if vertex.startswith("L")}
        right = {i for i, vertex in enumerate(vertices) if vertex.startswith("R")}
        linked = singleton_linkage_table(graph, vertices)
        print("singleton", name1, name2, len(graph), len(left), len(right), flush=True)
        for roots in itertools.permutations(range(len(vertices)), 6):
            # Demand e_i joins roots i,i+1.
            if any(linked(roots[i], roots[(i + 1) % 6],
                          roots[(i + 3) % 6], roots[(i + 4) % 6])
                   for i in range(3)):
                continue
            frames = []
            for frame in range(6):
                frames.append(linked(
                    roots[(frame - 2) % 6], roots[(frame - 1) % 6],
                    roots[(frame + 2) % 6], roots[(frame + 3) % 6],
                ))
            owned = [i for i in range(3) if frames[i] and frames[i + 3]]
            if len(owned) < 2:
                continue
            left_count = sum(root in left for root in roots)
            right_count = sum(root in right for root in roots)
            if left_count < 2 or right_count < 2:
                continue
            print("SINGLETON SAT", name1, name2,
                  "roots", tuple(vertices[i] for i in roots),
                  "frames", frames, "interior counts", left_count, right_count)
            return
    print("no singleton survivor")


if __name__ == "__main__":
    import sys
    if "--singleton" in sys.argv:
        singleton_search()
    else:
        main()
