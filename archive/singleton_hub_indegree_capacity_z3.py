#!/usr/bin/env python3
"""Exact nine-vertex interface check for the degree-nine singleton hub.

The graph F has vertices 0,...,8.  A vertex v is LOCAL when

    d_F(v)=4 and F[N_F(v)] = 2 K_2.

It is DARK when one of the two K_2 components of F[N_F(v)] has a
common antineighbour x which is also nonadjacent to v.  Equivalently,
some triangle containing v has an antivertex.

The check proves:

  (i) seven prescribed LOCAL vertices and DARK(0) is UNSAT;
  (ii) six prescribed LOCAL+DARK vertices is SAT.

By relabelling, (i) says that no graph on nine vertices has seven
vertices which are both LOCAL and DARK.  Item (ii) proves sharpness of
the finite interface statement.
"""

from itertools import combinations
import z3


N = 9
EDGE = {
    (u, v): z3.Bool(f"e_{u}_{v}")
    for u in range(N)
    for v in range(u + 1, N)
}


def edge(u: int, v: int):
    if u == v:
        return z3.BoolVal(False)
    return EDGE[tuple(sorted((u, v)))]


def local(v: int):
    degree_four = z3.PbEq(
        [(edge(v, u), 1) for u in range(N) if u != v], 4
    )

    # If u is a neighbour of v, it has exactly one neighbour among the
    # other three vertices of N(v).  With d(v)=4 this is precisely 2 K_2.
    matching_neighbourhood = []
    for u in range(N):
        if u == v:
            continue
        co_neighbours = [
            z3.And(edge(v, w), edge(u, w))
            for w in range(N)
            if w not in (u, v)
        ]
        matching_neighbourhood.append(
            z3.Implies(
                edge(v, u), z3.PbEq([(term, 1) for term in co_neighbours], 1)
            )
        )
    return z3.And(degree_four, *matching_neighbourhood)


def dark(v: int):
    witnesses = []
    for a, c in combinations([u for u in range(N) if u != v], 2):
        for x in range(N):
            if x in (v, a, c):
                continue
            witnesses.append(
                z3.And(
                    edge(v, a),
                    edge(v, c),
                    edge(a, c),
                    z3.Not(edge(v, x)),
                    z3.Not(edge(a, x)),
                    z3.Not(edge(c, x)),
                )
            )
    return z3.Or(witnesses)


def edge_list(model):
    return [
        pair for pair, variable in EDGE.items() if z3.is_true(model.eval(variable))
    ]


seven = z3.Solver()
seven.add(*(local(v) for v in range(7)))
seven.add(dark(0))
result_seven = seven.check()
print("seven local vertices, vertex 0 dark:", result_seven)
assert result_seven == z3.unsat

six = z3.Solver()
six.add(*(local(v) for v in range(6)))
six.add(*(dark(v) for v in range(6)))
result_six = six.check()
print("six local and dark vertices:", result_six)
assert result_six == z3.sat
print("sharpness witness edges:", edge_list(six.model()))

# A deterministic sharpness witness used in the accompanying note.  Its
# six special vertices are checked without asking the solver for a model.
H_EDGES = {
    tuple(sorted(pair))
    for pair in [
        (0, 2), (0, 3), (0, 5), (0, 7),
        (1, 3), (1, 4), (1, 5), (1, 8),
        (2, 4), (2, 5), (2, 6),
        (3, 4), (3, 7), (4, 6), (5, 8), (7, 8),
    ]
}


def h_edge(u: int, v: int) -> bool:
    return tuple(sorted((u, v))) in H_EDGES


for v in range(6):
    neighbours = [u for u in range(N) if u != v and h_edge(u, v)]
    assert len(neighbours) == 4
    local_edges = [pair for pair in combinations(neighbours, 2) if h_edge(*pair)]
    assert len(local_edges) == 2
    assert len(set(local_edges[0]) & set(local_edges[1])) == 0
    assert any(
        h_edge(v, a)
        and h_edge(v, c)
        and h_edge(a, c)
        and not h_edge(v, x)
        and not h_edge(a, x)
        and not h_edge(c, x)
        for a, c in combinations(range(N), 2)
        if v not in (a, c)
        for x in range(N)
        if x not in (v, a, c)
    )

print("deterministic planar-family block: checked")
