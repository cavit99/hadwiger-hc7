#!/usr/bin/env python3
"""Search larger all-crossless wheel shores for genuine residual transitions.

This is a falsification probe for the proposed claim that the thirty
high-root/nonstar states always lift across a safe contraction.
"""

from __future__ import annotations

import itertools

import networkx as nx

from moser_safe_transition_state_probe import N, U, classes, kind, matching, NONEDGES


A, W = 1, 7
LABELS = tuple(range(8))
M_EDGES = {
    tuple(sorted(x))
    for x in {
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
        (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
    }
}


def colourable(graph: nx.Graph, allowed: dict[int, frozenset[int]]) -> bool:
    assigned: dict[int, int] = {}

    def rec() -> bool:
        if len(assigned) == len(graph):
            return True
        best = None
        best_opts = None
        for x in graph:
            if x in assigned:
                continue
            opts = allowed[x] - {assigned[y] for y in graph[x] if y in assigned}
            if not opts:
                return False
            if best_opts is None or len(opts) < len(best_opts):
                best, best_opts = x, opts
        assert best is not None and best_opts is not None
        for c in best_opts:
            assigned[best] = c
            if rec():
                return True
            del assigned[best]
        return False

    return rec()


def boundary_colours(edges, w_colour):
    cs = classes(edges)
    cmap = {}
    for i, block in enumerate(cs):
        for x in block:
            cmap[x] = i
    cmap[W] = w_colour
    return cmap


def relative7(graph: nx.Graph, contacts: dict[int, set[int]]) -> bool:
    verts = tuple(graph)
    for q in range(1, len(verts)):
        for xs in itertools.combinations(verts, q):
            xset = set(xs)
            internal = set().union(*(set(graph[x]) for x in xset)) - xset
            labels = set().union(*(contacts[x] for x in xset))
            if len(internal) + len(labels) < 7:
                return False
    return True


ABSTRACT_TO_PHYSICAL = (0, 5, 2, 4, 6)
PRESENT_PROFILES = tuple(
    frozenset((i, j))
    for i, j in itertools.combinations(range(5), 2)
    if (j - i) % 5 not in (1, 4)
)
TRIPLE_PROFILES = tuple(
    frozenset({i, (i + 1) % 5, (i + 3) % 5}) for i in range(5)
)


def circular_crossless(word: tuple[frozenset[int], ...]) -> bool:
    occurrences = {
        i: tuple(p for p, profile in enumerate(word) if i in profile)
        for i in range(5)
    }

    def between(x: int, a: int, b: int) -> bool:
        return 0 < (x - a) % len(word) < (b - a) % len(word)

    for j in range(5):
        a, b = (j + 1) % 5, (j + 2) % 5
        c, d = (j + 3) % 5, (j + 4) % 5
        for pa, pb, pc, pd in itertools.product(
            occurrences[a], occurrences[b], occurrences[c], occurrences[d]
        ):
            if {pa, pb}.isdisjoint({pc, pd}):
                if pa == pb or pc == pd:
                    return False
                if between(pc, pa, pb) == between(pd, pa, pb):
                    return False
    return True


def exact_profile_words(n: int):
    profiles = PRESENT_PROFILES + TRIPLE_PROFILES
    for word in itertools.product(profiles, repeat=n):
        if set().union(*word) != set(range(5)):
            continue
        valid = True
        for i, triple in enumerate(TRIPLE_PROFILES):
            if triple not in word:
                continue
            shield = (i + 3) % 5
            if sum(shield in profile for profile in word) != 1:
                valid = False
                break
        if valid and circular_crossless(word):
            yield word


def main() -> None:
    residual = [
        es for q in (2, 3) for es in itertools.combinations(NONEDGES, q)
        if matching(es) and kind(es) != "decorated-T trace"
    ]
    for rim_n in range(5, 8):
        # D is a wheel: rim 0..rim_n-1 and hub rim_n.
        d = nx.wheel_graph(rim_n + 1)
        # NetworkX wheel rim is 1..rim_n; hub is 0. Relabel for clarity.
        d = nx.relabel_nodes(d, {0: rim_n, **{i: i - 1 for i in range(1, rim_n + 1)}})
        crossless_words = list(exact_profile_words(rim_n))
        print("rim", rim_n, "crossless words", len(crossless_words))
        uncolourable = 0
        for word in crossless_words:
            triple_positions = [i for i, profile in enumerate(word) if len(profile) == 3]
            for decorations in itertools.product((1, 2, 3), repeat=len(triple_positions)):
                contacts = {x: {A, W} for x in d}
                for p, profile in enumerate(word):
                    contacts[p].update(ABSTRACT_TO_PHYSICAL[i] for i in profile)
                for p, decoration in zip(triple_positions, decorations):
                    contacts[p].discard(A)
                    contacts[p].discard(W)
                    if decoration & 1:
                        contacts[p].add(A)
                    if decoration & 2:
                        contacts[p].add(W)
                if not relative7(d, contacts):
                    continue
                for es in residual:
                    for wc in range(6):
                        bc = boundary_colours(es, wc)
                        palette = frozenset(range(6))
                        allowed = {
                            x: palette - {bc[z] for z in contacts[x]}
                            for x in d
                        }
                        if any(not ls for ls in allowed.values()) or colourable(d, allowed):
                            continue
                        uncolourable += 1
                        for x, y in d.edges:
                            q = nx.contracted_edge(d, (x, y), self_loops=False)
                            z = x
                            q_allowed = {u: allowed[u] for u in q if u != z}
                            q_allowed[z] = allowed[x] & allowed[y]
                            if q_allowed[z] and colourable(q, q_allowed):
                                print("FOUND", rim_n, word, decorations, es, "w", wc, "edge", (x, y))
                                return
        print("rim", rim_n, "uncolourable residual boundary systems", uncolourable)
    # A structurally different all-crossless disk: delete one vertex from
    # the icosahedron.  Its five neighbours form the common portal face;
    # all other vertices have internal degree five.
    ico = nx.icosahedral_graph()
    deleted = 0
    rim = tuple(ico[deleted])
    # Recover the cyclic order in the neighbour C5.
    rim_graph = ico.subgraph(rim)
    order = [rim[0]]
    previous = None
    while len(order) < 5:
        choices = [z for z in rim_graph[order[-1]] if z != previous]
        nxt = next(z for z in choices if z not in order or len(order) == 4)
        previous, nxt0 = order[-1], nxt
        if nxt0 in order:
            break
        order.append(nxt0)
    assert len(order) == 5 and order[0] in rim_graph[order[-1]]
    d = ico.copy()
    d.remove_node(deleted)
    for word in itertools.product(PRESENT_PROFILES, repeat=5):
        if not circular_crossless(word):
            continue
        contacts = {x: {A, W} for x in d}
        for x, profile in zip(order, word):
            contacts[x].update(ABSTRACT_TO_PHYSICAL[i] for i in profile)
        if not relative7(d, contacts):
            continue
        for es in residual:
            base_classes = len(classes(es))
            for wc in range(6):
                bc = boundary_colours(es, wc)
                palette = frozenset(range(6))
                allowed = {x: palette - {bc[z] for z in contacts[x]} for x in d}
                if any(not ls for ls in allowed.values()) or colourable(d, allowed):
                    continue
                for x, y in d.edges:
                    q = nx.contracted_edge(d, (x, y), self_loops=False)
                    q_allowed = {u: allowed[u] for u in q if u != x}
                    q_allowed[x] = allowed[x] & allowed[y]
                    if q_allowed[x] and colourable(q, q_allowed):
                        print("FOUND ICOSAHEDRAL", word, es, "w", wc, "edge", (x, y))
                        return
    print("no wheel residual transition found")


if __name__ == "__main__":
    main()
