#!/usr/bin/env python3
"""Exhaustive n=4 audit of the flat full-host matching dichotomy.

The diagonal cross-pairs are required carrier edges, so the nonedge
relation has 12 optional entries.  For every type word and every one of
the 4096 relations, this script constructs and validates exactly the
colouring or clique model used in Theorem 2.1 of
``hadwiger_flat_full_host_matching_dichotomy.md``.
"""

from itertools import combinations, permutations, product


def matchings_of_size(matrix: int, n: int, size: int):
    for lefts in combinations(range(n), size):
        for rights in combinations(range(n), size):
            for perm in permutations(rights):
                matching = tuple(zip(lefts, perm))
                if all(matrix >> (i * n + j) & 1 for i, j in matching):
                    yield matching


def maximum_matching(matrix: int, n: int):
    for size in range(n, -1, -1):
        matching = next(matchings_of_size(matrix, n, size), None)
        if matching is not None:
            return matching
    raise AssertionError


def minimum_cover(matrix: int, n: int, size: int):
    for cover in combinations(range(2 * n), size):
        chosen = set(cover)
        if all(
            i in chosen or n + j in chosen
            for i in range(n)
            for j in range(n)
            if matrix >> (i * n + j) & 1
        ):
            return chosen
    raise AssertionError((matrix, size))


def host_edges(types: tuple[int, ...], matrix: int):
    n = len(types)
    a, b, c = 0, 1, 2
    xs = tuple(range(3, 3 + n))
    ys = tuple(range(3 + n, 3 + 2 * n))
    edges = {tuple(sorted((b, c)))}
    edges.update(tuple(sorted((xs[i], xs[j]))) for i, j in combinations(range(n), 2))
    edges.update(tuple(sorted((ys[i], ys[j]))) for i, j in combinations(range(n), 2))
    for i, t in enumerate(types):
        if t == 0:
            edges.update(
                tuple(sorted(e))
                for e in ((a, xs[i]), (b, xs[i]), (b, ys[i]), (c, ys[i]))
            )
        else:
            edges.update(
                tuple(sorted(e))
                for e in ((b, xs[i]), (c, xs[i]), (a, ys[i]), (c, ys[i]))
            )
    edges.update(
        tuple(sorted((xs[i], ys[j])))
        for i in range(n)
        for j in range(n)
        if not (matrix >> (i * n + j) & 1)
    )
    return edges, xs, ys


def add_all_optional_boundary_edges(edges, types, xs, ys):
    """Add every boundary contact not required or forbidden by (1.3)-(1.4)."""
    maximal = set(edges)
    a = 0
    for i, t in enumerate(types):
        # For type zero only a-y_i is optional; for type one only a-x_i.
        optional_vertex = ys[i] if t == 0 else xs[i]
        maximal.add(tuple(sorted((a, optional_vertex))))
    return maximal


def valid_colouring(edges, colour):
    return all(colour[u] != colour[v] for u, v in edges)


def valid_model(edges, bags, target):
    if len(bags) != target:
        return False
    if sum(map(len, bags)) != len(set().union(*map(set, bags))):
        return False
    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, set()).add(v)
        adjacency.setdefault(v, set()).add(u)

    def connected(bag):
        reached = {bag[0]}
        while True:
            new = reached | {
                v for u in reached for v in adjacency.get(u, ()) if v in bag
            }
            if new == reached:
                return len(reached) == len(bag)
            reached = new

    return all(connected(bag) for bag in bags) and all(
        any(tuple(sorted((u, v))) in edges for u in bags[i] for v in bags[j])
        for i in range(target)
        for j in range(i)
    )


def alternating_reach(matrix: int, n: int, matching, unmatched_left: int):
    left_to_right = dict(matching)
    right_to_left = {r: l for l, r in matching}
    zx, zy = {unmatched_left}, set()
    changed = True
    while changed:
        changed = False
        for i in tuple(zx):
            for j in range(n):
                if left_to_right.get(i) == j or not (matrix >> (i * n + j) & 1):
                    continue
                if j not in zy:
                    zy.add(j)
                    changed = True
        for j in tuple(zy):
            if j in right_to_left and right_to_left[j] not in zx:
                zx.add(right_to_left[j])
                changed = True
    return zx, zy


