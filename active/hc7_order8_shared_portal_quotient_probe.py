#!/usr/bin/env python3
"""Falsification support for two three-component path constructions.

The theorem ``results/hc7_order8_three_component_path_completion.md`` is
proved without computation.  This script independently checks its displayed
branch sets over all 82 audited order-eight boundary types.

It uses only the Python standard library and the existing boundary decoder.
It does not search component interiors and does not promote a finite check to
an unbounded theorem.

Run from the repository root with::

    geng -q 8 | python3 active/hc7_order8_shared_portal_quotient_probe.py
"""

from __future__ import annotations

import hashlib
import sys
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "results")]

from hc7_order8_three_component_boundary_verify import (  # noqa: E402
    decode_g6,
    encode_g6,
    induced_cycle,
    is_residual,
)


N = 8
ALL = (1 << N) - 1


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def connected(adjacency: tuple[int, ...], vertices: int) -> bool:
    if not vertices:
        return False
    reached = vertices & -vertices
    while True:
        expanded = reached
        todo = reached
        while todo:
            bit = todo & -todo
            todo ^= bit
            expanded |= adjacency[bit.bit_length() - 1] & vertices
        if expanded == reached:
            return reached == vertices
        reached = expanded


def adjacent(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    todo = left
    while todo:
        bit = todo & -todo
        todo ^= bit
        if adjacency[bit.bit_length() - 1] & right:
            return True
    return False


def verify_model(adjacency: tuple[int, ...], model: tuple[int, ...]) -> None:
    assert len(model) == 7
    used = 0
    for branch in model:
        assert branch and not (used & branch)
        used |= branch
        assert connected(adjacency, branch)
    assert all(
        adjacent(adjacency, left, right)
        for left, right in combinations(model, 2)
    )


def cycle_order(
    adjacency: tuple[int, ...], vertices: frozenset[int]
) -> tuple[int, ...]:
    start = min(vertices)
    neighbours = sorted(
        vertex
        for vertex in vertices
        if (adjacency[start] >> vertex) & 1
    )
    assert len(neighbours) == 2
    answer = [start, neighbours[0]]
    while len(answer) < len(vertices):
        previous, current = answer[-2:]
        choices = [
            vertex
            for vertex in vertices
            if vertex != previous and ((adjacency[current] >> vertex) & 1)
        ]
        assert len(choices) == 1
        answer.append(choices[0])
    assert (adjacency[answer[-1]] >> start) & 1
    return tuple(answer)


def k3_on_cycle(
    boundary: tuple[int, ...], cycle: frozenset[int]
) -> tuple[int, int, int]:
    order = cycle_order(boundary, cycle)
    if len(order) == 3:
        return (1 << order[0], 1 << order[1], 1 << order[2])
    assert len(order) == 5
    return (
        1 << order[0],
        (1 << order[1]) | (1 << order[2]),
        (1 << order[3]) | (1 << order[4]),
    )


def odd_cycle_avoiding(
    boundary: tuple[int, ...], avoided: int
) -> frozenset[int]:
    for order in (3, 5):
        for choice in combinations(
            (vertex for vertex in range(N) if vertex != avoided), order
        ):
            cycle = frozenset(choice)
            if induced_cycle(boundary, cycle):
                return cycle
    raise AssertionError("the audited boundary should have an odd cycle avoiding d")


def shared_portal_quotient(
    boundary: tuple[int, ...], d: int, e: int
) -> tuple[int, ...]:
    # Boundary 0,...,7; Q0=8, Q1=9, L=10, R=11, v=12.
    adjacency = list(boundary) + [0] * 5
    for full in (8, 9):
        for vertex in range(N):
            add_edge(adjacency, full, vertex)
    for vertex in range(N):
        if vertex != d:
            add_edge(adjacency, 10, vertex)
        if vertex != e:
            add_edge(adjacency, 11, vertex)
    for vertex in (10, 11, d, e):
        add_edge(adjacency, 12, vertex)
    return tuple(adjacency)


def shared_portal_model(
    boundary: tuple[int, ...], d: int, e: int
) -> tuple[int, ...]:
    cycle = odd_cycle_avoiding(boundary, d)
    anchors = [
        vertex for vertex in range(N) if vertex not in cycle and vertex != d
    ]
    assert len(anchors) >= 2
    return (
        (1 << 8) | (1 << anchors[0]),
        (1 << 9) | (1 << anchors[1]),
        1 << 10,
        (1 << 11) | (1 << 12),
        *k3_on_cycle(boundary, cycle),
    )


def three_block_models(boundary: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    """Enumerate all boundary K3 models leaving at least two vertices."""

    models: set[tuple[int, int, int]] = set()
    for support in range(1 << N):
        if not 3 <= support.bit_count() <= 6:
            continue
        vertices = [vertex for vertex in range(N) if (support >> vertex) & 1]
        blocks: list[int] = []

        def assign(index: int) -> None:
            if index == len(vertices):
                if len(blocks) != 3:
                    return
                ordered = tuple(sorted(blocks))
                if all(connected(boundary, block) for block in ordered) and all(
                    adjacent(boundary, left, right)
                    for left, right in combinations(ordered, 2)
                ):
                    models.add(ordered)
                return
            vertex_bit = 1 << vertices[index]
            for block_index in range(len(blocks)):
                blocks[block_index] |= vertex_bit
                assign(index + 1)
                blocks[block_index] ^= vertex_bit
            if len(blocks) < 3:
                blocks.append(vertex_bit)
                assign(index + 1)
                blocks.pop()

        assign(0)
    return tuple(sorted(models))


def strict_reversal_certificate(
    boundary: tuple[int, ...],
    d: int,
    e: int,
    models: tuple[tuple[int, int, int], ...],
) -> tuple[int, int, tuple[int, int, int]] | None:
    for model in models:
        support = model[0] | model[1] | model[2]
        anchors = ALL & ~support & ~(1 << d) & ~(1 << e)
        if anchors.bit_count() < 2:
            continue
        if any(
            not (branch & ~(1 << d)) or not (branch & ~(1 << e))
            for branch in model
        ):
            continue
        first = anchors & -anchors
        second = (anchors ^ first) & -(anchors ^ first)
        return first.bit_length() - 1, second.bit_length() - 1, model
    return None


def strict_reversal_quotient(
    boundary: tuple[int, ...], d: int, e: int
) -> tuple[int, ...]:
    # Boundary 0,...,7; Q0=8, Q1=9, A=10, B=11.
    adjacency = list(boundary) + [0] * 4
    for full in (8, 9):
        for vertex in range(N):
            add_edge(adjacency, full, vertex)
    for vertex in range(N):
        if vertex != d:
            add_edge(adjacency, 10, vertex)
        if vertex != e:
            add_edge(adjacency, 11, vertex)
    add_edge(adjacency, 10, 11)
    return tuple(adjacency)


def width_five_ordering(adjacency: tuple[int, ...]) -> tuple[int, ...] | None:
    """Find an exact elimination-order certificate of width at most five."""

    full = (1 << len(adjacency)) - 1

    @lru_cache(maxsize=None)
    def search(alive: int, graph: tuple[int, ...]) -> tuple[int, ...] | None:
        if not alive:
            return ()
        candidates = []
        todo = alive
        while todo:
            bit = todo & -todo
            todo ^= bit
            vertex = bit.bit_length() - 1
            neighbours = graph[vertex] & alive & ~bit
            if neighbours.bit_count() <= 5:
                fill = 0
                scan = neighbours
                while scan:
                    item = scan & -scan
                    scan ^= item
                    other = item.bit_length() - 1
                    fill += (neighbours & ~graph[other]).bit_count()
                candidates.append((fill, neighbours.bit_count(), vertex, neighbours))
        for _, _, vertex, neighbours in sorted(candidates):
            reduced = list(graph)
            scan = neighbours
            while scan:
                item = scan & -scan
                scan ^= item
                other = item.bit_length() - 1
                reduced[other] |= neighbours & ~(1 << other)
                reduced[other] &= ~(1 << vertex)
            reduced[vertex] = 0
            next_alive = alive & ~(1 << vertex)
            suffix = search(
                next_alive, tuple(row & next_alive for row in reduced)
            )
            if suffix is not None:
                return (vertex,) + suffix
        return None

    return search(full, adjacency)


def verify_width_five(
    adjacency: tuple[int, ...], ordering: tuple[int, ...]
) -> None:
    assert sorted(ordering) == list(range(len(adjacency)))
    graph = list(adjacency)
    alive = (1 << len(adjacency)) - 1
    for vertex in ordering:
        neighbours = graph[vertex] & alive & ~(1 << vertex)
        assert neighbours.bit_count() <= 5
        scan = neighbours
        while scan:
            item = scan & -scan
            scan ^= item
            other = item.bit_length() - 1
            graph[other] |= neighbours & ~(1 << other)
            graph[other] &= ~(1 << vertex)
        alive &= ~(1 << vertex)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    keep = [vertex for vertex in range(len(adjacency)) if vertex != right]
    position = {vertex: index for index, vertex in enumerate(keep)}
    answer = [0] * len(keep)
    for first_index, first in enumerate(keep):
        for second_index in range(first_index + 1, len(keep)):
            second = keep[second_index]
            edge = bool((adjacency[first] >> second) & 1)
            if first == left:
                edge |= bool((adjacency[right] >> second) & 1)
            if second == left:
                edge |= bool((adjacency[first] >> right) & 1)
            if edge:
                answer[first_index] |= 1 << second_index
                answer[second_index] |= 1 << first_index
    return tuple(answer)


def spanning_clique_model(
    adjacency: tuple[int, ...], target: int
) -> tuple[int, ...] | None:
    """Exact contraction-only search in a connected graph."""

    failed: set[tuple[int, ...]] = set()

    def search(
        graph: tuple[int, ...], bags: tuple[int, ...]
    ) -> tuple[int, ...] | None:
        if len(graph) == target:
            if all(row.bit_count() == target - 1 for row in graph):
                return bags
            return None
        if graph in failed:
            return None
        choices = []
        for left in range(len(graph)):
            for right in range(left + 1, len(graph)):
                if not ((graph[left] >> right) & 1):
                    continue
                reduced = contract_edge(graph, left, right)
                missing = sum(
                    len(reduced) - 1 - row.bit_count() for row in reduced
                ) // 2
                choices.append((missing, left, right, reduced))
        for _, left, right, reduced in sorted(choices):
            reduced_bags = list(bags)
            reduced_bags[left] |= reduced_bags[right]
            del reduced_bags[right]
            result = search(reduced, tuple(reduced_bags))
            if result is not None:
                return result
        failed.add(graph)
        return None

    return search(adjacency, tuple(1 << vertex for vertex in range(len(adjacency))))


def bipartite_on(boundary: tuple[int, ...], vertices: int) -> bool:
    colours = [-1] * N
    todo_roots = vertices
    while todo_roots:
        root_bit = todo_roots & -todo_roots
        root = root_bit.bit_length() - 1
        colours[root] = 0
        stack = [root]
        todo_roots ^= root_bit
        while stack:
            vertex = stack.pop()
            neighbours = boundary[vertex] & vertices
            while neighbours:
                bit = neighbours & -neighbours
                neighbours ^= bit
                other = bit.bit_length() - 1
                if colours[other] < 0:
                    colours[other] = colours[vertex] ^ 1
                    stack.append(other)
                    todo_roots &= ~bit
                elif colours[other] == colours[vertex]:
                    return False
    return True


def shortest_cycle_order(boundary: tuple[int, ...], vertices: int) -> int | None:
    available = [vertex for vertex in range(N) if (vertices >> vertex) & 1]
    for order in range(3, len(available) + 1):
        if any(
            induced_cycle(boundary, frozenset(choice))
            for choice in combinations(available, order)
        ):
            return order
    return None


def automorphisms(boundary: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    degree = tuple(row.bit_count() for row in boundary)
    order = sorted(
        range(N),
        key=lambda vertex: (
            sum(1 for item in degree if item == degree[vertex]),
            -degree[vertex],
            vertex,
        ),
    )
    image = [-1] * N
    answer: list[tuple[int, ...]] = []

    def search(index: int, used: int) -> None:
        if index == N:
            answer.append(tuple(image))
            return
        vertex = order[index]
        for target in range(N):
            if (used >> target) & 1 or degree[target] != degree[vertex]:
                continue
            if any(
                bool((boundary[vertex] >> earlier) & 1)
                != bool((boundary[target] >> image[earlier]) & 1)
                for earlier in order[:index]
            ):
                continue
            image[vertex] = target
            search(index + 1, used | (1 << target))
            image[vertex] = -1

    search(0, 0)
    return tuple(answer)


def main() -> None:
    boundaries: list[tuple[str, tuple[int, ...]]] = []
    for line in sys.stdin:
        boundary = decode_g6(line)
        if boundary and is_residual(boundary):
            boundaries.append((encode_g6(boundary), boundary))

    shared_cases = 0
    strict_cases = 0
    strict_certificates = 0
    strict_uncovered: list[str] = []
    strict_live: list[str] = []
    uncovered_types: Counter[tuple[bool, bool, bool, int | None]] = Counter()
    live_types: Counter[tuple[bool, bool, bool, int | None]] = Counter()
    reflected_bipartite_edge = 0
    uncovered_width_five = 0
    uncovered_width_unresolved: list[str] = []
    uncovered_extra_models = 0
    uncovered_true_quotient_survivors: list[str] = []
    true_survivor_types: Counter[tuple[bool, bool, bool, int | None]] = Counter()
    true_survivor_pairs: dict[str, list[tuple[int, int]]] = {}
    basic_live: list[str] = []
    basic_live_types: Counter[tuple[bool, bool, bool, int | None]] = Counter()
    for code, boundary in boundaries:
        boundary_models = three_block_models(boundary)
        for d in range(N):
            for e in range(N):
                if d == e:
                    continue
                shared_cases += 1
                shared_graph = shared_portal_quotient(boundary, d, e)
                verify_model(
                    shared_graph,
                    shared_portal_model(boundary, d, e),
                )

                strict_cases += 1
                remainder = ALL & ~(1 << d) & ~(1 << e)
                bipartite = bipartite_on(boundary, remainder)
                girth = shortest_cycle_order(boundary, remainder)
                forest = girth is None
                de_edge = bool((boundary[d] >> e) & 1)
                kind = (de_edge, bipartite, forest, girth)
                if not (girth is not None and girth <= 4) and not (
                    de_edge and bipartite
                ):
                    basic_live.append(f"{code} d={d} e={e}")
                    basic_live_types[kind] += 1
                certificate = strict_reversal_certificate(
                    boundary, d, e, boundary_models
                )
                if certificate is None:
                    item = f"{code} d={d} e={e}"
                    strict_uncovered.append(item)
                    uncovered_types[kind] += 1
                    strict_graph = strict_reversal_quotient(boundary, d, e)
                    ordering = width_five_ordering(strict_graph)
                    if ordering is None:
                        uncovered_width_unresolved.append(item)
                        model = spanning_clique_model(strict_graph, 7)
                        if model is None:
                            # This is the exact structural invariant isolated by
                            # the finite quotient check.  Keep it as an assertion,
                            # not merely a conclusion inferred from printed counts.
                            assert not de_edge and bipartite
                            uncovered_true_quotient_survivors.append(item)
                            true_survivor_types[kind] += 1
                            true_survivor_pairs.setdefault(code, []).append((d, e))
                        else:
                            verify_model(strict_graph, model)
                            uncovered_extra_models += 1
                    else:
                        verify_width_five(strict_graph, ordering)
                        uncovered_width_five += 1
                        assert not de_edge and bipartite
                        uncovered_true_quotient_survivors.append(item)
                        true_survivor_types[kind] += 1
                        true_survivor_pairs.setdefault(code, []).append((d, e))
                    if de_edge and bipartite:
                        reflected_bipartite_edge += 1
                    else:
                        strict_live.append(item)
                        live_types[kind] += 1
                    continue
                strict_certificates += 1
                x0, x1, model = certificate
                strict_graph = strict_reversal_quotient(boundary, d, e)
                verify_model(
                    strict_graph,
                    (
                        (1 << 8) | (1 << x0),
                        (1 << 9) | (1 << x1),
                        1 << 10,
                        1 << 11,
                        *model,
                    ),
                )

    digest = hashlib.sha256(
        ("\n".join(strict_uncovered) + "\n").encode()
    ).hexdigest()
    true_survivor_digest = hashlib.sha256(
        ("\n".join(uncovered_true_quotient_survivors) + "\n").encode()
    ).hexdigest()
    assert len(boundaries) == 82
    assert shared_cases == 82 * 8 * 7
    assert strict_cases == shared_cases
    assert strict_certificates == 4_458
    assert len(strict_uncovered) == 134
    assert digest == "c560e7411af1f92c8f9dab389807e1e386d3201dc6a998e0b160b54471ad5b1e"
    assert true_survivor_digest == (
        "1a2325307e7bd5c856b0a1888295b9424a738ac11a8a69c2edcdda8279221110"
    )
    assert uncovered_width_five == 122
    assert uncovered_extra_models == 10
    assert len(uncovered_true_quotient_survivors) == 124
    print(f"boundaries={len(boundaries)}")
    print(f"shared_portal_models={shared_cases}/{shared_cases}")
    print(f"strict_reversal_boundary_certificates={strict_certificates}/{strict_cases}")
    print(f"strict_live_after_short_cycle_and_reflection={len(basic_live)}")
    for kind, count in sorted(
        basic_live_types.items(), key=lambda item: repr(item[0])
    ):
        print(f"basic_live_type={kind} count={count}")
    print(f"strict_reversal_uncovered={len(strict_uncovered)}")
    print(f"strict_uncovered_width_five={uncovered_width_five}")
    print(f"strict_uncovered_width_unresolved={len(uncovered_width_unresolved)}")
    print(f"strict_uncovered_extra_k7_models={uncovered_extra_models}")
    print(
        "strict_true_quotient_survivors="
        f"{len(uncovered_true_quotient_survivors)}"
    )
    print("strict_true_survivor_invariant=de_nonedge_and_bipartite_remainder")
    for kind, count in sorted(
        true_survivor_types.items(), key=lambda item: repr(item[0])
    ):
        print(f"strict_true_survivor_type={kind} count={count}")
    orbit_representatives: list[tuple[str, int, int]] = []
    boundary_by_code = dict(boundaries)
    for code, pairs in sorted(true_survivor_pairs.items()):
        group = automorphisms(boundary_by_code[code])
        remaining = set(pairs)
        while remaining:
            representative = min(remaining)
            orbit = {
                (permutation[representative[0]], permutation[representative[1]])
                for permutation in group
            }
            remaining -= orbit
            orbit_representatives.append((code, *representative))
    assert len(orbit_representatives) == 19
    print(f"strict_true_quotient_orbits={len(orbit_representatives)}")
    print(f"strict_true_survivor_sha256={true_survivor_digest}")
    for code, d, e in orbit_representatives:
        print(f"strict_quotient_orbit {code} d={d} e={e}")
    for item in uncovered_true_quotient_survivors:
        if item in uncovered_width_unresolved:
            print("strict_cyclic_quotient_survivor", item)
    for item in uncovered_width_unresolved:
        print("strict_width_unresolved", item)
    print(f"strict_reflected_bipartite_edge={reflected_bipartite_edge}")
    print(f"strict_live_after_reflection={len(strict_live)}")
    print(f"strict_uncovered_sha256={digest}")
    for kind, count in sorted(
        uncovered_types.items(), key=lambda item: repr(item[0])
    ):
        print(f"uncovered_type={kind} count={count}")
    for kind, count in sorted(live_types.items(), key=lambda item: repr(item[0])):
        print(f"live_type={kind} count={count}")
    for item in strict_uncovered[:40]:
        print("strict_uncovered", item)


if __name__ == "__main__":
    main()
