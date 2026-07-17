#!/usr/bin/env python3
"""Independent carrier cross-check for arm-order-six, overlap three.

Shared input: only the joined nine-support relation produced by
``hc7_cross_arm_overlap_three_kernel_decoder.joined_states(6)``.

Independent layers in this file:

* the exact automorphism group and orbit representatives;
* the common rooted-K4 filter;
* the K7-minor search, implemented by at most three edge contractions;
* all 360 labelled C7 orders and all 35 labelled K3,4 bipartitions; and
* literal verification of every returned seven-bag certificate.

Carrier edges are inserted only after the original support relation has
been joined.  They are never used as literal terminal edges in a support
constraint or in the common-state filter.
"""

from __future__ import annotations

import functools
import hashlib
import itertools

import hc7_cross_arm_overlap_three_kernel_decoder as relation


CELL, PAIRS, PAIR_INDEX, STATES = relation.joined_states(6)
N, A_TUPLE, I, X, P, Q, T, SUPPORTS_TUPLE, LITERAL_FIVES = CELL
A = frozenset(A_TUPLE)
L = (3, 4, 5)
Z = (6, 7)
ROOTS = (8, 9)
SUPPORTS = frozenset(frozenset(support) for support in SUPPORTS_TUPLE)


def pair(left: int, right: int) -> tuple[int, int]:
    return (left, right) if left < right else (right, left)


def has_edge(mask: int, left: int, right: int) -> bool:
    return bool(mask >> PAIR_INDEX[pair(left, right)] & 1)


def category_automorphisms() -> tuple[tuple[int, ...], ...]:
    """Return, and intrinsically certify, the full support automorphism group."""

    support_degree = {
        vertex: sum(vertex in support for support in SUPPORTS)
        for vertex in range(N)
    }
    assert {vertex for vertex in range(N) if support_degree[vertex] == 2} == set(Z)
    assert {vertex for vertex in range(N) if support_degree[vertex] == 4} == set(ROOTS)
    degree_seven = {vertex for vertex in range(N) if support_degree[vertex] == 7}
    assert degree_seven == set(I) | set(L)

    # Once Z is intrinsically identified, co-incidence with a Z-containing
    # support distinguishes I from L.  Thus every support automorphism must
    # preserve the four displayed categories.
    z_incidence = {
        vertex: sum(
            vertex in support and bool(set(support) & set(Z))
            for support in SUPPORTS
        )
        for vertex in degree_seven
    }
    assert {vertex for vertex in degree_seven if z_incidence[vertex] == 2} == set(I)
    assert {vertex for vertex in degree_seven if z_incidence[vertex] == 0} == set(L)

    answer = []
    for image_i in itertools.permutations(I):
        for image_l in itertools.permutations(L):
            for image_z in itertools.permutations(Z):
                for image_roots in itertools.permutations(ROOTS):
                    image = image_i + image_l + image_z + image_roots
                    transported = frozenset(
                        frozenset(image[vertex] for vertex in support)
                        for support in SUPPORTS
                    )
                    assert transported == SUPPORTS
                    answer.append(image)
    assert len(answer) == 144
    return tuple(answer)


AUTOMORPHISMS = category_automorphisms()


def transform(mask: int, image: tuple[int, ...]) -> int:
    answer = 0
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            answer |= 1 << PAIR_INDEX[pair(image[left], image[right])]
    return answer


def canonical_state(ones: int, zeros: int) -> tuple[int, int]:
    return min((transform(ones, image), transform(zeros, image)) for image in AUTOMORPHISMS)


