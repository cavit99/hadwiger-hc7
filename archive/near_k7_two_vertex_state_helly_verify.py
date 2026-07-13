#!/usr/bin/env python3
"""Finite audit for the two-vertex neutral-carrier parity theorem.

Each of four neutral bags is an edge.  A bag of type AB admits the AB
repeated-boundary state but not AC; type AC has the reverse behavior.
The failure of the opposite state forces both ends to meet each other
neutral bag, so every pair of bags contains a perfect matching.  Up to
discarding helpful edges, there are 2^6 signed K4 covers.  This verifier
tests every nonconstant type word and every signed cover.  The only
K7-minor-free cover is the type coboundary s_ij=t_i xor t_j; that cover has
the explicit two-layer six-colouring used in the hand proof.
"""

from __future__ import annotations

from itertools import combinations, permutations, product


A, B, C = 0, 1, 2
U = ((3, 4), (5, 6), (7, 8), (9, 10))
V = tuple(range(11))


def set_partitions(items: tuple[int, ...], k: int):
    blocks: list[list[int]] = []

    def rec(pos: int):
        if pos == len(items):
            if len(blocks) == k:
                yield tuple(tuple(block) for block in blocks)
            return
        if len(blocks) + len(items) - pos < k:
            return
        x = items[pos]
        for block in blocks:
            block.append(x)
            yield from rec(pos + 1)
            block.pop()
        if len(blocks) < k:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


PARTITIONS = tuple(
    partition
    for size in range(7, len(V) + 1)
    for support in combinations(V, size)
    for partition in set_partitions(support, 7)
)


def find_k7(edges: set[tuple[int, int]]):
    adj = [0] * len(V)
    for x, y in edges:
        adj[x] |= 1 << y
        adj[y] |= 1 << x

    def connected(block: tuple[int, ...]) -> bool:
        target = sum(1 << x for x in block)
        reached = target & -target
        while True:
            expanded = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                expanded |= adj[bit.bit_length() - 1] & target
            if expanded == reached:
                return reached == target
            reached = expanded

    for bags in PARTITIONS:
        if not all(connected(bag) for bag in bags):
            continue
        if all(
            any(adj[x] >> y & 1 for x in bags[i] for y in bags[j])
            for i in range(7)
            for j in range(i)
        ):
            return bags
    return None


def graph(types: tuple[int, ...], signs: tuple[int, ...]):
    # type 0 = only AB among repeated states, type 1 = only AC.
    edges = {(B, C)}
    for i, (x, y) in enumerate(U):
        edges.add((x, y))
        if types[i] == 0:
            # x sees A,B; y sees B,C.
            edges.update(((A, x), (B, x), (B, y), (C, y)))
        else:
            # x sees A,C; y sees B,C.
            edges.update(((A, x), (C, x), (B, y), (C, y)))

    for sign, (i, j) in zip(signs, combinations(range(4), 2)):
        xi, yi = U[i]
        xj, yj = U[j]
        if sign == 0:
            edges.update(((xi, xj), (yi, yj)))
        else:
            edges.update(((xi, yj), (yi, xj)))
    return {tuple(sorted(edge)) for edge in edges}


def valid_model(
    edges: set[tuple[int, int]], bags: tuple[tuple[int, ...], ...]
) -> bool:
    """Check the displayed branch sets, independently of the exact search."""
    if len(bags) != 7:
        return False
    if sum(map(len, bags)) != len(set().union(*map(set, bags))):
        return False
    adjacency = {x: set() for x in V}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)

    def connected(bag: tuple[int, ...]) -> bool:
        reached = {bag[0]}
        while True:
            expanded = reached | {
                y for x in reached for y in adjacency[x] if y in bag
            }
            if expanded == reached:
                return len(reached) == len(bag)
            reached = expanded

    return all(connected(bag) for bag in bags) and all(
        any(tuple(sorted((x, y))) in edges for x in bags[i] for y in bags[j])
        for i in range(7)
        for j in range(i)
    )


