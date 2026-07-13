"""Boundary probe for the sole cutvertex residue in the bipartite (1,2) cell.

The two components of L-z have literal boundary defects {a} and {b}, with
a,b distinct and in one bipartition class, while z contacts neither.  After
putting z into the first component, the resulting carriers are adjacent and
have contact sets S-{a}, S-{b}.  This probe asks whether Lemma 3.1 of the
audited thin-shore exchange always supplies an admissible exact state.
"""

from __future__ import annotations

import itertools

import networkx as nx


S = frozenset(range(7))


def independent(h: nx.Graph, x: frozenset[int]) -> bool:
    return h.subgraph(x).number_of_edges() == 0


def clique(h: nx.Graph, x: frozenset[int]) -> bool:
    return h.subgraph(x).number_of_edges() == len(x) * (len(x) - 1) // 2


def states(h: nx.Graph):
    """Yield unordered (A,B,Q) with two nontrivial independent blocks."""
    seen = set()
    for qmask in range(1 << 7):
        q = frozenset(x for x in S if qmask >> x & 1)
        if not clique(h, q):
            continue
        rem = sorted(S - q)
        for amask in range(1 << len(rem)):
            a = frozenset(rem[i] for i in range(len(rem)) if amask >> i & 1)
            b = S - q - a
            if len(a) < 2 or len(b) < 2:
                continue
            if not independent(h, a) or not independent(h, b):
                continue
            key = (tuple(sorted(min(a, b, key=lambda x: tuple(sorted(x))))),
                   tuple(sorted(max(a, b, key=lambda x: tuple(sorted(x))))),
                   tuple(sorted(q)))
            if key in seen:
                continue
            seen.add(key)
            yield a, b, q


def state_fits(h: nx.Graph, state, da: int, db: int) -> bool:
    """Allow either assignment of the two defect-one adjacent carriers."""
    for a, b, q in (state, (state[1], state[0], state[2])):
        if da in a or db in b:
            continue
        ok = True
        for x in q:
            if x == da and not any(h.has_edge(x, y) for y in a):
                ok = False
            if x == db and not any(h.has_edge(x, y) for y in b):
                ok = False
        if ok:
            return True
    return False


def robust_independent_block(h: nx.Graph) -> bool:
    for r in range(3, 8):
        for ii in itertools.combinations(S, r):
            i = frozenset(ii)
            if not independent(h, i):
                continue
            f = h.subgraph(S - i)
            if r >= 5:
                return True
            if r == 4 and f.number_of_edges() > 0:
                return True
            if r == 3 and any(clique(h, frozenset(t)) for t in itertools.combinations(S - i, 3)):
                return True
    return False


def has_clique_minor(h: nx.Graph, order: int) -> bool:
    vertices = tuple(h)
    connected = []
    for mask in range(1, 1 << len(vertices)):
        x = frozenset(vertices[k] for k in range(len(vertices)) if mask >> k & 1)
        if nx.is_connected(h.subgraph(x)):
            connected.append(x)

    def search(chosen, used):
        if len(chosen) == order:
            return True
        for x in connected:
            if x & used:
                continue
            if all(any(h.has_edge(a, b) for a in x for b in y) for y in chosen):
                if search(chosen + (x,), used | x):
                    return True
        return False

    return search((), frozenset())


def two_anchor_closed(h: nx.Graph) -> bool:
    return any(
        has_clique_minor(h.subgraph(S - {x, y}), 4)
        for x, y in itertools.combinations(S, 2)
    )


def bipartition_classes(h: nx.Graph):
    color = nx.bipartite.color(h)
    return (
        frozenset(x for x in h if color[x] == 0),
        frozenset(x for x in h if color[x] == 1),
    )


def main():
    graphs = 0
    pairs = 0
    failures = []
    for raw in nx.graph_atlas_g():
        if len(raw) != 7 or not nx.is_bipartite(raw):
            continue
        h = nx.convert_node_labels_to_integers(raw).copy()
        if max((len(c) for c in nx.find_cliques(h)), default=0) > 3:
            continue
        if robust_independent_block(h):
            continue
        if two_anchor_closed(h):
            continue
        graphs += 1
        st = list(states(h))
        # Enumerate all two-colourings, independently flipping components.
        comps = [h.subgraph(c).copy() for c in nx.connected_components(h)]
        base = [bipartition_classes(c) for c in comps]
        colourings = set()
        for flips in itertools.product((0, 1), repeat=len(comps)):
            left = frozenset().union(*(base[k][flips[k]] for k in range(len(comps))))
            right = S - left
            colourings.add((left, right))
        for left, right in colourings:
            for side in (left, right):
                for da, db in itertools.combinations(side, 2):
                    pairs += 1
                    if not any(state_fits(h, p, da, db) for p in st):
                        failures.append((nx.to_graph6_bytes(h, header=False).strip().decode(), da, db))
    print("nonrobust_bipartite_graphs", graphs)
    print("same_class_defect_pairs", pairs)
    print("state_failures", len(failures))
    unique = sorted(set(failures))
    print("unique_state_failures", len(unique))
    by_graph = {}
    for code, a, b in unique:
        by_graph.setdefault(code, []).append((a, b))
    for code, defect_pairs in sorted(by_graph.items()):
        g = nx.from_graph6_bytes(code.encode())
        print(code, "edges", sorted(g.edges()), "defects", defect_pairs)


if __name__ == "__main__":
    main()
