#!/usr/bin/env python3
"""Lazy exact search for an order-four shore in either sharp core.

For each connected four-vertex internal graph, boundary attachments are
constrained by:
  * full attachment to the seven-vertex boundary;
  * minimum degree seven at every shore vertex; and
  * every nonempty shore subset X has |N_D(X)|+|N_S(X)| >= 7, the local
    cut inequality forced by seven-connectivity.

The opposite full shore is contracted to one helper.  Z3 proposes an
attachment system.  An independent exact connected-branch-set search
either finds a K7 model, in which case a sufficient sorted-edge witness
is blocked, or returns a genuine local counterarchitecture.
"""

import itertools
import sys
import z3


S = tuple(range(7))
D = tuple(range(7, 11))
H = 11
V = tuple(range(12))
VARIABLE = tuple((s, d) for d in D for s in S)


INTERNAL_TYPES = {
    "P4": ((7, 8), (8, 9), (9, 10)),
    "K13": ((7, 8), (7, 9), (7, 10)),
    "C4": ((7, 8), (8, 9), (9, 10), (7, 10)),
    "paw": ((7, 8), (8, 9), (7, 9), (7, 10)),
    "diamond": tuple(
        edge for edge in itertools.combinations(D, 2) if edge != (9, 10)
    ),
    "K4": tuple(itertools.combinations(D, 2)),
}


def boundary_edges(kind):
    pairs = set(itertools.combinations(S, 2))
    if kind == "C5+2K1":
        missing = {
            tuple(sorted((i, (i + 2) % 5))) for i in range(5)
        }
    elif kind == "K3+2K2":
        missing = {(0, 1), (0, 2), (1, 2), (3, 4), (5, 6)}
    else:
        raise AssertionError(kind)
    return pairs - missing


def fixed_edges(core_kind, internal):
    edges = set(boundary_edges(core_kind))
    edges.update(tuple(sorted(edge)) for edge in internal)
    edges.update((s, H) for s in S)
    return {tuple(sorted(edge)) for edge in edges}


def k_minor_model(edges, k=7):
    n = len(V)
    adjacency = [0] * n
    for i, j in edges:
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << n)
    connected = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(a, b):
        return not (a & b) and bool(neighbour_union[a] & b)

    def rec(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        if len(candidates) < needed:
            return None
        for pos, a in enumerate(candidates):
            if a & used:
                continue
            nxt = [
                b for b in candidates[pos + 1:]
                if not b & (used | a) and adjacent(a, b)
            ]
            if len(nxt) >= needed - 1:
                answer = rec(chosen + [a], nxt, used | a)
                if answer is not None:
                    return answer
        return None
    return rec([], connected, 0)


def verify_model(edges, model):
    edges = set(edges)
    bags = [set(v for v in V if mask >> v & 1) for mask in model]
    assert len(bags) == 7
    assert all(bags)
    assert all(bags[i].isdisjoint(bags[j])
               for i in range(7) for j in range(i))
    for bag in bags:
        reached = {next(iter(bag))}
        while True:
            expanded = reached | {
                y for x in reached for y in bag
                if tuple(sorted((x, y))) in edges
            }
            if expanded == reached:
                break
            reached = expanded
        assert reached == bag
    for i in range(7):
        for j in range(i):
            assert any(tuple(sorted((x, y))) in edges
                       for x in bags[i] for y in bags[j])


def model_witness(edges, fixed, model):
    """Return variable edges sufficient to preserve this exact model."""
    edges = set(edges)
    fixed = set(fixed)
    variable = set(VARIABLE)
    bags = [tuple(v for v in V if mask >> v & 1) for mask in model]
    witness = set()

    # Prefer fixed edges in a deterministic spanning tree of each bag.
    for bag in bags:
        reached = {bag[0]}
        while len(reached) < len(bag):
            candidates = sorted(
                tuple(sorted((x, y)))
                for x in reached for y in bag
                if y not in reached and tuple(sorted((x, y))) in edges
            )
            assert candidates, (bag, reached)
            chosen = next((edge for edge in candidates if edge in fixed),
                          candidates[0])
            witness.add(chosen) if chosen in variable else None
            reached.add(chosen[0] if chosen[1] in reached else chosen[1])

    # Prefer a fixed cross-edge for every pair of bags.
    for i, first in enumerate(bags):
        for second in bags[:i]:
            candidates = sorted(
                tuple(sorted((x, y)))
                for x in first for y in second
                if tuple(sorted((x, y))) in edges
            )
            assert candidates
            chosen = next((edge for edge in candidates if edge in fixed),
                          candidates[0])
            witness.add(chosen) if chosen in variable else None

    assert witness <= variable
    assert witness <= edges
    # The witness must preserve this very model without any other optional
    # edge.  This is the key safety check for the lazy blocking clause.
    verify_model(fixed | witness, model)
    return tuple(sorted(witness))


def solve(core_kind, internal_name, limit=100000):
    internal = INTERNAL_TYPES[internal_name]
    fixed = fixed_edges(core_kind, internal)
    variables = {edge: z3.Bool(f"e_{edge[0]}_{edge[1]}")
                 for edge in VARIABLE}
    solver = z3.Solver()

    # Full attachment and vertex degree.
    for s in S:
        solver.add(z3.Or([variables[(s, d)] for d in D]))
    for d in D:
        internal_degree = sum(d in edge for edge in internal)
        solver.add(z3.Sum([variables[(s, d)] for s in S])
                   + internal_degree >= 7)

    # Necessary local cut inequalities from seven-connectivity.
    internal_set = {tuple(sorted(edge)) for edge in internal}
    for size in range(1, len(D)):
        for subset_tuple in itertools.combinations(D, size):
            subset = set(subset_tuple)
            outside_neighbours = {
                y for x in subset for y in D if y not in subset
                and tuple(sorted((x, y))) in internal_set
            }
            boundary_seen = [
                z3.Or([variables[(s, d)] for d in subset_tuple]) for s in S
            ]
            solver.add(z3.Sum(boundary_seen) + len(outside_neighbours) >= 7)

    for iteration in range(limit):
        if solver.check() != z3.sat:
            return {"status": "unsat", "iterations": iteration}
        assignment = solver.model()
        chosen = {
            edge for edge, variable in variables.items()
            if z3.is_true(assignment.eval(variable, model_completion=True))
        }
        edges = fixed | chosen
        model = k_minor_model(edges)
        if model is None:
            return {
                "status": "counterarchitecture",
                "iterations": iteration,
                "chosen": sorted(chosen),
            }
        verify_model(edges, model)
        witness = model_witness(edges, fixed, model)
        if not witness:
            return {"status": "unsat", "iterations": iteration + 1,
                    "fixed_model": True}
        solver.add(z3.Or([z3.Not(variables[edge]) for edge in witness]))
    return {"status": "limit", "iterations": limit}


def main():
    selected_core = sys.argv[1] if len(sys.argv) > 1 else None
    selected_internal = sys.argv[2] if len(sys.argv) > 2 else None
    cores = (selected_core,) if selected_core else ("C5+2K1", "K3+2K2")
    internals = (selected_internal,) if selected_internal else tuple(INTERNAL_TYPES)
    for core_kind in cores:
        for internal_name in internals:
            result = solve(core_kind, internal_name)
            print(core_kind, internal_name, result, flush=True)


if __name__ == "__main__":
    main()
