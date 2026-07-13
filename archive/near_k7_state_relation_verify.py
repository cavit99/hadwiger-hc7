#!/usr/bin/env python3
"""Finite audit of the matching-relation results in Section 6.

This independently checks the rectangular classification of edge-maximal
non-perfect bipartite graphs through order four and, for n=4, every mixed
type word and every full flat cross-layer relation.  In every canonically
deletion-critical non-perfect case it validates either the explicit
boundary colouring or the explicit K7 model from Theorem 6.4.
"""

from __future__ import annotations

from itertools import combinations, permutations, product


def maximum_matching(matrix: int, n: int) -> tuple[tuple[int, int], ...]:
    """Return a maximum matching in an n by n bit matrix."""
    best: tuple[tuple[int, int], ...] = ()

    def search(left: int, used_right: int, chosen: list[tuple[int, int]]) -> None:
        nonlocal best
        if left == n:
            if len(chosen) > len(best):
                best = tuple(chosen)
            return
        if len(chosen) + n - left <= len(best):
            return
        search(left + 1, used_right, chosen)
        for right in range(n):
            bit = 1 << (left * n + right)
            if matrix & bit and not (used_right >> right & 1):
                chosen.append((left, right))
                search(left + 1, used_right | (1 << right), chosen)
                chosen.pop()

    search(0, 0, [])
    return best


def perfect(matrix: int, n: int) -> bool:
    return len(maximum_matching(matrix, n)) == n


def rectangular_witness(matrix: int, n: int):
    """Find S,T satisfying (6.3)--(6.4), if they exist."""
    for s_mask in range(1, 1 << n):
        t_mask = 0
        for left in range(n):
            if any(
                matrix >> (left * n + right) & 1
                for right in range(n)
                if s_mask >> right & 1
            ):
                t_mask |= 1 << left
        if t_mask.bit_count() != s_mask.bit_count() - 1:
            continue
        expected = 0
        for left in range(n):
            for right in range(n):
                if (s_mask >> right & 1 and t_mask >> left & 1) or not (
                    s_mask >> right & 1
                ):
                    expected |= 1 << (left * n + right)
        if matrix == expected:
            return s_mask, t_mask
    return None


def check_rectangular_theorem() -> int:
    checked = 0
    for n in range(1, 5):
        universe = (1 << (n * n)) - 1
        for matrix in range(1 << (n * n)):
            checked += 1
            if perfect(matrix, n):
                continue
            maximal = all(
                perfect(matrix | (1 << bit), n)
                for bit in range(n * n)
                if not (matrix >> bit & 1)
            )
            assert maximal == (rectangular_witness(matrix, n) is not None), (n, matrix)
            # Every alleged rectangular relation really is maximal.
            if rectangular_witness(matrix, n) is not None:
                assert maximal
        assert universe >= 0
    return checked


def full_edges(types: tuple[int, ...], actual_cross: int):
    """The switched n=4 flat host, with exact forced boundary rows."""
    n = 4
    a, b, c = 0, 1, 2
    xs = tuple(range(3, 7))
    ys = tuple(range(7, 11))
    edges = {tuple(sorted((b, c)))}
    edges.update(tuple(sorted((xs[i], xs[j]))) for i, j in combinations(range(n), 2))
    edges.update(tuple(sorted((ys[i], ys[j]))) for i, j in combinations(range(n), 2))
    for i, t in enumerate(types):
        if t == 0:
            edges.update({tuple(sorted((a, xs[i]))), tuple(sorted((b, xs[i]))),
                          tuple(sorted((b, ys[i]))), tuple(sorted((c, ys[i])))})
        else:
            edges.update({tuple(sorted((b, xs[i]))), tuple(sorted((c, xs[i]))),
                          tuple(sorted((a, ys[i]))), tuple(sorted((c, ys[i])))})
    for i in range(n):
        for j in range(n):
            if actual_cross >> (i * n + j) & 1:
                edges.add(tuple(sorted((xs[i], ys[j]))))
    return edges, xs, ys


def valid_colouring(edges, colour) -> bool:
    return all(colour[x] != colour[y] for x, y in edges)


def valid_model(edges, bags) -> bool:
    if len(bags) != 7 or sum(map(len, bags)) != len(set().union(*map(set, bags))):
        return False
    adjacency = {v: set() for v in range(11)}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)

    def connected(bag):
        reached = {bag[0]}
        while True:
            new = reached | {y for x in reached for y in adjacency[x] if y in bag}
            if new == reached:
                return len(reached) == len(bag)
            reached = new

    return all(connected(bag) for bag in bags) and all(
        any(tuple(sorted((x, y))) in edges for x in bags[i] for y in bags[j])
        for i in range(7) for j in range(i)
    )


def matching_leaving(matrix: int, n: int, left_out: int, right_out: int):
    for perm in permutations(r for r in range(n) if r != right_out):
        lefts = tuple(l for l in range(n) if l != left_out)
        if all(matrix >> (l * n + r) & 1 for l, r in zip(lefts, perm)):
            return tuple(zip(lefts, perm))
    raise AssertionError((matrix, left_out, right_out))


