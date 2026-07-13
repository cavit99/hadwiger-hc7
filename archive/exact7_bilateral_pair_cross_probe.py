#!/usr/bin/env python3
"""Test two full-shore (13|24) crossings at the Moser seven-cut."""

from itertools import product

from reserved_terminal_specific_web_quotient_verify import e, minor_model


def main():
    # Boundary: q,h,1,2,3,4,6 = 0,...,6.
    q, h, a, b, c, d, six = range(7)
    fixed = {
        e(h, a), e(h, b), e(h, c), e(h, d),
        e(a, b), e(a, six), e(b, six), e(c, d),
    }
    x1, y1, x2, y2 = 7, 8, 9, 10
    fixed |= {
        e(x1, y1), e(x2, y2),
        e(x1, a), e(x1, c), e(y1, b), e(y1, d),
        e(x2, a), e(x2, c), e(y2, b), e(y2, d),
    }
    failures = []
    remaining = (q, h, six)
    for left_mask, right_mask in product(range(8), repeat=2):
        graph = set(fixed)
        for mask, x, y in ((left_mask, x1, y1), (right_mask, x2, y2)):
            for i, z in enumerate(remaining):
                graph.add(e(x if mask >> i & 1 else y, z))
        model = minor_model(11, graph, 7)
        if model is None:
            failures.append((left_mask, right_mask))
    print("checked", 64, "failures", len(failures))
    print(failures)


if __name__ == "__main__":
    main()
