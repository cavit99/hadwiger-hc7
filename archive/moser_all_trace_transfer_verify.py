#!/usr/bin/env python3
"""Verify all pure-Moser exact traces under supported-pair transfer.

This reconstructs the ten traces from the labelled boundary and solves the
finite exact-state ownership constraints independently of the handwritten
orientation proof.
"""

import itertools

import z3


N = tuple(range(7))
M = {
    tuple(sorted(edge))
    for edge in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}
NONEDGES = tuple(edge for edge in itertools.combinations(N, 2) if edge not in M)


def trace(repeated):
    missing = tuple(edge for edge in NONEDGES if set(edge).isdisjoint(repeated))
    disjoint = tuple(
        (i, j)
        for i, j in itertools.combinations(range(len(missing)), 2)
        if set(missing[i]).isdisjoint(missing[j])
    )
    return missing, disjoint


def degree_sequence(vertex_count, edges):
    return tuple(sorted(sum(vertex in edge for edge in edges) for vertex in range(vertex_count)))


def mixed_survivors(missing, disjoint):
    survivors = []
    for symbols in itertools.product("12B", repeat=len(missing)):
        if "1" not in symbols or "2" not in symbols:
            continue
        double = [z3.Int(f"d_{i}") for i in range(len(missing))]
        triple = {edge: z3.Int(f"t_{edge[0]}_{edge[1]}") for edge in disjoint}
        solver = z3.Solver()
        for variable in double + list(triple.values()):
            solver.add(variable >= 0, variable <= 2)

        # One-swap states.
        for i, symbol in enumerate(symbols):
            if symbol == "1":
                solver.add(double[i] == 2)
            elif symbol == "2":
                solver.add(double[i] == 1)

        # Two-anchor coverage on both sides.
        for side in (1, 2):
            for i in range(len(missing)):
                solver.add(z3.Or(
                    double[i] == side,
                    *(triple[edge] == side for edge in disjoint if i in edge),
                ))

        # Supported-pair transfer.  Ownership values already encode
        # exact-state exclusivity.
        for edge in disjoint:
            i, j = edge
            if symbols[i] in "1B" and symbols[j] in "1B":
                solver.add(triple[edge] == 2)
            if symbols[i] in "2B" and symbols[j] in "2B":
                solver.add(triple[edge] == 1)

        if solver.check() == z3.sat:
            survivors.append("".join(symbols))
    return survivors


EXPECTED_C6 = {(0, 5), (0, 6)}
EXPECTED_C5 = {(1, 3), (1, 4), (2, 3), (2, 4)}
EXPECTED_P5 = {(1, 5), (2, 5), (3, 6), (4, 6)}
assert set(NONEDGES) == EXPECTED_C6 | EXPECTED_C5 | EXPECTED_P5

for repeated in NONEDGES:
    missing, disjoint = trace(repeated)
    roots = tuple(sorted(set(N) - set(repeated)))
    root_index = {vertex: index for index, vertex in enumerate(roots)}
    f_degrees = degree_sequence(5, [
        tuple(sorted(root_index[x] for x in edge))
        for edge in missing
    ])
    p_degrees = degree_sequence(len(missing), disjoint)

    if repeated in EXPECTED_C6:
        assert len(missing) == 6 and f_degrees == (2, 2, 2, 3, 3)
        assert len(disjoint) == 6 and p_degrees == (2, 2, 2, 2, 2, 2)
    elif repeated in EXPECTED_C5:
        assert len(missing) == 5 and f_degrees == (2, 2, 2, 2, 2)
        assert len(disjoint) == 5 and p_degrees == (2, 2, 2, 2, 2)
    else:
        assert len(missing) == 5 and f_degrees == (1, 2, 2, 2, 3)
        assert len(disjoint) == 4 and p_degrees == (1, 1, 2, 2, 2)

    survivors = mixed_survivors(missing, disjoint)
    if repeated == (0, 5):
        assert survivors == ["121212", "212121"]
    elif repeated == (0, 6):
        assert survivors == ["111222", "222111"]
    else:
        assert survivors == []

print("verified all ten pure-Moser traces")
print("types: 2 K2,3/C6; 4 C5/C5; 4 (C4+leaf)/P5")
print("mixed survivors: only the two alternating binary words in each C6 trace")
