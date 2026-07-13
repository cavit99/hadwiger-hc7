#!/usr/bin/env python3
"""Random falsification probe for decorated w-positions in a linked Moser frame.

This is a discovery aid, not a proof certificate.  It samples six-vertex
relative shores satisfying every local seven-cut inequality and tests the
three independent merged positions for w when w is anticomplete to U.
"""

from __future__ import annotations

import itertools
import random


U = range(5)
W = 5
A = 6
L = range(7)
C5 = {tuple(sorted(e)) for e in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]}
BOUNDARY_EDGES = {
    (i, j) for i in U for j in U if i < j and (i, j) not in C5
}


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for u, v in edges:
            y = v if u == x else u if v == x else None
            if y is not None and y in vertices and y not in seen:
                seen.add(y)
                stack.append(y)
    return seen == vertices


def valid_relative_shore(
    n: int, internal: set[tuple[int, int]], rows: tuple[int, ...]
) -> bool:
    if set().union(*({j for j in L if rows[x] >> j & 1} for x in range(n))) != set(L):
        return False
    for bits in range(1, (1 << n) - 1):
        xs = {x for x in range(n) if bits >> x & 1}
        inner = {
            v
            for u, v in internal
            if u in xs and v not in xs
        } | {
            u
            for u, v in internal
            if v in xs and u not in xs
        }
        labels = {j for x in xs for j in L if rows[x] >> j & 1}
        if len(inner) + len(labels) < 7:
            return False
    return True


def realizes(
    n: int,
    internal: set[tuple[int, int]],
    rows: tuple[int, ...],
    traces: tuple[frozenset[int], ...],
) -> bool:
    # Each shore vertex is unused or belongs to one of the trace blocks.
    q = len(traces)
    for assignment in itertools.product(range(q + 1), repeat=n):
        bags: list[set[tuple[str, int]]] = []
        good = True
        for k, trace in enumerate(traces):
            bag = {("l", x) for x in trace} | {
                ("d", x) for x, c in enumerate(assignment) if c == k
            }
            # Connectivity in boundary + shore incidence graph.
            seen = {next(iter(bag))}
            stack = list(seen)
            while stack:
                typ, x = stack.pop()
                nbrs: list[tuple[str, int]] = []
                if typ == "d":
                    for u, v in internal:
                        if u == x:
                            nbrs.append(("d", v))
                        elif v == x:
                            nbrs.append(("d", u))
                    nbrs += [("l", j) for j in L if rows[x] >> j & 1]
                else:
                    nbrs += [("d", d) for d in range(n) if rows[d] >> x & 1]
                    nbrs += [("l", y) for y in U if tuple(sorted((x, y))) in BOUNDARY_EDGES]
                for y in nbrs:
                    if y in bag and y not in seen:
                        seen.add(y)
                        stack.append(y)
            if seen != bag:
                good = False
                break
            bags.append(bag)
        if not good:
            continue

        def adjacent(b1: set[tuple[str, int]], b2: set[tuple[str, int]]) -> bool:
            for typ, x in b1:
                for typ2, y in b2:
                    if typ == typ2 == "d" and tuple(sorted((x, y))) in internal:
                        return True
                    if typ == "d" and typ2 == "l" and rows[x] >> y & 1:
                        return True
                    if typ == "l" and typ2 == "d" and rows[y] >> x & 1:
                        return True
                    if typ == typ2 == "l" and tuple(sorted((x, y))) in BOUNDARY_EDGES:
                        return True
            return False

        if all(adjacent(bags[i], bags[j]) for i in range(q) for j in range(i + 1, q)):
            return True
    return False


