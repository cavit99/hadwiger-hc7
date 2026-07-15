#!/usr/bin/env python3
"""Probe the static fifth-bag step after the rural rooted-K4 normalization.

The probe deliberately forgets the internal geometry of the four rooted
bags.  For every audited connected-bipartite frontier and every canonical
root-split list assignment with no adaptive return, it chooses two disjoint
bad paths.  Their four ends root a K4; the other three boundary vertices
may see rooted bags through literal boundary edges and through one arbitrary
portal bag each.  We ask whether some connected subset of the three spare
boundary vertices is then adjacent to all four rooted bags.

A survivor is a barrier only to this static quotient step.  It is not an
HC7 counterexample: actual portal paths may split or reroute rooted bags.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

DEPS = Path(__file__).resolve().parent / "runtime" / "deps"
if DEPS.exists():
    sys.path.insert(0, str(DEPS))

import networkx as nx

from hc7_two_list_reservoir_obstruction_check import frontiers, has_return


def connected_nonempty_subsets(graph: nx.Graph, vertices: tuple[int, ...]):
    for size in range(1, len(vertices) + 1):
        for chosen in combinations(vertices, size):
            if nx.is_connected(graph.subgraph(chosen)):
                yield frozenset(chosen)


def static_fifth_bag(
    graph: nx.Graph,
    available: tuple[int, ...],
    boundary_bag: dict[int, int],
    portal_bag: dict[int, int],
) -> frozenset[int] | None:
    for chosen in connected_nonempty_subsets(graph, available):
        seen = {portal_bag[v] for v in chosen}
        for vertex in chosen:
            seen.update(boundary_bag[q] for q in graph[vertex] if q in boundary_bag)
        if len(seen) == 4:
            return chosen
    return None


def canonical_masks(graph: nx.Graph, root: int):
    others = tuple(v for v in graph if v != root)
    for flexible in product((False, True), repeat=len(others)):
        masks = [2] * len(graph)
        masks[root] = 1
        for vertex, is_flexible in zip(others, flexible, strict=True):
            masks[vertex] = 3 if is_flexible else 2
        yield tuple(masks)


def ordered_bad_paths(graph: nx.Graph, masks: tuple[int, ...]):
    forced = tuple(v for v in graph if masks[v] in (1, 2))
    answer = []
    for x, y in combinations(forced, 2):
        prescribed_different = masks[x] != masks[y]
        distance_odd = nx.shortest_path_length(graph, x, y) % 2 == 1
        if prescribed_different == distance_odd:
            continue
        for path in nx.all_simple_paths(graph, x, y):
            answer.append((x, y, frozenset(path)))
    return answer


def main() -> None:
    instances = 0
    path_pairs = 0
    universally_closed = 0
    survivors = 0
    both_nontrivial = 0
    first = None

    for name, graph in frontiers():
        for root in graph:
            for masks in canonical_masks(graph, root):
                if has_return(graph, masks):
                    continue
                instances += 1
                paths = ordered_bad_paths(graph, masks)
                pairs = [
                    pair
                    for pair in combinations(paths, 2)
                    if pair[0][2].isdisjoint(pair[1][2])
                ]
                if any(len(left[2]) >= 3 and len(right[2]) >= 3 for left, right in pairs):
                    both_nontrivial += 1
                instance_closed = False
                for left, right in pairs:
                    roots = (left[0], right[0], left[1], right[1])
                    if len(set(roots)) != 4:
                        continue
                    path_pairs += 1
                    spare = tuple(v for v in graph if v not in roots)
                    all_assignments_close = True
                    for assignment in product(range(4), repeat=len(spare)):
                        portal_bag = dict(zip(spare, assignment, strict=True))
                        for repaired in (left, right):
                            boundary_bag = {q: index for index, q in enumerate(roots)}
                            repaired_index = 0 if repaired is left else 1
                            owner = repaired_index
                            absorbed = repaired[2] - {repaired[0], repaired[1]}
                            boundary_bag.update({v: owner for v in absorbed})
                            available = tuple(v for v in spare if v not in absorbed)
                            if not available or static_fifth_bag(
                                graph, available, boundary_bag, portal_bag
                            ) is None:
                                all_assignments_close = False
                                survivors += 1
                                if first is None:
                                    first = (
                                        name, root, masks, roots, spare,
                                        assignment, "repair", repaired_index,
                                    )
                                break
                        if not all_assignments_close:
                            break
                    if all_assignments_close:
                        instance_closed = True
                        universally_closed += 1
                        break
                # A no-return instance must have a disjoint bad-path pair;
                # the imported uniform theorem proves this analytically.
                assert pairs

    print(
        "RURAL_K4_STATIC_AUGMENTATION",
        "instances", instances,
        "path_pairs", path_pairs,
        "universally_closed", universally_closed,
        "survivors", survivors,
        "both_nontrivial", both_nontrivial,
    )
    if first is not None:
        print("FIRST_SURVIVOR", first)


if __name__ == "__main__":
    main()
