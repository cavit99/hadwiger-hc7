#!/usr/bin/env python3
"""Verify a same-bag two-edge exact-seven response barrier.

The graph is obtained from the audited adjacent-edge first-hit barrier by
adding one vertex of degree seven.  The new vertex exposes an actual
order-seven separation without changing the two critical edge responses.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from hc7_joint_pair_first_hit_hall_barrier_verify import (
    Graph,
    build_adjacent_example,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def proper_colouring(graph: Graph, colouring: dict[str, int]) -> bool:
    return set(colouring) == graph.vertices and all(
        colouring[x] != colouring[y]
        for x, y in (tuple(item) for item in graph.edges)
    )


def model_missing_pairs(
    graph: Graph, bags: dict[str, set[str]]
) -> set[frozenset[str]]:
    require(
        set().union(*bags.values()) == graph.vertices,
        "the branch sets do not span",
    )
    require(
        sum(map(len, bags.values())) == len(graph.vertices),
        "the branch sets are not disjoint",
    )
    for label, bag in bags.items():
        require(bag and graph.connected(bag), f"disconnected bag {label}")

    missing: set[frozenset[str]] = set()
    for left, right in combinations(sorted(bags), 2):
        if not any(
            graph.has_edge(x, y) for x in bags[left] for y in bags[right]
        ):
            missing.add(frozenset((left, right)))
    return missing


def verify_kappa_seven(graph: Graph, boundary: set[str]) -> None:
    vertices = sorted(graph.vertices)
    for order in range(7):
        for deleted in combinations(vertices, order):
            require(
                graph.connected_after_deleting(set(deleted)),
                f"cut below seven: {deleted}",
            )
    require(
        not graph.connected_after_deleting(boundary),
        "the displayed seven-set is not a cut",
    )


def verify_clique(graph: Graph, vertices: set[str]) -> None:
    for x, y in combinations(sorted(vertices), 2):
        require(graph.has_edge(x, y), f"missing clique edge {x}{y}")


def contract_edge(
    graph: Graph,
    x: str,
    y: str,
    colouring: dict[str, int],
) -> tuple[Graph, dict[str, int], str]:
    image = f"[{x},{y}]"
    quotient = Graph()
    for vertex in graph.vertices - {x, y}:
        quotient.add_vertex(vertex)
    quotient.add_vertex(image)
    for item in graph.edges:
        left, right = tuple(item)
        qleft = image if left in {x, y} else left
        qright = image if right in {x, y} else right
        if qleft != qright:
            quotient.add_edge(qleft, qright)
    qcolouring = {
        vertex: colour
        for vertex, colour in colouring.items()
        if vertex not in {x, y}
    }
    require(colouring[x] == colouring[y], "contracted colours differ")
    qcolouring[image] = colouring[x]
    return quotient, qcolouring, image


def support_by_colour(
    graph: Graph,
    root: str,
    colouring: dict[str, int],
    bags: dict[str, set[str]],
) -> dict[int, set[str]]:
    neighbours = graph.neighbours(root)
    return {
        colour: {
            label
            for label, bag in bags.items()
            if label != "R"
            and any(v in neighbours and colouring[v] == colour for v in bag)
        }
        for colour in range(6)
        if colour != colouring[root]
    }


def normalized_common_deletion_profiles(
    graph: Graph, boundary: set[str]
) -> Counter[tuple[str, tuple[tuple[str, ...], ...]]]:
    """Enumerate all six-colourings after fixing the displayed K6 palette."""

    fixed_order = ("a", "b", "c1", "c2", "c3", "c4")
    assigned = {vertex: colour for colour, vertex in enumerate(fixed_order)}
    adjacency = {vertex: graph.neighbours(vertex) for vertex in graph.vertices}
    profiles: Counter[tuple[str, tuple[tuple[str, ...], ...]]] = Counter()

    def search() -> None:
        if len(assigned) == len(graph.vertices):
            signature = (
                ("E" if assigned["v"] == assigned["a"] else "P")
                + ("E" if assigned["v"] == assigned["b"] else "P")
            )
            blocks: dict[int, list[str]] = {}
            for vertex in sorted(boundary):
                blocks.setdefault(assigned[vertex], []).append(vertex)
            partition = tuple(sorted(tuple(block) for block in blocks.values()))
            profiles[(signature, partition)] += 1
            return

        remaining = graph.vertices - set(assigned)
        vertex = max(
            remaining,
            key=lambda item: (
                len({assigned[x] for x in adjacency[item] if x in assigned}),
                len(adjacency[item]),
                item,
            ),
        )
        unavailable = {
            assigned[x] for x in adjacency[vertex] if x in assigned
        }
        for colour in range(6):
            if colour in unavailable:
                continue
            assigned[vertex] = colour
            search()
            del assigned[vertex]

    search()
    return profiles


def has_system_of_distinct_representatives(
    supports: dict[int, set[str]],
) -> bool:
    colours = sorted(supports, key=lambda c: len(supports[c]))

    def search(index: int, used: set[str]) -> bool:
        if index == len(colours):
            return True
        return any(
            search(index + 1, used | {label})
            for label in supports[colours[index]] - used
        )

    return search(0, set())


def main() -> None:
    graph, common_deletion, first, second, _ = build_adjacent_example()

    boundary = {"pA", "pB", "p1", "p2", "p3", "c2", "c3"}
    graph.add_vertex("ell")
    common_deletion.add_vertex("ell")
    for vertex in boundary:
        graph.add_edge("ell", vertex)
        common_deletion.add_edge("ell", vertex)
    first["ell"] = 5
    second["ell"] = 5

    bags = {
        "R": {"v"},
        "U": {"a", "b", "pA", "pB"},
        "C1": {"c1", "c2", "ell"},
        "C2": {"c3", "c4"},
        "Y1": {"p1", "r1"},
        "Y2": {"p2", "r2"},
        "Y3": {"p3", "r3"},
    }
    distinct_label_bags = {
        "R": {"v"},
        "A": {"a", "pA"},
        "B": {"b", "pB"},
        "C": {"c1", "c2", "c3", "c4", "ell"},
        "Y1": {"p1", "r1"},
        "Y2": {"p2", "r2"},
        "Y3": {"p3", "r3"},
    }

    verify_kappa_seven(graph, boundary)
    require(graph.neighbours("ell") == boundary, "wrong new neighbourhood")
    old_side = graph.vertices - boundary - {"ell"}
    require(graph.connected(old_side), "opposite open shore is disconnected")
    for vertex in boundary:
        require(
            bool(graph.neighbours(vertex) & old_side),
            f"opposite shore misses boundary vertex {vertex}",
        )

    expected_missing = {frozenset(("Y1", "Y2"))}
    require(model_missing_pairs(graph, bags) == expected_missing, "wrong model")
    require(
        model_missing_pairs(common_deletion, bags) == expected_missing,
        "the common deletion does not preserve the model",
    )
    require(
        model_missing_pairs(graph, distinct_label_bags) == expected_missing,
        "wrong distinct-label model",
    )
    require(
        model_missing_pairs(common_deletion, distinct_label_bags)
        == expected_missing,
        "the common deletion does not preserve the distinct-label model",
    )

    clique = {"v", "a", "b", "c1", "c2", "c3", "c4"}
    verify_clique(graph, clique)
    seven_colouring = dict(first)
    seven_colouring["v"] = 6
    require(proper_colouring(graph, seven_colouring), "bad seven-colouring")

    require(
        proper_colouring(common_deletion, first)
        and proper_colouring(common_deletion, second),
        "bad common-deletion response",
    )
    six_core = {"a", "b", "c1", "c2", "c3", "c4"}
    verify_clique(common_deletion, six_core)
    require(
        not common_deletion.has_edge("v", "a")
        and not common_deletion.has_edge("v", "b"),
        "selected edges survive in the common deletion",
    )
    require(
        all(common_deletion.has_edge("v", x) for x in {"c1", "c2", "c3", "c4"}),
        "the shared portal misses a fixed-clique vertex",
    )
    alpha_beta_vertices = {
        vertex for vertex in common_deletion.vertices if first[vertex] in {0, 2}
    }
    require(
        not any(
            common_deletion.has_edge("v", other)
            for other in alpha_beta_vertices - {"v"}
        ),
        "the response-changing Kempe component is not the singleton portal",
    )
    switched = dict(first)
    switched["v"] = 2
    require(switched == second, "the singleton interchange does not give PE")
    boundary_partition = (
        ("c2",),
        ("c3",),
        ("p1", "p2", "p3", "pA", "pB"),
    )
    require(
        normalized_common_deletion_profiles(common_deletion, boundary)
        == Counter({("EP", boundary_partition): 3, ("PE", boundary_partition): 3}),
        "unexpected common-deletion signature or boundary language",
    )
    edge_responses = {
        ("v", "a"): first,
        ("v", "b"): second,
    }
    for (x, y), colouring in edge_responses.items():
        deletion = graph.copy()
        deletion.remove_edge(x, y)
        require(proper_colouring(deletion, colouring), f"bad response for {x}{y}")
        six_clique = (clique - {y}) if x == "v" else (clique - {x})
        verify_clique(deletion, six_clique)
        require(colouring[x] == colouring[y], "response does not contract")
        quotient, qcolouring, image = contract_edge(graph, x, y, colouring)
        require(proper_colouring(quotient, qcolouring), f"bad contraction {x}{y}")
        verify_clique(quotient, {image} | (clique - {x, y}))

    require(
        {first[v] for v in boundary} == {1, 3, 4},
        "unexpected first boundary trace",
    )
    require(
        {second[v] for v in boundary} == {1, 3, 4},
        "unexpected second boundary trace",
    )
    require(
        all(first[v] == second[v] for v in boundary),
        "the two edge responses do not share the labelled boundary trace",
    )
    require(
        all(first[v] != first["ell"] for v in boundary),
        "the selected trace does not extend through the singleton shore",
    )

    supports = support_by_colour(graph, "v", first, bags)
    require(supports[3] == {"C1"}, "wrong colour-3 support")
    require(supports[4] == {"C2"}, "wrong colour-4 support")
    require(supports[5] == {"C2"}, "wrong colour-5 support")
    require(
        not has_system_of_distinct_representatives(supports),
        "unexpected first-hit label allocation",
    )
    distinct_supports = support_by_colour(
        graph, "v", first, distinct_label_bags
    )
    require(
        all(distinct_supports[colour] == {"C"} for colour in (3, 4, 5)),
        "wrong distinct-label first-hit supports",
    )
    require(
        not has_system_of_distinct_representatives(distinct_supports),
        "unexpected distinct-label first-hit allocation",
    )

    # A further proper-minor response exists inside the repeated first-hit
    # bag C2 and retains the selected boundary trace exactly.
    third = {
        "a": 2,
        "b": 0,
        "c1": 1,
        "c2": 3,
        "c3": 4,
        "c4": 4,
        "ell": 0,
        "p1": 1,
        "p2": 1,
        "p3": 1,
        "pA": 1,
        "pB": 1,
        "r1": 2,
        "r2": 0,
        "r3": 2,
        "v": 5,
    }
    internal_deletion = graph.copy()
    internal_deletion.remove_edge("c3", "c4")
    require(
        proper_colouring(internal_deletion, third),
        "bad internal collision-bag response",
    )
    require(
        all(third[v] == first[v] for v in boundary),
        "internal response does not retain the selected trace",
    )
    quotient, qcolouring, image = contract_edge(
        graph, "c3", "c4", third
    )
    require(proper_colouring(quotient, qcolouring), "bad internal contraction")
    verify_clique(quotient, {image} | (clique - {"c3", "c4"}))

    root_response = {
        "a": 5,
        "b": 2,
        "c1": 1,
        "c2": 3,
        "c3": 4,
        "c4": 0,
        "ell": 0,
        "p1": 1,
        "p2": 1,
        "p3": 1,
        "pA": 1,
        "pB": 1,
        "r1": 5,
        "r2": 2,
        "r3": 5,
    }
    root_deletion = graph.copy()
    root_deletion.vertices.remove("v")
    root_deletion.edges = {
        edge for edge in root_deletion.edges if "v" not in edge
    }
    require(
        proper_colouring(root_deletion, root_response),
        "bad repeated-source vertex-deletion response",
    )
    require(
        all(root_response[v] == first[v] for v in boundary),
        "root-deletion response does not retain the selected trace",
    )
    verify_clique(root_deletion, clique - {"v"})

    # Deleting ell leaves the original seven-chromatic graph, so the host
    # is deliberately not minor-minimal.
    old_graph = graph.copy()
    old_graph.vertices.remove("ell")
    old_graph.edges = {edge for edge in old_graph.edges if "ell" not in edge}
    verify_clique(old_graph, clique)

    print(
        "GREEN shared-portal exact-seven two-edge barrier: "
        "kappa=7, chi=7, same/distinct outer labels, shared trace, "
        "internal/root responses, Hall failure, explicit K7"
    )


if __name__ == "__main__":
    main()