def realizes_decorated(
    n: int,
    internal: set[tuple[int, int]],
    rows: tuple[int, ...],
    traces: tuple[frozenset[int], ...],
    w_edges: int,
) -> bool:
    """Strong local certificate; a trace containing A is the apex-star bag."""
    q = len(traces)
    if any(
        any(
            (x == W and y != A and (w_edges >> y) & 1)
            or (y == W and x != A and (w_edges >> x) & 1)
            or (set((x, y)) == {W, A} and (w_edges >> A) & 1)
            for x, y in itertools.combinations(trace, 2)
        )
        for trace in traces
    ):
        return False

    boundary_edges = set(BOUNDARY_EDGES)
    boundary_edges |= {
        tuple(sorted((W, x))) for x in list(U) + [A] if (w_edges >> x) & 1
    }

    def bag_connected(bag: set[tuple[str, int]]) -> bool:
        seen = {next(iter(bag))}
        stack = list(seen)
        while stack:
            typ, x = stack.pop()
            nbrs: list[tuple[str, int]] = []
            if typ == "d":
                for u, v in internal:
                    if u == x:
                        nbrs.append(("d", v))
                    elif v == x:
                        nbrs.append(("d", u))
                nbrs += [("l", j) for j in L if rows[x] >> j & 1]
            else:
                nbrs += [("d", d) for d in range(n) if rows[d] >> x & 1]
                nbrs += [("l", y) for y in L if tuple(sorted((x, y))) in boundary_edges]
            for y in nbrs:
                if y in bag and y not in seen:
                    seen.add(y)
                    stack.append(y)
        return seen == bag

    def adjacent(b1: set[tuple[str, int]], b2: set[tuple[str, int]]) -> bool:
        # The actual star contains v and is adjacent to every U-root block.
        if any(x == ("l", A) for x in b1) and any(t == "l" and y in U for t, y in b2):
            return True
        if any(x == ("l", A) for x in b2) and any(t == "l" and y in U for t, y in b1):
            return True
        for typ, x in b1:
            for typ2, y in b2:
                if typ == typ2 == "d" and tuple(sorted((x, y))) in internal:
                    return True
                if typ == "d" and typ2 == "l" and rows[x] >> y & 1:
                    return True
                if typ == "l" and typ2 == "d" and rows[y] >> x & 1:
                    return True
                if typ == typ2 == "l" and tuple(sorted((x, y))) in boundary_edges:
                    return True
        return False

    for assignment in itertools.product(range(q + 1), repeat=n):
        bags = [
            {("l", x) for x in trace}
            | {("d", x) for x, c in enumerate(assignment) if c == k}
            for k, trace in enumerate(traces)
        ]
        if all(bag_connected(b) for b in bags) and all(
            adjacent(bags[i], bags[j]) for i in range(q) for j in range(i + 1, q)
        ):
            return True
    return False


def probe_decorated_masks(
    internal: set[tuple[int, int]], rows: tuple[int, ...]
) -> tuple[int, tuple[int, int, list[bool], list[bool]]] | None:
    e = frozenset({0, 1})
    f = frozenset({2, 3})
    r = frozenset({4})
    traces = [
        (e, f, r, frozenset({A, W})),
        (e | {W}, f, r, frozenset({A})),
        (e, f | {W}, r, frozenset({A})),
        (e, f, r | {W}, frozenset({A})),
        (e, f, r, frozenset({A}), frozenset({W})),
    ]
    worst: tuple[int, int, list[bool], list[bool]] | None = None
    # Bits 0..4 are w-U, bit 6 is w-a; bit 7 records w-b only for legality.
    for mask in range(1 << 8):
        w_edges = (mask & 31) | (((mask >> 6) & 1) << A)
        legal = [
            not ((mask >> 6) & 1) and not ((mask >> 7) & 1),
            not (mask & 0b00011),
            not (mask & 0b01100),
            not (mask & 0b10000),
            True,
        ]
        realized = [
            legal[i] and realizes_decorated(6, internal, rows, traces[i], w_edges)
            for i in range(5)
        ]
        score = 2 * sum(realized) - sum(legal)
        if worst is None or score < worst[0]:
            worst = (score, mask, legal, realized)
    return worst


def graph_types() -> list[set[tuple[int, int]]]:
    k6 = {(i, j) for i in range(6) for j in range(i + 1, 6)}
    c6 = {tuple(sorted((i, (i + 1) % 6))) for i in range(6)}
    prism = c6 | {(0, 3), (1, 4), (2, 5)}
    wheel = {tuple(sorted((i, (i + 1) % 5))) for i in range(5)} | {(i, 5) for i in range(5)}
    return [k6, prism, wheel]


def main() -> None:
    rng = random.Random(0xC0FFEE)
    traces = [
        (frozenset({0, 1, W}), frozenset({2, 3}), frozenset({4})),
        (frozenset({0, 1}), frozenset({2, 3, W}), frozenset({4})),
        (frozenset({0, 1}), frozenset({2, 3}), frozenset({4, W})),
    ]
    for internal in graph_types():
        degrees = [sum(x in e for e in internal) for x in range(6)]
        best = 4
        best_rows: tuple[int, ...] | None = None
        for _ in range(300):
            rows = []
            for d in degrees:
                minimum = max(1, 7 - d)
                weight = rng.randint(minimum, min(7, minimum + 2))
                rows.append(sum(1 << j for j in rng.sample(list(L), weight)))
            row_tuple = tuple(rows)
            if not valid_relative_shore(6, internal, row_tuple):
                continue
            count = sum(realizes(6, internal, row_tuple, t) for t in traces)
            if count < best:
                best = count
                best_rows = row_tuple
                print("new best", len(internal), best, [f"{r:07b}" for r in row_tuple])
                if best == 0:
                    break
        print("type", len(internal), "best", best, "rows", best_rows)
        if best_rows is not None:
            print("decorated worst", probe_decorated_masks(internal, best_rows))


if __name__ == "__main__":
    main()
