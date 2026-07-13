#!/usr/bin/env python3
"""Verify the finite pentagon boundary-state lemma for the pure Moser cell.

This is a dependency-free exhaustive check of the *specialized* state axioms
used in ``hadwiger_moser_pentagon_boundary_lemma.md``.  It is not a search
for graphs and it is not used in place of the short propagation proofs in
that note.

The five vertices of ``P`` represent the five missing edges of the rooted
C5.  Two vertices of ``P`` are adjacent when the corresponding missing
edges are vertex-disjoint.  Thus ``P`` is again a C5.  A state is one of

    D_i       = {13, e_i},
    T_ij      = {13, e_i, e_j}  (ij in E(P)).

Every state may belong to side 1, side 2, or neither, but never both.
"""

from itertools import product


# The disjointness pentagon on e_0,...,e_4.
P_EDGES = ((0, 2), (0, 3), (1, 3), (1, 4), (2, 4))
STATES = tuple(("D", i) for i in range(5)) + tuple(
    ("T", i, j) for i, j in P_EDGES
)


def transforms(word: str):
    """Dihedral transforms of a cyclic word, also allowing 1<->2."""
    for reverse in (False, True):
        w = word[::-1] if reverse else word
        for shift in range(5):
            z = w[shift:] + w[:shift]
            yield z
            yield z.translate(str.maketrans("12", "21"))


def canonical(word: str) -> str:
    return min(transforms(word))


def compatible(word: str, assignment: tuple[int, ...]) -> bool:
    """Test one assignment; values 0,1,2 mean neither/side 1/side 2."""
    owner = dict(zip(STATES, assignment))

    # If e_i is supported only by side 1 (symbol 1), side 2 is
    # unsupported and hence contains D_i.  Likewise with 1 and 2 swapped.
    for i, symbol in enumerate(word):
        if symbol == "1" and owner[("D", i)] != 2:
            return False
        if symbol == "2" and owner[("D", i)] != 1:
            return False

    # Two-anchor coverage: on each side and at each i, one of D_i and the
    # two triples extending D_i must occur.
    for side in (1, 2):
        for i in range(5):
            extensions = [
                ("T", a, b) for a, b in P_EDGES if i == a or i == b
            ]
            if owner[("D", i)] != side and not any(
                owner[t] == side for t in extensions
            ):
                return False

    # Two commuting swaps: if two disjoint C5 edges are unsupported by
    # one side, the corresponding triple state occurs on that side.
    for i, j in P_EDGES:
        for side, unsupported_symbol in ((1, "2"), (2, "1")):
            if word[i] == word[j] == unsupported_symbol:
                if owner[("T", i, j)] != side:
                    return False

    return True


def feasible(word: str) -> bool:
    return any(compatible(word, a) for a in product(range(3), repeat=10))


def main() -> None:
    # A genuinely unconfined support word has a 1 and a 2.  The 14 orbit
    # representatives use the conventional order from the accompanying
    # note (rather than lexicographically canonical representatives).
    representatives = (
        "11112",
        "11122",
        "1112B",
        "11212",
        "1121B",
        "1122B",
        "112B2",
        "112BB",
        "11B2B",
        "1212B",
        "121BB",
        "12B1B",
        "12BBB",
        "1B2BB",
    )
    assert len({canonical(w) for w in representatives}) == 14

    all_words = {
        canonical("".join(w))
        for w in product("12B", repeat=5)
        if "1" in w and "2" in w
    }
    assert all_words == {canonical(w) for w in representatives}

    result = {word: feasible(word) for word in representatives}
    impossible = tuple(word for word, ok in result.items() if not ok)
    possible = tuple(word for word, ok in result.items() if ok)

    assert impossible == ("11112", "11122", "11212", "1121B", "1212B")
    print("infeasible:", " ".join(impossible))
    print("not excluded by these axioms:", " ".join(possible))

    # Verify the all-traces disjointness-graph table and the binary
    # cut-orientation criterion from Section 5 of the note.
    vertices = range(7)
    moser_edges = {
        tuple(sorted(e))
        for e in (
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        )
    }
    q_edges = sorted(
        e
        for e in __import__("itertools").combinations(vertices, 2)
        if e not in moser_edges
    )

    binary_survivors = {}
    degree_types = {}
    connected_types = {}
    for repeated in q_edges:
        f_edges = [e for e in q_edges if set(e).isdisjoint(repeated)]
        disjoint = [
            (i, j)
            for i in range(len(f_edges))
            for j in range(i + 1, len(f_edges))
            if set(f_edges[i]).isdisjoint(f_edges[j])
        ]
        degree_types[repeated] = tuple(
            sorted(sum(i in edge for edge in disjoint) for i in range(len(f_edges)))
        )
        reached = {0}
        while True:
            enlarged = reached | {
                b if a in reached else a
                for a, b in disjoint
                if a in reached or b in reached
            }
            if enlarged == reached:
                break
            reached = enlarged
        connected_types[repeated] = len(reached) == len(f_edges)

        survivors = []
        for bits in product((0, 1), repeat=len(f_edges)):
            if len(set(bits)) == 1:
                continue
            cut = [edge for edge in disjoint if bits[edge[0]] != bits[edge[1]]]
            unseen = set(range(len(f_edges)))
            cyclic_components = True
            while unseen:
                stack = [unseen.pop()]
                component = set(stack)
                while stack:
                    x = stack.pop()
                    for a, b in cut:
                        y = b if a == x else a if b == x else None
                        if y is not None and y not in component:
                            component.add(y)
                            unseen.discard(y)
                            stack.append(y)
                edge_count = sum(a in component and b in component for a, b in cut)
                if edge_count < len(component):
                    cyclic_components = False
            if cyclic_components:
                survivors.append(bits)
        binary_survivors[repeated] = survivors

    c6_repeats = {(0, 5), (0, 6)}
    c5_repeats = {(1, 3), (1, 4), (2, 3), (2, 4)}
    p5_repeats = {(1, 5), (2, 5), (3, 6), (4, 6)}
    assert set(q_edges) == c6_repeats | c5_repeats | p5_repeats
    assert all(connected_types.values())
    assert all(degree_types[r] == (2, 2, 2, 2, 2, 2) for r in c6_repeats)
    assert all(degree_types[r] == (2, 2, 2, 2, 2) for r in c5_repeats)
    assert all(degree_types[r] == (1, 1, 2, 2, 2) for r in p5_repeats)
    assert all(len(binary_survivors[r]) == 2 for r in c6_repeats)
    assert all(not binary_survivors[r] for r in c5_repeats | p5_repeats)
    print("binary mixed survivors by repeated pair:")
    for repeated in q_edges:
        print(" ", repeated, len(binary_survivors[repeated]))


if __name__ == "__main__":
    main()
