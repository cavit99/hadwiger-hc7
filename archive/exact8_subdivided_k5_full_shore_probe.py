#!/usr/bin/env python3
"""Test two full singleton shores over three-edge subdivisions of K5."""

from __future__ import annotations

import itertools

from contact_order7_sixedge_web_probe import generic_minor_model


K5_EDGES = list(itertools.combinations(range(5), 2))


def subdivided_core(chosen: tuple[tuple[int, int], ...]):
    edges = set(K5_EDGES) - set(chosen)
    for i, (u, v) in enumerate(chosen, start=5):
        edges.add(tuple(sorted((u, i))))
        edges.add(tuple(sorted((i, v))))
    return {tuple(sorted(e)) for e in edges}


def treewidth(n: int, edges: set[tuple[int, int]]) -> int:
    """Exact elimination-order search; n=10 here."""
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    best = n - 1

    def rec(alive: set[int], adj: list[set[int]], width: int):
        nonlocal best
        if width >= best:
            return
        if not alive:
            best = width
            return
        for v in sorted(alive, key=lambda x: len(adj[x] & alive)):
            nbr = adj[v] & alive
            new_width = max(width, len(nbr))
            if new_width >= best:
                continue
            nadj = [set(a) for a in adj]
            for x, y in itertools.combinations(nbr, 2):
                nadj[x].add(y)
                nadj[y].add(x)
            rec(alive - {v}, nadj, new_width)

    rec(set(range(n)), adjacency, 0)
    return best


def main():
    signatures: dict[tuple[int, ...], dict[str, object]] = {}
    positive = 0
    negative = 0
    for chosen in itertools.combinations(K5_EDGES, 3):
        core = subdivided_core(chosen)
        # The degree multiset of the three-edge graph records its orbit on K5.
        deg = [0] * 5
        for u, v in chosen:
            deg[u] += 1
            deg[v] += 1
        sig = tuple(sorted(deg, reverse=True))

        full = set(core)
        for shore in (8, 9):
            full.update((shore, x) for x in range(8))

        model = generic_minor_model(10, full, 7)
        tw = treewidth(10, full)
        if model:
            positive += 1
        else:
            negative += 1

        deletion_eta = []
        for x in range(8):
            verts = [v for v in range(8) if v != x]
            relabel = {v: i for i, v in enumerate(verts)}
            e2 = {
                tuple(sorted((relabel[u], relabel[v])))
                for u, v in core
                if u != x and v != x
            }
            deletion_eta.append(bool(generic_minor_model(7, e2, 5)))

        row = signatures.setdefault(
            sig,
            {
                "chosen": chosen,
                "count": 0,
                "k7": set(),
                "deletion_k5": set(),
                "model": model,
                "treewidth": set(),
            },
        )
        row["count"] = int(row["count"]) + 1
        row["k7"].add(bool(model))
        row["deletion_k5"].add(tuple(deletion_eta))
        row["treewidth"].add(tw)

    print("total", positive + negative, "K7", positive, "noK7", negative)
    for sig, row in sorted(signatures.items()):
        print(sig, row)


if __name__ == "__main__":
    main()
