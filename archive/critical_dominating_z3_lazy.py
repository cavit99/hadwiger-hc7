#!/usr/bin/env python3
"""Lazy exact SMT search for a vertex-critical counterexample to CD descent."""

from __future__ import annotations

import argparse

import z3

from critical_dominating_search import graph6, has_cd_remainder, chromatic_number


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("k", type=int)
    ap.add_argument("--timeout", type=int, default=300000)
    args = ap.parse_args()
    n, k = args.n, args.k
    s = z3.Solver()
    s.set(timeout=args.timeout)
    e = {(i, j): z3.Bool(f"e_{i}_{j}") for i in range(n) for j in range(i + 1, n)}

    def edge(i: int, j: int):
        return z3.BoolVal(False) if i == j else e[min(i, j), max(i, j)]

    deg = [z3.Sum([z3.If(edge(i, j), 1, 0) for j in range(n) if j != i]) for i in range(n)]
    for d in deg:
        s.add(d >= k - 1)
    for i in range(n - 1):
        s.add(deg[i] <= deg[i + 1])

    # Every vertex deletion is (k-1)-colorable.
    for deleted in range(n):
        c = {v: z3.Int(f"del_{deleted}_{v}") for v in range(n) if v != deleted}
        for v in c:
            s.add(0 <= c[v], c[v] < k - 1)
        for i in range(n):
            if i == deleted:
                continue
            for j in range(i + 1, n):
                if j != deleted:
                    s.add(z3.Implies(edge(i, j), c[i] != c[j]))

    # Eagerly forbid every canonical (k-1)-coloring.
    labels = [0] * n
    partition_count = 0

    def partitions(pos: int, current_max: int) -> None:
        nonlocal partition_count
        if pos == n:
            s.add(z3.Or([edge(i, j) for i in range(n) for j in range(i + 1, n) if labels[i] == labels[j]]))
            partition_count += 1
            return
        for c in range(min(current_max + 1, k - 2) + 1):
            labels[pos] = c
            partitions(pos + 1, max(current_max, c))

    partitions(1, 0)
    print("color partitions", partition_count, flush=True)

    def add_no_witness(mask: int, idx: int) -> None:
        ds = [v for v in range(n) if (mask >> v) & 1]
        hs = [v for v in range(n) if not ((mask >> v) & 1)]
        root = ds[0]
        reach = {v: z3.Or(z3.BoolVal(v == root), edge(root, v)) for v in ds}
        for _ in range(max(0, len(ds) - 1)):
            old = reach
            reach = {v: z3.Or(old[v], *[z3.And(old[u], edge(u, v)) for u in ds if u != v]) for v in ds}
        conn = z3.And([reach[v] for v in ds])
        dom = z3.And([z3.Or([edge(h, d) for d in ds]) for h in hs])
        c = {h: z3.Int(f"lazy_{idx}_{h}") for h in hs}
        proper = []
        for h in hs:
            proper += [0 <= c[h], c[h] < k - 2]
        for ii, i in enumerate(hs):
            for j in hs[ii + 1:]:
                proper.append(z3.Implies(edge(i, j), c[i] != c[j]))
        s.add(z3.Implies(z3.And(conn, dom), z3.And(proper)))

    seen_masks: set[int] = set()
    iteration = 0
    while True:
        status = s.check()
        print("iteration", iteration, "constraints", len(seen_masks), status, flush=True)
        if status != z3.sat:
            return
        m = s.model()
        adj = [0] * n
        for (i, j), x in e.items():
            if z3.is_true(m.eval(x)):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
        assert chromatic_number(adj) == k
        ok, d = has_cd_remainder(adj, k)
        if not ok:
            print("COUNTEREXAMPLE", graph6(adj))
            for v, a in enumerate(adj):
                print(v, [u for u in range(n) if (a >> u) & 1])
            return
        if d not in seen_masks:
            seen_masks.add(d)
            add_no_witness(d, iteration)
        else:
            # The fixed-mask formula should make exact repetition impossible;
            # block the labeled graph defensively if a solver/model quirk occurs.
            literals = []
            for x in e.values():
                literals.append(z3.Not(x) if z3.is_true(m.eval(x)) else x)
            s.add(z3.Or(literals))
        iteration += 1


if __name__ == "__main__":
    main()
