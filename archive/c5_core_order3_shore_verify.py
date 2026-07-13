#!/usr/bin/env python3
"""Exact audit of a three-vertex shore in both sharp five-edge cores.

The opposite full shore is contracted to one helper.  We enumerate every
boundary-neighbourhood assignment on a P3 or K3 shore satisfying the
minimum-degree constraints on the shore vertices and full attachment to
the seven-vertex boundary.  Isomorphic assignments under the internal
automorphism group are represented once.  Each resulting graph is tested
for an exact K7 branch-set model.
"""

import itertools


C = tuple(range(5))
R = (5, 6)
S = C + R
DVERT = (7, 8, 9)
H = 10
V = tuple(range(11))
FULL = (1 << 7) - 1


def boundary_edges(kind):
    if kind == "C5+2K1":
        missing = {
            tuple(sorted((i, (i + 2) % 5))) for i in C
        }
    elif kind == "K3+2K2":
        missing = {(0, 1), (0, 2), (1, 2), (3, 4), (5, 6)}
    else:
        raise AssertionError(kind)
    return {
        edge for edge in itertools.combinations(S, 2) if edge not in missing
    }


def core_edges(kind):
    edges = set()
    edges.update(boundary_edges(kind))
    edges.update((s, H) for s in S)
    return {tuple(sorted(e)) for e in edges}


def masks_at_least(size):
    return tuple(mask for mask in range(1 << 7) if mask.bit_count() >= size)


def k_minor_model(edges, k=7):
    n = len(V)
    adjacency = [0] * n
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << n)
    connected = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(a, b):
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1:]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                answer = rec(chosen + [a], nxt, used | a)
                if answer is not None:
                    return answer
        return None
    return rec([], connected, 0)


def graph_edges(kind, internal_edges, masks):
    edges = core_edges(kind) | {tuple(sorted(e)) for e in internal_edges}
    for d, mask in zip(DVERT, masks):
        edges.update(tuple(sorted((d, s))) for s in S if mask >> s & 1)
    return edges


def assignments(kind):
    if kind == "P3":
        endpoints = masks_at_least(6)
        centers = masks_at_least(5)
        for left in endpoints:
            for center in centers:
                for right in endpoints:
                    if left > right:  # quotient by endpoint reversal
                        continue
                    if left | center | right == FULL:
                        yield (left, center, right)
    elif kind == "K3":
        choices = masks_at_least(5)
        for masks in itertools.combinations_with_replacement(choices, 3):
            if masks[0] | masks[1] | masks[2] == FULL:
                yield masks
    else:
        raise AssertionError(kind)


def as_sets(model):
    return tuple(tuple(v for v in V if mask >> v & 1) for mask in model)


def verify_model(edges, model):
    edges = set(edges)
    bags = [set(bag) for bag in model]
    assert len(bags) == 7
    assert all(bags)
    assert all(bags[i].isdisjoint(bags[j])
               for i in range(7) for j in range(i))
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y for x in reached for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    for i in range(7):
        for j in range(i):
            assert any(tuple(sorted((x, y))) in edges
                       for x in bags[i] for y in bags[j])


def main():
    structures = {
        "P3": ((7, 8), (8, 9)),
        "K3": ((7, 8), (7, 9), (8, 9)),
    }
    for core_kind in ("C5+2K1", "K3+2K2"):
        for shore_kind, internal in structures.items():
            checked = 0
            failures = []
            for masks in assignments(shore_kind):
                edges = graph_edges(core_kind, internal, masks)
                model = k_minor_model(edges)
                checked += 1
                if model is None:
                    failures.append(masks)
                    if len(failures) >= 20:
                        break
                else:
                    verify_model(edges, as_sets(model))
            print(core_kind, shore_kind, "checked", checked,
                  "first failures", failures)
            if not failures:
                print(core_kind, shore_kind, "all K7")


if __name__ == "__main__":
    main()
