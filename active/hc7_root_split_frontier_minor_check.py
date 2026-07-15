"""Test the canonical root split against every audited width-two frontier.

The canonical carriers are X={z} and Y=A-z.  Thus the compulsory boundary
vertex u has list {X}; every other boundary vertex has list {Y} or {X,Y}.
For every seven-vertex tree and C6 with one pendant vertex, this script
checks whether failure of the adaptive singleton-reservoir return already
forces five disjoint, connected, pairwise adjacent bags each meeting S in
the literal two-carrier quotient.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx

from hc7_two_list_reservoir_obstruction_check import frontiers, has_return


def connected_masks(graph: nx.Graph) -> list[int]:
    nodes = tuple(graph)
    ans: list[int] = []
    for mask in range(1, 1 << len(nodes)):
        chosen = [v for v in nodes if mask & (1 << v)]
        if nx.is_connected(graph.subgraph(chosen)):
            ans.append(mask)
    return ans


def has_s_rooted_k5(graph: nx.Graph) -> bool:
    """Return whether five compatible connected bags each meet S={0,...,6}."""

    candidates = [mask for mask in connected_masks(graph) if mask & 0x7F]
    neighbours = [0] * len(candidates)
    edge_masks = [(1 << x) | (1 << y) for x, y in graph.edges]

    for i, left in enumerate(candidates):
        for j in range(i + 1, len(candidates)):
            right = candidates[j]
            if left & right:
                continue
            if not any((edge & left) and (edge & right) for edge in edge_masks):
                continue
            neighbours[i] |= 1 << j
            neighbours[j] |= 1 << i

    def clique(extension: tuple[int, ...], available: int) -> bool:
        if len(extension) == 5:
            return True
        if available.bit_count() < 5 - len(extension):
            return False
        while available:
            bit = available & -available
            available ^= bit
            index = bit.bit_length() - 1
            if clique((*extension, index), available & neighbours[index]):
                return True
        return False

    return clique((), (1 << len(candidates)) - 1)


def quotient(frontier: nx.Graph, masks: tuple[int, ...]) -> nx.Graph:
    graph = frontier.copy()
    graph.add_nodes_from((7, 8))  # X,Y
    graph.add_edge(7, 8)
    for vertex, mask in enumerate(masks):
        if mask & 1:
            graph.add_edge(vertex, 7)
        if mask & 2:
            graph.add_edge(vertex, 8)
    return graph


def main() -> None:
    checked = 0
    no_return = 0
    rooted = 0
    unresolved: list[tuple[str, int, tuple[int, ...]]] = []

    for name, graph in frontiers():
        for compulsory in graph:
            others = [v for v in graph if v != compulsory]
            for choices in product((2, 3), repeat=6):
                masks = [0] * 7
                masks[compulsory] = 1
                for vertex, mask in zip(others, choices, strict=True):
                    masks[vertex] = mask
                masks_tuple = tuple(masks)
                checked += 1
                if has_return(graph, masks_tuple):
                    continue
                no_return += 1
                if has_s_rooted_k5(quotient(graph, masks_tuple)):
                    rooted += 1
                else:
                    unresolved.append((name, compulsory, masks_tuple))

    print(
        "ROOT_SPLIT_FRONTIER",
        "checked", checked,
        "no_return", no_return,
        "rooted_k5", rooted,
        "unresolved", len(unresolved),
    )
    for item in unresolved[:40]:
        print("UNRESOLVED", item)


if __name__ == "__main__":
    main()
