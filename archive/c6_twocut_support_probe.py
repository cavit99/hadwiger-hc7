#!/usr/bin/env python3
"""Coarse support probe for a surviving two-cut in a C6 shore.

The two components are contracted to a,b and the cut vertices are p,q.
Every component sees p,q.  We retain exactly the boundary-contact masks
and require all four connected allocations of p,q to pass the negative
two-piece atlas.  The output records which of the six cyclic frames can
already be crossed in this four-node quotient.
"""

from __future__ import annotations

import itertools

from c6_two_piece_contact_atlas_fast import quotient_edges, S
from k331_two_piece_contact_atlas import fast_k7_model


FULL = (1 << 7) - 1
W = tuple(range(6))
CYCLE = (0, 4, 2, 3, 1, 5)
FRAMES = []
for i in range(6):
    FRAMES.append(((CYCLE[(i - 2) % 6], CYCLE[(i - 1) % 6]),
                   (CYCLE[(i + 2) % 6], CYCLE[(i + 3) % 6])))


def bits(mask):
    return frozenset(i for i in S if mask >> i & 1)


def negative_pairs():
    answer = set()
    for x in range(128):
        for y in range(128):
            if x | y != FULL:
                continue
            if fast_k7_model(quotient_edges(bits(x), bits(y))) is None:
                answer.add((x, y))
    return answer


def path_masks(u, v, contacts, pq_edge):
    # Internal nodes 0,1 are components; 2,3 are cut vertices.
    adj = ({2, 3}, {2, 3}, {0, 1}, {0, 1})
    adj = [set(row) for row in adj]
    if pq_edge:
        adj[2].add(3)
        adj[3].add(2)
    starts = [i for i, mask in enumerate(contacts) if mask >> u & 1]
    ends = {i for i, mask in enumerate(contacts) if mask >> v & 1}
    found = set()

    def dfs(x, used):
        if x in ends:
            found.add(sum(1 << z for z in used))
        for y in adj[x]:
            if y not in used:
                dfs(y, used + (y,))

    for start in starts:
        dfs(start, (start,))
    return found


def support_mask(contacts, pq_edge):
    answer = 0
    for i, (first, second) in enumerate(FRAMES):
        p1 = path_masks(*first, contacts, pq_edge)
        p2 = path_masks(*second, contacts, pq_edge)
        if any(not (x & y) for x in p1 for y in p2):
            answer |= 1 << i
    return answer


def capacity_two_support_mask(contacts, pq_edge):
    """Optimistic projection: components may carry two disjoint strands.

    The cut vertices retain capacity one.  This records the purely
    topological rope patterns not visible after contracting a component.
    """
    answer = 0
    cut_bits = (1 << 2) | (1 << 3)
    for i, (first, second) in enumerate(FRAMES):
        p1 = path_masks(*first, contacts, pq_edge)
        p2 = path_masks(*second, contacts, pq_edge)
        if any(not (x & y & cut_bits) for x in p1 for y in p2):
            answer |= 1 << i
    return answer


def same_component_upper(a, b):
    """Frames which could be locked wholly in one component.

    A component must contact all four crossing terminals.  Mutual portal
    separation is impossible if the other component contacts both omitted
    rim terminals, so its defect must hit the omitted cycle edge.
    """
    answer = 0
    for i in range(6):
        omitted = ((1 << CYCLE[i]) |
                   (1 << CYCLE[(i + 1) % 6]))
        crossing = ((1 << 6) - 1) ^ omitted
        da = FULL ^ a
        db = FULL ^ b
        in_a = not (da & crossing) and bool(db & omitted)
        in_b = not (db & crossing) and bool(da & omitted)
        if in_a or in_b:
            answer |= 1 << i
    return answer


def main():
    neg = negative_pairs()
    assert len(neg) == 762
    large = [m for m in range(1, 128) if m.bit_count() >= 5]
    counts = {}
    upper_counts = {}
    capacity_counts = {}
    examples = {}
    valid = 0
    for a in large:
        for b in large:
            for p in range(128):
                for q in range(128):
                    if (a, b | p | q) not in neg:
                        continue
                    if (a | p, b | q) not in neg:
                        continue
                    if (a | q, b | p) not in neg:
                        continue
                    if (a | p | q, b) not in neg:
                        continue
                    # Singleton cut-vertex splits are also connected.
                    if (p, a | b | q) not in neg:
                        continue
                    if (q, a | b | p) not in neg:
                        continue
                    valid += 1
                    contacts = (a, b, p, q)
                    for pq_edge in (False, True):
                        sig = support_mask(contacts, pq_edge)
                        counts[sig] = counts.get(sig, 0) + 1
                        examples.setdefault(sig, (a, b, p, q, pq_edge))
                        upper = sig | same_component_upper(a, b)
                        upper_counts[upper] = upper_counts.get(upper, 0) + 1
                        capacity = capacity_two_support_mask(contacts, pq_edge)
                        capacity_counts[capacity] = capacity_counts.get(capacity, 0) + 1
    print("valid contact rows", valid)
    print("support signatures", len(counts))
    for sig in sorted(counts, key=lambda z: (z.bit_count(), z)):
        print(f"{sig:06b}", counts[sig], examples[sig])
    cover = []
    signatures = tuple(counts)
    for x in signatures:
        for y in signatures:
            if x | y == 0b111111:
                cover.append((x, y))
    print("ordered two-shore covers", len(cover))
    print("cover signatures", cover[:100])
    print("upper support signatures", len(upper_counts))
    print([(f"{x:06b}", upper_counts[x]) for x in
           sorted(upper_counts, key=lambda z: (z.bit_count(), z))])
    print("capacity-two signatures", len(capacity_counts))
    print([(f"{x:06b}", capacity_counts[x]) for x in
           sorted(capacity_counts, key=lambda z: (z.bit_count(), z))])
    maximal = {x for x in counts
               if not any(x != y and x & ~y == 0 for y in counts)}
    opposite_states = []
    for a in large:
        for b in large:
            for p in range(128):
                for q in range(128):
                    if (a, b | p | q) not in neg:
                        continue
                    if (a | p, b | q) not in neg:
                        continue
                    if (a | q, b | p) not in neg:
                        continue
                    if (a | p | q, b) not in neg:
                        continue
                    if (p, a | b | q) not in neg:
                        continue
                    if (q, a | b | p) not in neg:
                        continue
                    contacts = (a, b, p, q)
                    sig = support_mask(contacts, False) | support_mask(contacts, True)
                    if any(sig >> i & 1 and sig >> (i + 3) & 1
                           for i in range(3)):
                        opposite_states.append((*contacts, sig))
    maximal_opposite = [
        state for state in opposite_states
        if not any(state != other and
                   all(state[i] | other[i] == other[i] for i in range(4))
                   for other in opposite_states)
    ]
    print("opposite-visible states", len(opposite_states))
    print("maximal opposite-visible states")
    for state in maximal_opposite:
        print(state[:4], "defects", tuple(FULL ^ x for x in state[:4]),
              f"support {state[4]:06b}")
    assert valid == 6240
    assert len(counts) == 21
    assert maximal == {0b000111, 0b001110, 0b011100,
                       0b111000, 0b110001, 0b100011,
                       0b001001, 0b010010, 0b100100}
    assert len(opposite_states) == 384
    assert len(maximal_opposite) == 6


if __name__ == "__main__":
    main()
