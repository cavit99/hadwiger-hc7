"""Replay the hand certificates for the rank-two packet circuits.

This verifier uses no minor search.  For every orientation of every
fully-positive matching in the seven-edge atlas, it constructs the seven
bags stated in ``hadwiger_atomic_three_packet_core_completion.md`` and
checks connectedness, disjointness, and all 21 adjacencies.
"""

from __future__ import annotations

from atomic_three_packet_actual_gate_search import (
    CIRCUITS,
    gate_graph,
    mappings,
)
from equality_gate_seven_edge_packet_atlas import FULL_PACKET_TRIANGLES


SDR5 = {
    0: (3, 2, 5, 1, 4),
    1: (0, 2, 5, 3, 4),
    2: (0, 4, 5, 3, 1),
    3: (0, 2, 5, 1, 4),
    4: (0, 2, 5, 3, 1),
    5: (0, 2, 1, 3, 4),
}

SDR6 = {
    0: (4, 2, 1, 5, 3),
    1: (4, 0, 5, 2, 3),
    2: (4, 0, 1, 5, 3),
    3: (4, 0, 5, 2, 1),
    4: (0, 2, 1, 5, 3),
    5: (4, 0, 1, 2, 3),
}

BOUNDARY_K4 = {
    7: (0, ((1,), (3,), (4,), (6,))),
    8: (0, ((1,), (3,), (6,), (2, 4, 5))),
    9: (0, ((1,), (3,), (4,), (2, 5, 6))),
    10: (1, ((0,), (2,), (4,), (6,))),
    11: (0, ((3,), (5,), (1, 6), (2, 4))),
    16: (0, ((1,), (2,), (5,), (3, 4))),
    29: (0, ((1,), (3,), (5,), (2, 6))),
}


def verify(graph, bags) -> None:
    assert len(bags) == 7 and all(bags)
    assert all(bags[i].isdisjoint(bags[j]) for i in range(7) for j in range(i))
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                neighbour
                for vertex in reached
                for neighbour in graph.neighbors(vertex)
                if neighbour in bag
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    assert all(
        any(graph.has_edge(left, right) for left in bags[i] for right in bags[j])
        for i in range(7)
        for j in range(i)
    )


def choose_omitted(graph, mapping):
    singleton = mapping[6]
    return next(
        local
        for local in range(6)
        if graph.has_edge(singleton, mapping[local])
    )


def certificate(order, index, graph, mapping):
    helper = 7 + order
    singleton = mapping[6]
    if order == 2:
        removed, boundary_model = BOUNDARY_K4[index]
        return ({7}, {8}) + tuple(set(bag) for bag in boundary_model) + ({removed, helper},)
    if order == 4:
        adjacent_common = [
            local for local in (4, 5)
            if graph.has_edge(singleton, mapping[local])
        ]
        if adjacent_common:
            near = adjacent_common[0]
            far = 9 - near
            return (
                {9, mapping[0], mapping[far]},
                {8, mapping[3]},
                {7, mapping[2]},
                {10, mapping[1]},
                {helper},
                {mapping[near]},
                {singleton},
            )

        # The sole symmetry-essential exceptional row.  Let c0 be the
        # endpoint of the common pair with one extra missing edge into
        # each grid pair; c1 is its mate.  The audited funnel forces this
        # exact pattern when s misses both common endpoints.
        common = (mapping[4], mapping[5])
        c0 = next(
            endpoint for endpoint in common
            if sum(not graph.has_edge(endpoint, mapping[local]) for local in range(4)) == 2
        )
        c1 = next(endpoint for endpoint in common if endpoint != c0)
        a0 = next(mapping[local] for local in (0, 1) if not graph.has_edge(c0, mapping[local]))
        a1 = next(mapping[local] for local in (0, 1) if mapping[local] != a0)
        b0 = next(mapping[local] for local in (2, 3) if not graph.has_edge(c0, mapping[local]))
        b1 = next(mapping[local] for local in (2, 3) if mapping[local] != b0)

        local_rows = CIRCUITS[4][1]
        inverse = {actual: local for local, actual in mapping.items()}
        def core_with(left, right):
            return 7 + next(
                vertex
                for vertex, row in enumerate(local_rows)
                if inverse[left] in row and inverse[right] in row
            )

        x00 = core_with(a0, b0)
        x10 = core_with(a1, b0)
        x01 = core_with(a0, b1)
        return (
            {a0},
            {b0},
            {c1},
            {x00},
            {a1, singleton},
            {x10, x01},
            {c0, helper},
        )

    omitted = choose_omitted(graph, mapping)
    if order == 5:
        core = ({7}, {8}, {9}, {10}, {11})
        assignment = SDR5[omitted]
    else:
        core = ({7, 8}, {9}, {10}, {11}, {12})
        assignment = SDR6[omitted]
    rooted = tuple(core[index] | {mapping[root]} for index, root in enumerate(assignment))
    return rooted + ({helper}, {singleton, mapping[omitted]})


def main() -> None:
    counts = {2: 0, 4: 0, 5: 0, 6: 0}
    for order in CIRCUITS:
        for index, matching in FULL_PACKET_TRIANGLES.items():
            for mapping in mappings(matching):
                graph = gate_graph(index, mapping, order)
                verify(graph, certificate(order, index, graph, mapping))
                counts[order] += 1
    print("explicit core-completion certificates", counts)


if __name__ == "__main__":
    main()
