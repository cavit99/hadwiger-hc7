#!/usr/bin/env python3
"""Exact finite search for a complete-routing degree-eight dirty core.

Part I starts from the retained ten-vertex dirty slice.  It adds the minimum
one D-coloured vertex needed to route b to d without forcing the literal bd
root edge, then exhausts all 64 B--D edge patterns.  This isolates one first
missing route; it is not itself a complete-routing search.

Part II is the complete-routing search.  It exhausts the 64 graphs having
two vertices in each of five fixed colour classes, root graph 2K2+K1 with
edges ab and cd, and the unique minimum three-edge bichromatic route for
each nonliteral root pair.  For every graph it checks all ten routes, the
two vertex-disjoint shortest paths for ae and bc, every rooted-bag
allocation, exact dirty two-defect certificates, chromatic number, whether
the five roots are colourful in every proper five-colouring, and the
colouring and rooted-K4 gates after deletion of each fixed colour class.
For each root x it also exhausts the rooted-K4 models in H_x=X-A_x and
maximizes the number of their four branch sets meeting N_X(x) in H_x.

The exact output counts are asserted in the code.  In particular, all 64
complete-routing graphs contain the same explicit rooted K5 model, including
the 9 graphs which have both a dirty certificate and the stronger colouring
gates.  Thus neither finite family contains a counterexample.

Run with:

    .venv/bin/python active/hc7_degree8_complete_routing_dirty_core_search.py

This is finite evidence only.  It does not prove an unbounded property-(*)
statement, and it does not test K7-minor exclusion or contraction-criticality.
"""

from collections import Counter
from itertools import combinations, product


COLOUR_NAMES = "ABCDE"
ROOT_NAMES = "abcde"
ROOT_PAIRS = tuple(combinations(range(5), 2))
LITERAL_PAIRS = {(0, 1), (2, 3)}
OMITTED_MATCHING = {(0, 4), (1, 2)}


def edge(v: str, w: str) -> tuple[str, str]:
    assert v != w
    return tuple(sorted((v, w)))


def adjacent(edges: set[tuple[str, str]], v: str, w: str) -> bool:
    return v != w and edge(v, w) in edges


def connected(
    vertices: set[str], edges: set[tuple[str, str]]
) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            v
            for v in vertices - reached
            if any(adjacent(edges, v, w) for w in reached)
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def roots_connected_in_two_colours(
    edges: set[tuple[str, str]],
    colours: dict[str, int],
    root_a: str,
    root_b: str,
) -> bool:
    allowed_colours = {colours[root_a], colours[root_b]}
    allowed = {v for v, colour in colours.items() if colour in allowed_colours}
    reached = {root_a}
    while True:
        enlarged = reached | {
            v
            for v in allowed - reached
            if any(adjacent(edges, v, w) for w in reached)
        }
        if enlarged == reached:
            return root_b in reached
        reached = enlarged


def rooted_minimum_missing(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
) -> tuple[int, tuple[int, ...] | None]:
    free = tuple(sorted(vertices - set(roots)))
    minimum = len(ROOT_PAIRS)
    witness = None
    for assignment in product(range(len(roots) + 1), repeat=len(free)):
        bags = {root: {root} for root in roots}
        for vertex, target in zip(free, assignment):
            if target < len(roots):
                bags[roots[target]].add(vertex)
        if not all(connected(bag, edges) for bag in bags.values()):
            continue
        missing = sum(
            not any(
                adjacent(edges, x, y)
                for x in bags[roots[i]]
                for y in bags[roots[j]]
            )
            for i, j in combinations(range(len(roots)), 2)
        )
        if missing < minimum:
            minimum = missing
            witness = assignment
            if minimum == 0:
                break
    return minimum, witness


