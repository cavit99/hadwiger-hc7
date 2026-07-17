"""Search the exact order-16 residue of the adjacent-pair principle.

Jorgensen's equality classification and Mader's edge bound imply that an
8-connected K7-minor-free graph of order 16 must be 8-regular.  For every
edge xy, K7-minor-freeness of G/xy first implies that xy lies in at least
three triangles.  Equality would make G/xy extremal; Jorgensen's equality
classification then contradicts 8-regularity of G.  Hence every edge lies
in at least four triangles.  In the 7-regular complement H this says that
every nonedge has at least four common neighbours.

This script searches those necessary complement graphs.  Whenever it finds
one, a second solver produces an explicit K7-minor certificate in G.  The
certificate is reduced to branch-set spanning-tree edges plus one edge for
each pair of branch sets and is added as a blocking clause.  UNSAT would
therefore certify that no graph in the necessary order-16 residue is
K7-minor-free, modulo trust in Z3's result.  SAT candidates are printed with
an exact adjacency list for independent checking.

This is a falsifier / finite experiment, not yet a promoted theorem.
"""

from __future__ import annotations

import argparse
import time

import networkx as nx
import z3


ORDER = 16
TARGET = 7


def graph_variables() -> tuple[z3.Solver, dict[tuple[int, int], z3.BoolRef]]:
    edge = {
        (left, right): z3.Bool(f"h_{left}_{right}")
        for left in range(ORDER)
        for right in range(left + 1, ORDER)
    }

    def adjacent(left: int, right: int) -> z3.BoolRef:
        assert left != right
        return edge[min(left, right), max(left, right)]

    solver = z3.Solver()
    for vertex in range(ORDER):
        solver.add(
            z3.PbEq(
                [
                    (adjacent(vertex, other), 1)
                    for other in range(ORDER)
                    if other != vertex
                ],
                7,
            )
        )

    # Every 7-regular graph can be relabelled this way.
    for other in range(1, ORDER):
        solver.add(adjacent(0, other) == (other <= 7))

    # If uv is an edge of G, then G/uv has 63-t(uv) edges.  Mader's
    # order-15 bound forces t(uv)>=3.  Complementing translates this into
    # the following common-neighbour condition in H.
    for left in range(ORDER):
        for right in range(left + 1, ORDER):
            common = [
                z3.And(adjacent(left, third), adjacent(right, third))
                for third in range(ORDER)
                if third not in (left, right)
            ]
            solver.add(
                z3.Implies(
                    z3.Not(adjacent(left, right)),
                    z3.PbGe([(term, 1) for term in common], 4),
                )
            )
    return solver, edge


def extract_graph(
    model: z3.ModelRef, edge: dict[tuple[int, int], z3.BoolRef]
) -> nx.Graph:
    complement = nx.Graph()
    complement.add_nodes_from(range(ORDER))
    complement.add_edges_from(
        pair for pair, variable in edge.items() if z3.is_true(model.eval(variable))
    )
    return nx.complement(complement)


def clique_minor_model(graph: nx.Graph) -> list[list[int]] | None:
    vertices = tuple(graph)
    solver = z3.Solver()
    label = {vertex: z3.Int(f"label_{vertex}") for vertex in vertices}
    depth = {vertex: z3.Int(f"depth_{vertex}") for vertex in vertices}
    root = {
        (vertex, branch): z3.Bool(f"root_{vertex}_{branch}")
        for vertex in vertices
        for branch in range(TARGET)
    }

    for vertex in vertices:
        # Every candidate graph in the target class is connected, and any
        # clique-minor model in a connected graph can absorb all unused
        # components.  Requiring a spanning model makes the subsequent
        # partition blocker exact rather than certificate-specific.
        solver.add(0 <= label[vertex], label[vertex] < TARGET)
        solver.add(0 <= depth[vertex], depth[vertex] < ORDER)

    for branch in range(TARGET):
        solver.add(z3.PbEq([(root[vertex, branch], 1) for vertex in vertices], 1))
        for vertex in vertices:
            solver.add(
                z3.Implies(
                    root[vertex, branch],
                    z3.And(label[vertex] == branch, depth[vertex] == 0),
                )
            )
            predecessors = [
                z3.And(
                    label[neighbour] == branch,
                    depth[neighbour] < depth[vertex],
                )
                for neighbour in graph[vertex]
            ]
            solver.add(
                z3.Implies(
                    z3.And(
                        label[vertex] == branch,
                        z3.Not(root[vertex, branch]),
                    ),
                    z3.And(depth[vertex] > 0, z3.Or(*predecessors)),
                )
            )

    for left in range(TARGET):
        for right in range(left + 1, TARGET):
            solver.add(
                z3.Or(
                    *(
                        z3.Or(
                            z3.And(label[x] == left, label[y] == right),
                            z3.And(label[x] == right, label[y] == left),
                        )
                        for x, y in graph.edges()
                    )
                )
            )

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return [
        [
            vertex
            for vertex in vertices
            if model.eval(label[vertex]).as_long() == branch
        ]
        for branch in range(TARGET)
    ]


