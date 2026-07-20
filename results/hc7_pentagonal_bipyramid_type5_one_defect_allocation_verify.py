#!/usr/bin/env python3
"""Verify one-defect models in all type-5 PB endpoint assignments."""

from __future__ import annotations

import importlib.util
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "active" / "hc7_pentagonal_bipyramid_enlargement_probe.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("pb_enlargement", GENERATOR)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def type5_instances(pb):
    vertices, edges = pb.base_graph()
    for u, v in pb.BASE_EDGES:
        common = sorted(set(pb.ROTATION[u]) & set(pb.ROTATION[v]))
        for u_partition in pb.split_partitions(u, conforming=True):
            u_sides = pb.oriented_partition(u, u_partition, v)
            for v_partition in pb.split_partitions(v, conforming=True):
                v_sides = pb.oriented_partition(v, v_partition, u)
                if not any(
                    x in u_sides[1] and y in v_sides[1]
                    for x, y in (common, tuple(reversed(common)))
                ):
                    continue
                out_v, out_e = pb.split_two(
                    vertices, edges, u, u_sides, v, v_sides
                )
                out_e.add(pb.canon_edge((u, 1), (v, 1)))
                yield u, v, out_v, out_e


def one_defect_model(pb, vertices, edges, full_set, defect_set):
    """Return five K5 bags all meeting full_set and four meeting defect_set."""
    order = tuple(sorted(vertices, key=repr))
    candidates = []
    for mask in range(1, 1 << len(order)):
        bag = {order[i] for i in range(len(order)) if mask & (1 << i)}
        if not (bag & full_set) or not pb.connected(edges, bag):
            continue
        candidates.append((mask, frozenset(bag), bool(bag & defect_set)))

    def search(start, used, chosen, defect_hits):
        remaining = 5 - len(chosen)
        if defect_hits + remaining < 4:
            return None
        if len(chosen) == 5:
            return chosen if defect_hits >= 4 else None
        for index in range(start, len(candidates)):
            mask, bag, hits_defect = candidates[index]
            if mask & used:
                continue
            if not all(
                any(pb.adjacent(edges, x, y) for x in bag for y in old_bag)
                for _, old_bag, _ in chosen
            ):
                continue
            answer = search(
                index + 1,
                used | mask,
                chosen + [(mask, bag, hits_defect)],
                defect_hits + int(hits_defect),
            )
            if answer is not None:
                return answer
        return None

    return search(0, 0, [], 0)


def main() -> None:
    pb = load_generator()
    choices = ({0}, {1}, {0, 1})
    paired_failures = 0
    one_defect_failures = 0
    double_confined = 0
    mismatches = 0

    for u, v, vertices, edges in type5_instances(pb):
        unsplit = set(pb.BASE) - {u, v}
        for i_a, i_b, j_a, j_b in product(choices, repeat=4):
            nominated_a = unsplit | {(u, i) for i in i_a} | {
                (v, j) for j in j_a
            }
            nominated_b = unsplit | {(u, i) for i in i_b} | {
                (v, j) for j in j_b
            }
            if pb.paired_rooted_k5(
                vertices, edges, nominated_a, nominated_b
            ) is not None:
                continue

            paired_failures += 1
            a_confined = i_a == j_a == {0}
            b_confined = i_b == j_b == {0}
            both_confined = a_confined and b_confined
            double_confined += int(both_confined)

            a_full = one_defect_model(
                pb, vertices, edges, nominated_a, nominated_b
            )
            b_full = one_defect_model(
                pb, vertices, edges, nominated_b, nominated_a
            )
            failure = a_full is None and b_full is None
            one_defect_failures += int(failure)

            predicted_a_full = b_confined and not a_confined
            predicted_b_full = a_confined and not b_confined
            correct = (
                failure == both_confined
                and (a_full is not None) == predicted_a_full
                and (b_full is not None) == predicted_b_full
            )
            mismatches += int(not correct)

    assert paired_failures == 340
    assert one_defect_failures == 20
    assert double_confined == 20
    assert mismatches == 0
    print(
        "GREEN type-5 one-defect allocation: "
        "paired-failures=340 one-defect-failures=20 "
        "double-confined=20 mismatches=0"
    )


if __name__ == "__main__":
    main()
