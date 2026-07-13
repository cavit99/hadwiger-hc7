#!/usr/bin/env python3
"""Exact 7-fan certificate for a one-ear C6 shore leaf.

The contact labels are those of the original atlas, whose missing cycle
is 0-4-2-3-1-5-0.  The normalized unique portal is 0, so the two fan
arms end at 4 and 5.  The body of the shore is deliberately deleted:
only the two internally disjoint fan arms are contracted.  Therefore a
model printed here lifts without assuming that their complement in the
body is connected.
"""

from __future__ import annotations

import networkx as nx

from c6_cycle_leaf_probe import quotient_one_vertex
from c6_portal_tetrahedron_verify import has_k7_minor


BROAD = (6, 70)   # {c_2,c_4}, optionally also z
THIN = (8, 72)    # {c_3}, optionally also z


def fan_quotient(p_mask: int, q_mask: int, orientation: tuple[int, int]):
    graph = quotient_one_vertex(126, p_mask, q_mask)
    # Nodes 9 and 10 are p,q; 4 and 5 are the two missing rim labels.
    graph.add_edge(9, orientation[0])
    graph.add_edge(10, orientation[1])
    # Node 8 is the contracted body.  It is not used by the certificate.
    graph.remove_node(8)
    return nx.convert_node_labels_to_integers(graph)


def old_labels(model: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    # After deleting old node 8, relabelled nodes 8,9,10 are old p,q,H.
    old = tuple(range(8)) + (9, 10, 11)
    return tuple(
        tuple(old[i] for i in range(11) if mask >> i & 1)
        for mask in model
    )


def main() -> None:
    for p_mask in BROAD + THIN:
        for q_mask in BROAD + THIN:
            for orientation in ((4, 5), (5, 4)):
                model, checked = has_k7_minor(
                    fan_quotient(p_mask, q_mask, orientation)
                )
                expected = p_mask in BROAD or q_mask in BROAD
                assert (model is not None) == expected
                print(
                    "rows", (p_mask, q_mask),
                    "arms", orientation,
                    "model", None if model is None else old_labels(model),
                    "checked", checked,
                )


if __name__ == "__main__":
    main()
