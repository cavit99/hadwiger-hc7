#!/usr/bin/env python3
"""Exact replay of the order-six decorated-w counterexample.

The verifier uses no graph library or solver.  It checks the relative
seven-cut inequalities, an explicit linked Moser frame, the legal-state
universe, and exhaustively rejects both legal strong decorations.
"""

from __future__ import annotations

import itertools


# Shore: rim 0,...,4 and hub 5.
D = set(range(6))
RIM = set(range(5))
H = 5

# Relative boundary.
Q0, Q1, Q2, W, Q4, R, A = range(6, 13)
L = {Q0, Q1, Q2, W, Q4, R, A}
U = {Q0, Q1, Q2, Q4, R}


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


EDGES: set[tuple[int, int]] = set()

# Internal wheel.
for i in range(5):
    EDGES.add(edge(i, (i + 1) % 5))
    EDGES.add(edge(i, H))

# Five outer portal classes: P(q_i)={l_i,l_{i-1}}.
outer = [Q0, Q1, Q2, W, Q4]
for i, q in enumerate(outer):
    EDGES.add(edge(q, i))
    EDGES.add(edge(q, (i - 1) % 5))

# The leftover root and terminal are complete to the shore.
for x in D:
    EDGES.add(edge(R, x))
    EDGES.add(edge(A, x))

# Pure-Moser graph on U: complement of q0-q1-q2-q4-r-q0.
missing_u = {
    edge(Q0, Q1), edge(Q1, Q2), edge(Q2, Q4), edge(Q4, R), edge(R, Q0)
}
for x, y in itertools.combinations(U, 2):
    if edge(x, y) not in missing_u:
        EDGES.add(edge(x, y))

# Moser terminal a=1 sees roots 0,2,6 in the usual labelling
# q0=0,q1=5,q2=2,q4=4,r=6.
for x in (Q0, Q2, R):
    EDGES.add(edge(A, x))

# The sixth portal w sees exactly the second pair, the leftover root,
# and the terminal (and may also see the opposite terminal b globally).
for x in (Q2, Q4, R, A):
    EDGES.add(edge(W, x))


def adjacent(u: int, v: int) -> bool:
    return edge(u, v) in EDGES


def connected(vertices: set[int], star_bag: bool = False) -> bool:
    if not vertices:
        return False
    # A star bag also contains v,a,b.  Its D vertices can attach only
    # through a in this one-shore certificate, which is already present.
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in vertices:
            if y not in seen and adjacent(x, y):
                seen.add(y)
                stack.append(y)
    return seen == vertices


def bags_adjacent(x: set[int], y: set[int], x_star: bool, y_star: bool) -> bool:
    # The actual star contains v, which sees every U-root.
    if x_star and y & U:
        return True
    if y_star and x & U:
        return True
    return any(adjacent(a, b) for a in x for b in y)


def strong_realization(traces: tuple[frozenset[int], ...], star_index: int) -> bool:
    q = len(traces)
    for assignment in itertools.product(range(q + 1), repeat=6):
        bags = [set(trace) for trace in traces]
        for x, owner in enumerate(assignment):
            if owner < q:
                bags[owner].add(x)
        if not all(connected(b, i == star_index) for i, b in enumerate(bags)):
            continue
        if all(
            bags_adjacent(bags[i], bags[j], i == star_index, j == star_index)
            for i in range(q)
            for j in range(i + 1, q)
        ):
            return True
    return False


def verify_cut_inequalities() -> None:
    for mask in range(1, (1 << 6) - 1):
        x = {i for i in D if mask >> i & 1}
        shore_boundary = {
            y for y in D - x if any(adjacent(y, z) for z in x)
        }
        label_boundary = {
            y for y in L if any(adjacent(y, z) for z in x)
        }
        assert len(shore_boundary) + len(label_boundary) >= 7, (
            x, shore_boundary, label_boundary
        )
    assert all(any(adjacent(x, q) for x in D) for q in L)


def verify_linked_frame() -> None:
    # e=q0q1 uses l0; f=q2q4 uses l2-l3.
    e_bag = {Q0, 0, Q1}
    f_bag = {Q2, 2, 3, Q4}
    r_bag = {R}
    assert e_bag.isdisjoint(f_bag)
    assert connected(e_bag) and connected(f_bag) and connected(r_bag)
    assert bags_adjacent(e_bag, f_bag, False, False)
    assert bags_adjacent(e_bag, r_bag, False, False)
    assert bags_adjacent(f_bag, r_bag, False, False)


def verify_legal_states_and_obstruction() -> None:
    e = frozenset({Q0, Q1})
    f = frozenset({Q2, Q4})
    r = frozenset({R})
    star = frozenset({A})

    # Globally wb is also present.  Hence w cannot share the 13/star
    # colour, f, or r; it can share e, or remain a singleton.
    assert not adjacent(W, Q0) and not adjacent(W, Q1)
    assert adjacent(W, Q2) and adjacent(W, Q4)
    assert adjacent(W, R) and adjacent(W, A)

    merged_e = (star, e | {W}, f, r)
    singleton_w = (star, e, f, r, frozenset({W}))

    assert not strong_realization(merged_e, 0)
    assert not strong_realization(singleton_w, 0)


def main() -> None:
    verify_cut_inequalities()
    verify_linked_frame()
    verify_legal_states_and_obstruction()
    print(
        "verified order-six wheel shore: all 7-cut inequalities, linked frame, "
        "and neither legal w-decoration has a strong realization"
    )


if __name__ == "__main__":
    main()
