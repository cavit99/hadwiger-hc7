#!/usr/bin/env python3
"""Search exact maximal C6 two-cut states on small two-sum hosts.

The cut is {p,q}.  In the canonical maximal opposite-visible state the
left interior misses portal labels {1,4}, the right interior misses
{0,3}, and p,q may carry only {2,5}.  Every permitted interior label is
required to occur.  The formula then asks for

* an SDR for the six portal classes;
* absence of all three antipodal demand linkages; and
* two owned opposite frame pairs.

Portal classes are arbitrary sets, not selected singleton roots.  Connected
carriers are encoded exactly by enumerating all connected vertex masks.
"""

from __future__ import annotations

import itertools
import subprocess

import networkx as nx


def disjunction(parts: list[str]) -> str:
    if not parts:
        return "false"
    if len(parts) == 1:
        return parts[0]
    return f"(or {' '.join(parts)})"


def conjunction(parts: list[str]) -> str:
    if not parts:
        return "true"
    if len(parts) == 1:
        return parts[0]
    return f"(and {' '.join(parts)})"


def two_sum(first: nx.Graph, second: nx.Graph) -> tuple[nx.Graph, set[int], set[int]]:
    """Glue endpoints 0,1 of two rooted torsos and delete the virtual edge."""
    assert first.has_edge(0, 1) and second.has_edge(0, 1)
    graph = nx.Graph()
    left_map = {0: 0, 1: 1}
    right_map = {0: 0, 1: 1}
    next_vertex = 2
    for vertex in range(2, len(first)):
        left_map[vertex] = next_vertex
        next_vertex += 1
    for vertex in range(2, len(second)):
        right_map[vertex] = next_vertex
        next_vertex += 1
    for source, mapping in ((first, left_map), (second, right_map)):
        graph.add_edges_from((mapping[u], mapping[v]) for u, v in source.edges)
    graph.remove_edge(0, 1)
    left = set(left_map.values()) - {0, 1}
    right = set(right_map.values()) - {0, 1}
    return graph, left, right


def rooted(graph: nx.Graph, edge: tuple[int, int]) -> nx.Graph:
    """Relabel an edge to the distinguished virtual edge 0--1."""
    u, v = edge
    others = [x for x in graph if x not in edge]
    mapping = {u: 0, v: 1}
    mapping.update({x: index + 2 for index, x in enumerate(others)})
    return nx.relabel_nodes(graph, mapping, copy=True)


def torso_families() -> list[tuple[str, nx.Graph]]:
    sources: list[tuple[str, nx.Graph]] = []
    for order in range(4, 9):
        sources.append((f"K{order}", nx.complete_graph(order)))
    for order in range(5, 10):
        sources.append((f"W{order}", nx.wheel_graph(order)))
    sources.extend(
        (
            ("prism", nx.circular_ladder_graph(3)),
            ("cube", nx.cubical_graph()),
            ("octa", nx.octahedral_graph()),
        )
    )
    answer: list[tuple[str, nx.Graph]] = []
    for name, graph in sources:
        # Keep one representative of every edge orbit detected by rooted
        # isomorphism.  The small family makes the quadratic test harmless.
        representatives: list[nx.Graph] = []
        for edge in graph.edges:
            candidate = rooted(nx.convert_node_labels_to_integers(graph), edge)
            decorated = candidate.copy()
            decorated.nodes[0]["root"] = "p"
            decorated.nodes[1]["root"] = "q"
            for vertex in range(2, len(decorated)):
                decorated.nodes[vertex]["root"] = "x"
            if any(
                nx.is_isomorphic(
                    decorated,
                    old,
                    node_match=lambda a, b: a["root"] == b["root"],
                )
                for old in representatives
            ):
                continue
            representatives.append(decorated)
            answer.append((f"{name}:e{edge[0]}-{edge[1]}", candidate))
    return answer


