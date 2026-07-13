"""Probe the sharpened bipartite thin-shore carrier claim.

For a fixed bipartite boundary H on S={0,...,6} and a connected open
shore L with labelled boundary-contact masks, test the necessary local
conditions inherited from a hypothetical HC7 counterexample:

* every nonempty X subseteq L has |N_L(X)|+|N_S(X)| >= 7;
* Dirac's contraction-critical neighbourhood inequality
      alpha(G[N(x)]) <= d(x)-5
  for every x in L;
* L is S-full but contains no two disjoint connected S-full packets.

The target certificate is a pair of disjoint connected carriers meeting
the two natural bipartition classes of H (in either orientation).

This is a falsification probe only.  Passing it is not a proof that the
listed necessary conditions are sufficient in an actual counterexample.
"""

from __future__ import annotations

import itertools
import random

import networkx as nx


S = tuple(range(7))
FULL = (1 << 7) - 1


def bits(mask: int):
    return [i for i in S if mask >> i & 1]


def connected_masks(g: nx.Graph):
    nodes = tuple(g.nodes())
    ans = []
    for r in range(1, len(nodes) + 1):
        for xs in itertools.combinations(nodes, r):
            m = sum(1 << x for x in xs)
            if nx.is_connected(g.subgraph(xs)):
                ans.append(m)
    return ans


def contact_union(xmask: int, contacts: tuple[int, ...]) -> int:
    out = 0
    for x, c in enumerate(contacts):
        if xmask >> x & 1:
            out |= c
    return out


def open_neighbour_mask(g: nx.Graph, xmask: int) -> int:
    out = 0
    for x in g.nodes():
        if xmask >> x & 1:
            for y in g[x]:
                if not (xmask >> y & 1):
                    out |= 1 << y
    return out


def rooted_cut_condition(g: nx.Graph, contacts: tuple[int, ...]) -> bool:
    for xmask in range(1, 1 << len(g)):
        lhs = open_neighbour_mask(g, xmask).bit_count()
        lhs += contact_union(xmask, contacts).bit_count()
        if lhs < 7:
            return False
    return True


def has_two_full_packets(g: nx.Graph, contacts: tuple[int, ...], cms) -> bool:
    full = [m for m in cms if contact_union(m, contacts) == FULL]
    return any(a & b == 0 for i, a in enumerate(full) for b in full[i + 1 :])


def has_bipartition_carriers(
    g: nx.Graph, contacts: tuple[int, ...], cms, left: int, right: int
) -> bool:
    for a in cms:
        ca = contact_union(a, contacts)
        for b in cms:
            if a & b:
                continue
            cb = contact_union(b, contacts)
            if ((ca & left) == left and (cb & right) == right) or (
                (ca & right) == right and (cb & left) == left
            ):
                return True
    return False


def alpha_of_neighbourhood(
    shore: nx.Graph, boundary: nx.Graph, contacts: tuple[int, ...], x: int
) -> int:
    # Work in the literal graph on L plus S; vertices of S are shifted by n.
    n = len(shore)
    whole = nx.Graph()
    whole.add_nodes_from(range(n + 7))
    whole.add_edges_from(shore.edges())
    whole.add_edges_from((n + a, n + b) for a, b in boundary.edges())
    for y, mask in enumerate(contacts):
        whole.add_edges_from((y, n + s) for s in bits(mask))
    ngh = list(whole[x])
    best = 0
    for mask in range(1 << len(ngh)):
        if mask.bit_count() <= best:
            continue
        chosen = [ngh[i] for i in range(len(ngh)) if mask >> i & 1]
        if whole.subgraph(chosen).number_of_edges() == 0:
            best = len(chosen)
    return best


def dirac_condition(
    shore: nx.Graph, boundary: nx.Graph, contacts: tuple[int, ...]
) -> bool:
    for x in shore:
        d = shore.degree(x) + contacts[x].bit_count()
        if alpha_of_neighbourhood(shore, boundary, contacts, x) > d - 5:
            return False
    return True


def random_contact_mask(min_size: int = 1) -> int:
    size = random.randint(min_size, 7)
    return sum(1 << s for s in random.sample(S, size))