def main():
    n = 4
    diagonal = sum(1 << (i * n + i) for i in range(n))
    optional_positions = [k for k in range(n * n) if not (diagonal >> k & 1)]
    outcomes = {"perfect-colour": 0, "corank-minor": 0,
                "exposed-colour": 0, "alternating-minor": 0}

    for types in product((0, 1), repeat=n):
        for bits in range(1 << len(optional_positions)):
            matrix = sum(
                ((bits >> q) & 1) << k for q, k in enumerate(optional_positions)
            )
            matching = maximum_matching(matrix, n)
            nu = len(matching)
            edges, xs, ys = host_edges(types, matrix)
            maximal_edges = add_all_optional_boundary_edges(edges, types, xs, ys)

            if nu == n:
                colour = {xs[i]: k for k, (i, _) in enumerate(matching)}
                colour.update({ys[j]: k for k, (_, j) in enumerate(matching)})
                colour.update({0: n, 1: n, 2: n + 1})
                assert valid_colouring(edges, colour)
                assert valid_colouring(maximal_edges, colour)
                outcomes["perfect-colour"] += 1
                continue

            if nu <= n - 2:
                cover = minimum_cover(matrix, n, nu)
                core = [(xs[i],) for i in range(n) if i not in cover]
                core += [(ys[j],) for j in range(n) if n + j not in cover]
                bags = tuple(core[: n + 2] + [(1, 2)])
                assert valid_model(edges, bags, n + 3)
                assert valid_model(maximal_edges, bags, n + 3)
                outcomes["corank-minor"] += 1
                continue

            unmatched_left = next(i for i in range(n) if i not in dict(matching))
            matched_right = {j for _, j in matching}
            unmatched_right = next(j for j in range(n) if j not in matched_right)

            # Search all maximum matchings for a favourable exposed end.
            favourable = None
            for candidate in matchings_of_size(matrix, n, n - 1):
                left_out = next(i for i in range(n) if i not in dict(candidate))
                candidate_rights = {j for _, j in candidate}
                right_out = next(j for j in range(n) if j not in candidate_rights)
                if types[left_out] == 0 or types[right_out] == 1:
                    favourable = candidate, left_out, right_out
                    break

            if favourable is not None:
                candidate, left_out, right_out = favourable
                colour = {}
                for k, (i, j) in enumerate(candidate):
                    colour[xs[i]] = colour[ys[j]] = k
                colour[xs[left_out]] = n - 1
                colour[ys[right_out]] = n
                if types[left_out] == 0:
                    colour[2] = n - 1
                    colour[0] = colour[1] = n + 1
                else:
                    assert types[right_out] == 1
                    colour[1] = n
                    colour[0] = colour[2] = n + 1
                assert valid_colouring(edges, colour)
                assert valid_colouring(maximal_edges, colour)
                outcomes["exposed-colour"] += 1
                continue

            zx, zy = alternating_reach(matrix, n, matching, unmatched_left)
            assert all(types[i] == 1 for i in zx)
            type_zero = next(i for i, t in enumerate(types) if t == 0)
            assert type_zero not in zx
            core = [(xs[i],) for i in zx]
            core += [(ys[j],) for j in range(n) if j not in zy]
            assert len(core) == n + 1
            bags = tuple(core + [(0, 1, xs[type_zero]), (2,)])
            assert valid_model(edges, bags, n + 3)
            assert valid_model(maximal_edges, bags, n + 3)

            # Stronger diagonal-carrier rooted completion: the X-part of
            # the alternating minimum cover, together with a, is one
            # connected branch set; {b,c} remains the reserved connector.
            cover_x = [xs[i] for i in range(n) if i not in zx]
            rooted_bags = tuple(core + [(0, *cover_x), (1, 2)])
            assert valid_model(edges, rooted_bags, n + 3)
            assert valid_model(maximal_edges, rooted_bags, n + 3)
            outcomes["alternating-minor"] += 1

    # Sharpness of the diagonal hypothesis in Theorem 2.3.  This relation
    # deliberately makes some paired diagonals nonedges of the host.
    sharp_types = (0, 0, 0, 1)
    sharp_pairs = ((0, 0), (0, 3), (1, 0), (1, 1), (2, 0))
    sharp_matrix = sum(1 << (i * n + j) for i, j in sharp_pairs)
    sharp_matchings = tuple(matchings_of_size(sharp_matrix, n, n - 1))
    assert sharp_matchings and all(
        sharp_types[next(i for i in range(n) if i not in dict(m))] == 1
        and sharp_types[
            next(j for j in range(n) if j not in {right for _, right in m})
        ] == 0
        for m in sharp_matchings
    )
    fixed = ((0, 3), (1, 1), (2, 0))
    zx, zy = alternating_reach(sharp_matrix, n, fixed, 3)
    assert zx == {3} and zy == set()
    sharp_edges, sharp_xs, sharp_ys = host_edges(sharp_types, sharp_matrix)
    candidate_r = {0, sharp_xs[0], sharp_xs[1], sharp_xs[2]}
    assert not any(
        tuple(sorted((v, sharp_ys[0]))) in sharp_edges for v in candidate_r
    )

    print("relations checked:", 2**n * 2 ** len(optional_positions))
    print("outcomes:", outcomes)


if __name__ == "__main__":
    main()