def bags_touch(mask: int, left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(has_edge(mask, u, v) for u in left for v in right)


def has_common_rooted_k4(mask: int) -> bool:
    """Independent support-at-most-five common-outcome test."""

    for omitted_core in I:
        available = tuple(sorted(A - {omitted_core}))
        partitions = [
            tuple((vertex,) for vertex in available if vertex != unused)
            for unused in available
        ]
        partitions.extend(
            ((left, right),)
            + tuple((vertex,) for vertex in available if vertex not in (left, right))
            for left, right in itertools.combinations(available, 2)
        )
        for bags in partitions:
            if any(len(bag) == 2 and not has_edge(mask, *bag) for bag in bags):
                continue
            if not all(bags_touch(mask, left, right) for left, right in itertools.combinations(bags, 2)):
                continue
            if all(
                all(any(has_edge(mask, named, vertex) for vertex in bag) for bag in bags)
                for named in (omitted_core, P, Q)
            ):
                return True
    return False


def adjacency(mask: int) -> tuple[int, ...]:
    answer = [0] * N
    for index, (left, right) in enumerate(PAIRS):
        if mask >> index & 1:
            answer[left] |= 1 << right
            answer[right] |= 1 << left
    return tuple(answer)


def first_seven_clique(graph: tuple[int, ...]) -> tuple[int, ...] | None:
    for vertices in itertools.combinations(range(len(graph)), 7):
        vertex_mask = sum(1 << vertex for vertex in vertices)
        if all((graph[vertex] & vertex_mask).bit_count() == 6 for vertex in vertices):
            return vertices
    return None


def contract(graph: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    """Contract left--right, where left < right, and relabel increasingly."""

    assert left < right and graph[left] >> right & 1
    image = tuple(left if vertex == right else vertex - (vertex > right) for vertex in range(len(graph)))
    answer = [0] * (len(graph) - 1)
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if not (graph[u] >> v & 1):
                continue
            x, y = image[u], image[v]
            if x == y:
                continue
            answer[x] |= 1 << y
            answer[y] |= 1 << x
    return tuple(answer)


# A K7 model on ten objects uses at most three contractions.  At any
# intermediate order, finding a literal seven-clique permits every other
# quotient vertex to be deleted.  The cached recipe is independent of the
# original branch-set ownership and can be replayed on any occurrence of
# the exact labelled quotient.
@functools.lru_cache(maxsize=None)
def k7_recipe(graph: tuple[int, ...]):
    clique = first_seven_clique(graph)
    if clique is not None:
        return ("clique", clique)
    if len(graph) == 7:
        return None
    for left in range(len(graph)):
        for right in range(left + 1, len(graph)):
            if graph[left] >> right & 1:
                child = k7_recipe(contract(graph, left, right))
                if child is not None:
                    return ("contract", left, right, child)
    return None


def replay_recipe(recipe, branch_sets: tuple[int, ...]) -> tuple[int, ...]:
    if recipe[0] == "clique":
        return tuple(branch_sets[index] for index in recipe[1])
    _, left, right, child = recipe
    updated = list(branch_sets)
    updated[left] |= updated[right]
    del updated[right]
    return replay_recipe(child, tuple(updated))


def connected(mask: int, vertices: int) -> bool:
    first = (vertices & -vertices).bit_length() - 1
    reached = 1 << first
    while True:
        expanded = reached
        for vertex in range(N):
            if reached >> vertex & 1:
                expanded |= sum(
                    1 << other
                    for other in range(N)
                    if other != vertex and has_edge(mask, vertex, other)
                )
        expanded &= vertices
        if expanded == reached:
            return reached == vertices
        reached = expanded


def verify_model(mask: int, bags: tuple[int, ...]) -> None:
    assert len(bags) == 7
    assert all(bag for bag in bags)
    assert all(not (left & right) for left, right in itertools.combinations(bags, 2))
    assert all(connected(mask, bag) for bag in bags)
    for left, right in itertools.combinations(bags, 2):
        assert any(
            has_edge(mask, u, v)
            for u in range(N)
            if left >> u & 1
            for v in range(N)
            if right >> v & 1
        )


def k7_model(mask: int) -> tuple[int, ...] | None:
    recipe = k7_recipe(adjacency(mask))
    if recipe is None:
        return None
    bags = replay_recipe(recipe, tuple(1 << vertex for vertex in range(N)))
    verify_model(mask, bags)
    return bags


def cycle_carriers():
    first = T[0]
    for tail in itertools.permutations(T[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        mask = sum(
            1 << PAIR_INDEX[pair(order[index], order[(index + 1) % 7])]
            for index in range(7)
        )
        yield order, mask


def biclique_carriers():
    for left in itertools.combinations(T, 3):
        right = tuple(vertex for vertex in T if vertex not in left)
        mask = sum(
            1 << PAIR_INDEX[pair(u, v)]
            for u in left
            for v in right
        )
        yield (left, right), mask


def live_orbits() -> tuple[tuple[int, int], ...]:
    canonical = {
        canonical_state(ones, zeros)
        for ones, zeros in STATES
        if not has_common_rooted_k4(ones)
    }
    assert len(canonical) == 140
    live = tuple(sorted((ones, zeros) for ones, zeros in canonical if k7_model(ones) is None))
    assert len(live) == 110
    return live


def encode_bags(bags: tuple[int, ...]) -> str:
    return ";".join(
        ",".join(str(vertex) for vertex in range(N) if bag >> vertex & 1)
        for bag in sorted(bags)
    )


def main() -> None:
    live = live_orbits()
    cycles = tuple(cycle_carriers())
    bicliques = tuple(biclique_carriers())
    assert len(cycles) == 360
    assert len(bicliques) == 35

    cycle_bad_pairs = []
    cycle_bad_states = set()
    cycle_all_good_states = set()
    biclique_bad_pairs = []
    certificate_hash = hashlib.sha256()

    for state_index, (ones, _) in enumerate(live):
        bad_here = 0
        for order, carrier in cycles:
            if k7_model(ones | carrier) is None:
                cycle_bad_pairs.append((state_index, order))
                bad_here += 1
        if bad_here:
            cycle_bad_states.add(state_index)
        else:
            cycle_all_good_states.add(state_index)

        for partition, carrier in bicliques:
            bags = k7_model(ones | carrier)
            if bags is None:
                biclique_bad_pairs.append((state_index, partition))
                continue
            record = f"{state_index}|{partition}|{encode_bags(bags)}\n"
            certificate_hash.update(record.encode())

    assert not biclique_bad_pairs

    # The first canonical live state also gives a compact guardrail against
    # treating the full order-seven kernel as automatically sufficient.  The
    # following carrier is the wheel with hub 3 and rim
    # 4-5-6-7-8-9-4.  It is minimally three-connected, but its union with the
    # forced original edges still has no K7 minor.
    wheel_edges = (
        (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
        (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (4, 9),
    )
    wheel = sum(1 << PAIR_INDEX[pair(*edge)] for edge in wheel_edges)
    assert k7_model(live[0][0] | wheel) is None

    print("seven-terminal carrier/live-state cross-check: verified")
    print("support_automorphisms=144 noncommon_orbits=140 live_orbits=110")
    print(
        f"C7_pairs={len(live) * len(cycles)} "
        f"bad_pairs={len(cycle_bad_pairs)} "
        f"bad_states={len(cycle_bad_states)} "
        f"all_good_states={len(cycle_all_good_states)}"
    )
    print(
        f"K34_pairs={len(live) * len(bicliques)} "
        "bad_pairs=0 certificate_sha256=" + certificate_hash.hexdigest()
    )
    print("full_W7_guardrail=bad on canonical live state 0")
    print("first_bad_C7", cycle_bad_pairs[:10])


if __name__ == "__main__":
    main()
