#!/usr/bin/env python3
"""Build exact labelled owner bundles for eight terminal kernels.

Discovery script.  The structural proof must remain independent of nauty;
this program measures and freezes the finite catalogue needed by a labelled
composition decoder.
"""

from __future__ import annotations

import collections
import hashlib
import itertools

import hc7_eight_terminal_kernel_feasibility as base


PAIRS = tuple(itertools.combinations(range(8), 2))
PAIR_INDEX = {edge: index for index, edge in enumerate(PAIRS)}


def edge_mask(edge_set) -> int:
    return sum(1 << PAIR_INDEX[tuple(sorted(edge))] for edge in edge_set)


def relabelled_terminal_mask(adjacency, terminals, image) -> int:
    label = dict(zip(terminals, image))
    return edge_mask(
        (label[left], label[right])
        for left, right in base.edges(adjacency)
        if left in label and right in label
    )


def order_eight_unlabelled():
    answer = []
    for adjacency in base.geng(8):
        if not base.three_connected(adjacency):
            continue
        if any(
            base.three_connected(base.delete_edge(adjacency, left, right))
            for left, right in base.edges(adjacency)
        ):
            continue
        answer.append(adjacency)
    assert len(answer) == 18
    return tuple(answer)


def order_eight_carriers():
    answer = set()
    terminals = tuple(range(8))
    for adjacency in order_eight_unlabelled():
        for image in itertools.permutations(range(8)):
            answer.add(relabelled_terminal_mask(adjacency, terminals, image))
    return tuple(sorted(answer))


def order_nine_unlabelled_rooted():
    answer = []
    for adjacency in base.geng(9):
        if not base.three_connected(adjacency):
            continue
        for extra in range(9):
            neighbours = tuple(
                vertex
                for vertex in range(9)
                if adjacency[extra] >> vertex & 1
            )
            if any(
                base.contractible(adjacency, extra, vertex)
                for vertex in neighbours
            ):
                continue
            answer.append((adjacency, extra))
    assert len(answer) == 97
    return tuple(answer)


def owner_family(adjacency, extra, terminals, image):
    label = dict(zip(terminals, image))
    terminal_mask = relabelled_terminal_mask(adjacency, terminals, image)
    neighbours = tuple(
        vertex
        for vertex in terminals
        if adjacency[extra] >> vertex & 1
    )
    family = set()
    for owner in neighbours:
        mask = terminal_mask
        owner_label = label[owner]
        for other in neighbours:
            if other == owner:
                continue
            mask |= 1 << PAIR_INDEX[
                tuple(sorted((owner_label, label[other])))
            ]
        family.add(mask)
    return tuple(sorted(family))


def order_nine_families():
    answer = set()
    for adjacency, extra in order_nine_unlabelled_rooted():
        terminals = tuple(vertex for vertex in range(9) if vertex != extra)
        for image in itertools.permutations(range(8)):
            answer.add(owner_family(adjacency, extra, terminals, image))
    return tuple(sorted(answer))


def labelled_cycles():
    answer = set()
    for tail in itertools.permutations(range(1, 8)):
        cycle = (0,) + tail
        if cycle[1] > cycle[-1]:
            continue
        answer.add(
            frozenset(
                tuple(sorted((cycle[index], cycle[(index + 1) % 8])))
                for index in range(8)
            )
        )
    assert len(answer) == 2520
    return tuple(answer)


def order_ten_families():
    answer = set()
    template_count = 0
    for cycle_edges in labelled_cycles():
        cycle_adjacency = [set() for _ in range(8)]
        for left, right in cycle_edges:
            cycle_adjacency[left].add(right)
            cycle_adjacency[right].add(left)
        # There are four cyclic AABBAABB charge words.  Start at each
        # possible transition modulo the period four.
        cycle = [0]
        previous = None
        current = 0
        while len(cycle) < 8:
            choices = sorted(cycle_adjacency[current] - ({previous} if previous is not None else set()))
            if previous is None:
                # Canonical orientation at the fixed root.
                nxt = min(choices)
            else:
                assert len(choices) == 1
                nxt = choices[0]
            cycle.append(nxt)
            previous, current = current, nxt
        assert cycle_adjacency[cycle[-1]] == {cycle[-2], cycle[0]}
        terminal_mask = edge_mask(cycle_edges)
        for shift in range(4):
            first = frozenset(
                cycle[index]
                for index in range(8)
                if ((index - shift) % 4) in (0, 1)
            )
            second = frozenset(range(8)) - first
            template_count += 1
            family = set()
            for owner_first in first:
                for owner_second in second:
                    mask = terminal_mask
                    mask |= edge_mask(
                        (owner_first, other)
                        for other in first
                        if other != owner_first
                    )
                    mask |= edge_mask(
                        (owner_second, other)
                        for other in second
                        if other != owner_second
                    )
                    family.add(mask)
            assert len(family) == 16
            answer.add(tuple(sorted(family)))
    assert template_count == 10080
    return tuple(sorted(answer)), template_count


def digest(items) -> str:
    stream = "\n".join(str(item) for item in items).encode()
    return hashlib.sha256(stream).hexdigest()


def main():
    order_eight = order_eight_carriers()
    print("order8_unlabelled", 18, flush=True)
    print("order8_labelled", len(order_eight), flush=True)
    print(
        "order8_edge_profile",
        dict(sorted(collections.Counter(mask.bit_count() for mask in order_eight).items())),
        flush=True,
    )
    print("order8_digest", digest(order_eight), flush=True)

    order_nine = order_nine_families()
    print("order9_rooted_occurrences", 97, flush=True)
    print("order9_owner_families", len(order_nine), flush=True)
    print(
        "order9_family_size_profile",
        dict(sorted(collections.Counter(map(len, order_nine)).items())),
        flush=True,
    )
    print("order9_digest", digest(order_nine), flush=True)

    order_ten, templates = order_ten_families()
    print("order10_templates", templates, flush=True)
    print("order10_owner_families", len(order_ten), flush=True)
    print(
        "order10_family_size_profile",
        dict(sorted(collections.Counter(map(len, order_ten)).items())),
        flush=True,
    )
    print("order10_digest", digest(order_ten), flush=True)


if __name__ == "__main__":
    main()
