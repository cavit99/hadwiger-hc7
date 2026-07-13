#!/usr/bin/env python3
"""Superseded discovery probe for the triangular Moser shore.

This expensive search was replaced by the exact dependency-free certificate
in active/hc7_exact7_moser_triangle_shore_verify.py.  It remains a discovery
aid, not a proof certificate.  It checks every boundary
defect triple compatible with the immediate seven-connectivity inequalities
in the compressed host containing the two crossed Moser paths.
"""

from itertools import combinations, combinations_with_replacement

import networkx as nx

from hc7_exact7_double_triangle_four_carrier_probe import has_k7_minor


S = set(range(7))
M_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}


def host(defects: tuple[frozenset[int], ...]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(13))
    graph.add_edges_from(M_EDGES)
    v, p05, p24 = 7, 8, 9
    graph.add_edges_from((v, s) for s in S)
    graph.add_edges_from(((0, p05), (p05, 5), (2, p24), (p24, 4)))
    graph.add_edges_from(((10, 11), (11, 12), (12, 10)))
    for vertex, defect in zip((10, 11, 12), defects):
        graph.add_edges_from((vertex, s) for s in S - set(defect))
    return graph


def main() -> None:
    defect_sets = [
        frozenset(choice)
        for size in range(3)
        for choice in combinations(S, size)
    ]
    tested = 0
    failures = []
    for defects in combinations_with_replacement(defect_sets, 3):
        # Full attachment of the triangular component.
        if set.intersection(*(set(defect) for defect in defects)):
            continue
        # Every two-vertex side has only the third triangle vertex outside,
        # so seven-connectivity forces at least six boundary contacts.
        if any(
            len(defects[i] & defects[j]) > 1
            for i, j in combinations(range(3), 2)
        ):
            continue
        tested += 1
        if not has_k7_minor(host(defects)):
            failures.append(defects)
            print("FAIL", defects)
    print(f"tested={tested} failures={len(failures)}")


if __name__ == "__main__":
    main()
