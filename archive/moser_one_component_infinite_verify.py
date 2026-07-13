#!/usr/bin/env python3
"""Verify two finite representative lemmas used for infinite exterior classes.

The first check treats three one-defect components behind a cutvertex.
The second asks Z3 for a counterexample to the six-shore path
representative lemma.  UNSAT proves that no such counterexample exists.
"""

import itertools

import z3


N = tuple(range(7))
M_EDGES = {
    tuple(sorted(e))
    for e in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
TRIANGLES = tuple(
    frozenset(t)
    for t in itertools.combinations(N, 3)
    if all(tuple(sorted(e)) in M_EDGES for e in itertools.combinations(t, 2))
)


def adjacent(x, y):
    return tuple(sorted((x, y))) in M_EDGES


def branching_witness(defects):
    """Return a triangle and three anchors, or None."""
    for triangle in TRIANGLES:
        available = set(N) - triangle
        for anchors in itertools.permutations(available, 3):
            if any(anchors[i] in defects[i] for i in range(3)):
                continue
            if any(
                anchors[i] in defects[j] and anchors[j] in defects[i]
                for i, j in itertools.combinations(range(3), 2)
            ):
                continue
            if any(
                t in defects[i] and not adjacent(anchors[i], t)
                for i in range(3) for t in triangle
            ):
                continue
            return triangle, anchors
    return None


def verify_branching_lemma():
    defects = (frozenset(),) + tuple(frozenset((x,)) for x in N)
    cases = 0
    for triple in itertools.product(defects, repeat=3):
        assert branching_witness(triple) is not None, triple
        cases += 1
    return cases


def verify_path_lemma():
    """Search for six defect sets for which every injection is invalid."""
    rows = 6
    membership = [
        [z3.Bool(f"s_{i}_{x}") for x in N]
        for i in range(rows)
    ]
    solver = z3.Solver()

    for i in range(rows):
        bound = 1 if i in (0, rows - 1) else 2
        solver.add(z3.PbLe([(membership[i][x], 1) for x in N], bound))

    # The six shores together see every boundary vertex.
    for x in N:
        solver.add(z3.Or([z3.Not(membership[i][x]) for i in range(rows)]))

    injections = 0
    for representative in itertools.permutations(N, rows):
        invalid = [membership[i][representative[i]] for i in range(rows)]
        for i, j in itertools.combinations(range(rows), 2):
            if j == i + 1:
                continue
            invalid.append(z3.And(
                membership[i][representative[j]],
                membership[j][representative[i]],
            ))
        # A counterexample set system has no valid representative injection.
        solver.add(z3.Or(invalid))
        injections += 1

    status = solver.check()
    assert status == z3.unsat, status
    return injections


def verify_path_lemma_direct():
    """Independently check all maximal systems, modulo boundary relabeling."""
    pairs = tuple(itertools.combinations(N, 2))
    injections = tuple(itertools.permutations(N, 6))

    def image(sequence, permutation):
        return tuple(
            tuple(sorted((permutation[a], permutation[b])))
            for a, b in sequence
        )

    def witness(sequence, first, last):
        defects = ({first}, *map(set, sequence), {last})
        for representative in injections:
            if any(representative[i] in defects[i] for i in range(6)):
                continue
            if any(
                representative[j] in defects[i]
                and representative[i] in defects[j]
                for i, j in itertools.combinations(range(6), 2)
                if j != i + 1
            ):
                continue
            return representative
        return None

    def check_normal_form(first, last, movable):
        permutations = []
        for target in itertools.permutations(movable):
            permutation = list(N)
            for source, value in zip(movable, target):
                permutation[source] = value
            permutations.append(permutation)

        systems = set(itertools.product(pairs, repeat=4))
        if first == last:
            systems = {
                sequence for sequence in systems
                if not all(first in pair for pair in sequence)
            }

        orbits = 0
        while systems:
            sequence = next(iter(systems))
            orbit = {image(sequence, permutation) for permutation in permutations}
            systems.difference_update(orbit)
            assert witness(sequence, first, last) is not None, sequence
            orbits += 1
        return orbits

    distinct = check_normal_form(0, 1, (2, 3, 4, 5, 6))
    equal = check_normal_form(0, 0, (1, 2, 3, 4, 5, 6))
    return distinct, equal


branch_cases = verify_branching_lemma()
path_orbits = verify_path_lemma_direct()
path_injections = verify_path_lemma()
print(f"branching cases verified: {branch_cases}")
print(
    "path maximal-system orbits verified directly: "
    f"{path_orbits[0]} distinct-end + {path_orbits[1]} equal-end"
)
print(f"path injections excluded in counterexample encoding: {path_injections}")
print("path representative counterexample formula: UNSAT")
