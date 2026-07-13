#!/usr/bin/env python3
"""Enumerate Property-B state colourings for the ten seven-edge packet cores.

The output is a diagnostic for operation-state exchange: it records the
number of exact-block red/blue colourings (up to global swap), and all
state pairs forced to the same or opposite shore by every such colouring.
"""

from __future__ import annotations

from equality_gate_exact_block_property_b import RAW, S, clique
from equality_gate_seven_edge_packet_atlas import FINAL_RESIDUAL, seven_edge_types


THETA_OMEGA_012 = (
    ((0, 1, 2), (3,), (4,), (5,), (6,)),
    ((0, 1, 2), (3,), (4, 5), (6,)),
)
THETA_OMEGA_015 = (
    ((0, 1, 5), (2,), (3,), (4,), (6,)),
    ((0, 1, 5), (2, 4), (3,), (6,)),
)
THETA_FORCED_OPPOSITE = {
    frozenset(THETA_OMEGA_012),
    frozenset(THETA_OMEGA_015),
}


def instance(missing):
    missing_edges = {tuple(sorted(e)) for e in missing.edges()}
    states = [pi for pi in RAW if len(pi) <= 6 and all(clique(b, missing_edges) for b in pi)]
    idx = {pi: i for i, pi in enumerate(states)}
    blocks = [
        tuple(v for v in S if mask >> v & 1)
        for mask in range(1, 1 << 7)
    ]
    blocks = [b for b in blocks if clique(b, missing_edges)]
    edges = [tuple(idx[pi] for pi in states if b in pi) for b in blocks]
    return states, blocks, edges


def enumerate_nae(n, edges, cap=500_000):
    incident = [[] for _ in range(n)]
    for j, edge in enumerate(edges):
        for v in edge:
            incident[v].append(j)
    count = 0
    samples = []
    relation = [[0] * n for _ in range(n)]

    def propagate(colour, queue):
        colour = list(colour)
        while queue:
            ei = queue.pop()
            edge = edges[ei]
            vals = {colour[v] for v in edge if colour[v] >= 0}
            free = [v for v in edge if colour[v] < 0]
            if not free:
                if len(vals) < 2:
                    return None
                continue
            if len(vals) == 1 and len(free) == 1:
                v = free[0]
                forced = 1 - next(iter(vals))
                colour[v] = forced
                queue.extend(incident[v])
        return tuple(colour)

    def rec(colour):
        nonlocal count
        if count >= cap:
            return
        colour = propagate(colour, list(range(len(edges))))
        if colour is None:
            return
        if all(c >= 0 for c in colour):
            count += 1
            if len(samples) < 32:
                samples.append(colour)
            for i in range(n):
                for j in range(i + 1, n):
                    relation[i][j] |= 1 << (colour[i] ^ colour[j])
            return
        candidates = []
        for edge in edges:
            vals = {colour[v] for v in edge if colour[v] >= 0}
            if len(vals) == 2:
                continue
            free = [v for v in edge if colour[v] < 0]
            if free:
                candidates.append((len(free), free[0]))
        v = min(candidates)[1] if candidates else colour.index(-1)
        for c in (0, 1):
            child = list(colour)
            child[v] = c
            rec(tuple(child))
            if count >= cap:
                break

    start = [-1] * n
    start[0] = 0  # quotient by global red/blue interchange
    rec(tuple(start))
    return count, count >= cap, samples, relation


def nae_satisfiable(n, edges, fixed):
    def propagate(colour):
        colour = list(colour)
        changed = True
        while changed:
            changed = False
            for edge in edges:
                vals = {colour[v] for v in edge if colour[v] >= 0}
                free = [v for v in edge if colour[v] < 0]
                if not free:
                    if len(vals) < 2:
                        return None
                    continue
                if len(vals) == 1 and len(free) == 1:
                    colour[free[0]] = 1 - next(iter(vals))
                    changed = True
        return tuple(colour)

    def rec(colour):
        colour = propagate(colour)
        if colour is None:
            return False
        if all(c >= 0 for c in colour):
            return True
        best = None
        for edge in edges:
            vals = {colour[v] for v in edge if colour[v] >= 0}
            if len(vals) == 2:
                continue
            free = [v for v in edge if colour[v] < 0]
            if free and (best is None or len(free) < best[0]):
                best = (len(free), free[0])
        v = best[1] if best else colour.index(-1)
        for c in (0, 1):
            child = list(colour)
            child[v] = c
            if rec(tuple(child)):
                return True
        return False

    start = [-1] * n
    for v, c in fixed.items():
        start[v] = c
    return rec(tuple(start))


def main():
    types = seven_edge_types()
    for index in sorted(FINAL_RESIDUAL):
        states, blocks, edges = instance(types[index])
        forced_same = []
        forced_opp = []
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                same = nae_satisfiable(len(states), edges, {i: 0, j: 0})
                opposite = nae_satisfiable(len(states), edges, {i: 0, j: 1})
                assert same or opposite
                if same and not opposite:
                    forced_same.append((i, j))
                elif opposite and not same:
                    forced_opp.append((i, j))
        forced_partitions = {
            frozenset((states[i], states[j])) for i, j in forced_opp
        }
        assert not forced_same
        assert forced_partitions == (
            THETA_FORCED_OPPOSITE if index == 0 else set()
        )
        if index == 0:
            omega_012 = tuple(pi for pi in states if (0, 1, 2) in pi)
            omega_015 = tuple(pi for pi in states if (0, 1, 5) in pi)
            assert omega_012 == THETA_OMEGA_012
            assert omega_015 == THETA_OMEGA_015
            merged_012 = states.index(THETA_OMEGA_012[1])
            merged_015 = states.index(THETA_OMEGA_015[1])
            assert nae_satisfiable(
                len(states), edges, {merged_012: 0, merged_015: 0}
            )
            assert nae_satisfiable(
                len(states), edges, {merged_012: 0, merged_015: 1}
            )
        print(
            "type", index,
            "states", len(states),
            "blocks", len(blocks),
            "forced_same", len(forced_same),
            "forced_opp", len(forced_opp),
        )
        if forced_same:
            print(" same", forced_same[:40])
        if forced_opp:
            print(" opposite", forced_opp[:40])
            print(" opposite_partitions", [
                (states[i], states[j]) for i, j in forced_opp[:40]
            ])


if __name__ == "__main__":
    main()
