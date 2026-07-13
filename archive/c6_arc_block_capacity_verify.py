#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verify the six explicit K7 models in the four-label capacity lemma."""

from __future__ import annotations

from collections.abc import Iterable


Bag = tuple[int, ...]
Edge = tuple[int, int]


MODELS: dict[tuple[str, int], tuple[Bag, ...]] = {
    ("O", 2): ((0,), (1,), (6,), (8,), (5, 7), (3, 9), (2, 11)),
    ("O", 3): ((0,), (1,), (6,), (8,), (5, 7), (2, 9), (3, 11)),
    ("O", 4): ((0,), (1,), (6,), (8,), (5, 7), (2, 9), (3, 4, 11)),
    ("A", 2): ((0,), (1,), (6,), (8,), (9,), (2, 11), (3, 5, 7)),
    ("A", 3): ((0,), (1,), (6,), (8,), (9,), (3, 11), (2, 5, 7)),
    ("A", 4): ((0,), (1,), (6,), (8,), (9,), (2, 5, 7), (3, 4, 11)),
}


def edge(u: int, v: int) -> Edge:
    return (u, v) if u < v else (v, u)


def quotient(mode: str, extra_contact: int) -> set[Edge]:
    """Build the normalized nested-passage quotient.

    Vertices 0..5 are the C6 labels, 6 is z, 7 is the one-defect
    retained helper, 8 is the other full helper, 9 and 10 are the two
    arc pieces, and 11 is the peeled connector passage.
    """
    edges = {edge(i, (i + 1) % 6) for i in range(6)}
    edges |= {edge(i, 6) for i in range(6)}
    edges.add(edge(9, 10))
    edges.add(edge(7, 8) if mode == "O" else edge(8, 9))

    # Helper 7 has the sole defect c0; helper 8 is full.
    edges |= {edge(s, 7) for s in range(1, 7)}
    edges |= {edge(s, 8) for s in range(7)}

    # Complementary antipodal arc rows.
    edges |= {edge(s, 9) for s in (0, 1, 2, 3, 6)}
    edges |= {edge(s, 10) for s in (0, 3, 4, 5, 6)}

    # Nested passage c1--c0--c5, adjacent to its retained helper,
    # plus one forbidden contact outside the four-label block.
    edges |= {edge(s, 11) for s in (0, 1, 5, 7, extra_contact)}
    return edges


def connected(bag: Bag, edges: set[Edge]) -> bool:
    if not bag:
        return False
    seen = {bag[0]}
    frontier = [bag[0]]
    vertices = set(bag)
    while frontier:
        u = frontier.pop()
        for v in vertices - seen:
            if edge(u, v) in edges:
                seen.add(v)
                frontier.append(v)
    return seen == vertices


def adjacent(left: Bag, right: Bag, edges: set[Edge]) -> bool:
    return any(edge(u, v) in edges for u in left for v in right)


def verify_model(bags: Iterable[Bag], edges: set[Edge]) -> None:
    model = tuple(bags)
    assert len(model) == 7
    used: set[int] = set()
    for bag in model:
        assert connected(bag, edges), f"disconnected bag {bag}"
        assert used.isdisjoint(bag), f"overlapping bag {bag}"
        used.update(bag)
    for i, left in enumerate(model):
        for right in model[i + 1 :]:
            assert adjacent(left, right, edges), (left, right)


def main() -> None:
    for key, model in MODELS.items():
        mode, extra = key
        verify_model(model, quotient(mode, extra))
        print(f"verified mode={mode} extra=c{extra}: {model}")
    print(f"verified {len(MODELS)} explicit K7 models")


if __name__ == "__main__":
    main()
