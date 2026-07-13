#!/usr/bin/env python3
"""Exhaustive small audit of the state-shore / one-gate lemma.

All connected labelled graphs through order four and all nonempty,
possibly overlapping portal triples are checked.  Paths of order one are
handled by the component formulation of a gate.
"""

from itertools import combinations


def connected(mask: int, vertices: int, n: int) -> bool:
    if vertices == 0:
        return False
    reached = vertices & -vertices
    while True:
        expanded = reached
        for i in range(n):
            if reached >> i & 1:
                for j in range(n):
                    bit = i * n + j
                    if mask >> bit & 1 and vertices >> j & 1:
                        expanded |= 1 << j
        if expanded == reached:
            return reached == vertices
        reached = expanded


def adjacent(mask: int, x: int, y: int, n: int) -> bool:
    return any(mask >> (i * n + j) & 1 for i in range(n) if x >> i & 1
               for j in range(n) if y >> j & 1)


def shore(mask: int, a: int, b: int, c: int, n: int) -> bool:
    universe = (1 << n) - 1
    for x in range(1, universe + 1):
        if not (x & a and x & b) or not connected(mask, x, n):
            continue
        remaining = universe ^ x
        y = remaining
        while y:
            if y & b and y & c and connected(mask, y, n) and adjacent(mask, x, y, n):
                return True
            y = (y - 1) & remaining
    return False


def gate(mask: int, sources: int, targets: int, z: int, n: int) -> bool:
    remaining = ((1 << n) - 1) ^ (1 << z)
    s = sources & remaining
    t = targets & remaining
    # An order-one path avoiding z exists when s and t overlap.
    if s & t:
        return False
    unseen = remaining
    while unseen:
        start = unseen & -unseen
        comp = start
        while True:
            expanded = comp
            for i in range(n):
                if comp >> i & 1:
                    for j in range(n):
                        if mask >> (i * n + j) & 1 and remaining >> j & 1:
                            expanded |= 1 << j
            if expanded == comp:
                break
            comp = expanded
        if comp & s and comp & t:
            return False
        unseen &= ~comp
    return True


def main() -> None:
    checked = 0
    for n in range(1, 5):
        pairs = tuple(combinations(range(n), 2))
        for bits in range(1 << len(pairs)):
            mask = 0
            for k, (i, j) in enumerate(pairs):
                if bits >> k & 1:
                    mask |= 1 << (i * n + j)
                    mask |= 1 << (j * n + i)
            if not connected(mask, (1 << n) - 1, n):
                continue
            for a in range(1, 1 << n):
                for b in range(1, 1 << n):
                    for c in range(1, 1 << n):
                        checked += 1
                        first = shore(mask, a, b, c, n)
                        first_gate = any(gate(mask, a | c, b, z, n) for z in range(n))
                        assert first or first_gate, (n, bits, a, b, c)
                        second = shore(mask, a, c, b, n)
                        second_gate = any(gate(mask, a | b, c, z, n) for z in range(n))
                        assert second or second_gate, (n, bits, a, b, c)
                        assert first or second or (first_gate and second_gate)
    print("connected graph / overlapping portal triples checked:", checked)


if __name__ == "__main__":
    main()