def displayed_curvature_model(
    types: tuple[int, ...], signs: tuple[int, ...]
) -> tuple[tuple[int, ...], ...] | None:
    """Return exactly model (5.3) or (5.4) from the hand proof."""
    pairs = tuple(combinations(range(4), 2))
    sign = dict(zip(pairs, signs))
    mismatch = next(
        ((i, j) for (i, j), s in sign.items() if s != (types[i] ^ types[j])),
        None,
    )
    if mismatch is None:
        return None
    i, j = mismatch

    # Formula (5.3): an opposite-type parallel matching.
    parallel_opposite = next(
        ((u, v) for (u, v), s in sign.items() if types[u] != types[v] and s == 0),
        None,
    )
    if parallel_opposite is not None:
        i, j = parallel_opposite
        k, l = (r for r in range(4) if r not in {i, j})
        pi, qi = U[i]
        pj, qj = U[j]
        return ((B,), (C,), (pi, pj), (qi,), (qj,), U[k], U[l])

    # Formula (5.4): a same-type crossed matching, with all opposite-type
    # matchings crossed (otherwise the preceding branch would have fired).
    assert types[i] == types[j] and sign[i, j] == 1
    k = next(r for r in range(4) if types[r] != types[i])
    l = next(r for r in range(4) if r not in {i, j, k})
    pi, qi = U[i]
    pj, qj = U[j]
    pk, qk = U[k]
    first_boundary, second_boundary = ((B, C) if types[i] == 0 else (C, B))
    return (
        (A, pi),
        (first_boundary,),
        (second_boundary, qi),
        (pj,),
        (qj, pk),
        U[l],
        (qk,),
    )


def balanced_colouring(types: tuple[int, ...]) -> dict[int, int]:
    """Six-colour the type-coboundary architecture."""
    colour = {A: 4, B: 4, C: 5}
    for i, (p, q) in enumerate(U):
        # After switching the endpoints of type-1 carriers, the x vertices
        # and y vertices induce two K4s.  Use a derangement between layers.
        x, y = (p, q) if types[i] == 0 else (q, p)
        colour[x] = i
        colour[y] = (i + 1) % 4
    return colour


def main() -> None:
    negative = []
    checked = 0
    for types in product((0, 1), repeat=4):
        if len(set(types)) == 1:
            continue
        for signs in product((0, 1), repeat=6):
            checked += 1
            edges = graph(types, signs)
            displayed = displayed_curvature_model(types, signs)
            if displayed is not None:
                assert valid_model(edges, displayed), (types, signs, displayed)
            model = find_k7(edges)
            if model is None:
                negative.append((types, signs))
    expected = {
        (types, tuple(types[i] ^ types[j] for i, j in combinations(range(4), 2)))
        for types in product((0, 1), repeat=4)
        if len(set(types)) != 1
    }
    assert set(negative) == expected, (set(negative) ^ expected)
    for types, signs in negative:
        colour = balanced_colouring(types)
        assert all(colour[x] != colour[y] for x, y in graph(types, signs))

    # A sharp full-host warning.  Start with the flat type 0001 skeleton and
    # add x0-y3,x1-y3,x2-y3.  Together with the vertical x3-y3, these forbid
    # every carrier-palette colour at y3, so the canonical layer matching
    # has a Hall defect.  Nevertheless the graph is still K7-minor-free and
    # has the displayed five-colouring.  Static Hall failure is therefore
    # not a clique-minor certificate; critical operation transitions remain
    # necessary.
    types = (0, 0, 0, 1)
    signs = tuple(types[i] ^ types[j] for i, j in combinations(range(4), 2))
    hall_edges = graph(types, signs)
    switched = [(U[i] if types[i] == 0 else tuple(reversed(U[i]))) for i in range(4)]
    for i in range(3):
        hall_edges.add(tuple(sorted((switched[i][0], switched[3][1]))))

    # Proposition 6.1 in this instance: after fixing colour i on x_i,
    # admissible y-layer colourings are exactly perfect matchings in the
    # nonedge matrix.  In particular y_3 has no admissible colour here.
    admissible = {
        (i, j)
        for i in range(4)
        for j in range(4)
        if tuple(sorted((switched[i][0], switched[j][1]))) not in hall_edges
    }
    matching_permutations = {
        perm
        for perm in permutations(range(4))
        if all((colour, j) in admissible for j, colour in enumerate(perm))
    }
    assert not matching_permutations
    assert not any((i, 3) in admissible for i in range(4))
    assert find_k7(hall_edges) is None
    five_colour = {0: 4, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2,
                   6: 3, 7: 3, 8: 4, 9: 0, 10: 4}
    assert all(five_colour[x] != five_colour[y] for x, y in hall_edges)

    print("instances checked:", checked)
    print("negative instances:", len(negative))
    for item in negative[:20]:
        print(item)
    print("all negatives are exactly the type coboundaries and are 6-coloured")
    print("Hall-defect completion: K7-free and explicitly 5-coloured")


if __name__ == "__main__":
    main()
