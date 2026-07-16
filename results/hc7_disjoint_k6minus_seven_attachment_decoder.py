#!/usr/bin/env python3
"""Exact endpoint-attachment decoder for the canonical 3+1 quotient.

The script proves a finite statement only.  It does not infer that arbitrary
attachments in the interiors of the six linkage paths can be replaced by
endpoint attachments.
"""

from __future__ import annotations

import functools
import hashlib
import itertools
import json


A0, A1, A2, A3, X, Y = range(6)
B0, B1, B2, R, P, Q = range(6, 12)
C = 12

NAMES = (
    "a0", "a1", "a2", "a3", "x", "y",
    "b0", "b1", "b2", "r", "p", "q", "c",
)

MATCHING = (
    (A0, B0),
    (A1, B1),
    (A2, B2),
    (A3, P),
    (X, Q),
    (Y, R),
)

BASE_EDGES = frozenset(
    tuple(sorted(pair))
    for pair in
    {
        *map(tuple, itertools.combinations((A0, A1, A2, A3), 2)),
        (X, Y),
        (X, A0),
        (X, A1),
        (X, A2),
        (Y, A3),
        *(
            edge
            for edge in itertools.combinations((B0, B1, B2, R, P, Q), 2)
            if edge != (P, Q)
        ),
        *MATCHING,
    }
)

FIXED_CONTACTS = frozenset((A3, X))
OTHER_ENDPOINTS = tuple(vertex for vertex in range(12) if vertex not in FIXED_CONTACTS)

EXPECTED_SIX_ATTACHMENT_NEGATIVES = {
    frozenset((A3, X, A0, A1, A2, Y)),
    frozenset((A3, X, A0, A1, B0, B1)),
    frozenset((A3, X, A0, A2, B0, B2)),
    frozenset((A3, X, A1, A2, B1, B2)),
    frozenset((A3, X, Y, R, B0, B1)),
    frozenset((A3, X, Y, R, B0, B2)),
    frozenset((A3, X, Y, R, B1, B2)),
}

# Filled from the deterministic canonical certificate catalogue below.  It
# makes accidental changes to either the quotient or the search visible.
EXPECTED_SEVEN_ATTACHMENT_CERTIFICATE_DIGEST = (
    "2b2b5f5b30bed58f598a3f491ec434682d3845951235cf0d710ddffd1ad368cb"
)

EndpointSite = tuple[str, int]


def endpoint_site(vertex: int) -> EndpointSite:
    return ("e", vertex)


def midpoint_site(rail: int) -> EndpointSite:
    return ("m", rail)


EXPECTED_MIXED_NEGATIVES: set[frozenset[EndpointSite]] = set()
for first, second in itertools.combinations(range(3), 2):
    for distinguished in (first, second):
        EXPECTED_MIXED_NEGATIVES.add(
            frozenset(
                (
                    endpoint_site(first),
                    endpoint_site(second),
                    endpoint_site(B0 + first),
                    endpoint_site(B0 + second),
                    midpoint_site(distinguished),
                )
            )
        )
        EXPECTED_MIXED_NEGATIVES.add(
            frozenset(
                (
                    endpoint_site(first),
                    endpoint_site(second),
                    endpoint_site(B0 + distinguished),
                    midpoint_site(first),
                    midpoint_site(second),
                )
            )
        )
        EXPECTED_MIXED_NEGATIVES.add(
            frozenset(
                (
                    endpoint_site(distinguished),
                    endpoint_site(B0 + first),
                    endpoint_site(B0 + second),
                    midpoint_site(first),
                    midpoint_site(second),
                )
            )
        )
    EXPECTED_MIXED_NEGATIVES.add(
        frozenset(
            (
                endpoint_site(Y),
                endpoint_site(R),
                endpoint_site(B0 + first),
                endpoint_site(B0 + second),
                midpoint_site(5),
            )
        )
    )

EXPECTED_MIXED_STATUS_DIGEST = (
    "24c1fc7e8b81591d71c7d0dc701f867d0682f8bad19a9a60161fbf1df96195d7"
)


def edge(left: int, right: int) -> tuple[int, int]:
    return tuple(sorted((left, right)))


