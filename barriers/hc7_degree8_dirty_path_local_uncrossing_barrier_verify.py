#!/usr/bin/env python3
"""Verify the matching-defect dirty-path barrier at a degree-eight interface.

This checks one exact local inference.  It does not search for, or claim to
construct, a minor-minimal contraction-critical host.
"""

from itertools import combinations, product


U = ("a", "b", "c", "d", "e")
Q = ("q0", "q1", "q2")
S = set(U + Q)
AUXILIARY = {"x", "y", "r", "s", "t"}
SIXTH_COLOUR_HUBS = {"h", "h1", "h2", "h3", "h4", "h5", "h6"}
C = AUXILIARY | SIXTH_COLOUR_HUBS
POLE = "u"
VERTICES = S | C | {POLE}


def edge(v: str, w: str) -> tuple[str, str]:
    assert v != w
    return tuple(sorted((v, w)))


# The five-colour slice.  The roots induce exactly 2K2+K1, with literal
# edges ab,cd.  The two omitted matching demands are ae,bc.
SLICE_EDGES = {
    edge("e", "x"),
    edge("x", "y"),
    edge("y", "a"),
    edge("d", "x"),
    edge("b", "r"),
    edge("r", "s"),
    edge("s", "c"),
    edge("e", "r"),
    edge("a", "b"),
    edge("c", "d"),
    edge("b", "x"),
    edge("a", "t"),
    edge("t", "c"),
}

EDGES = set(SLICE_EDGES)

# The degree-eight pole and a jointly dominating Q--U boundary pattern.
EDGES.update(edge(POLE, v) for v in S)
EDGES.update(edge(q, v) for q in ("q0", "q1") for v in ("a", "b", "c", "d"))
EDGES.update(edge("q2", v) for v in U)

# q0,q1 have the same six-vertex neighbourhood in G-u.  q2 needs only one
# extra open-side contact to make it a boundary vertex.
EDGES.update(edge(q, v) for q in ("q0", "q1") for v in ("x", "y"))
EDGES.add(edge("q2", "x"))

# Seven independent sixth-colour hubs are complete to the five-colour slice.
# This makes the displayed wrapper exactly seven-connected without changing
# the local slice in which the rooted certificate and paths live.
EDGES.update(
    edge(hub, v)
    for hub in SIXTH_COLOUR_HUBS
    for v in set(U) | AUXILIARY
)

COLOUR = {
    POLE: "Q",
    "q0": "Q",
    "q1": "Q",
    "q2": "Q",
    "h": "Q",
    "h1": "Q",
    "h2": "Q",
    "h3": "Q",
    "h4": "Q",
    "h5": "Q",
    "h6": "Q",
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E",
    "x": "A",
    "y": "E",
    "r": "C",
    "s": "B",
    "t": "B",
}

PATHS = {
    edge("a", "e"): ("e", "x", "y", "a"),
    edge("b", "c"): ("b", "r", "s", "c"),
}
MODEL = {
    "a": {"a", "t"},
    "b": {"b"},
    "c": {"c"},
    "d": {"d", "x", "y"},
    "e": {"e", "r", "s"},
}
W = set().union(*MODEL.values())
Z = {"a", "b", "c", "d", "x", "y"}
LITERAL_ROOT_EDGES = {edge("a", "b"), edge("c", "d")}
OMITTED_MATCHING = {edge("a", "e"), edge("b", "c")}
SIX_DEMANDS = {
    edge(v, w)
    for v, w in combinations(U, 2)
    if edge(v, w) not in LITERAL_ROOT_EDGES | OMITTED_MATCHING
}


def neighbours(v: str, vertices: set[str] = VERTICES) -> set[str]:
    return {w for w in vertices - {v} if edge(v, w) in EDGES}


def connected(
    vertices: set[str], edges: set[tuple[str, str]] = EDGES
) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            v
            for v in vertices - reached
            if any(edge(v, w) in edges for w in reached)
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def components(vertices: set[str]) -> list[set[str]]:
    remaining = set(vertices)
    answer = []
    while remaining:
        start = next(iter(remaining))
        component = {start}
        while True:
            enlarged = component | {
                v
                for v in remaining - component
                if any(edge(v, w) in EDGES for w in component)
            }
            if enlarged == component:
                break
            component = enlarged
        answer.append(component)
        remaining -= component
    return answer


