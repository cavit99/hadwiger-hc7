"""Verify a 7-connected Dirac-valid barrier to the raw carrier theorem.

This construction is deliberately *not* K7-minor-free or contraction-
critical.  Its purpose is to show that seven-connectivity, packet vector
(1,2), a bipartite seven-boundary, and all literal Dirac neighbourhood
inequalities do not by themselves force the two bipartition carriers.
"""

from __future__ import annotations

import itertools

import networkx as nx


S = tuple(("s", i) for i in range(7))
COMMON = {0, 1, 2}
UNIQUE = (4, 3, 6, 5)  # I,J,I,J in this cyclic order.


def alpha(g: nx.Graph) -> int:
    return max((len(c) for c in nx.find_cliques(nx.complement(g))), default=0)


def connected_subsets(g: nx.Graph, vertices):
    vertices = tuple(vertices)
    for mask in range(1, 1 << len(vertices)):
        x = frozenset(vertices[k] for k in range(len(vertices)) if mask >> k & 1)
        if nx.is_connected(g.subgraph(x)):
            yield x


def packet_number(g: nx.Graph, shore, boundary) -> int:
    packets = [
        x
        for x in connected_subsets(g, shore)
        if all(any(g.has_edge(v, s) for v in x) for s in boundary)
    ]

    def search(start, used):
        best = 0
        for k in range(start, len(packets)):
            if not packets[k] & used:
                best = max(best, 1 + search(k + 1, used | packets[k]))
        return best

    return search(0, frozenset())


def build():
    g = nx.Graph()
    g.add_nodes_from(S)
    g.add_edges_from((S[i], S[i + 1]) for i in range(6))  # H=P7.

    ico = nx.icosahedral_graph()
    deleted = 0
    outer = list(ico.neighbors(deleted))
    outer_graph = ico.subgraph(outer)
    cycle = nx.cycle_basis(outer_graph)[0]
    assert len(cycle) == 5
    ico.remove_node(deleted)
    lmap = {x: ("l", x) for x in ico}
    l = {lmap[x] for x in ico}
    g.add_nodes_from(l)
    g.add_edges_from((lmap[x], lmap[y]) for x, y in ico.edges())

    # Every thin-shore vertex sees three common labels.  Four vertices in
    # alternating order on the unique outer face carry the four remaining
    # labels; the fifth outer vertex carries no unique label.
    for x in ico:
        g.add_edges_from((lmap[x], S[s]) for s in COMMON)
    for x, s in zip(cycle[:4], UNIQUE):
        g.add_edge(lmap[x], S[s])

    # A rich shore with exact packet number two.  The two distinguished
    # vertices see all S.  Every other rich vertex misses s0, so a third
    # disjoint full packet is impossible.
    r = {("r", k) for k in range(6)}
    g.add_nodes_from(r)
    g.add_edges_from(itertools.combinations(r, 2))
    for k in range(6):
        contacts = range(7) if k < 2 else range(1, 7)
        g.add_edges_from((("r", k), S[s]) for s in contacts)

    return g, l, r, cycle, lmap


def main():
    g, l, r, cycle, lmap = build()
    i_side = {S[s] for s in (0, 2, 4, 6)}
    j_side = {S[s] for s in (1, 3, 5)}

    assert nx.node_connectivity(g) == 7
    assert packet_number(g, l, S) == 1
    assert packet_number(g, r, S) == 2

    # Check the contraction-critical Dirac inequality numerically at every
    # literal vertex, although the graph itself is not contraction-critical.
    for x in g:
        ngh = g.subgraph(g[x])
        assert alpha(ngh) <= g.degree(x) - 5, (
            x,
            alpha(ngh),
            g.degree(x) - 5,
        )

    carriers_i = [
        x
        for x in connected_subsets(g, l)
        if all(any(g.has_edge(v, s) for v in x) for s in i_side)
    ]
    carriers_j = [
        x
        for x in connected_subsets(g, l)
        if all(any(g.has_edge(v, s) for v in x) for s in j_side)
    ]
    assert not any(x.isdisjoint(y) for x in carriers_i for y in carriers_j)

    # The reason is literal: every I-carrier contains the two alternating
    # I portals and every J-carrier the two alternating J portals.  Planarity
    # of the punctured icosahedron forbids the two disjoint connections.
    portal_order = [(lmap[cycle[k]], UNIQUE[k]) for k in range(4)]
    print("VERIFIED")
    print("vertices", len(g), "edges", g.number_of_edges())
    print("node_connectivity", nx.node_connectivity(g))
    print("packet_vector", (packet_number(g, l, S), packet_number(g, r, S)))
    print("portal_order", portal_order)
    print("I_carriers", len(carriers_i), "J_carriers", len(carriers_j))


if __name__ == "__main__":
    main()
