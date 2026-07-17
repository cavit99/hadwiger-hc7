#!/usr/bin/env python3
"""Feasibility census for exact eight-terminal irreducible kernels.

This is a discovery probe, not a proof dependency.  It uses only the
standard library and the installed nauty ``geng`` executable.
"""

from __future__ import annotations

import collections
import itertools
import subprocess


def graph6_adjacency(line: bytes) -> tuple[int, ...]:
    data = line.strip()
    assert data and data[0] != ord(">")
    order = data[0] - 63
    assert 0 <= order <= 62
    payload = data[1:]
    bits = []
    for value in payload:
        value -= 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def connected(adjacency: tuple[int, ...], removed: int = 0) -> bool:
    remaining = ((1 << len(adjacency)) - 1) & ~removed
    if not remaining:
        return True
    reached = remaining & -remaining
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adjacency[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == old:
            return reached == remaining


def three_connected(adjacency: tuple[int, ...]) -> bool:
    order = len(adjacency)
    if order < 4:
        return False
    return all(
        connected(adjacency, sum(1 << vertex for vertex in removed))
        for size in range(3)
        for removed in itertools.combinations(range(order), size)
    )


def edges(adjacency: tuple[int, ...]):
    for left in range(len(adjacency)):
        for right in range(left + 1, len(adjacency)):
            if adjacency[left] >> right & 1:
                yield left, right


def delete_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    answer = list(adjacency)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    assert left < right and adjacency[left] >> right & 1
    image = tuple(
        left if vertex == right else vertex - (vertex > right)
        for vertex in range(len(adjacency))
    )
    answer = [0] * (len(adjacency) - 1)
    for old_left, old_right in edges(adjacency):
        new_left, new_right = image[old_left], image[old_right]
        if new_left == new_right:
            continue
        if new_left > new_right:
            new_left, new_right = new_right, new_left
        answer[new_left] |= 1 << new_right
        answer[new_right] |= 1 << new_left
    return tuple(answer)


def contractible(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    if left > right:
        left, right = right, left
    return three_connected(contract_edge(adjacency, left, right))


def geng(order: int):
    process = subprocess.Popen(
        ["geng", "-cq", "-d3", str(order)],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    for line in process.stdout:
        yield graph6_adjacency(line)
    assert process.wait() == 0


def order_eight_base():
    total = three = minimal = 0
    profile = collections.Counter()
    for adjacency in geng(8):
        total += 1
        if not three_connected(adjacency):
            continue
        three += 1
        if any(
            three_connected(delete_edge(adjacency, left, right))
            for left, right in edges(adjacency)
        ):
            continue
        minimal += 1
        profile[sum(1 for _ in edges(adjacency))] += 1
    return total, three, minimal, dict(sorted(profile.items()))


def order_nine_one_extra():
    total = three = rooted = 0
    charge_profile = collections.Counter()
    edge_profile = collections.Counter()
    for adjacency in geng(9):
        total += 1
        if not three_connected(adjacency):
            continue
        three += 1
        for extra in range(9):
            neighbours = tuple(
                vertex
                for vertex in range(9)
                if adjacency[extra] >> vertex & 1
            )
            if any(contractible(adjacency, extra, vertex) for vertex in neighbours):
                continue
            charged = []
            for vertex in neighbours:
                if adjacency[vertex].bit_count() != 3:
                    continue
                others = tuple(
                    old
                    for old in range(9)
                    if old != extra and adjacency[vertex] >> old & 1
                )
                if len(others) == 2 and all(
                    contractible(adjacency, vertex, old) for old in others
                ):
                    charged.append(vertex)
            assert len(charged) >= 4
            rooted += 1
            charge_profile[len(charged)] += 1
            edge_profile[sum(1 for _ in edges(adjacency))] += 1
    return (
        total,
        three,
        rooted,
        dict(sorted(charge_profile.items())),
        dict(sorted(edge_profile.items())),
    )


def two_regular_graphs() -> tuple[tuple[int, ...], ...]:
    answer = set()

    # One eight-cycle.
    for tail in itertools.permutations(range(1, 8)):
        cycle = (0,) + tail
        if cycle[1] > cycle[-1]:
            continue
        edge_set = frozenset(
            tuple(sorted((cycle[index], cycle[(index + 1) % 8])))
            for index in range(8)
        )
        answer.add(edge_set)

    # A triangle and a five-cycle.
    for triangle in itertools.combinations(range(8), 3):
        five = tuple(vertex for vertex in range(8) if vertex not in triangle)
        first = five[0]
        for tail in itertools.permutations(five[1:]):
            cycle = (first,) + tail
            if cycle[1] > cycle[-1]:
                continue
            edge_set = {
                tuple(sorted(edge)) for edge in itertools.combinations(triangle, 2)
            }
            edge_set.update(
                tuple(sorted((cycle[index], cycle[(index + 1) % 5])))
                for index in range(5)
            )
            answer.add(frozenset(edge_set))

    # Two four-cycles.
    for first_part in itertools.combinations(range(1, 8), 3):
        left = (0,) + first_part
        right = tuple(vertex for vertex in range(8) if vertex not in left)
        left_cycles = []
        right_cycles = []
        for vertices, target in ((left, left_cycles), (right, right_cycles)):
            start = vertices[0]
            for tail in itertools.permutations(vertices[1:]):
                cycle = (start,) + tail
                if cycle[1] > cycle[-1]:
                    continue
                target.append(
                    frozenset(
                        tuple(sorted((cycle[index], cycle[(index + 1) % 4])))
                        for index in range(4)
                    )
                )
        for left_cycle in left_cycles:
            for right_cycle in right_cycles:
                answer.add(left_cycle | right_cycle)

    assert len(answer) == 3507
    result = []
    for edge_set in answer:
        adjacency = [0] * 8
        for left, right in edge_set:
            adjacency[left] |= 1 << right
            adjacency[right] |= 1 << left
        result.append(tuple(adjacency))
    return tuple(result)


def add_edge(adjacency: list[int], left: int, right: int) -> None:
    adjacency[left] |= 1 << right
    adjacency[right] |= 1 << left


def order_ten_two_extras():
    tested = irreducible = 0
    profile = collections.Counter()
    cycle_profile = collections.Counter()
    for terminal_graph in two_regular_graphs():
        component_sizes = []
        unseen = (1 << 8) - 1
        while unseen:
            seed = unseen & -unseen
            reached = seed
            while True:
                old = reached
                frontier = reached
                neighbours = 0
                while frontier:
                    bit = frontier & -frontier
                    neighbours |= terminal_graph[bit.bit_length() - 1]
                    frontier -= bit
                reached |= neighbours
                if reached == old:
                    break
            component_sizes.append(reached.bit_count())
            unseen &= ~reached
        cycle_type = tuple(sorted(component_sizes, reverse=True))

        for first_charge in itertools.combinations(range(8), 4):
            first_charge = frozenset(first_charge)
            second_charge = frozenset(range(8)) - first_charge
            for extra_edge in (False, True):
                tested += 1
                adjacency = list(terminal_graph) + [0, 0]
                for terminal in first_charge:
                    add_edge(adjacency, terminal, 8)
                for terminal in second_charge:
                    add_edge(adjacency, terminal, 9)
                if extra_edge:
                    add_edge(adjacency, 8, 9)
                adjacency = tuple(adjacency)
                if not three_connected(adjacency):
                    continue
                if any(
                    contractible(adjacency, extra, terminal)
                    for extra, charge in ((8, first_charge), (9, second_charge))
                    for terminal in charge
                ):
                    continue
                if extra_edge and contractible(adjacency, 8, 9):
                    continue
                irreducible += 1
                profile[(extra_edge, cycle_type)] += 1
                cycle_profile[cycle_type] += 1
    return tested, irreducible, dict(sorted(profile.items())), dict(sorted(cycle_profile.items()))


def main():
    print("order8", order_eight_base(), flush=True)
    print("order9", order_nine_one_extra(), flush=True)
    print("order10", order_ten_two_extras(), flush=True)


if __name__ == "__main__":
    main()
