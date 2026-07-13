#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Sharpness check for the singleton-hub arc-lock geometry.

This is not a K7-free obstruction: the script also checks its explicit
K7 model. It shows that strict interface surplus and one-step state
creation can both be saturated, so K7 exclusion must enter the next lemma.
"""

from __future__ import annotations

import itertools


BOUNDARY_EDGES = {
    tuple(sorted((i, (i + 1) % 6))) for i in range(6)
} | {(i, 6) for i in range(6)}

# D is W5: hub 7 and rim 8,...,12.
D_VERTICES = tuple(range(7, 13))
HUB = 7
RIM = tuple(range(8, 13))
D_EDGES = {(HUB, x) for x in RIM} | {
    tuple(sorted((RIM[i], RIM[(i + 1) % 5]))) for i in range(5)
}

# Every D vertex sees the common triangle {0,1,6}; rim vertex 8 sees
# the remaining boundary labels. Thus P={hub} has the short arc row
# and Q=rim has the full row.
CONTACTS = {x: {0, 1, 6} for x in D_VERTICES}
CONTACTS[8] |= {2, 3, 4, 5}


def canonical_partitions() -> tuple[tuple[int, ...], ...]:
    out: list[tuple[int, ...]] = []

    def rec(word: list[int], maximum: int) -> None:
        if len(word) == 7:
            state = tuple(word)
            if max(state) >= 6:
                return
            if any(state[i] == state[(i + 1) % 6] for i in range(6)):
                return
            if any(state[i] == state[6] for i in range(6)):
                return
            out.append(state)
            return
        for colour in range(min(maximum + 1, 5) + 1):
            if colour <= maximum + 1:
                word.append(colour)
                rec(word, max(maximum, colour))
                word.pop()

    rec([0], 0)
    return tuple(out)


STATES = canonical_partitions()


def colourable(
    vertices: tuple[int, ...],
    edges: set[tuple[int, int]],
    contacts: dict[int, set[int]],
    state: tuple[int, ...],
) -> bool:
    available = {
        x: tuple(
            c for c in range(6)
            if c not in {state[s] for s in contacts[x]}
        )
        for x in vertices
    }
    neighbours = {x: set() for x in vertices}
    for x, y in edges:
        neighbours[x].add(y)
        neighbours[y].add(x)
    order = tuple(sorted(vertices, key=lambda x: len(available[x])))
    colouring: dict[int, int] = {}

    def search(index: int) -> bool:
        if index == len(order):
            return True
        x = order[index]
        for colour in available[x]:
            if all(colouring.get(y) != colour for y in neighbours[x]):
                colouring[x] = colour
                if search(index + 1):
                    return True
                del colouring[x]
        return False

    return search(0)


def contract_edge(edge: tuple[int, int]):
    x, y = edge
    z = min(x, y)
    keep = tuple(v for v in D_VERTICES if v not in edge)
    vertices = (z,) + keep
    image = {x: z, y: z} | {v: v for v in keep}
    edges = {
        tuple(sorted((image[u], image[v])))
        for u, v in D_EDGES
        if image[u] != image[v]
    }
    contacts = {v: set(CONTACTS[v]) for v in keep}
    contacts[z] = CONTACTS[x] | CONTACTS[y]
    return vertices, edges, contacts


def connected(bag: set[int], edges: set[tuple[int, int]]) -> bool:
    reached = {next(iter(bag))}
    while True:
        expanded = reached | {
            y
            for edge in edges
            for x, y in (edge, edge[::-1])
            if x in reached and y in bag
        }
        if expanded == reached:
            return reached == bag
        reached = expanded


def verify_k7_model() -> None:
    edges = set(BOUNDARY_EDGES) | set(D_EDGES)
    edges |= {
        tuple(sorted((s, x)))
        for x, row in CONTACTS.items()
        for s in row
    }
    bags = ({0}, {1}, {6}, {7}, {8}, {9}, {10, 11, 12})
    assert all(connected(bag, edges) for bag in bags)
    for first, second in itertools.combinations(bags, 2):
        assert any(
            tuple(sorted((x, y))) in edges
            for x in first for y in second
        )


def main() -> None:
    assert len(STATES) == 40
    original = {
        state for state in STATES
        if colourable(D_VERTICES, set(D_EDGES), CONTACTS, state)
    }
    assert not original

    for edge in sorted(D_EDGES):
        deletion = {
            state for state in STATES
            if colourable(
                D_VERTICES, set(D_EDGES) - {edge}, CONTACTS, state
            )
        }
        vertices, edges, contacts = contract_edge(edge)
        contraction = {
            state for state in STATES
            if colourable(vertices, edges, contacts, state)
        }
        assert len(deletion) == 31
        assert deletion == contraction
        assert deletion - original

    assert len(CONTACTS[HUB]) + len(RIM) == 8
    assert len(set().union(*(CONTACTS[x] for x in RIM))) + 1 == 8
    verify_k7_model()
    print("40 boundary states checked")
    print("all 10 wheel edges: deletion = contraction = 31 new states")
    print("both portal separators have order 8")
    print("explicit K7 model verified")


if __name__ == "__main__":
    main()

