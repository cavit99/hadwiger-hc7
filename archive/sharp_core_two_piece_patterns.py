#!/usr/bin/env python3
"""Extract minimal boundary-contact patterns for an adjacent shore split."""

import itertools

import c5_core_k2_shore_verify as exact


S = exact.S
X, Y, H = exact.X, exact.Y, exact.D
FULL = (1 << 7) - 1


def graph_edges(kind, mx, my):
    edges = set(exact.boundary_edges(kind))
    edges.add((X, Y))
    edges.update((s, H) for s in S)
    edges.update(tuple(sorted((X, s))) for s in S if mx >> s & 1)
    edges.update(tuple(sorted((Y, s))) for s in S if my >> s & 1)
    return {tuple(sorted(edge)) for edge in edges}


def set_string(mask):
    return "".join(str(s) for s in S if mask >> s & 1) or "-"


def main():
    for kind in ("C5+2K1", "K3+2K2"):
        positive = set()
        for mx in range(1, 1 << 7):
            for my in range(mx, 1 << 7):  # quotient by swapping X,Y
                if exact.k_minor_model(graph_edges(kind, mx, my)) is not None:
                    positive.add((mx, my))

        def succeeds(mx, my):
            return (min(mx, my), max(mx, my)) in positive

        minimal = []
        for mx, my in positive:
            if any(succeeds(mx ^ (1 << s), my)
                   for s in S if mx >> s & 1):
                continue
            if any(succeeds(mx, my ^ (1 << s))
                   for s in S if my >> s & 1):
                continue
            minimal.append((mx, my))

        full_minimal = [(mx, my) for mx, my in minimal if mx | my == FULL]
        print(kind, "positive", len(positive), "minimal", len(minimal),
              "full-minimal", len(full_minimal))
        for mx, my in sorted(minimal,
                             key=lambda pair: (sum(x.bit_count() for x in pair), pair))[:40]:
            print(" ", set_string(mx), set_string(my),
                  "union", set_string(mx | my))


if __name__ == "__main__":
    main()