def adjacent(
    left: set[str],
    right: set[str],
    edges: set[tuple[str, str]] = EDGES,
) -> bool:
    return any(edge(v, w) in edges for v in left for w in right)


def assert_interface_and_colouring() -> None:
    assert set(COLOUR) == VERTICES
    assert neighbours(POLE) == S
    assert connected(C)
    assert set().union(*(neighbours(v) - C for v in C)) == S

    root_edges = {
        edge(v, w) for v, w in combinations(U, 2) if edge(v, w) in EDGES
    }
    assert root_edges == LITERAL_ROOT_EDGES
    assert all(edge(v, w) not in EDGES for v, w in combinations(Q, 2))
    assert all(any(edge(q, root) in EDGES for q in Q) for root in U)

    alpha = max(
        len(independent)
        for size in range(len(S) + 1)
        for independent in combinations(S, size)
        if all(edge(v, w) not in EDGES for v, w in combinations(independent, 2))
    )
    assert alpha == 3

    deleted_star_edges = {edge(POLE, q) for q in Q}
    assert all(
        COLOUR[v] != COLOUR[w]
        for v, w in EDGES - deleted_star_edges
    )
    assert {COLOUR[q] for q in Q} == {"Q"}
    assert len({COLOUR[root] for root in U}) == 5
    assert "Q" not in {COLOUR[root] for root in U}


def assert_exact_connectivity() -> None:
    vertices = tuple(sorted(VERTICES))
    cuts_checked = 0
    for size in range(7):
        for deleted in combinations(vertices, size):
            cuts_checked += 1
            assert connected(VERTICES - set(deleted))
    assert cuts_checked == 82160

    # The seven neighbours of q0 are an actual cut, so connectivity is exact.
    cut = neighbours("q0")
    assert cut == Z | {POLE}
    assert len(cut) == 7
    assert not connected(VERTICES - cut)


def reduced_bag_trace(path: tuple[str, ...]) -> list[str]:
    owner = {v: root for root, bag in MODEL.items() for v in bag}
    trace = []
    for v in path:
        current = owner[v]
        if not trace or trace[-1] != current:
            trace.append(current)
    return trace


def assert_paths_and_certificate() -> None:
    assert set(PATHS[edge("a", "e")]).isdisjoint(PATHS[edge("b", "c")])
    for ends, path in PATHS.items():
        assert edge(path[0], path[-1]) == ends
        assert all(edge(v, w) in EDGES for v, w in zip(path, path[1:]))
        assert len({COLOUR[v] for v in path}) == 2
        assert set(path[1:-1]) <= C
        assert set(path[1:-1]).isdisjoint(S | {POLE})

    assert set(MODEL) == set(U)
    assert all(root in bag for root, bag in MODEL.items())
    assert sum(map(len, MODEL.values())) == len(W)
    assert all(connected(bag, SLICE_EDGES) for bag in MODEL.values())

    quotient_edges = {
        edge(v, w)
        for v, w in combinations(U, 2)
        if adjacent(MODEL[v], MODEL[w], SLICE_EDGES)
    }
    assert quotient_edges == LITERAL_ROOT_EDGES | SIX_DEMANDS
    assert len(SIX_DEMANDS) == 6
    assert {
        edge(v, w) for v, w in combinations(U, 2)
    } - quotient_edges == OMITTED_MATCHING

    assert reduced_bag_trace(PATHS[edge("a", "e")]) == ["e", "d", "a"]
    assert reduced_bag_trace(PATHS[edge("b", "c")]) == ["b", "e", "c"]

    # Adding the two routed pairs to the literal 2K2+K1 gives the spanning P5
    # e-a-b-c-d.
    path_edges = LITERAL_ROOT_EDGES | OMITTED_MATCHING
    assert path_edges == {
        edge("e", "a"),
        edge("a", "b"),
        edge("b", "c"),
        edge("c", "d"),
    }

    routing_edges = set()
    for v, w in combinations(U, 2):
        two_colours = {COLOUR[v], COLOUR[w]}
        induced_vertices = {z for z in W if COLOUR[z] in two_colours}
        if any(
            v in component and w in component
            for component in components(induced_vertices)
        ):
            routing_edges.add(edge(v, w))
    assert routing_edges == LITERAL_ROOT_EDGES | OMITTED_MATCHING