def probe(boundary: nx.Graph, left: int, right: int, trials: int = 300_000):
    atlas = nx.graph_atlas_g()
    candidates = [
        nx.convert_node_labels_to_integers(g).copy()
        for g in atlas
        if 2 <= len(g) <= 6 and nx.is_connected(g)
    ]
    candidate_data = [(g, connected_masks(g)) for g in candidates]
    random.seed(20260713)
    checked = 0
    for _ in range(trials):
        shore, cms = random.choice(candidate_data)
        n = len(shore)
        # Bias toward dense contact masks, as the rooted cut inequalities force.
        contacts = tuple(random_contact_mask(random.choice((2, 3, 4, 5))) for _ in range(n))
        if contact_union((1 << n) - 1, contacts) != FULL:
            continue
        if has_bipartition_carriers(shore, contacts, cms, left, right):
            continue
        checked += 1
        if not rooted_cut_condition(shore, contacts):
            continue
        if has_two_full_packets(shore, contacts, cms):
            continue
        if not dirac_condition(shore, boundary, contacts):
            continue
        return shore, contacts, checked
    return None, None, checked


def exhaustive_small(boundary: nx.Graph, left: int, right: int, max_n: int = 3):
    atlas = nx.graph_atlas_g()
    tested = 0
    negative = 0
    for raw in atlas:
        if not (2 <= len(raw) <= max_n and nx.is_connected(raw)):
            continue
        shore = nx.convert_node_labels_to_integers(raw).copy()
        cms = connected_masks(shore)
        for contacts in itertools.product(range(1, 128), repeat=len(shore)):
            tested += 1
            if contact_union((1 << len(shore)) - 1, contacts) != FULL:
                continue
            if has_bipartition_carriers(shore, contacts, cms, left, right):
                continue
            negative += 1
            if not rooted_cut_condition(shore, contacts):
                continue
            if has_two_full_packets(shore, contacts, cms):
                continue
            if not dirac_condition(shore, boundary, contacts):
                continue
            return shore, contacts, tested, negative
    return None, None, tested, negative


def exhaustive_cycle4(boundary: nx.Graph, left: int, right: int):
    shore = nx.cycle_graph(4)
    cms = connected_masks(shore)
    choices = [m for m in range(1, 128) if m.bit_count() >= 5]
    tested = negative = 0
    for contacts in itertools.product(choices, repeat=4):
        tested += 1
        if contact_union(15, contacts) != FULL:
            continue
        if has_bipartition_carriers(shore, contacts, cms, left, right):
            continue
        negative += 1
        if not rooted_cut_condition(shore, contacts):
            continue
        if has_two_full_packets(shore, contacts, cms):
            continue
        if not dirac_condition(shore, boundary, contacts):
            continue
        return shore, contacts, tested, negative
    return None, None, tested, negative


def main():
    instances = []
    p7 = nx.path_graph(7)
    instances.append(("P7", p7, (0, 2, 4, 6)))
    c6i = nx.Graph()
    c6i.add_nodes_from(S)
    c6i.add_edges_from((x, (x + 1) % 6) for x in range(6))
    instances.append(("C6+I", c6i, (0, 2, 4, 6)))
    for name, h, left_vertices in instances:
        print("BOUNDARY", name)
        left = sum(1 << s for s in left_vertices)
        right = FULL ^ left
        shore, contacts, tested, negative = exhaustive_small(h, left, right)
        print(f"exhaustive_assignments_tested={tested}")
        print(f"exhaustive_carrier_negative={negative}")
        if shore is None:
            shore, contacts, tested, negative = exhaustive_cycle4(h, left, right)
            print(f"cycle4_assignments_tested={tested}")
            print(f"cycle4_carrier_negative={negative}")
        if shore is None:
            shore, contacts, checked = probe(h, left, right)
            print(f"carrier_negative_assignments_seen={checked}")
        if shore is None:
            print("NO_COUNTEREXAMPLE_FOUND")
            continue
        print("COUNTEREXAMPLE_TO_SHARPENED_LOCAL_LEMMA")
        print("shore_edges", sorted(shore.edges()))
        print("contacts", [bits(c) for c in contacts])
        return


if __name__ == "__main__":
    main()
