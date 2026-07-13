#!/usr/bin/env python3
"""Find small 3-connected graphs whose 3-cut lobe deletion loses a T-rooted K3.

This is a falsification probe for the nonplanar exact-seven thin-shore route.
It uses the NetworkX graph atlas (orders at most seven) and an exhaustive
connected-branch-set test.  A rooted K3 model consists of three pairwise
disjoint, pairwise adjacent connected vertex sets, the ith containing the
ith root and no other root.
"""

from itertools import combinations, product

import networkx as nx


def connected_masks(g: nx.Graph, allowed: set[int], root: int) -> list[frozenset[int]]:
    others = sorted(allowed - {root})
    out: list[frozenset[int]] = []
    for bits in range(1 << len(others)):
        bag = {root}
        bag.update(others[i] for i in range(len(others)) if bits & (1 << i))
        if nx.is_connected(g.subgraph(bag)):
            out.append(frozenset(bag))
    return out


def adjacent(g: nx.Graph, a: frozenset[int], b: frozenset[int]) -> bool:
    return any(g.has_edge(x, y) for x in a for y in b)


def rooted_k3(g: nx.Graph, roots: tuple[int, int, int]) -> bool:
    root_set = set(roots)
    choices = [connected_masks(g, set(g) - (root_set - {r}), r) for r in roots]
    for bags in product(*choices):
        if any(bags[i] & bags[j] for i, j in combinations(range(3), 2)):
            continue
        if all(adjacent(g, bags[i], bags[j]) for i, j in combinations(range(3), 2)):
            return True
    return False


def main() -> None:
    seen = 0
    first_deletion = None
    augmented_tested = 0
    for g0 in nx.graph_atlas_g():
        if len(g0) < 4 or not nx.is_connected(g0):
            continue
        g = nx.convert_node_labels_to_integers(g0)
        if nx.node_connectivity(g) < 3:
            continue
        for t in combinations(g.nodes, 3):
            h = g.copy()
            h.remove_nodes_from(t)
            components = list(nx.connected_components(h))
            if len(components) < 2:
                continue
            for k in components:
                if set().union(*(set(g.neighbors(x)) for x in k)) - set(k) != set(t):
                    continue
                remainder = g.subgraph(set(g) - set(k)).copy()
                seen += 1
                if not rooted_k3(remainder, t):
                    if first_deletion is None:
                        first_deletion = (g.copy(), t, set(k), remainder.copy())

        # Independently test the bridge augmentation principle: for each
        # connected T-full bridge H=C union T, does nonplanarity after
        # completing T force a T-rooted K3 already in H?
        for t in combinations(g.nodes, 3):
            c = set(g) - set(t)
            if not c or not nx.is_connected(g.subgraph(c)):
                continue
            if any(not any(g.has_edge(x, z) for x in c) for z in t):
                continue
            plus = g.copy()
            plus.add_edges_from(combinations(t, 2))
            if nx.check_planarity(plus)[0]:
                continue
            augmented_tested += 1
            if not rooted_k3(g, t):
                print("AUGMENTED_COUNTEREXAMPLE")
                print(f"n={len(g)} m={g.number_of_edges()} T={t}")
                print("edges=" + repr(sorted(tuple(sorted(e)) for e in g.edges())))
                return
    if first_deletion is not None:
        g, t, k, remainder = first_deletion
        print("DELETION_COUNTEREXAMPLE")
        print(f"n={len(g)} m={g.number_of_edges()} T={t} K={sorted(k)}")
        print("edges=" + repr(sorted(tuple(sorted(e)) for e in g.edges())))
        print(f"connectivity={nx.node_connectivity(g)}")
        print(f"remainder_edges={sorted(tuple(sorted(e)) for e in remainder.edges())}")
    else:
        print(f"NO_DELETION_COUNTEREXAMPLE tested={seen}")
    print(f"NO_AUGMENTED_COUNTEREXAMPLE tested={augmented_tested}")


if __name__ == "__main__":
    main()
