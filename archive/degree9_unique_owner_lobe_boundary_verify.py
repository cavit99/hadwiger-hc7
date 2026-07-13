#!/usr/bin/env python3
"""Certificates for the unique-owner distributed-lobe sharpness family."""

from degree9_complementary_star_probe import (
    build_double_same_spines,
    elimination_order_at_most,
    min_balanced_ordinary_sum,
)


def neighbours(vertex, edges):
    out = set()
    for edge in edges:
        if vertex in edge:
            out.update(edge - {vertex})
    return out


def main():
    # One distributed lobe and two edge-simplicial capacity vertices on
    # each side retain four distinct neighbours in every prefix row.
    for length in range(2, 13):
        vertices, edges = build_double_same_spines(
            length, capacity=3, distributed_capacity=1
        )
        order = elimination_order_at_most(vertices, edges, 5)
        assert order is not None
        left_boundary = neighbours("kx0", edges)
        right_boundary = neighbours("jy0", edges)
        assert left_boundary == {"K", *(f"u{i}" for i in range(length))}
        assert right_boundary == {"J", *(f"w{i}" for i in range(length))}
        assert len(left_boundary) == length + 1
        assert len(right_boundary) == length + 1
        print(
            "length", length,
            "vertices", len(vertices),
            "lobe-boundary", len(left_boundary),
            "width<=5", True,
        )

    # Independent exhaustive potential check on the capacity-free core.
    vertices, edges = build_double_same_spines(4)
    best, witness = min_balanced_ordinary_sum(vertices, edges)
    assert best == 10
    print("m=4 exact potential", best, witness)


if __name__ == "__main__":
    main()
