"""Search the paired width-two frontier for a capacity-triangle allocation gap.

This is a discovery script, not a proof certificate.  It enumerates every
labelled paired boundary in the three structural forms from the audited
width-two frontier, every dutyless four-support A, every second four-support
C, and every exceptional gate support Z which makes A,C,Z a capacity
triangle.  It tests the adaptive clique-reservoir two-carrier criterion for
both allocations of Z.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


S = tuple(range(7))
CENTRE = 0
PAIRS = ((1, 2), (3, 4), (5, 6))
ALL_EDGES = tuple(combinations(S, 2))
ALLOWED_EDGES = tuple(e for e in ALL_EDGES if e not in PAIRS)


def paired_boundary(g: nx.Graph) -> bool:
    if any(g.has_edge(*pair) for pair in PAIRS):
        return False
    if any(not any(g.has_edge(CENTRE, x) for x in pair) for pair in PAIRS):
        return False
    for p, q in combinations(PAIRS, 2):
        if not any(g.has_edge(x, y) for x in p for y in q):
            return False
    return True


def frontier_form(g: nx.Graph) -> bool:
    if nx.is_connected(g):
        if g.number_of_edges() == 6:
            return nx.is_tree(g)
        if g.number_of_edges() != 7:
            return False
        cycles = nx.cycle_basis(g)
        return len(cycles) == 1 and len(cycles[0]) == 6

    components = [g.subgraph(c).copy() for c in nx.connected_components(g)]
    if sorted(map(len, components)) != [3, 4]:
        return False
    small = next(h for h in components if len(h) == 3)
    large = next(h for h in components if len(h) == 4)
    return nx.is_isomorphic(small, nx.complete_graph(3)) and nx.is_isomorphic(
        large, nx.star_graph(3)
    )


def cliques(g: nx.Graph):
    for mask in range(1 << 7):
        u = {v for v in S if mask & (1 << v)}
        if all(g.has_edge(x, y) for x, y in combinations(u, 2)):
            yield u


def allocation(g: nx.Graph, left: set[int], right: set[int]):
    for u in cliques(g):
        f = [v for v in S if v not in u]
        for mask in range(1 << len(f)):
            i = {f[j] for j in range(len(f)) if mask & (1 << j)}
            j = set(f) - i
            if not i or not j:
                continue
            if not i <= left or not j <= right:
                continue
            if any(g.has_edge(x, y) for x, y in combinations(i, 2)):
                continue
            if any(g.has_edge(x, y) for x, y in combinations(j, 2)):
                continue
            return u, i, j
    return None


def boundary_graphs():
    for mask in range(1 << len(ALLOWED_EDGES)):
        edge_count = mask.bit_count()
        if edge_count not in (6, 7):
            continue
        g = nx.Graph()
        g.add_nodes_from(S)
        g.add_edges_from(
            edge for bit, edge in enumerate(ALLOWED_EDGES) if mask & (1 << bit)
        )
        if paired_boundary(g) and frontier_form(g):
            yield g


def main() -> None:
    checked = 0
    graphs = 0
    found: set[str] = set()
    dutyless_supports = [
        {CENTRE, x, y, z}
        for x in PAIRS[0]
        for y in PAIRS[1]
        for z in PAIRS[2]
    ]
    four_sets = list(map(set, combinations(S, 4)))

    for g in boundary_graphs():
        graphs += 1
        if not nx.is_connected(g):
            form = "claw+triangle"
        elif g.number_of_edges() == 6:
            form = "tree"
        else:
            form = "six-cycle+pendant"
        for a in dutyless_supports:
            for c in four_sets:
                if a == c:
                    continue
                for gate_mask in range(1 << 7):
                    z = {v for v in S if gate_mask & (1 << v)}
                    if a | c | z != set(S):
                        continue
                    if len(a | z) < 5 or len(c | z) < 5:
                        continue
                    checked += 1
                    if allocation(g, a | z, c) is not None:
                        continue
                    if allocation(g, a, c | z) is not None:
                        continue
                    if form in found:
                        continue
                    found.add(form)
                    print("COUNTEREXAMPLE", form)
                    print("edges", sorted(map(tuple, g.edges())))
                    print("A", sorted(a), "C", sorted(c), "Z", sorted(z))
                    print("checked", checked, "graphs", graphs)
                    if len(found) == 3:
                        return

    print("SEARCH_COMPLETE", sorted(found))
    print("checked", checked, "graphs", graphs)


if __name__ == "__main__":
    main()
