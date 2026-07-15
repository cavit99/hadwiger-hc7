#!/usr/bin/env python3
"""Classify the exact mask data in the sole direct-reserve rural residue.

This is a boundary-language probe only.  It enumerates canonical atomic
lists, keeps no-return instances, and records disjoint bad-path pairs with
exactly one literal edge and one nontrivial path.  It checks which facts are
forced before any shore geometry is used.
"""

from __future__ import annotations

from collections import Counter

from hc7_rural_rooted_k4_augmentation_probe import (
    canonical_masks,
    ordered_bad_paths,
)
from hc7_two_list_reservoir_obstruction_check import frontiers, has_return


def main() -> None:
    counts: Counter[tuple[object, ...]] = Counter()
    checked = 0
    violations = []

    for name, graph in frontiers():
        for root in graph:
            for masks in canonical_masks(graph, root):
                if has_return(graph, masks):
                    continue
                paths = ordered_bad_paths(graph, masks)
                for left_index, left in enumerate(paths):
                    for right in paths[left_index + 1 :]:
                        if not left[2].isdisjoint(right[2]):
                            continue
                        lengths = sorted((len(left[2]), len(right[2])))
                        if lengths[0] != 2 or lengths[1] <= 2:
                            continue
                        edge, long_path = (
                            (left, right) if len(left[2]) == 2 else (right, left)
                        )
                        checked += 1

                        edge_forced = tuple(sorted(masks[v] for v in edge[:2]))
                        root_role = (
                            "long_endpoint"
                            if root in long_path[:2]
                            else "long_internal"
                            if root in long_path[2]
                            else "outside"
                        )
                        counts[
                            (
                                name,
                                len(long_path[2]) - 2,
                                edge_forced,
                                root_role,
                            )
                        ] += 1

                        # A direct bad edge must join two vertices forced to
                        # carrier 1, hence neither endpoint sees the root z.
                        if edge_forced != (2, 2) or root in edge[:2]:
                            violations.append((name, root, masks, edge, long_path))

    print("DIRECT_RESERVE_MASKS", "pairs", checked, "violations", len(violations))
    for key, value in sorted(counts.items(), key=lambda item: repr(item[0])):
        print("TYPE", key, value)
    for item in violations[:10]:
        print("VIOLATION", item)


if __name__ == "__main__":
    main()
