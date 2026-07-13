#!/usr/bin/env python3
"""Dependency-free certificate for the pure-Moser triangular-shore lemma.

The ten-vertex crossed page consists of the seven literal Moser vertices,
the apex v, and one internal vertex on each of the disjoint 0--5 and 2--4
paths.  We enumerate every literal boundary-meeting K4 model in this page.
For every unordered triple of boundary defects of order at most two whose
total intersection is empty, we certify a model each of whose four bags is
seen by all three corresponding shore vertices.
"""

from hashlib import sha256
from itertools import combinations, combinations_with_replacement


S_MASK = (1 << 7) - 1
MOSER_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 6), (2, 6),
    (3, 4), (3, 5), (4, 5), (5, 6),
}


def crossed_page() -> list[int]:
    # 0,...,6 are literal boundary vertices; 7=v; 8=p05; 9=p24.
    adjacency = [0] * 10

    def add_edge(left: int, right: int) -> None:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left

    for left, right in MOSER_EDGES:
        add_edge(left, right)
    for boundary in range(7):
        add_edge(7, boundary)
    add_edge(0, 8)
    add_edge(8, 5)
    add_edge(2, 9)
    add_edge(9, 4)
    return adjacency


def connected(vertex_set: int, adjacency: list[int]) -> bool:
    reached = vertex_set & -vertex_set
    while True:
        expanded = reached
        scan = reached
        while scan:
            bit = scan & -scan
            scan -= bit
            expanded |= adjacency[bit.bit_length() - 1] & vertex_set
        if expanded == reached:
            return reached == vertex_set
        reached = expanded


def boundary_k4_models(adjacency: list[int]) -> dict[tuple[int, ...], tuple[int, ...]]:
    connected_sets = [
        vertex_set
        for vertex_set in range(1, 1 << 10)
        if vertex_set & S_MASK and connected(vertex_set, adjacency)
    ]
    neighbours = {}
    for vertex_set in connected_sets:
        union = 0
        scan = vertex_set
        while scan:
            bit = scan & -scan
            scan -= bit
            union |= adjacency[bit.bit_length() - 1]
        neighbours[vertex_set] = union

    models: dict[tuple[int, ...], tuple[int, ...]] = {}

    def search(chosen: list[int], used: int, start: int) -> None:
        if len(chosen) == 4:
            ordered = tuple(sorted(chosen, key=lambda bag: (bag & S_MASK, bag)))
            trace = tuple(bag & S_MASK for bag in ordered)
            models.setdefault(trace, ordered)
            return
        for index in range(start, len(connected_sets)):
            bag = connected_sets[index]
            if bag & used:
                continue
            if any(not (neighbours[bag] & old_bag) for old_bag in chosen):
                continue
            search(chosen + [bag], used | bag, index + 1)

    search([], 0, 0)
    return models


def main() -> None:
    models = boundary_k4_models(crossed_page())
    defect_sets = [
        sum(1 << vertex for vertex in choice)
        for size in range(3)
        for choice in combinations(range(7), size)
    ]

    records = []
    for defects in combinations_with_replacement(defect_sets, 3):
        # Empty total intersection is exactly fullness of the three-vertex
        # shore: no boundary label is missed by all three vertices.
        if defects[0] & defects[1] & defects[2]:
            continue
        contacts = tuple(S_MASK ^ defect for defect in defects)
        witness = next(
            (
                trace
                for trace in sorted(models)
                if all(
                    all(trace_bag & contact for trace_bag in trace)
                    for contact in contacts
                )
            ),
            None,
        )
        assert witness is not None, defects
        records.append((defects, witness))

    payload = "\n".join(
        f"{','.join(map(str, defects))}:{','.join(map(str, witness))}"
        for defects, witness in records
    ).encode()
    digest = sha256(payload).hexdigest()
    assert len(models) == 598
    assert len(records) == 3928
    print(f"boundary_K4_models={len(models)}")
    print(f"defect_triples={len(records)} failures=0")
    print(f"certificate_sha256={digest}")


if __name__ == "__main__":
    main()