def proper_k_colouring_exists(
    vertices: set[str],
    edges: set[tuple[str, str]],
    k: int,
    roots: tuple[str, ...] = (),
    require_root_collision: bool = False,
) -> bool:
    order = sorted(
        vertices,
        key=lambda v: (-sum(adjacent(edges, v, w) for w in vertices), v),
    )
    assigned: dict[str, int] = {}

    def search(position: int) -> bool:
        if position == len(order):
            root_colours = {assigned[root] for root in roots}
            return not require_root_collision or len(root_colours) < len(roots)
        vertex = order[position]
        forbidden = {
            assigned[w]
            for w in assigned
            if adjacent(edges, vertex, w)
        }
        for colour in range(k):
            if colour in forbidden:
                continue
            assigned[vertex] = colour
            if search(position + 1):
                return True
            del assigned[vertex]
        return False

    return search(0)


def chromatic_number(
    vertices: set[str], edges: set[tuple[str, str]]
) -> int:
    for k in range(1, 6):
        if proper_k_colouring_exists(vertices, edges, k):
            return k
    raise AssertionError("the displayed proper five-colouring must work")


def rooted_complete_model_exists(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
) -> bool:
    free = tuple(sorted(vertices - set(roots)))
    for assignment in product(range(len(roots) + 1), repeat=len(free)):
        bags = {root: {root} for root in roots}
        for vertex, target in zip(free, assignment):
            if target < len(roots):
                bags[roots[target]].add(vertex)
        if not all(connected(bag, edges) for bag in bags.values()):
            continue
        if all(
            any(
                adjacent(edges, x, y)
                for x in bags[root_a]
                for y in bags[root_b]
            )
            for root_a, root_b in combinations(roots, 2)
        ):
            return True
    return False


def rooted_complete_model_maximum_contact(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    contact_vertices: set[str],
) -> int:
    """Maximize the number of rooted branch sets meeting contact_vertices."""
    free = tuple(sorted(vertices - set(roots)))
    maximum = -1
    for assignment in product(range(len(roots) + 1), repeat=len(free)):
        bags = {root: {root} for root in roots}
        for vertex, target in zip(free, assignment):
            if target < len(roots):
                bags[roots[target]].add(vertex)
        if not all(connected(bag, edges) for bag in bags.values()):
            continue
        if not all(
            any(
                adjacent(edges, x, y)
                for x in bags[root_a]
                for y in bags[root_b]
            )
            for root_a, root_b in combinations(roots, 2)
        ):
            continue
        maximum = max(
            maximum,
            sum(bool(bag & contact_vertices) for bag in bags.values()),
        )
        if maximum == len(roots):
            return maximum
    return maximum