def assert_connector_separator_alternative() -> None:
    h_vertices = VERTICES - {POLE}
    outside_components = components(h_vertices - W)
    assert all(len(component & set(Q)) <= 1 for component in outside_components)

    assert Z <= W and len(Z) == 6
    assert MODEL["d"] & Z == {"d", "x", "y"}
    for q in ("q0", "q1"):
        assert neighbours(q, h_vertices) == Z

    residual_components = components(h_vertices - Z)
    q_components = {
        q: next(component for component in residual_components if q in component)
        for q in ("q0", "q1")
    }
    assert all(q_components[q] == {q} for q in ("q0", "q1"))

    # Inclusion-minimality: restoring any z in Z restores q0-z-q1.
    assert all(edge("q0", z) in EDGES and edge(z, "q1") in EDGES for z in Z)


def assert_explicit_k8_scope_warning() -> None:
    k8_bags = (
        {"h", "a"},
        {"h1", "b"},
        {"h2", "c"},
        {"h3", "d"},
        {"h4", "e"},
        {"h5", "x"},
        {"h6"},
        {"y"},
    )
    assert sum(map(len, k8_bags)) == len(set().union(*k8_bags))
    assert all(connected(bag) for bag in k8_bags)
    assert all(adjacent(left, right) for left, right in combinations(k8_bags, 2))


def is_rooted_model(
    assignment: tuple[int, ...], allowed_defects: set[tuple[str, str]]
) -> bool:
    free = tuple(sorted(W - set(U)))
    bags = {root: {root} for root in U}
    for vertex, target in zip(free, assignment):
        if target < len(U):
            bags[U[target]].add(vertex)
    if not all(connected(bag, SLICE_EDGES) for bag in bags.values()):
        return False
    return all(
        edge(v, w) in allowed_defects
        or adjacent(bags[v], bags[w], SLICE_EDGES)
        for v, w in combinations(U, 2)
    )


def count_rooted_models(allowed_defects: set[tuple[str, str]]) -> int:
    free = tuple(sorted(W - set(U)))
    # Values 0,...,4 assign a vertex to that rooted bag; 5 leaves it unused.
    return sum(
        is_rooted_model(assignment, allowed_defects)
        for assignment in product(range(len(U) + 1), repeat=len(free))
    )


def main() -> None:
    assert_interface_and_colouring()
    assert_exact_connectivity()
    assert_paths_and_certificate()
    assert_connector_separator_alternative()
    assert_explicit_k8_scope_warning()

    two_matching_defect_count = count_rooted_models(OMITTED_MATCHING)
    no_defect_count = count_rooted_models(set())
    singleton_defect_counts = {
        "".join(edge(v, w)): count_rooted_models({edge(v, w)})
        for v, w in combinations(U, 2)
    }
    assert two_matching_defect_count == 8
    assert no_defect_count == 0
    assert singleton_defect_counts == {
        "ab": 0,
        "ac": 0,
        "ad": 0,
        "ae": 0,
        "bc": 0,
        "bd": 0,
        "be": 0,
        "cd": 0,
        "ce": 0,
        "de": 0,
    }
    if no_defect_count:
        minimum_missing_adjacencies = 0
    elif any(singleton_defect_counts.values()):
        minimum_missing_adjacencies = 1
    elif two_matching_defect_count:
        minimum_missing_adjacencies = 2
    else:
        minimum_missing_adjacencies = None
    assert minimum_missing_adjacencies == 2

    print("GREEN: matching-defect dirty-path barrier verified")
    print("vertices=21; connectivity=7; five_colour_slice_vertices=10")
    print("vertex_cuts_of_order_at_most_6_checked=82160")
    print("assignments_per_rooted_model_test=7776")
    print("literal_root_graph=2K2+K1; routed_matching=ae,bc; union=P5")
    print("bag_traces=ae:e-d-a,bc:b-e-c; separator={a,b,c,d,x,y}; |Z|=6")
    print(f"two_matching_defect_models={two_matching_defect_count}")
    print("singleton_allowed_defect_counts", singleton_defect_counts)
    print(f"no_defect_models={no_defect_count}")
    print(f"minimum_missing_adjacencies={minimum_missing_adjacencies}")
    print("routing_graph_edges=ab,ae,bc,cd (not complete)")
    print("full_host_scope_warning=explicit_K8_minor")
    print("scope=local_certificate_only; minor exclusion and criticality absent")


if __name__ == "__main__":
    main()
