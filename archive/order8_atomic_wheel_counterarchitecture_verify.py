#!/usr/bin/env python3
"""Independent finite checks for the sharp atomic order-eight wheel."""

from itertools import combinations

import networkx as nx


ACTIVE = ("x", "c2", "c4", "c5")
NEUTRAL = ("c0", "z", "p", "q")
RIM = ("v0", "v1", "v2", "v3")
KVERTICES = RIM + ("h",)


def wheel_and_contacts():
    k = nx.Graph()
    k.add_nodes_from(KVERTICES)
    k.add_edges_from((RIM[i], RIM[(i + 1) % 4]) for i in range(4))
    k.add_edges_from(("h", u) for u in RIM)
    contacts = {
        "v0": {"x", "c5", "c0", "z", "p"},
        "v1": {"c5", "c2", "c0", "z", "p"},
        "v2": {"c2", "c4", "c0", "z", "q"},
        "v3": {"c4", "x", "c0", "z", "q"},
        "h": {"c0", "z", "p", "q"},
    }
    return k, contacts


def relative_boundary_check(k, contacts):
    vertices = list(KVERTICES)
    minimum = 100
    tight = []
    for size in range(1, len(vertices)):
        for y_tuple in combinations(vertices, size):
            y = set(y_tuple)
            nk = set().union(*(set(k[u]) for u in y)) - y
            nb = set().union(*(contacts[u] for u in y))
            value = len(nk) + len(nb)
            minimum = min(minimum, value)
            if value == 8:
                tight.append(tuple(sorted(y)))
            assert value >= 8, (y, nk, nb)
    return minimum, tight


def connected_subsets(k):
    vertices = list(KVERTICES)
    result = []
    for size in range(1, len(vertices) + 1):
        for subset in combinations(vertices, size):
            if nx.is_connected(k.subgraph(subset)):
                result.append(set(subset))
    return result


def packet_check(k, contacts):
    carriers = connected_subsets(k)
    a = {"x", "c2"}
    c = {"c4", "c5"}
    for left in carriers:
        if not a <= set().union(*(contacts[u] for u in left)):
            continue
        for right in carriers:
            if left & right:
                continue
            if c <= set().union(*(contacts[u] for u in right)):
                return False, (left, right)
    return True, None


def quotient(k, contacts):
    g = nx.Graph()
    old = [f"c{i}" for i in range(6)]
    g.add_nodes_from(old + ["z", "H", "x", "p", "q"] + list(KVERTICES))
    for i in range(6):
        for j in range(i + 1, 6):
            if (i - j) % 6 not in (1, 5):
                g.add_edge(f"c{i}", f"c{j}")
    g.add_edges_from(("z", u) for u in old)
    g.add_edges_from(("H", u) for u in old + ["z"])
    g.add_edges_from((("x", "c0"), ("x", "c1")))
    g.add_edges_from(k.edges())
    for u in KVERTICES:
        g.add_edges_from((u, b) for b in contacts[u])
    return g


def main():
    k, contacts = wheel_and_contacts()
    minimum, tight = relative_boundary_check(k, contacts)
    no_packet, witness = packet_check(k, contacts)
    assert no_packet, witness

    g = quotient(k, contacts)
    gate = {"x", "p", "q", "c0", "c2", "c4", "c5", "z"}
    actual_gate = set().union(*(contacts[u] for u in KVERTICES))
    assert actual_gate == gate
    assert not any(g.has_edge(u, b) for u in KVERTICES for b in ("c1", "c3"))

    planar = g.copy()
    planar.remove_nodes_from(("c0", "z"))
    is_planar, embedding = nx.check_planarity(planar)
    assert is_planar

    # The active-terminal disk is maximally triangulated relative to its
    # outer 8-cycle: n=9, boundary length=8, e=3n-3-b=16.
    active_disk = k.copy()
    active_disk.add_nodes_from(ACTIVE)
    for u in KVERTICES:
        active_disk.add_edges_from((u, b) for b in contacts[u] & set(ACTIVE))
    assert active_disk.number_of_nodes() == 9
    assert active_disk.number_of_edges() == 16
    assert nx.check_planarity(active_disk)[0]

    print("relative boundary minimum", minimum)
    print("tight proper subsets", len(tight))
    print("two-packet absent")
    print("exact gate", sorted(gate))
    print("Q-{c0,z} planar on", planar.number_of_nodes(), "vertices")
    print("active disk saturated with", active_disk.number_of_edges(), "edges")


if __name__ == "__main__":
    main()
