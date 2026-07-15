"""Exhaust the two-label/singleton-reservoir obstruction on the HC7 frontiers.

This checks every nonempty list assignment L(v) subset {0,1} on every
unlabelled seven-vertex tree and on C6 with one pendant vertex.  A return is
a proper list colouring after deleting at most one vertex that uses both
labels.  A bad path joins two singleton-list vertices whose prescribed
labels have the wrong parity.  The proposed corrected dichotomy is:

    return, or two vertex-disjoint bad paths, or a monochromatic star.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx


def has_return(graph: nx.Graph, masks: tuple[int, ...]) -> bool:
    vertices = tuple(graph)
    for deleted in (None, *vertices):
        kept = tuple(v for v in vertices if v != deleted)
        for labels in product((0, 1), repeat=len(kept)):
            if len(set(labels)) < 2:
                continue
            colour = dict(zip(kept, labels, strict=True))
            if any(not (masks[v] & (1 << colour[v])) for v in kept):
                continue
            if any(colour[x] == colour[y] for x, y in graph.edges if x != deleted and y != deleted):
                continue
            return True
    return False


def bad_paths(graph: nx.Graph, masks: tuple[int, ...]) -> list[frozenset[int]]:
    forced = [v for v in graph if masks[v] in (1, 2)]
    paths: set[frozenset[int]] = set()
    for x, y in combinations(forced, 2):
        prescribed_different = masks[x] != masks[y]
        graph_distance_odd = nx.shortest_path_length(graph, x, y) % 2 == 1
        if prescribed_different == graph_distance_odd:
            continue
        for path in nx.all_simple_paths(graph, x, y):
            paths.add(frozenset(path))
    return sorted(paths, key=lambda path: (len(path), tuple(sorted(path))))


def has_two_disjoint_bad_paths(graph: nx.Graph, masks: tuple[int, ...]) -> bool:
    paths = bad_paths(graph, masks)
    return any(left.isdisjoint(right) for left, right in combinations(paths, 2))


def is_monochromatic_star(graph: nx.Graph, masks: tuple[int, ...]) -> bool:
    if len(set(masks)) != 1 or masks[0] not in (1, 2):
        return False
    degrees = sorted(dict(graph.degree).values())
    return degrees == [1, 1, 1, 1, 1, 1, 6]


def frontiers() -> list[tuple[str, nx.Graph]]:
    ans = [(f"tree_{index}", nx.convert_node_labels_to_integers(tree))
           for index, tree in enumerate(nx.generators.nonisomorphic_trees(7))]
    cycle = nx.cycle_graph(6)
    cycle.add_edge(0, 6)
    ans.append(("c6_pendant", cycle))
    return ans


def main() -> None:
    checked = 0
    no_return = 0
    disjoint_bad = 0
    star = 0
    unresolved: list[tuple[str, tuple[int, ...]]] = []

    for name, graph in frontiers():
        for masks in product((1, 2, 3), repeat=7):
            checked += 1
            if has_return(graph, masks):
                continue
            no_return += 1
            if has_two_disjoint_bad_paths(graph, masks):
                disjoint_bad += 1
            elif is_monochromatic_star(graph, masks):
                star += 1
            else:
                unresolved.append((name, masks))

    print(
        "TWO_LIST_DICHOTOMY",
        "checked", checked,
        "no_return", no_return,
        "disjoint_bad", disjoint_bad,
        "monochromatic_star", star,
        "unresolved", len(unresolved),
    )
    for item in unresolved[:20]:
        print("UNRESOLVED", item)


if __name__ == "__main__":
    main()
