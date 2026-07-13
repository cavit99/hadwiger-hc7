#!/usr/bin/env python3
"""Exact sole-exterior atlas for the C5 + adjacent-pair link.

This is deliberately dependency-free.  It varies the ten edges from the
adjacent pair 5,6 to the induced cycle 0,...,4, requires alpha <= 2, and
rejects every graph containing a K5 minor supported on at most six
vertices (so that the unused boundary vertex can anchor the sole exterior
shore), and every local K6 minor.  Survivors are quotiented by the
dihedral group of the cycle and interchange of 5,6.
"""

from itertools import combinations

from planar_frame_neighborhood_probe import (
    BASE,
    CROSS,
    V,
    adjacency,
    alpha_at_most_two,
    canonical,
    connected,
)


def partitions(items, count):
    items = tuple(items)
    bags = []

    def rec(index):
        if index == len(items):
            if len(bags) == count:
                yield tuple(frozenset(bag) for bag in bags)
            return
        value = items[index]
        for bag in bags:
            bag.append(value)
            yield from rec(index + 1)
            bag.pop()
        if len(bags) < count:
            bags.append([value])
            yield from rec(index + 1)
            bags.pop()

    yield from rec(0)


def has_k5_minor_with_anchor(edges):
    adj = adjacency(edges)
    for size in (5, 6):
        for used in combinations(V, size):
            for bags in partitions(used, 5):
                if not all(connected(set(bag), adj) for bag in bags):
                    continue
                if all(
                    any(y in adj[x] for x in bags[i] for y in bags[j])
                    for i in range(5)
                    for j in range(i)
                ):
                    return True
    return False


def has_k6_minor(edges):
    adj = adjacency(edges)
    # A K6 model on seven vertices either uses six singleton bags or has
    # exactly one two-vertex (hence edge) bag.
    for deleted in V:
        remaining = set(V) - {deleted}
        if all(y in adj[x] for x, y in combinations(remaining, 2)):
            return True
    for x, y in edges:
        bags = [{x, y}] + [{u} for u in V if u not in (x, y)]
        if all(
            any(v in adj[u] for u in bags[i] for v in bags[j])
            for i in range(6) for j in range(i)
        ):
            return True
    return False


def width_three_elimination(edges):
    """Return an elimination order of fill width at most three, if one exists."""
    initial = adjacency(edges)

    def search(adj, order):
        if not adj:
            return tuple(order)
        for vertex in sorted(adj, key=lambda item: len(adj[item])):
            neighbours = set(adj[vertex])
            if len(neighbours) > 3:
                continue
            nxt = {u: set(vs) for u, vs in adj.items() if u != vertex}
            for u in neighbours:
                nxt[u].discard(vertex)
            for u, w in combinations(neighbours, 2):
                nxt[u].add(w)
                nxt[w].add(u)
            answer = search(nxt, order + [vertex])
            if answer is not None:
                return answer
        return None

    return search(initial, [])


def main():
    survivors = {}
    for mask in range(1 << len(CROSS)):
        edges = set(BASE)
        edges.update(CROSS[index] for index in range(len(CROSS)) if mask >> index & 1)
        edges = {tuple(sorted(edge)) for edge in edges}
        if (not alpha_at_most_two(edges)
                or has_k5_minor_with_anchor(edges)
                or has_k6_minor(edges)):
            continue
        form = canonical(edges)
        survivors[form] = survivors.get(form, 0) + 1

    print("survivor_orbits", len(survivors), "labelled", sum(survivors.values()))
    for form, orbit_size in sorted(survivors.items(), key=lambda item: (len(item[0]), item[0])):
        cross = tuple(edge for edge in form if edge not in BASE)
        misses = {
            terminal: tuple(vertex for vertex in range(5)
                            if tuple(sorted((terminal, vertex))) not in form)
            for terminal in (5, 6)
        }
        print("orbit", orbit_size, "edges", len(form), "misses", misses,
              "cross", cross, "width3_order", width_three_elimination(set(form)))


if __name__ == "__main__":
    main()
