#!/usr/bin/env python3
"""Exact K7-minor probe for the extra portal in the order-six Moser cell.

The quotient contracts each of the two connected full terminal shores to
one vertex.  The only optional edges are from the extra portal w to the five
unique roots U.  A positive model lifts literally to the original graph.

This is a discovery/falsification aid.  It prints every negative contact
set and the inclusion-minimal positive contact sets, together with exact
branch-set certificates for the latter.
"""

from __future__ import annotations

N = 11
V, W, DA, DB = 7, 8, 9, 10
U = (0, 2, 4, 5, 6)
MOSER = (
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
)


def adjacency(contact_mask: int) -> list[int]:
    adj = [0] * N

    def edge(x: int, y: int) -> None:
        adj[x] |= 1 << y
        adj[y] |= 1 << x

    for edge_pair in MOSER:
        edge(*edge_pair)
    for root in range(7):
        edge(V, root)
    for label in (*U, W, 1):
        edge(DA, label)
    for label in (*U, W, 3):
        edge(DB, label)
    for index, root in enumerate(U):
        if contact_mask >> index & 1:
            edge(W, root)
    return adj


def clique_minor_model(adj: list[int], target: int = 7) -> tuple[int, ...] | None:
    connected: list[int] = []
    for mask in range(1, 1 << N):
        seed = mask & -mask
        seen = seed
        while True:
            nxt = seen
            rest = seen
            while rest:
                bit = rest & -rest
                rest -= bit
                nxt |= adj[bit.bit_length() - 1] & mask
            if nxt == seen:
                break
            seen = nxt
        if seen == mask:
            connected.append(mask)

    neighbourhood = {}
    for branch in connected:
        nbr = 0
        rest = branch
        while rest:
            bit = rest & -rest
            rest -= bit
            nbr |= adj[bit.bit_length() - 1]
        neighbourhood[branch] = nbr

    def search(chosen: tuple[int, ...], used: int, start: int):
        if len(chosen) == target:
            return chosen
        if N - used.bit_count() < target - len(chosen):
            return None
        for index in range(start, len(connected)):
            branch = connected[index]
            if branch & used:
                continue
            if all(neighbourhood[branch] & old for old in chosen):
                answer = search(chosen + (branch,), used | branch, index + 1)
                if answer is not None:
                    return answer
        return None

    return search((), 0, 0)


def solve(mask: int):
    return mask, clique_minor_model(adjacency(mask))


def roots(mask: int) -> tuple[int, ...]:
    return tuple(root for index, root in enumerate(U) if mask >> index & 1)


def bags(model: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(i for i in range(N) if branch >> i & 1) for branch in model)


def main() -> None:
    results = dict(solve(mask) for mask in range(1 << len(U)))

    negative = [mask for mask, model in results.items() if model is None]
    positive = [mask for mask, model in results.items() if model is not None]
    minimal_positive = [
        mask for mask in positive
        if not any(other != mask and other & mask == other for other in positive)
    ]

    print("negative", len(negative), [roots(mask) for mask in negative])
    print("minimal_positive", len(minimal_positive))
    for mask in minimal_positive:
        print(roots(mask), bags(results[mask]))

    # Monotonicity sanity check: every positive state remains positive after
    # adding optional edges.
    for mask in positive:
        for extra in range(1 << len(U)):
            if mask & extra == mask:
                assert results[extra] is not None


if __name__ == "__main__":
    main()