def retained_slice() -> tuple[
    set[str], set[tuple[str, str]], tuple[str, ...], dict[str, int]
]:
    roots = tuple(ROOT_NAMES)
    vertices = set(roots) | {"x", "y", "r", "s", "t"}
    edges = {
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
    colours = {
        "a": 0,
        "x": 0,
        "b": 1,
        "s": 1,
        "t": 1,
        "c": 2,
        "r": 2,
        "d": 3,
        "e": 4,
        "y": 4,
    }
    assert all(colours[v] != colours[w] for v, w in edges)
    return vertices, edges, roots, colours


def assert_retained_dirty_certificate(
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    colours: dict[str, int],
) -> None:
    bags = {
        0: {"a", "t"},
        1: {"b"},
        2: {"c"},
        3: {"d", "x", "y"},
        4: {"e", "r", "s"},
    }
    assert all(roots[index] in bag for index, bag in bags.items())
    assert all(connected(bag, edges) for bag in bags.values())
    missing = {
        (i, j)
        for i, j in ROOT_PAIRS
        if not any(adjacent(edges, v, w) for v in bags[i] for w in bags[j])
    }
    assert missing == OMITTED_MATCHING

    owner = {v: index for index, bag in bags.items() for v in bag}
    paths = {
        (0, 4): ("e", "x", "y", "a"),
        (1, 2): ("b", "r", "s", "c"),
    }
    assert set(paths[(0, 4)]).isdisjoint(paths[(1, 2)])
    for missing_pair, path in paths.items():
        assert all(adjacent(edges, v, w) for v, w in zip(path, path[1:]))
        assert {colours[v] for v in path} == set(missing_pair)
        assert path_distance(edges, colours, path[0], path[-1]) == 3
        trace = []
        for vertex in path:
            if not trace or trace[-1] != owner[vertex]:
                trace.append(owner[vertex])
        assert not any(
            {left, right} == set(missing_pair)
            for left, right in zip(trace, trace[1:])
        )


def minimum_additive_bd_route_search() -> tuple[
    Counter[int], Counter[int], Counter[int]
]:
    vertices, base_edges, roots, colours = retained_slice()
    assert_retained_dirty_certificate(base_edges, roots, colours)
    assert rooted_minimum_missing(vertices, base_edges, roots)[0] == 2

    # With no new D-coloured vertex, the B--D route forces the literal edge
    # bd.  That single edge already gives a rooted model with one defect.
    assert rooted_minimum_missing(
        vertices, base_edges | {edge("b", "d")}, roots
    )[0] == 1

    vertices = vertices | {"z"}
    colours = colours | {"z": 3}
    b_class = {"b", "s", "t"}
    d_class = {"d", "z"}
    possible_edges = tuple(sorted(edge(v, w) for v in b_class for w in d_class))

    routed_histogram: Counter[int] = Counter()
    exact_root_graph_histogram: Counter[int] = Counter()
    minimum_edge_histogram: Counter[int] = Counter()
    routed_patterns = 0
    for mask in range(1 << len(possible_edges)):
        added = {
            possible_edges[index]
            for index in range(len(possible_edges))
            if mask & (1 << index)
        }
        edges = base_edges | added
        if not roots_connected_in_two_colours(edges, colours, "b", "d"):
            continue
        routed_patterns += 1
        minimum, _ = rooted_minimum_missing(vertices, edges, roots)
        routed_histogram[minimum] += 1
        if edge("b", "d") not in added:
            exact_root_graph_histogram[minimum] += 1
            if len(added) == 3:
                minimum_edge_histogram[minimum] += 1

    assert routed_patterns == 39
    assert routed_histogram == Counter({1: 21, 0: 18})
    assert exact_root_graph_histogram == Counter({1: 7})
    assert minimum_edge_histogram == Counter({1: 2})
    return routed_histogram, exact_root_graph_histogram, minimum_edge_histogram


def balanced_complete_routing_graph(
    optional_mask: int,
) -> tuple[
    set[str], set[tuple[str, str]], tuple[str, ...], tuple[str, ...], dict[str, int]
]:
    roots = tuple(f"r{name}" for name in ROOT_NAMES)
    mates = tuple(f"m{name}" for name in ROOT_NAMES)
    vertices = set(roots) | set(mates)
    colours = {
        vertex: colour
        for colour in range(5)
        for vertex in (roots[colour], mates[colour])
    }
    edges: set[tuple[str, str]] = set()
    optional_edges = []
    for i, j in ROOT_PAIRS:
        if (i, j) in LITERAL_PAIRS:
            edges.add(edge(roots[i], roots[j]))
            optional_edges.extend(
                (
                    edge(roots[i], mates[j]),
                    edge(mates[i], roots[j]),
                    edge(mates[i], mates[j]),
                )
            )
        else:
            # With two vertices per colour and no root edge, these are the
            # unique three edges which connect the two roots bichromatically.
            edges.update(
                (
                    edge(roots[i], mates[j]),
                    edge(mates[j], mates[i]),
                    edge(mates[i], roots[j]),
                )
            )
    edges.update(
        optional_edges[index]
        for index in range(len(optional_edges))
        if optional_mask & (1 << index)
    )
    assert len(optional_edges) == 6
    assert all(colours[v] != colours[w] for v, w in edges)
    return vertices, edges, roots, mates, colours


def path_distance(
    edges: set[tuple[str, str]],
    colours: dict[str, int],
    start: str,
    end: str,
) -> int | None:
    allowed_colours = {colours[start], colours[end]}
    allowed = {v for v, colour in colours.items() if colour in allowed_colours}
    frontier = {start}
    seen = set(frontier)
    distance = 0
    while frontier:
        if end in frontier:
            return distance
        frontier = {
            v
            for v in allowed - seen
            if any(adjacent(edges, v, w) for w in frontier)
        }
        seen.update(frontier)
        distance += 1
    return None


def dirty_two_defect_certificate_exists(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    mates: tuple[str, ...],
) -> bool:
    paths = {
        (0, 4): (roots[4], mates[0], mates[4], roots[0]),
        (1, 2): (roots[1], mates[2], mates[1], roots[2]),
    }
    free = tuple(sorted(vertices - set(roots)))
    for assignment in product(range(6), repeat=len(free)):
        bags = {index: {roots[index]} for index in range(5)}
        owner = {roots[index]: index for index in range(5)}
        for vertex, target in zip(free, assignment):
            if target < 5:
                bags[target].add(vertex)
                owner[vertex] = target
        if not all(connected(bag, edges) for bag in bags.values()):
            continue
        missing = {
            (i, j)
            for i, j in ROOT_PAIRS
            if not any(
                adjacent(edges, x, y)
                for x in bags[i]
                for y in bags[j]
            )
        }
        if missing != OMITTED_MATCHING:
            continue
        both_dirty = True
        for missing_pair, path in paths.items():
            trace = []
            for vertex in path:
                if vertex not in owner:
                    continue
                if not trace or trace[-1] != owner[vertex]:
                    trace.append(owner[vertex])
            if any(
                {left, right} == set(missing_pair)
                for left, right in zip(trace, trace[1:])
            ):
                both_dirty = False
                break
        if both_dirty:
            return True
    return False


def balanced_universal_rooted_k5_model(
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    mates: tuple[str, ...],
) -> bool:
    bags = {
        0: {roots[0], mates[0], mates[2], mates[3]},
        1: {roots[1], mates[4]},
        2: {roots[2]},
        3: {roots[3]},
        4: {roots[4], mates[1]},
    }
    return all(connected(bag, edges) for bag in bags.values()) and all(
        any(adjacent(edges, v, w) for v in bags[i] for w in bags[j])
        for i, j in ROOT_PAIRS
    )


def fixed_colour_deletion_gates(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    colours: dict[str, int],
) -> tuple[bool, bool]:
    colouring_gate = True
    rooted_k4_gate = True
    for omitted_colour in range(5):
        residual = {
            v for v in vertices if colours[v] != omitted_colour
        }
        residual_roots = tuple(
            roots[index] for index in range(5) if index != omitted_colour
        )
        colouring_gate &= chromatic_number(residual, edges) == 4
        colouring_gate &= not proper_k_colouring_exists(
            residual,
            edges,
            4,
            roots=residual_roots,
            require_root_collision=True,
        )
        rooted_k4_gate &= rooted_complete_model_exists(
            residual, edges, residual_roots
        )
    return colouring_gate, rooted_k4_gate


def fixed_colour_deletion_contact_profile(
    vertices: set[str],
    edges: set[tuple[str, str]],
    roots: tuple[str, ...],
    colours: dict[str, int],
) -> tuple[int, ...]:
    """For each x, maximize residual K4 bags meeting N(x) in X-A_x."""
    profile = []
    for omitted_colour in range(5):
        residual = {
            vertex
            for vertex in vertices
            if colours[vertex] != omitted_colour
        }
        residual_roots = tuple(
            roots[index] for index in range(5) if index != omitted_colour
        )
        deleted_root = roots[omitted_colour]
        residual_neighbourhood = {
            vertex
            for vertex in residual
            if adjacent(edges, deleted_root, vertex)
        }
        maximum = rooted_complete_model_maximum_contact(
            residual,
            edges,
            residual_roots,
            residual_neighbourhood,
        )
        assert maximum >= 0
        profile.append(maximum)
    return tuple(profile)


def summarize_contact_profiles(
    profiles: list[tuple[int, ...]],
) -> dict[str, object]:
    maxima = [max(profile) for profile in profiles]
    individual_contacts = Counter(
        contact for profile in profiles for contact in profile
    )
    return {
        "graphs": len(profiles),
        "minimum_max_over_deleted_roots": min(maxima),
        "some_deleted_root_contact_4": sum(maximum == 4 for maximum in maxima),
        "some_deleted_root_contact_at_least_3": sum(
            maximum >= 3 for maximum in maxima
        ),
        "all_deleted_roots_contact_at_most_2": sum(
            maximum <= 2 for maximum in maxima
        ),
        "all_five_deleted_roots_contact_4": sum(
            all(contact == 4 for contact in profile) for profile in profiles
        ),
        "max_over_deleted_roots_histogram": dict(sorted(Counter(maxima).items())),
        "individual_deleted_root_contact_histogram": dict(
            sorted(individual_contacts.items())
        ),
    }


def balanced_complete_routing_atlas() -> tuple[
    dict[str, int], dict[str, dict[str, object]]
]:
    chromatic_histogram: Counter[int] = Counter()
    complete_models = 0
    dirty_certificates = 0
    colourful_cores = 0
    dirty_colourful_cores = 0
    colourful_deletion_colouring_gate = 0
    colourful_deletion_rooted_k4_gate = 0
    universal_model_checks = 0
    all_contact_profiles = []
    colourful_contact_profiles = []
    dirty_colourful_contact_profiles = []

    for optional_mask in range(64):
        vertices, edges, roots, mates, colours = balanced_complete_routing_graph(
            optional_mask
        )
        assert all(
            roots_connected_in_two_colours(edges, colours, roots[i], roots[j])
            for i, j in ROOT_PAIRS
        )
        path_ea = (roots[4], mates[0], mates[4], roots[0])
        path_bc = (roots[1], mates[2], mates[1], roots[2])
        assert set(path_ea).isdisjoint(path_bc)
        assert path_distance(edges, colours, path_ea[0], path_ea[-1]) == 3
        assert path_distance(edges, colours, path_bc[0], path_bc[-1]) == 3
        universal_model_checks += balanced_universal_rooted_k5_model(
            edges, roots, mates
        )

        minimum, _ = rooted_minimum_missing(vertices, edges, roots)
        if minimum == 0:
            complete_models += 1

        dirty = dirty_two_defect_certificate_exists(
            vertices, edges, roots, mates
        )
        dirty_certificates += dirty

        chi = chromatic_number(vertices, edges)
        chromatic_histogram[chi] += 1
        colourful = chi == 5 and not proper_k_colouring_exists(
            vertices,
            edges,
            5,
            roots=roots,
            require_root_collision=True,
        )
        colourful_cores += colourful
        dirty_colourful_cores += dirty and colourful
        deletion_colouring_gate, deletion_rooted_k4_gate = (
            fixed_colour_deletion_gates(vertices, edges, roots, colours)
        )
        colourful_deletion_colouring_gate += (
            colourful and deletion_colouring_gate
        )
        colourful_deletion_rooted_k4_gate += (
            colourful and deletion_rooted_k4_gate
        )
        contact_profile = fixed_colour_deletion_contact_profile(
            vertices, edges, roots, colours
        )
        all_contact_profiles.append(contact_profile)
        if colourful:
            colourful_contact_profiles.append(contact_profile)
        if dirty and colourful:
            dirty_colourful_contact_profiles.append(contact_profile)

    assert chromatic_histogram == Counter({5: 55, 4: 9})
    assert complete_models == 64
    assert dirty_certificates == 16
    assert colourful_cores == 24
    assert dirty_colourful_cores == 9
    assert colourful_deletion_colouring_gate == 24
    assert colourful_deletion_rooted_k4_gate == 24
    assert universal_model_checks == 64
    atlas = {
        "graphs": 64,
        "rooted_k5": complete_models,
        "same_explicit_rooted_k5_model": universal_model_checks,
        "dirty_two_defect_certificates": dirty_certificates,
        "five_chromatic": chromatic_histogram[5],
        "five_chromatic_and_U_colourful": colourful_cores,
        "dirty_and_colourful": dirty_colourful_cores,
        "colourful_passing_all_five_deletion_colourful_gates": (
            colourful_deletion_colouring_gate
        ),
        "colourful_passing_all_five_deletion_rooted_K4_gates": (
            colourful_deletion_rooted_k4_gate
        ),
        "counterexamples_to_complete_routing_assertion": 0,
    }
    contact_summaries = {
        "all_64": summarize_contact_profiles(all_contact_profiles),
        "colourful_24": summarize_contact_profiles(colourful_contact_profiles),
        "dirty_colourful_9": summarize_contact_profiles(
            dirty_colourful_contact_profiles
        ),
    }
    assert contact_summaries == {
        "all_64": {
            "graphs": 64,
            "minimum_max_over_deleted_roots": 4,
            "some_deleted_root_contact_4": 64,
            "some_deleted_root_contact_at_least_3": 64,
            "all_deleted_roots_contact_at_most_2": 0,
            "all_five_deleted_roots_contact_4": 64,
            "max_over_deleted_roots_histogram": {4: 64},
            "individual_deleted_root_contact_histogram": {4: 320},
        },
        "colourful_24": {
            "graphs": 24,
            "minimum_max_over_deleted_roots": 4,
            "some_deleted_root_contact_4": 24,
            "some_deleted_root_contact_at_least_3": 24,
            "all_deleted_roots_contact_at_most_2": 0,
            "all_five_deleted_roots_contact_4": 24,
            "max_over_deleted_roots_histogram": {4: 24},
            "individual_deleted_root_contact_histogram": {4: 120},
        },
        "dirty_colourful_9": {
            "graphs": 9,
            "minimum_max_over_deleted_roots": 4,
            "some_deleted_root_contact_4": 9,
            "some_deleted_root_contact_at_least_3": 9,
            "all_deleted_roots_contact_at_most_2": 0,
            "all_five_deleted_roots_contact_4": 9,
            "max_over_deleted_roots_histogram": {4: 9},
            "individual_deleted_root_contact_histogram": {4: 45},
        },
    }
    return atlas, contact_summaries


def main() -> None:
    additive_histogram, exact_root_histogram, minimum_edge_histogram = (
        minimum_additive_bd_route_search()
    )
    atlas, contact_summaries = balanced_complete_routing_atlas()
    print("GREEN: targeted complete-routing dirty-core search verified")
    print("minimum_additive_BD_routed_patterns=39")
    print(
        "minimum_additive_minimum_missing_histogram",
        dict(sorted(additive_histogram.items())),
    )
    print("minimum_additive_exact_root_graph_patterns=7")
    print(
        "minimum_additive_exact_root_graph_histogram",
        dict(sorted(exact_root_histogram.items())),
    )
    print("minimum_additive_exact_root_graph_minimum_edge_patterns=2")
    print(
        "minimum_additive_exact_root_graph_minimum_edge_histogram",
        dict(sorted(minimum_edge_histogram.items())),
    )
    print("minimum_additive_BD_route_counterexamples=0")
    print("minimum_additive_scope=one_BD_route_only; not complete routing")
    print("balanced_complete_routing_atlas", atlas)
    for family, summary in contact_summaries.items():
        print(f"balanced_deletion_contact_{family}", summary)
    print("balanced_chromatic_histogram={4: 9, 5: 55}")
    print("balanced_scope=exact two-vertices-per-colour complete-routing atlas")
    print("result=no counterexample in either exact finite search")
    print("omitted_gates=K7-minor exclusion; contraction-criticality")
    print("scope=finite; not a property-(*) theorem or full-host proof")


if __name__ == "__main__":
    main()
