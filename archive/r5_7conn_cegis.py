import z3
from itertools import combinations
import sys

import r5_7conn_search as search


V = tuple(range(12))
pairs = tuple((i, j) for i in V for j in V if i < j)
edge_var = {p: z3.Bool(f"e_{p[0]}_{p[1]}") for p in pairs}


def edge(x, y):
    return edge_var[min(x, y), max(x, y)]


def configure_roots(roots):
    """Update the exact apex neighbourhood used by the exhaustive checker."""
    search.roots = tuple(roots)
    search.nonroots = tuple(x for x in search.h_vertices if x not in search.roots)
    root_partitions = []
    for used in combinations(search.roots, 6):
        root_partitions.append(tuple((x,) for x in used))
    for partition in search.set_partitions(search.roots, 6):
        root_partitions.append(partition)
    search.root_partitions = root_partitions


def connected_formula(block):
    block = tuple(sorted(block))
    if len(block) <= 1:
        return z3.BoolVal(True)
    first = block[0]
    constraints = []
    rest = block[1:]
    # Every proper cut of the induced subgraph has a crossing edge.
    for mask in range(1 << len(rest)):
        side = {first}
        side.update(rest[i] for i in range(len(rest)) if mask & (1 << i))
        if len(side) == len(block):
            continue
        other = set(block) - side
        constraints.append(z3.Or(*[edge(x, y) for x in side for y in other]))
    return z3.And(*constraints)


def model_formula(model):
    conditions = [connected_formula(B) for B in model]
    for i in range(6):
        for j in range(i):
            conditions.append(z3.Or(*[edge(x, y) for x in model[i] for y in model[j]]))
    return z3.And(*conditions)


def make_solver(regular=False):
    S = z3.Solver()
    # Exact apex neighbourhood.
    for j in range(1, 12):
        S.add(edge(0, j) == (j in search.roots))
    # Saturated two-portal bag and its four target monopolies.
    S.add(edge(2, 3), edge(1, 2), edge(1, 3))
    for j in search.bags[0] + search.bags[1]:
        S.add(edge(2, j), z3.Not(edge(3, j)))
    for j in search.bags[2] + search.bags[3]:
        S.add(edge(3, j), z3.Not(edge(2, j)))
    # Fixed two-vertex target bags and required model adjacencies.
    for bag in search.bags:
        S.add(edge(*bag))
        S.add(z3.Or(*[edge(1, x) for x in bag]))
    for i in range(4):
        for j in range(i + 1, 4):
            S.add(z3.Or(*[edge(x, y) for x in search.bags[i] for y in search.bags[j]]))
    # Search the sharp regular case or the full minimum-degree class.
    for i in V:
        degree = z3.Sum(*[z3.If(edge(i, j), 1, 0) for j in V if i != j])
        S.add(degree == 7 if regular else degree >= 7)
    return S


def edge_set(model):
    return {p for p in pairs if z3.is_true(model[edge_var[p]])}


def disconnected_cut(E):
    N = search.neighbourhoods(E)
    from itertools import combinations

    for k in range(1, 7):
        for cut_tuple in combinations(V, k):
            cut = set(cut_tuple)
            rem = set(V) - cut
            seen = {next(iter(rem))}
            while True:
                new = seen | {y for x in seen for y in N[x] & rem}
                if new == seen:
                    break
                seen = new
            if seen != rem:
                return cut, seen, rem - seen
    return None


def main(limit=10000, regular=False):
    S = make_solver(regular=regular)
    forbidden_models = 0
    repaired_cuts = 0
    for iteration in range(limit):
        verdict = S.check()
        if verdict != z3.sat:
            print("VERDICT", verdict, "iterations", iteration,
                  "models", forbidden_models, "cuts", repaired_cuts)
            return
        E = edge_set(S.model())
        cut = disconnected_cut(E)
        if cut is not None:
            deleted, side, other = cut
            S.add(z3.Or(*[edge(x, y) for x in side for y in other]))
            repaired_cuts += 1
            continue
        model = search.has_six_contact_model(E)
        if model is None:
            print("FOUND", sorted(E), "iterations", iteration,
                  "models", forbidden_models, "cuts", repaired_cuts)
            return
        S.add(z3.Not(model_formula(model)))
        forbidden_models += 1
        if forbidden_models % 100 == 0:
            print("progress", forbidden_models, repaired_cuts, flush=True)
    print("LIMIT", limit, forbidden_models, repaired_cuts)


if __name__ == "__main__":
    if "--all-contact-patterns" not in sys.argv:
        main()
    else:
        # Up to the symmetries preserving the two saturated portal sides,
        # these are all ways for v to meet a,b, at least one vertex of each
        # two-vertex target bag, and at least seven vertices in total.
        patterns = (
            (2, 3, 4, 5, 6, 8, 10),              # one doubled target
            (2, 3, 4, 5, 6, 7, 8, 10),           # two doubled, same side
            (2, 3, 4, 5, 6, 8, 9, 10),           # two doubled, split sides
            (2, 3, 4, 5, 6, 7, 8, 9, 10),        # three doubled targets
            (2, 3, 4, 5, 6, 7, 8, 9, 10, 11),    # all doubled targets
        )
        for roots in patterns:
            print("ROOTS", roots, flush=True)
            configure_roots(roots)
            main()
