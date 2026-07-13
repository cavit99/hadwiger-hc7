#!/usr/bin/env python3
"""Atlas of rooted-K4 behaviour at a full four-cut quotient."""

from itertools import combinations, product, permutations

import networkx as nx


def rooted_k4(graph, root_sets):
    roots = [set(x) for x in root_sets]
    if any(roots[i] & roots[j] for i in range(4) for j in range(i + 1, 4)):
        return None
    occupied = set().union(*roots)
    free = [v for v in graph if v not in occupied]
    for assignment in product(range(5), repeat=len(free)):
        bags = [set(x) for x in roots]
        for v, slot in zip(free, assignment):
            if slot < 4:
                bags[slot].add(v)
        if not all(nx.is_connected(graph.subgraph(b)) for b in bags):
            continue
        if all(any(graph.has_edge(u, v) for u in bags[i] for v in bags[j])
               for i in range(4) for j in range(i + 1, 4)):
            return bags
    return None


def main():
    t = ("p", "x", "y", "z")
    t_pairs = list(combinations(t, 2))
    failures = []
    for shores in range(2, 5):
        c = tuple(f"c{i}" for i in range(shores))
        for mask in range(1 << len(t_pairs)):
            graph = nx.Graph()
            graph.add_nodes_from(t + c)
            for i, edge in enumerate(t_pairs):
                if mask >> i & 1:
                    graph.add_edge(*edge)
            if not graph.has_edge("p", "x"):
                continue
            for q in c:
                for s in t:
                    graph.add_edge(q, s)
            if nx.node_connectivity(graph) < 4:
                continue
            for a, b, d in permutations(set(graph) - {"p", "x"}, 3):
                model = rooted_k4(graph, ({"p", "x"}, {a}, {b}, {d}))
                if model is None:
                    failures.append((shores, tuple(sorted(graph.subgraph(t).edges())), (a, b, d)))
                    if len(failures) <= 12:
                        print("FAIL", failures[-1])
    print("failures", len(failures))


if __name__ == "__main__":
    main()
