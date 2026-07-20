#!/usr/bin/env python3
"""Verify endpoint allocation in all type-5 PB enlargements."""

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
                out_vertices, out_edges = pb.split_two(
                    vertices, edges, u, u_sides, v, v_sides
                )
                out_edges.add(pb.canon_edge((u, 1), (v, 1)))
                yield u, v, out_vertices, out_edges


def main() -> None:
    pb = load_generator()
    instances = list(type5_instances(pb))
    assert len(instances) == 50

    tests = 0
    failures = 0
    mismatches = 0
    exceptional = 0

    for u, v, vertices, edges in instances:
        split_labels = {u, v}
        unsplit = set(pb.BASE) - split_labels
        unsplit_failure = pb.rooted_k5(vertices, edges, tuple(unsplit)) is None
        exceptional += int(unsplit_failure)

        choices = ({0}, {1}, {0, 1})
        for i_a, i_b, j_a, j_b in product(choices, repeat=4):
            nominated_a = unsplit | {(u, i) for i in i_a} | {
                (v, j) for j in j_a
            }
            nominated_b = unsplit | {(u, i) for i in i_b} | {
                (v, j) for j in j_b
            }
            failure = (
                pb.paired_rooted_k5(
                    vertices, edges, nominated_a, nominated_b
                )
                is None
            )
            predicted = unsplit_failure and (
                (i_a == j_a == {0}) or (i_b == j_b == {0})
            )
            tests += 1
            failures += int(failure)
            mismatches += int(failure != predicted)

    assert exceptional == 20
    assert tests == 4050
    assert failures == 340
    assert mismatches == 0
    print(
        "GREEN type-5 endpoint allocation: "
        "instances=50 tests=4050 failures=340 root-trap-mismatches=0"
    )


if __name__ == "__main__":
    main()
