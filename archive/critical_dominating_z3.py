#!/usr/bin/env python3
"""Exact SMT search for a k-vertex-critical graph violating the CDS lemma.

For fixed n,k the solver enforces:
  * every vertex deletion is (k-1)-colourable;
  * minimum degree at least k-1 and connectedness follows;
  * every connected dominating D leaves a (k-2)-colourable graph.

Non-(k-1)-colourability of G is imposed by a CEGIS loop: whenever the
current model admits such a colouring, add the exact blocking clause saying
that some same-colour pair must be an edge.
"""

from __future__ import annotations

import argparse

import z3

from critical_dominating_search import chromatic_number, connected, dominates, graph6


def build(n: int, k: int, triangle_free: bool = False) -> tuple[z3.Solver, dict[tuple[int, int], z3.BoolRef]]:
    s = z3.Solver()
    e = {(i, j): z3.Bool(f"e_{i}_{j}") for i in range(n) for j in range(i + 1, n)}

    def edge(i: int, j: int):
        if i == j:
            return z3.BoolVal(False)
        return e[min(i, j), max(i, j)]

    deg = [z3.Sum([z3.If(edge(i, j), 1, 0) for j in range(n) if j != i]) for i in range(n)]
    for d in deg:
        s.add(d >= k - 1)
    # Every unlabeled graph has a labeling of nondecreasing degree.
    for i in range(n - 1):
        s.add(deg[i] <= deg[i + 1])
    if triangle_free:
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    s.add(z3.Or(z3.Not(edge(a, b)), z3.Not(edge(a, c)), z3.Not(edge(b, c))))

    # Each vertex deletion has a (k-1)-coloring.
    for deleted in range(n):
        color = {v: z3.Int(f"del_{deleted}_c_{v}") for v in range(n) if v != deleted}
        for v in color:
            s.add(color[v] >= 0, color[v] < k - 1)
        for i in range(n):
            if i == deleted:
                continue
            for j in range(i + 1, n):
                if j == deleted:
                    continue
                s.add(z3.Implies(edge(i, j), color[i] != color[j]))

    # No connected dominating D may leave chromatic number k-1.
    full = (1 << n) - 1
    for dmask in range(1, full):
        dverts = [v for v in range(n) if (dmask >> v) & 1]
        hverts = [v for v in range(n) if not ((dmask >> v) & 1)]

        root = dverts[0]
        # Fixed-point recurrence for root reachability inside D.  Use |D|-1
        # synchronous rounds, so the formula is independent of vertex order.
        reach = {v: z3.Or(z3.BoolVal(v == root), edge(root, v)) for v in dverts}
        for _ in range(max(0, len(dverts) - 1)):
            old = reach
            reach = {
                v: z3.Or(old[v], *[z3.And(old[u], edge(u, v)) for u in dverts if u != v])
                for v in dverts
            }
        conn = z3.And([reach[v] for v in dverts])
        dom = z3.And([z3.Or([edge(h, d) for d in dverts]) for h in hverts])

        col = {h: z3.Int(f"D_{dmask}_c_{h}") for h in hverts}
        colorable = []
        for h in hverts:
            colorable.extend([col[h] >= 0, col[h] < k - 2])
        for ii, i in enumerate(hverts):
            for j in hverts[ii + 1:]:
                colorable.append(z3.Implies(edge(i, j), col[i] != col[j]))
        s.add(z3.Implies(z3.And(conn, dom), z3.And(colorable)))

    return s, e


def extract(n: int, model: z3.ModelRef, e: dict[tuple[int, int], z3.BoolRef]) -> list[int]:
    adj = [0] * n
    for (i, j), x in e.items():
        if z3.is_true(model.eval(x)):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def find_coloring(adj: list[int], q: int) -> list[int] | None:
    n = len(adj)
    colors = [-1] * n

    def rec(left: int) -> bool:
        if not left:
            return True
        candidates = [v for v in range(n) if (left >> v) & 1]
        v = max(candidates, key=lambda x: (len({colors[u] for u in range(n) if colors[u] >= 0 and ((adj[x] >> u) & 1)}), (adj[x] & left).bit_count()))
        forbidden = {colors[u] for u in range(n) if colors[u] >= 0 and ((adj[v] >> u) & 1)}
        for c in range(q):
            if c not in forbidden:
                colors[v] = c
                if rec(left & ~(1 << v)):
                    return True
                colors[v] = -1
        return False

    return colors.copy() if rec((1 << n) - 1) else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("k", type=int)
    ap.add_argument("--triangle-free", action="store_true")
    ap.add_argument("--full-block", action="store_true", help="eagerly block every (k-1)-coloring partition")
    ap.add_argument("--timeout", type=int, default=0, help="milliseconds per SMT check")
    args = ap.parse_args()
    s, e = build(args.n, args.k, args.triangle_free)
    if args.timeout:
        s.set(timeout=args.timeout)
    def edge(i: int, j: int):
        return e[min(i, j), max(i, j)]

    if args.full_block:
        labels = [0] * args.n
        count = 0

        def partitions(pos: int, current_max: int) -> None:
            nonlocal count
            if pos == args.n:
                blockers = [edge(i, j) for i in range(args.n) for j in range(i + 1, args.n) if labels[i] == labels[j]]
                s.add(z3.Or(blockers))
                count += 1
                return
            for c in range(min(current_max + 1, args.k - 2) + 1):
                labels[pos] = c
                partitions(pos + 1, max(current_max, c))

        labels[0] = 0
        partitions(1, 0)
        print("blocked canonical colorings", count, flush=True)

    iteration = 0
    while True:
        status = s.check()
        print("iteration", iteration, status, flush=True)
        if status != z3.sat:
            return
        model = s.model()
        adj = extract(args.n, model, e)
        coloring = None if args.full_block else find_coloring(adj, args.k - 1)
        if coloring is None:
            print("COUNTEREXAMPLE", args.n, args.k, graph6(adj), "chi", chromatic_number(adj))
            full = (1 << args.n) - 1
            for d in range(1, full):
                assert not (connected(adj, d) and dominates(adj, d) and chromatic_number(adj, full ^ d) >= args.k - 1)
            for v, a in enumerate(adj):
                print(v, [u for u in range(args.n) if (a >> u) & 1])
            return
        # Every graph realizing the same proper coloring must add an edge inside
        # one of its color classes to destroy it.
        blockers = [x for (i, j), x in e.items() if coloring[i] == coloring[j]]
        s.add(z3.Or(blockers))
        iteration += 1


if __name__ == "__main__":
    main()
