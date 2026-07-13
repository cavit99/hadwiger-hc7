#!/usr/bin/env python3
"""Exhaust small actual-shell instances of the connected-set triangle claim."""

from itertools import combinations, product

import networkx as nx

from nested_triangle_connected_set_search import spanning_k4_models


def augmented(h, roots, piece, codes):
    g = h.copy()
    q = [len(h), len(h) + 1, len(h) + 2]
    g.add_edges_from(combinations(q, 2))
    for root in roots:
        g.add_edges_from((root, qi) for qi in q)
    for vertex, code in zip(piece, codes):
        g.add_edges_from((vertex, q[i]) for i in range(3) if code >> i & 1)
    return g


def has_portal_k4(models, n, roots, piece, codes):
    coverage = [0] * n
    for root in roots:
        coverage[root] = 7
    for vertex, code in zip(piece, codes):
        coverage[vertex] = code
    for model in models:
        if all(
            sum(coverage[v] for v in range(n) if bag >> v & 1) >= 0
            and __import__("functools").reduce(
                int.__or__, (coverage[v] for v in range(n) if bag >> v & 1), 0
            )
            == 7
            for bag in model
        ):
            return True
    return False


def main():
    tested = 0
    seven = 0
    for h in nx.graph_atlas_g():
        n = len(h)
        if n < 6 or not nx.is_connected(h) or nx.node_connectivity(h) < 4:
            continue
        models = spanning_k4_models(h)
        for a, b, c in combinations(h, 3):
            # Actual K6-{ab,ac} shell after relabelling a.
            triples = [(a, b, c), (b, a, c), (c, a, b)]
            for aa, bb, cc in triples:
                if h.has_edge(aa, bb) or h.has_edge(aa, cc) or not h.has_edge(bb, cc):
                    continue
                roots = (aa, bb, cc)
                piece = sorted(set(h) - set(roots))
                if not nx.is_connected(h.subgraph(piece)):
                    continue
                if not all(any(h.has_edge(root, x) for x in piece) for root in roots):
                    continue
                choices = []
                for x in piece:
                    choices.append(
                        [code for code in range(1, 8) if h.degree(x) + code.bit_count() >= 7]
                    )
                for codes in product(*choices):
                    tested += 1
                    if __import__("functools").reduce(int.__or__, codes, 0) != 7:
                        continue
                    if has_portal_k4(models, n, roots, piece, codes):
                        continue
                    g = augmented(h, roots, piece, codes)
                    if nx.node_connectivity(g) < 7:
                        continue
                    seven += 1
                    planar_h = nx.check_planarity(h)[0]
                    # If H itself is nonplanar, deleting any two Q vertices
                    # cannot give a planar graph.
                    if planar_h:
                        continue
                    print(
                        "COUNTER",
                        nx.to_graph6_bytes(h, header=False).decode().strip(),
                        "roots",
                        roots,
                        "piece",
                        piece,
                        "codes",
                        codes,
                        "G",
                        nx.to_graph6_bytes(g, header=False).decode().strip(),
                    )
                    return
    print("tested", tested, "seven_connected_no_portal_k4", seven, "counterexamples 0")


if __name__ == "__main__":
    main()