def certificate_edges(graph: nx.Graph, branches: list[list[int]]) -> set[tuple[int, int]]:
    certificate: set[tuple[int, int]] = set()
    for branch in branches:
        tree = nx.minimum_spanning_tree(graph.subgraph(branch))
        certificate.update(tuple(sorted(pair)) for pair in tree.edges())
    for left in range(TARGET):
        for right in range(left + 1, TARGET):
            certificate.add(
                next(
                    tuple(sorted((x, y)))
                    for x in branches[left]
                    for y in branches[right]
                    if graph.has_edge(x, y)
                )
            )
    return certificate


def partition_model_blocker(
    branches: list[list[int]],
    complement_edge: dict[tuple[int, int], z3.BoolRef],
) -> z3.BoolRef:
    """Return the exact assertion that this branch partition is not a model.

    An H-edge is a missing G-edge.  The partition fails precisely when two
    branch sets are anticomplete in G or one branch set has a cut with no
    G-edge across it.
    """

    def h_edge(left: int, right: int) -> z3.BoolRef:
        assert left != right
        return complement_edge[min(left, right), max(left, right)]

    failures: list[z3.BoolRef] = []
    for left in range(TARGET):
        for right in range(left + 1, TARGET):
            failures.append(
                z3.And(
                    *(
                        h_edge(x, y)
                        for x in branches[left]
                        for y in branches[right]
                    )
                )
            )

    for branch in branches:
        anchor = branch[0]
        others = branch[1:]
        for mask in range(1 << len(others)):
            first = {anchor}
            first.update(
                vertex
                for index, vertex in enumerate(others)
                if mask >> index & 1
            )
            second = set(branch) - first
            if not second:
                continue
            failures.append(
                z3.And(*(h_edge(x, y) for x in first for y in second))
            )
    return z3.Or(*failures)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5_000)
    parser.add_argument("--progress", type=int, default=100)
    args = parser.parse_args()

    solver, complement_edge = graph_variables()
    started = time.monotonic()
    for iteration in range(1, args.limit + 1):
        status = solver.check()
        if status == z3.unsat:
            print(f"UNSAT after {iteration - 1} K7 certificates")
            print(f"seconds {time.monotonic() - started:.3f}")
            return
        assert status == z3.sat
        graph = extract_graph(solver.model(), complement_edge)
        branches = clique_minor_model(graph)
        if branches is None:
            print("K7-MINOR-FREE CANDIDATE")
            print("connectivity", nx.node_connectivity(graph))
            print("edges", sorted(tuple(sorted(pair)) for pair in graph.edges()))
            return

        certificate = certificate_edges(graph, branches)
        solver.add(partition_model_blocker(branches, complement_edge))
        if iteration % args.progress == 0:
            print(
                "certificates",
                iteration,
                "seconds",
                f"{time.monotonic() - started:.3f}",
                flush=True,
            )

    print(f"LIMIT {args.limit}; no K7-minor-free candidate found")
    print(f"seconds {time.monotonic() - started:.3f}")


if __name__ == "__main__":
    main()
