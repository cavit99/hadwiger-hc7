#!/usr/bin/env python3
"""Verify the finite boundary claims in the boundary-operation barrier."""

from itertools import combinations


S = ("j0", "b", "r", "j1", "z1", "z2", "q")
TRIANGLES = (
    frozenset(("j0", "b", "r")),
    frozenset(("j1", "z1", "z2")),
)
EDGES = {
    frozenset(edge)
    for triangle in TRIANGLES
    for edge in combinations(triangle, 2)
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def partitions(items, max_blocks=6):
    blocks = []

    def visit(index):
        if index == len(items):
            yield frozenset(frozenset(block) for block in blocks)
            return
        item = items[index]
        for block in blocks:
            block.append(item)
            yield from visit(index + 1)
            block.pop()
        if len(blocks) < max_blocks:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def independent(block):
    return all(not edge <= block for edge in EDGES)


def proper(partition):
    return all(independent(block) for block in partition)


def restrict(partition, deleted):
    return frozenset(block - {deleted} for block in partition if block - {deleted})


def main():
    omega = {partition for partition in partitions(S) if proper(partition)}
    even = {partition for partition in omega if len(partition) % 2 == 0}
    odd = omega - even

    pi_star = frozenset(
        (
            frozenset(("j0", "j1", "q")),
            frozenset(("b", "z1")),
            frozenset(("r",)),
            frozenset(("z2",)),
        )
    )
    pi_z1 = frozenset(
        (
            frozenset(("j0", "j1", "q")),
            frozenset(("b",)),
            frozenset(("r",)),
            frozenset(("z2",)),
            frozenset(("z1",)),
        )
    )
    pi_z2 = frozenset(
        (
            frozenset(("j0", "j1", "q")),
            frozenset(("b", "z1")),
            frozenset(("r", "z2")),
        )
    )

    require(pi_star in even, "Pi_* is not an even proper state")
    require(pi_z1 in odd, "the z1-deletion partner is not an odd proper state")
    require(pi_z2 in odd, "the z2-deletion partner is not an odd proper state")
    require(
        restrict(pi_star, "z1") == restrict(pi_z1, "z1"),
        "z1-deletion traces differ",
    )
    require(
        restrict(pi_star, "z2") == restrict(pi_z2, "z2"),
        "z2-deletion traces differ",
    )

    for edge in EDGES:
        edge_state = frozenset(
            [edge] + [frozenset((vertex,)) for vertex in S if vertex not in edge]
        )
        require(len(edge_state) == 6, f"edge state for {sorted(edge)} has wrong size")
        require(edge_state not in omega, f"edge state for {sorted(edge)} is proper on H")
        remaining_edges = EDGES - {edge}
        require(
            all(not other <= block for block in edge_state for other in remaining_edges),
            f"edge state for {sorted(edge)} is not proper on H-e",
        )

    independent_sets = {
        frozenset(subset)
        for size in range(1, len(S) + 1)
        for subset in combinations(S, size)
        if independent(frozenset(subset))
    }
    for block in independent_sets:
        require(
            any(block in partition for partition in even),
            f"even language misses exact block {sorted(block)}",
        )
        require(
            any(block in partition for partition in odd),
            f"odd language misses exact block {sorted(block)}",
        )

    print("GREEN boundary operation parity barrier")
    print(f"states={len(omega)} even={len(even)} odd={len(odd)}")
    print(f"boundary_edges={len(EDGES)} independent_sets={len(independent_sets)}")


if __name__ == "__main__":
    main()