class Encoding:
    def __init__(self, host: nx.Graph, left: set[int], right: set[int]) -> None:
        self.host = host
        self.vertices = tuple(range(len(host)))
        self.order = len(host)
        self.left = left
        self.right = right
        self.connected_masks = tuple(
            mask
            for mask in range(1, 1 << self.order)
            if nx.is_connected(
                host.subgraph(i for i in self.vertices if mask >> i & 1)
            )
        )
        self.disjoint_pairs = tuple(
            (first, second)
            for first in self.connected_masks
            for second in self.connected_masks
            if not first & second
        )

    def meets_fixed_mask(self, label: int, mask: int) -> str:
        return disjunction(
            [f"p_{label}_{vertex}" for vertex in self.vertices if mask >> vertex & 1]
        )

    def carries_fixed(self, edge: tuple[int, int], mask: int) -> str:
        return conjunction(
            [self.meets_fixed_mask(edge[0], mask),
             self.meets_fixed_mask(edge[1], mask)]
        )

    def formula(self, owned_pairs: tuple[int, int]) -> str:
        n = self.order
        lines = ["(set-logic QF_BV)"]
        for label in range(6):
            for vertex in self.vertices:
                lines.append(f"(declare-fun p_{label}_{vertex} () Bool)")
            lines.append(f"(declare-fun r_{label} () (_ BitVec {n}))")
            # Representative is a singleton bit and lies in its portal set.
            singleton_terms = []
            for vertex in self.vertices:
                bit = 1 << vertex
                singleton_terms.append(
                    f"(and (= r_{label} (_ bv{bit} {n})) p_{label}_{vertex})"
                )
            lines.append(f"(assert {disjunction(singleton_terms)})")
        for first, second in itertools.combinations(range(6), 2):
            lines.append(
                f"(assert (= (bvand r_{first} r_{second}) (_ bv0 {n})))"
            )

        # Canonical maximal defect placement.
        left_allowed = {0, 2, 3, 5}
        right_allowed = {1, 2, 4, 5}
        cut_allowed = {2, 5}
        for label in range(6):
            for vertex in self.vertices:
                allowed = (
                    (vertex in self.left and label in left_allowed)
                    or (vertex in self.right and label in right_allowed)
                    or (vertex in {0, 1} and label in cut_allowed)
                )
                if not allowed:
                    lines.append(f"(assert (not p_{label}_{vertex}))")
        for label in left_allowed:
            lines.append(
                f"(assert {disjunction([f'p_{label}_{v}' for v in sorted(self.left)])})"
            )
        for label in right_allowed:
            lines.append(
                f"(assert {disjunction([f'p_{label}_{v}' for v in sorted(self.right)])})"
            )

        # All three antipodal demand pairs are absent.
        for index in range(3):
            first_edge = (index, (index + 1) % 6)
            second_edge = ((index + 3) % 6, (index + 4) % 6)
            for first, second in self.disjoint_pairs:
                lines.append(
                    "(assert (not "
                    + conjunction(
                        [self.carries_fixed(first_edge, first),
                         self.carries_fixed(second_edge, second)]
                    )
                    + "))"
                )

        # Existential exact connected carriers for the four owned frames.
        for frame in tuple(x for pair in owned_pairs for x in (pair, pair + 3)):
            for side in range(2):
                lines.append(f"(declare-fun m_{frame}_{side} () (_ BitVec {n}))")
                lines.append(
                    "(assert "
                    + disjunction(
                        [f"(= m_{frame}_{side} (_ bv{mask} {n}))"
                         for mask in self.connected_masks]
                    )
                    + ")"
                )
            lines.append(
                f"(assert (= (bvand m_{frame}_0 m_{frame}_1) (_ bv0 {n})))"
            )
            first_edge = ((frame - 2) % 6, (frame - 1) % 6)
            second_edge = ((frame + 2) % 6, (frame + 3) % 6)
            for side, edge in enumerate((first_edge, second_edge)):
                for label in edge:
                    lines.append(
                        "(assert "
                        + disjunction(
                            [
                                f"(and (= ((_ extract {vertex} {vertex}) "
                                f"m_{frame}_{side}) #b1) p_{label}_{vertex})"
                                for vertex in self.vertices
                            ]
                        )
                        + ")"
                    )
        lines.extend(("(check-sat)", "(get-model)"))
        return "\n".join(lines)


def solve(formula: str, timeout: int = 60) -> tuple[str, str]:
    result = subprocess.run(
        ("z3", "-in", f"-T:{timeout}"),
        input=formula,
        text=True,
        capture_output=True,
        timeout=timeout + 5,
    )
    output = result.stdout.strip()
    status = output.splitlines()[0] if output else "error"
    return status, output


def main() -> None:
    families = torso_families()
    print("rooted torsos", len(families), flush=True)
    tested = 0
    for (left_name, left_torso), (right_name, right_torso) in itertools.combinations_with_replacement(families, 2):
        host, left, right = two_sum(left_torso, right_torso)
        if len(host) > 12:
            continue
        encoding = Encoding(host, left, right)
        for owned in itertools.combinations(range(3), 2):
            tested += 1
            status, output = solve(encoding.formula(owned))
            if status == "sat":
                print("SAT", left_name, right_name, "n", len(host), "owned", owned)
                print("edges", sorted(host.edges))
                print(output)
                return
            if status not in {"unsat"}:
                print("INDETERMINATE", left_name, right_name, len(host), owned, status)
                return
        print("UNSAT_HOST", left_name, right_name, "n", len(host), flush=True)
    print("NO_SAT", tested)


if __name__ == "__main__":
    main()