def check_canonical_closure() -> tuple[int, int]:
    n = 4
    universe = (1 << 16) - 1
    diagonal = sum(1 << (i * n + i) for i in range(n))
    checked = critical = 0
    for types in product((0, 1), repeat=n):
        if len(set(types)) == 1:
            continue
        for optional in range(1 << 12):
            off_bits = [bit for bit in range(16) if bit % 5 != 0]
            actual = diagonal | sum(
                ((optional >> k) & 1) << bit for k, bit in enumerate(off_bits)
            )
            allowed = universe ^ actual
            checked += 1
            if perfect(allowed, n):
                continue
            if not all(
                perfect(allowed | (1 << bit), n)
                for bit in range(16)
                if actual >> bit & 1
            ):
                continue
            critical += 1
            witness = rectangular_witness(allowed, n)
            assert witness is not None
            s_mask, t_mask = witness
            edges, xs, ys = full_edges(types, actual)

            left_type_zero = next(
                (i for i in range(n) if not (t_mask >> i & 1) and types[i] == 0), None
            )
            right_type_one = next(
                (j for j in range(n) if s_mask >> j & 1 and types[j] == 1), None
            )
            if left_type_zero is not None or right_type_one is not None:
                li = left_type_zero
                rj = next(j for j in range(n) if s_mask >> j & 1)
                share_boundary = 2
                fresh_pair = (0, 1)
                if li is None:
                    rj = right_type_one
                    li = next(i for i in range(n) if not (t_mask >> i & 1))
                    share_boundary = 1
                    fresh_pair = (0, 2)
                matching = matching_leaving(allowed, n, li, rj)
                colour = {}
                for colour_id, (i, j) in enumerate(matching):
                    colour[xs[i]] = colour_id
                    colour[ys[j]] = colour_id
                colour[xs[li]] = n - 1
                colour[ys[rj]] = n
                colour[share_boundary] = colour[xs[li] if left_type_zero is not None else ys[rj]]
                colour[fresh_pair[0]] = colour[fresh_pair[1]] = n + 1
                assert valid_colouring(edges, colour), (types, actual, witness, colour)
            else:
                r = next(i for i, t in enumerate(types) if t == 0)
                s = next(i for i, t in enumerate(types) if t == 1)
                clique = [(xs[i],) for i in range(n) if not (t_mask >> i & 1)]
                clique += [(ys[j],) for j in range(n) if s_mask >> j & 1]
                bags = tuple(clique + [(xs[r], 0, ys[s]), (1, 2)])
                assert valid_model(edges, bags), (types, actual, witness, bags)
    return checked, critical


def check_abstract_rectangular_branch() -> int:
    """Validate Proposition 6.5, where diagonal contacts may be suppressed."""
    n = 4
    universe = (1 << 16) - 1
    checked = 0
    for types in product((0, 1), repeat=n):
        if len(set(types)) == 1:
            continue
        for s_mask in range(1, 1 << n):
            for t_vertices in combinations(range(n), s_mask.bit_count() - 1):
                t_mask = sum(1 << i for i in t_vertices)
                allowed = 0
                for i in range(n):
                    for j in range(n):
                        if (s_mask >> j & 1 and t_mask >> i & 1) or not (
                            s_mask >> j & 1
                        ):
                            allowed |= 1 << (i * n + j)
                actual = universe ^ allowed
                edges, xs, ys = full_edges(types, actual)
                checked += 1

                left_type_zero = next(
                    (i for i in range(n) if not (t_mask >> i & 1) and types[i] == 0),
                    None,
                )
                right_type_one = next(
                    (j for j in range(n) if s_mask >> j & 1 and types[j] == 1),
                    None,
                )
                if left_type_zero is not None or right_type_one is not None:
                    li = left_type_zero
                    rj = next(j for j in range(n) if s_mask >> j & 1)
                    share_boundary = 2
                    fresh_pair = (0, 1)
                    if li is None:
                        rj = right_type_one
                        li = next(i for i in range(n) if not (t_mask >> i & 1))
                        share_boundary = 1
                        fresh_pair = (0, 2)
                    matching = matching_leaving(allowed, n, li, rj)
                    colour = {}
                    for colour_id, (i, j) in enumerate(matching):
                        colour[xs[i]] = colour_id
                        colour[ys[j]] = colour_id
                    colour[xs[li]] = n - 1
                    colour[ys[rj]] = n
                    colour[share_boundary] = colour[
                        xs[li] if left_type_zero is not None else ys[rj]
                    ]
                    colour[fresh_pair[0]] = colour[fresh_pair[1]] = n + 1
                    assert valid_colouring(edges, colour), (types, allowed, colour)
                else:
                    r = next(i for i, t in enumerate(types) if t == 0)
                    s = next(i for i, t in enumerate(types) if t == 1)
                    clique = [(xs[i],) for i in range(n) if not (t_mask >> i & 1)]
                    clique += [(ys[j],) for j in range(n) if s_mask >> j & 1]
                    bags = tuple(clique + [(xs[r], 0, ys[s]), (1, 2)])
                    assert valid_model(edges, bags), (types, allowed, bags)
    return checked


def main() -> None:
    relations = check_rectangular_theorem()
    hosts, critical = check_canonical_closure()
    rectangles = check_abstract_rectangular_branch()
    assert critical == 0  # The diagonal obstruction of Theorem 6.4.
    print("bipartite relations checked:", relations)
    print("mixed flat hosts checked:", hosts)
    print("nonperfect canonically deletion-critical hosts:", critical)
    print("abstract mixed rectangular branches checked:", rectangles)


if __name__ == "__main__":
    main()