def adjacency(order: int, edges: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    answer = [0] * order
    for left, right in edges:
        answer[left] |= 1 << right
        answer[right] |= 1 << left
    return tuple(answer)


def connected(mask: int, adj: tuple[int, ...]) -> bool:
    reached = mask & -mask
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            neighbours |= adj[bit.bit_length() - 1]
        reached |= neighbours & mask
        if reached == old:
            return reached == mask


def touches(left: int, right: int, adj: tuple[int, ...]) -> bool:
    while left:
        bit = left & -left
        left -= bit
        if adj[bit.bit_length() - 1] & right:
            return True
    return False


def find_k7_model(
    order: int, edges: frozenset[tuple[int, int]]
) -> tuple[int, ...] | None:
    """Exact connected-branch-set search for the order-thirteen quotients.

    If a seven-bag model uses ``s`` singleton bags, its other bags have at
    least two vertices.  Hence ``s >= 14-order``.  The outer loop tries every
    possible exact singleton clique, and the inner search tries every family
    of mutually adjacent, disjoint connected non-singleton bags.  Vertices
    unused by the model are allowed.
    """

    assert order <= 13
    vertices = tuple(range(order))
    adj = adjacency(order, edges)
    full = (1 << order) - 1

    @functools.lru_cache(maxsize=None)
    def is_connected(mask: int) -> bool:
        return connected(mask, adj)

    @functools.lru_cache(maxsize=None)
    def are_adjacent(left: int, right: int) -> bool:
        return touches(left, right, adj)

    minimum_singletons = max(0, 14 - order)
    for singleton_count in range(7, minimum_singletons - 1, -1):
        non_singleton_count = 7 - singleton_count
        for singletons in itertools.combinations(vertices, singleton_count):
            if any(
                not (adj[left] >> right & 1)
                for left, right in itertools.combinations(singletons, 2)
            ):
                continue

            singleton_masks = tuple(1 << vertex for vertex in singletons)
            singleton_union = sum(singleton_masks)
            remainder = full ^ singleton_union
            if non_singleton_count == 0:
                return singleton_masks

            maximum_size = remainder.bit_count() - 2 * (non_singleton_count - 1)
            candidates: list[int] = []
            subset = remainder
            while subset:
                if (
                    2 <= subset.bit_count() <= maximum_size
                    and is_connected(subset)
                    and all(are_adjacent(subset, singleton) for singleton in singleton_masks)
                ):
                    candidates.append(subset)
                subset = (subset - 1) & remainder
            candidates.sort(key=lambda mask: (mask.bit_count(), mask))

            def search(
                start: int, chosen: tuple[int, ...], used: int
            ) -> tuple[int, ...] | None:
                if len(chosen) == non_singleton_count:
                    return singleton_masks + chosen
                missing = non_singleton_count - len(chosen)
                if (remainder & ~used).bit_count() < 2 * missing:
                    return None
                for position in range(start, len(candidates)):
                    candidate = candidates[position]
                    if candidate & used:
                        continue
                    if not all(are_adjacent(candidate, old) for old in chosen):
                        continue
                    result = search(
                        position + 1, chosen + (candidate,), used | candidate
                    )
                    if result is not None:
                        return result
                return None

            result = search(0, (), 0)
            if result is not None:
                return result
    return None


def verify_model(
    order: int, edges: frozenset[tuple[int, int]], model: tuple[int, ...]
) -> None:
    adj = adjacency(order, edges)
    assert len(model) == 7
    assert all(model)
    assert all(not (left & right) for left, right in itertools.combinations(model, 2))
    assert all(connected(bag, adj) for bag in model)
    assert all(touches(left, right, adj) for left, right in itertools.combinations(model, 2))


def star_graph(contacts: frozenset[int]) -> frozenset[tuple[int, int]]:
    return BASE_EDGES | frozenset(edge(C, vertex) for vertex in contacts)


def named_model(model: tuple[int, ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(
        tuple(NAMES[vertex] for vertex in range(13) if bag >> vertex & 1)
        for bag in model
    )


def symmetry_maps() -> tuple[dict[int, int], ...]:
    maps = []
    for permutation in itertools.permutations(range(3)):
        mapping = {index: permutation[index] for index in range(3)}
        mapping.update({B0 + index: B0 + permutation[index] for index in range(3)})
        mapping.update({vertex: vertex for vertex in (A3, X, Y, R, P, Q)})
        maps.append(mapping)
    return tuple(maps)


def orbit_representative(contacts: frozenset[int]) -> tuple[int, ...]:
    return min(
        tuple(sorted(mapping[vertex] for vertex in contacts))
        for mapping in symmetry_maps()
    )


def contract_label(
    edges: frozenset[tuple[int, int]], removed: int, retained: int
) -> frozenset[tuple[int, int]]:
    answer = set()
    for left, right in edges:
        new_left = retained if left == removed else left
        new_right = retained if right == removed else right
        if new_left != new_right:
            answer.add(edge(new_left, new_right))
    return frozenset(answer)


def normalize_graph(
    vertices: frozenset[int] | set[int], edges: frozenset[tuple[int, int]] | set[tuple[int, int]]
) -> tuple[int, frozenset[tuple[int, int]]]:
    relabel = {vertex: index for index, vertex in enumerate(sorted(vertices))}
    normalized = frozenset(
        edge(relabel[left], relabel[right])
        for left, right in edges
        if left in relabel and right in relabel and left != right
    )
    return len(relabel), normalized


def delete_vertex(
    order: int, edges: frozenset[tuple[int, int]], vertex: int
) -> tuple[int, frozenset[tuple[int, int]]]:
    return normalize_graph(set(range(order)) - {vertex}, edges)


def contract_edge(
    order: int,
    edges: frozenset[tuple[int, int]],
    retained: int,
    removed: int,
) -> tuple[int, frozenset[tuple[int, int]]]:
    contracted = set()
    for left, right in edges:
        new_left = retained if left == removed else left
        new_right = retained if right == removed else right
        if new_left != new_right:
            contracted.add(edge(new_left, new_right))
    return normalize_graph(set(range(order)) - {removed}, contracted)


@functools.lru_cache(maxsize=None)
def has_k7_minor(
    order: int, edges: frozenset[tuple[int, int]]
) -> bool:
    """Exact detector above order thirteen by low-degree recursion."""

    if order <= 13:
        return find_k7_model(order, edges) is not None

    adj = adjacency(order, edges)
    vertex = min(range(order), key=lambda old: adj[old].bit_count())
    assert adj[vertex].bit_count() < 6

    if has_k7_minor(*delete_vertex(order, edges, vertex)):
        return True
    return any(
        has_k7_minor(*contract_edge(order, edges, vertex, neighbour))
        for neighbour in range(order)
        if adj[vertex] >> neighbour & 1
    )


def projection_forces_k7(sites: frozenset[EndpointSite]) -> bool:
    endpoint_contacts = [value for kind, value in sites if kind == "e"]
    midpoint_contacts = [value for kind, value in sites if kind == "m"]
    for choices in itertools.product((0, 1), repeat=len(midpoint_contacts)):
        contacts = set(FIXED_CONTACTS) | set(endpoint_contacts)
        contacts.update(
            MATCHING[rail][choice]
            for rail, choice in zip(midpoint_contacts, choices)
        )
        frozen = frozenset(contacts)
        if len(frozen) >= 7:
            return True
        if len(frozen) == 6 and frozen not in EXPECTED_SIX_ATTACHMENT_NEGATIVES:
            return True
    return False


def mixed_attachment_graph(
    sites: frozenset[EndpointSite],
) -> tuple[int, frozenset[tuple[int, int]]]:
    graph = set(BASE_EDGES)
    vertices = set(range(13))
    graph.update((edge(C, A3), edge(C, X)))
    for kind, value in sites:
        if kind == "e":
            graph.add(edge(C, value))
            continue
        midpoint = 13 + value
        left, right = MATCHING[value]
        vertices.add(midpoint)
        graph.remove(edge(left, right))
        graph.update((edge(left, midpoint), edge(midpoint, right), edge(C, midpoint)))
    return normalize_graph(vertices, graph)


def site_orbit_representative(sites: frozenset[EndpointSite]) -> tuple[EndpointSite, ...]:
    candidates = []
    for permutation in itertools.permutations(range(3)):
        image = []
        for kind, value in sites:
            if kind == "e" and value < 3:
                image.append((kind, permutation[value]))
            elif kind == "e" and B0 <= value <= B2:
                image.append((kind, B0 + permutation[value - B0]))
            elif kind == "m" and value < 3:
                image.append((kind, permutation[value]))
            else:
                image.append((kind, value))
        candidates.append(tuple(sorted(image)))
    return min(candidates)


def verify_mixed_endpoint_midpoint_catalogue() -> tuple[int, int, int, str]:
    sites = tuple(endpoint_site(vertex) for vertex in OTHER_ENDPOINTS) + tuple(
        midpoint_site(rail) for rail in range(6)
    )
    resistant = []
    actual_negative = set()
    status = []
    for selected_tuple in itertools.combinations(sites, 5):
        selected = frozenset(selected_tuple)
        if projection_forces_k7(selected):
            outcome = True
        else:
            resistant.append(selected)
            outcome = has_k7_minor(*mixed_attachment_graph(selected))
        if not outcome:
            actual_negative.add(selected)
        status.append((selected_tuple, outcome))

    assert actual_negative == EXPECTED_MIXED_NEGATIVES
    negative_orbits = {
        site_orbit_representative(selected) for selected in actual_negative
    }
    assert len(negative_orbits) == 4
    payload = json.dumps(status, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    assert digest == EXPECTED_MIXED_STATUS_DIGEST
    return len(resistant), len(actual_negative), len(negative_orbits), digest


def verify_interior_rail_projection() -> int:
    """Check all ways to retain five of six one-subdivision rail contacts."""

    chosen_endpoint = (A0, A1, A2, P, Q, Y)
    checks = 0
    for selected in itertools.combinations(range(6), 5):
        graph = set(BASE_EDGES)
        midpoints = {}
        for rail, (left, right) in enumerate(MATCHING):
            midpoint = 13 + rail
            midpoints[rail] = midpoint
            graph.remove(edge(left, right))
            graph.add(edge(left, midpoint))
            graph.add(edge(midpoint, right))
        graph.add(edge(C, A3))
        graph.add(edge(C, X))
        graph.update(edge(C, midpoints[rail]) for rail in selected)

        contracted = frozenset(graph)
        for rail in range(6):
            retained = chosen_endpoint[rail]
            contracted = contract_label(contracted, midpoints[rail], retained)

        contacts = FIXED_CONTACTS | frozenset(chosen_endpoint[rail] for rail in selected)
        assert contracted == star_graph(contacts)
        assert find_k7_model(13, contracted) is not None
        checks += 1
    return checks


def verify_two_vertex_distributions() -> int:
    """Check every distribution of each minimal contact over an edge cd.

    Status 1 assigns a contact only to c, status 2 only to d, and status 3
    to both.  Contracting cd must give exactly the corresponding star graph.
    """

    D = 13
    checks = 0
    for extra in itertools.combinations(OTHER_ENDPOINTS, 5):
        contacts = tuple(sorted(FIXED_CONTACTS | frozenset(extra)))
        for statuses in itertools.product((1, 2, 3), repeat=7):
            graph = set(BASE_EDGES)
            graph.add(edge(C, D))
            for vertex, status in zip(contacts, statuses):
                if status & 1:
                    graph.add(edge(C, vertex))
                if status & 2:
                    graph.add(edge(D, vertex))
            contracted = contract_label(frozenset(graph), D, C)
            assert contracted == star_graph(frozenset(contacts))
            checks += 1
    return checks


def main() -> None:
    certificates = {}
    for extra in itertools.combinations(OTHER_ENDPOINTS, 5):
        contacts = FIXED_CONTACTS | frozenset(extra)
        graph = star_graph(contacts)
        model = find_k7_model(13, graph)
        assert model is not None
        verify_model(13, graph, model)
        certificates[tuple(NAMES[vertex] for vertex in sorted(contacts))] = named_model(model)

    payload = json.dumps(sorted(certificates.items()), separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    assert digest == EXPECTED_SEVEN_ATTACHMENT_CERTIFICATE_DIGEST

    six_attachment_negatives = set()
    six_attachment_positives = 0
    for extra in itertools.combinations(OTHER_ENDPOINTS, 4):
        contacts = FIXED_CONTACTS | frozenset(extra)
        model = find_k7_model(13, star_graph(contacts))
        if model is None:
            six_attachment_negatives.add(contacts)
        else:
            verify_model(13, star_graph(contacts), model)
            six_attachment_positives += 1
    assert six_attachment_negatives == EXPECTED_SIX_ATTACHMENT_NEGATIVES

    seven_orbits = {
        orbit_representative(FIXED_CONTACTS | frozenset(extra))
        for extra in itertools.combinations(OTHER_ENDPOINTS, 5)
    }
    negative_orbits = {
        orbit_representative(contacts) for contacts in six_attachment_negatives
    }
    assert len(seven_orbits) == 72
    assert len(negative_orbits) == 3

    interior_checks = verify_interior_rail_projection()
    mixed_resistant, mixed_negative, mixed_orbits, mixed_digest = (
        verify_mixed_endpoint_midpoint_catalogue()
    )
    distribution_checks = verify_two_vertex_distributions()

    print("minimal_seven_attachment_sets", len(certificates))
    print("minimal_seven_attachment_orbits", len(seven_orbits))
    print("certificate_digest", digest)
    print("six_attachment_positive_sets", six_attachment_positives)
    print("six_attachment_negative_sets", len(six_attachment_negatives))
    print("six_attachment_negative_orbits", len(negative_orbits))
    print("five_of_six_interior_rail_projections", interior_checks)
    print("mixed_site_sets", 4368)
    print("mixed_projection_resistant_sets", mixed_resistant)
    print("mixed_actual_negative_sets", mixed_negative)
    print("mixed_actual_negative_orbits", mixed_orbits)
    print("mixed_status_digest", mixed_digest)
    print("two_vertex_contact_distributions", distribution_checks)
    print("GREEN: endpoint saturation and projection checks verified")


if __name__ == "__main__":
    main()
