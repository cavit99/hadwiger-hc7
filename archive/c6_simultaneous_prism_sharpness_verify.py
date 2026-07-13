#!/usr/bin/env python3
"""Exact sharpness check for the simultaneous six-state packet.

The triangular prism, with one singleton representative for every portal
class, has all three antipodal demand linkages absent and owns every frame.
Thus a simultaneous-web theorem must allow a coherent prism/disk outcome;
the packet hypotheses alone cannot force a crossing.
"""

from __future__ import annotations

import networkx as nx


def main() -> None:
    host = nx.circular_ladder_graph(3)
    vertices = tuple(host)
    # Portal class i is the singleton roots[i].
    roots = (0, 4, 2, 3, 1, 5)
    assert len(set(roots)) == 6

    connected = tuple(
        mask for mask in range(1, 1 << len(vertices))
        if nx.is_connected(host.subgraph(
            vertices[index]
            for index in range(len(vertices))
            if mask >> index & 1
        ))
    )

    def linked(a: int, b: int, c: int, d: int) -> bool:
        first = tuple(
            mask for mask in connected
            if mask >> roots[a] & 1 and mask >> roots[b] & 1
        )
        second = tuple(
            mask for mask in connected
            if mask >> roots[c] & 1 and mask >> roots[d] & 1
        )
        return any(not (x & y) for x in first for y in second)

    antipodal = tuple(
        linked(i, (i + 1) % 6, (i + 3) % 6, (i + 4) % 6)
        for i in range(3)
    )
    frames = tuple(
        linked((i - 2) % 6, (i - 1) % 6,
               (i + 2) % 6, (i + 3) % 6)
        for i in range(6)
    )
    relabelled_edges = tuple(sorted(
        tuple(sorted((roots.index(u), roots.index(v))))
        for u, v in host.edges()
    ))

    assert nx.node_connectivity(host) == 3
    assert antipodal == (False, False, False)
    assert frames == (True, True, True, True, True, True)
    assert relabelled_edges == (
        (0, 2), (0, 3), (0, 4),
        (1, 3), (1, 4), (1, 5),
        (2, 4), (2, 5), (3, 5),
    )

    print("portal roots", roots)
    print("host connectivity", nx.node_connectivity(host))
    print("antipodal linkages", antipodal)
    print("owned frames", frames)
    print("relabelled prism edges", relabelled_edges)


if __name__ == "__main__":
    main()
