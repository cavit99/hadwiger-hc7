"""Exhaustive small-graph falsifier for the set-root rural-order theorem.

Checks every graph in NetworkX's graph atlas with at most seven vertices,
every assignment of its vertices to four nonempty pairwise-disjoint terminal
sets A,B,P,Q (or to no terminal set), and every 4-connected instance.

For a no-linkage instance it verifies planarity and a facial cyclic block
order A,Q,P,B up to reflection.  This is a falsifier, not a proof.
"""

from __future__ import annotations

from itertools import product

import networkx as nx


LABELS = (1, 2, 3, 4)  # A, B, P, Q
TARGET = (1, 4, 3, 2)  # A, Q, P, B


def has_two_linkage(
    graph: nx.Graph,
    a_set: set[int],
    b_set: set[int],
    p_set: set[int],
    q_set: set[int],
) -> bool:
    """Return whether disjoint A-P and B-Q paths exist."""
    for a in a_set:
        for p in p_set:
            for path in nx.all_simple_paths(graph, a, p):
                remaining = set(graph) - set(path)
                b_remaining = b_set & remaining
                q_remaining = q_set & remaining
                if not b_remaining or not q_remaining:
                    continue
                subgraph = graph.subgraph(remaining)
                for component in nx.connected_components(subgraph):
                    if component & b_remaining and component & q_remaining:
                        return True
    return False


def rotations(sequence: tuple[int, ...]):
    for index in range(len(sequence)):
        yield sequence[index:] + sequence[:index]


def has_target_block_order(face: list[int], assignment: tuple[int, ...]) -> bool:
    labelled = [assignment[vertex] for vertex in face if assignment[vertex]]
    if not labelled:
        return False
    runs: list[int] = []
    for label in labelled:
        if not runs or runs[-1] != label:
            runs.append(label)
    if len(runs) > 1 and runs[0] == runs[-1]:
        runs.pop()
    compressed = tuple(runs)
    return TARGET in set(rotations(compressed)) or TARGET[::-1] in set(
        rotations(compressed)
    )


def facial_block_order(
    graph: nx.Graph, embedding: nx.PlanarEmbedding, assignment: tuple[int, ...]
) -> bool:
    required = {vertex for vertex, label in enumerate(assignment) if label}
    seen: set[tuple[int, int]] = set()
    for u, v in embedding.edges():
        if (u, v) in seen:
            continue
        face = embedding.traverse_face(u, v, seen)
        if required <= set(face) and has_target_block_order(face, assignment):
            return True
    return False


def main() -> None:
    graphs_checked = 0
    assignments_checked = 0
    no_linkage_checked = 0
    for original in nx.graph_atlas_g():
        if len(original) < 5 or len(original) > 7 or not nx.is_connected(original):
            continue
        graph = nx.convert_node_labels_to_integers(original)
        if nx.node_connectivity(graph) < 4:
            continue
        graphs_checked += 1
        planar, embedding = nx.check_planarity(graph)
        for assignment in product(range(5), repeat=len(graph)):
            if any(label not in assignment for label in LABELS):
                continue
            assignments_checked += 1
            sets = {
                label: {vertex for vertex, value in enumerate(assignment) if value == label}
                for label in LABELS
            }
            if has_two_linkage(graph, sets[1], sets[2], sets[3], sets[4]):
                continue
            no_linkage_checked += 1
            if not planar or not facial_block_order(graph, embedding, assignment):
                raise AssertionError(
                    "counterexample",
                    nx.to_graph6_bytes(graph, header=False).decode().strip(),
                    assignment,
                    planar,
                )
    print(
        "GREEN:",
        graphs_checked,
        "4-connected atlas graphs;",
        assignments_checked,
        "terminal assignments;",
        no_linkage_checked,
        "no-linkage instances",
    )

    # Two known sharp four-connected rural obstructions lie just beyond
    # the atlas range.  They must be no-linkage and must realize the
    # asserted four-block order.
    sharp_cases = [
        ("GQyurg", ({0}, {5}, {3}, {6})),
        ("HCZTfP}", ({0}, {7}, {1}, {5})),
    ]
    for graph6, (a_set, b_set, p_set, q_set) in sharp_cases:
        graph = nx.from_graph6_bytes(graph6.encode())
        planar, embedding = nx.check_planarity(graph)
        assignment = tuple(
            1
            if vertex in a_set
            else 2
            if vertex in b_set
            else 3
            if vertex in p_set
            else 4
            if vertex in q_set
            else 0
            for vertex in range(len(graph))
        )
        assert nx.node_connectivity(graph) >= 4
        assert not has_two_linkage(graph, a_set, b_set, p_set, q_set)
        assert planar and facial_block_order(graph, embedding, assignment)
    print("GREEN: sharp square-antiprism and double-book rural orders")


if __name__ == "__main__":
    main()
