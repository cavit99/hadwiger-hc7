#!/usr/bin/env python3
"""Test whether every rooted-K4 handoff quotient already has a K7 minor.

This is a discovery probe.  It reuses only the quotient generator; clique
minor models are found and then checked directly.  Monotone certificates
are reused only after their exact bags survive deletion of optional edges.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


HERE = Path(__file__).parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


QUOTIENT = load(
    "rooted_handoff",
    HERE.parent / "results" / "hc7_exact7_cross_lobe_rooted_k4_handoff_verify.py",
)
MINOR = load("minor_probe", HERE.parent / "results" / "hc7_mobile_path_probe.py")


def adjacency(edges):
    index = {vertex: i for i, vertex in enumerate(QUOTIENT.VERTICES)}
    answer = [0] * len(index)
    for left, right in edges:
        i, j = index[left], index[right]
        answer[i] |= 1 << j
        answer[j] |= 1 << i
    return answer


def bags_from_masks(masks):
    return tuple(
        frozenset(
            vertex
            for i, vertex in enumerate(QUOTIENT.VERTICES)
            if mask & (1 << i)
        )
        for mask in masks
    )


def verify_k7(edges, bags):
    assert len(bags) == 7
    assert all(left.isdisjoint(right) for i, left in enumerate(bags) for right in bags[i + 1 :])
    assert all(QUOTIENT.connected(bag, edges) for bag in bags)
    assert all(
        QUOTIENT.bags_adjacent(left, right, edges)
        for i, left in enumerate(bags)
        for right in bags[i + 1 :]
    )


def find_k7(edges):
    masks = MINOR.has_k7_minor(adjacency(edges))
    if masks is None:
        return None
    bags = bags_from_masks(masks)
    verify_k7(edges, bags)
    return bags


def cover_contact(c_contact: str) -> int | None:
    base = QUOTIENT.fixed_edges(c_contact)
    uncovered = set(range(len(QUOTIENT.BOUNDARIES)))
    certificates = 0
    while uncovered:
        case = min(uncovered)
        boundary = QUOTIENT.BOUNDARIES[case]
        bags = find_k7(base | boundary)
        if bags is None:
            print("NO K7", c_contact, case, sorted(boundary))
            return None

        required = set(boundary)
        for optional in tuple(required):
            smaller = frozenset(base | (required - {optional}))
            try:
                verify_k7(smaller, bags)
            except AssertionError:
                continue
            required.remove(optional)

        certificate_edges = frozenset(base | required)
        verify_k7(certificate_edges, bags)
        covered = {
            index
            for index in uncovered
            if required <= QUOTIENT.BOUNDARIES[index]
        }
        assert covered
        uncovered.difference_update(covered)
        certificates += 1
    print(c_contact, "all 512 quotients have K7; certificates", certificates)
    return certificates


def main():
    total = 0
    for c_contact in QUOTIENT.CORE:
        count = cover_contact(c_contact)
        if count is None:
            raise SystemExit(1)
        total += count
    print("all 2048 rooted-K4 quotients contain K7; certificates", total)


if __name__ == "__main__":
    main()
