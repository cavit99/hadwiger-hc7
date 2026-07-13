#!/usr/bin/env python3
"""Audit SDR thresholds and the sharp vertex-critical Mycielski profile."""

from itertools import combinations

import networkx as nx


def has_sdr(family):
    def search(i, used):
        if i == len(family):
            return True
        return any(search(i + 1, used | {x}) for x in family[i] if x not in used)
    return search(0, set())


def antichain(family):
    return all(not (a <= b or b <= a) for a, b in combinations(family, 2))


def k_colourable(g, k):
    order = sorted(g, key=lambda v: -g.degree[v])
    colour = {}

    def search(i):
        if i == len(order):
            return True
        v = order[i]
        forbidden = {colour[w] for w in g[v] if w in colour}
        for c in range(k):
            if c not in forbidden:
                colour[v] = c
                if search(i + 1):
                    return True
                del colour[v]
        return False

    return search(0)


def mycielski_k3():
    g = nx.Graph()
    vs = [f"v{i}" for i in range(3)]
    us = [f"u{i}" for i in range(3)]
    g.add_edges_from(combinations(vs, 2))
    for i in range(3):
        for j in range(3):
            if i != j:
                g.add_edge(us[i], vs[j])
        g.add_edge("w", us[i])
    return g, vs, us


def valid_model(g, bags):
    if sum(map(len, bags)) != len(set().union(*map(set, bags))):
        return False
    return all(nx.is_connected(g.subgraph(bag)) for bag in bags) and all(
        any(g.has_edge(x, y) for x in bags[i] for y in bags[j])
        for i in range(len(bags)) for j in range(i)
    )


def main():
    # Exhaust every antichain on ground sets through order four.
    checked = 0
    for r in range(1, 5):
        subsets = [frozenset(s) for q in range(1, r + 1) for s in combinations(range(r), q)]
        for m in range(1, min(4, len(subsets)) + 1):
            for family in combinations(subsets, m):
                if antichain(family):
                    checked += 1
                    assert has_sdr(family), (r, family)
    bad = tuple(frozenset(s) for s in list(combinations(range(4), 2))[:5])
    assert antichain(bad) and not has_sdr(bad)

    g, vs, us = mycielski_k3()
    assert not k_colourable(g, 3) and k_colourable(g, 4)
    assert all(k_colourable(g.copy().subgraph(set(g) - {v}), 3) for v in g)
    u_set = set(us) | {"w"}
    profiles = [frozenset(set(g[u]) - u_set) for u in us]
    assert antichain(profiles) and has_sdr(profiles)
    assert set().union(*map(set, profiles)) == set(vs)

    # The three columns plus the common local vertex do have an unlabelled
    # rooted K4; this deliberately does not certify any prescribed portal
    # row on those branch sets.
    bags = ({"w"}, {us[0], vs[1]}, {us[1], vs[2]}, {us[2], vs[0]})
    assert valid_model(g, bags)

    print("antichains of order at most four checked:", checked)
    print("five-set threshold counterexample:", [sorted(s) for s in bad])
    print("Mycielski K3: 4-vertex-critical; three outside profiles on three endpoints")
    print("rooted K4 exists but carries no prescribed state labels")


if __name__ == "__main__":
    main()
