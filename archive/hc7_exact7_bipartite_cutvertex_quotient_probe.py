"""Search literal seven-bag models in the bipartite cutvertex quotient.

The quotient has two rich full packets P,Q; two thin lobes A,B with defects
{a},{b}; their cutvertex z; and the seven literal boundary vertices.  It
enumerates five core-derived bags plus two literal boundary singleton bags.
This restricted search is complete only for that displayed bag form.
"""

from __future__ import annotations

import itertools

import networkx as nx


S = tuple(range(7))
CORES = ("P", "Q", "A", "B", "z")


def quotient(h: nx.Graph, a: int, b: int, z_contacts: set[int]) -> nx.Graph:
    g = h.copy()
    g.add_nodes_from(CORES)
    g.add_edges_from((("A", "z"), ("B", "z")))
    g.add_edges_from(("A", s) for s in S if s != a)
    g.add_edges_from(("B", s) for s in S if s != b)
    g.add_edges_from(("z", s) for s in z_contacts)
    g.add_edges_from((p, s) for p in ("P", "Q") for s in S)
    return g


def adjacent(g: nx.Graph, x: set, y: set) -> bool:
    return any(g.has_edge(a, b) for a in x for b in y)


def five_core_two_singletons(g: nx.Graph):
    for u, v in itertools.combinations(S, 2):
        if not g.has_edge(u, v):
            continue
        remaining = [x for x in S if x not in (u, v)]
        # Each remaining literal vertex is unused or assigned to one core.
        for assignment in itertools.product(range(6), repeat=len(remaining)):
            bags = [{c} for c in CORES] + [{u}, {v}]
            for x, owner in zip(remaining, assignment):
                if owner < 5:
                    bags[owner].add(x)
            if not all(nx.is_connected(g.subgraph(b)) for b in bags):
                continue
            if all(adjacent(g, bags[i], bags[j]) for i in range(7) for j in range(i + 1, 7)):
                return bags
    return None


def run_instance(name: str, h: nx.Graph, sides, pairs):
    print("BOUNDARY", name)
    for a, b in pairs:
        rem = sorted(set(S) - {a, b})
        failures = []
        for mask in range(1 << len(rem)):
            zc = {x for k, x in enumerate(rem) if mask >> k & 1}
            bags = five_core_two_singletons(quotient(h, a, b, zc))
            if bags is None:
                failures.append(tuple(sorted(zc)))
        print("defects", (a, b), "failed_z_contacts", failures)


def main():
    c6i = nx.Graph()
    c6i.add_nodes_from(S)
    c6i.add_edges_from((x, (x + 1) % 6) for x in range(6))
    run_instance("C6+I", c6i, None, [(0, 2), (0, 4)])

    c4k2i = nx.Graph()
    c4k2i.add_nodes_from(S)
    c4k2i.add_edges_from(((2, 3), (3, 6), (6, 5), (5, 2), (1, 4)))
    run_instance("C4+K2+I", c4k2i, None, [(2, 6), (3, 5)])


if __name__ == "__main__":
    main()
