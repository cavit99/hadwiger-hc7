#!/usr/bin/env python3
"""Verify the critical-triangle Kempe-separation barrier without dependencies."""

from itertools import combinations


GRAPH6 = "HCpvbqk"
V, A, B = 0, 3, 6
DELETED = {frozenset((V, A)), frozenset((V, B))}


def decode_graph6(code):
    data = [ord(char) - 63 for char in code.strip()]
    assert data and 0 <= data[0] <= 62
    n = data[0]
    bits = []
    for value in data[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    graph = {vertex: set() for vertex in range(n)}
    position = 0
    # graph6 stores the upper triangle column by column.
    for right in range(1, n):
        for left in range(right):
            if bits[position]:
                graph[left].add(right)
                graph[right].add(left)
            position += 1
    return graph


def copy_graph(graph):
    return {vertex: set(neighbours) for vertex, neighbours in graph.items()}


def add_edge(graph, left, right):
    graph[left].add(right)
    graph[right].add(left)


def remove_edge(graph, left, right):
    graph[left].remove(right)
    graph[right].remove(left)


def induced(graph, vertices):
    vertices = set(vertices)
    return {
        vertex: graph[vertex] & vertices
        for vertex in vertices
    }


def delete_vertices(graph, deleted):
    return induced(graph, set(graph) - set(deleted))


def components(graph, vertices=None):
    remaining = set(graph if vertices is None else vertices)
    answer = []
    while remaining:
        root = min(remaining)
        part = {root}
        stack = [root]
        remaining.remove(root)
        while stack:
            vertex = stack.pop()
            new = graph[vertex] & remaining
            remaining -= new
            part |= new
            stack.extend(new)
        answer.append(part)
    return answer


def connected(graph, vertices=None):
    vertices = set(graph if vertices is None else vertices)
    return not vertices or len(components(graph, vertices)) == 1


def vertex_connectivity_at_least(graph, k):
    vertices = sorted(graph)
    for order in range(k):
        for deleted in combinations(vertices, order):
            remainder = delete_vertices(graph, deleted)
            if len(remainder) > 1 and not connected(remainder):
                return False
    return True


def colourings(graph, number):
    order = sorted(graph, key=lambda vertex: (-len(graph[vertex]), vertex))
    colour = {}

    def rec(position):
        if position == len(order):
            yield dict(colour)
            return
        vertex = order[position]
        forbidden = {colour[other] for other in graph[vertex] if other in colour}
        for value in range(number):
            if value not in forbidden:
                colour[vertex] = value
                yield from rec(position + 1)
                del colour[vertex]

    yield from rec(0)


def is_colourable(graph, number):
    return next(colourings(graph, number), None) is not None


def is_vertex_critical(graph, chromatic_number):
    if is_colourable(graph, chromatic_number - 1):
        return False
    if not is_colourable(graph, chromatic_number):
        return False
    for vertex in graph:
        if not is_colourable(delete_vertices(graph, {vertex}), chromatic_number - 1):
            return False
    return True


def colouring_tuple(colouring, vertices):
    return tuple(colouring[vertex] for vertex in vertices)


def kempe_neighbours(graph, colouring, number):
    for first in range(number):
        for second in range(first + 1, number):
            allowed = {
                vertex for vertex in graph
                if colouring[vertex] in {first, second}
            }
            for part in components(graph, allowed):
                changed = dict(colouring)
                for vertex in part:
                    changed[vertex] = (
                        second if colouring[vertex] == first else first
                    )
                yield changed


def kempe_components(graph, all_colourings, number):
    vertices = sorted(graph)
    records = {
        colouring_tuple(colouring, vertices): colouring
        for colouring in all_colourings
    }
    remaining = set(records)
    answer = []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        part = {start}
        stack = [start]
        while stack:
            current = stack.pop()
            colouring = records[current]
            for changed in kempe_neighbours(graph, colouring, number):
                key = colouring_tuple(changed, vertices)
                assert key in records
                if key in remaining:
                    remaining.remove(key)
                    part.add(key)
                    stack.append(key)
        answer.append(part)
    return answer


def join_triangle(core):
    graph = copy_graph(core)
    triangle = (9, 10, 11)
    for vertex in triangle:
        graph[vertex] = set()
    for left, right in combinations(triangle, 2):
        add_edge(graph, left, right)
    for vertex in triangle:
        for core_vertex in range(9):
            add_edge(graph, vertex, core_vertex)
    return graph


def adjacent_sets(graph, left, right):
    return any(graph[vertex] & set(right) for vertex in left)


def verify_minor_model(graph, bags, required_pairs=None):
    assert all(bags)
    assert sum(map(len, bags)) == len(set().union(*map(set, bags)))
    assert all(connected(graph, bag) for bag in bags)
    if required_pairs is None:
        required_pairs = combinations(range(len(bags)), 2)
    assert all(adjacent_sets(graph, bags[i], bags[j]) for i, j in required_pairs)


def main():
    core = decode_graph6(GRAPH6)
    expected_edges = {
        frozenset(edge)
        for edge in (
            (0, 3), (0, 4), (0, 6), (0, 8),
            (1, 4), (1, 5), (1, 6), (1, 7),
            (2, 5), (2, 6), (2, 7), (2, 8),
            (3, 5), (3, 6), (3, 7),
            (4, 7), (4, 8), (5, 8),
        )
    }
    actual_edges = {
        frozenset((left, right))
        for left in core for right in core[left] if left < right
    }
    assert actual_edges == expected_edges
    assert vertex_connectivity_at_least(core, 4)
    assert not vertex_connectivity_at_least(core, 5)
    assert is_vertex_critical(core, 4)
    assert all(right in core[left] for left, right in ((V, A), (V, B), (A, B)))
    print("core graph6 HCpvbqk: 4-connected and 4-vertex-critical")

    common = copy_graph(core)
    for edge in DELETED:
        left, right = tuple(edge)
        remove_edge(common, left, right)
    all_three = list(colourings(common, 3))
    assert len(all_three) == 24
    assert all(
        (colouring[V] == colouring[A]) ^ (colouring[V] == colouring[B])
        for colouring in all_three
    )
    # Exact contraction traces for both deleted edges.
    for left, right in ((V, A), (V, B)):
        witnesses = [c for c in all_three if c[left] == c[right]]
        assert witnesses
        assert any(
            all(
                c[other] != c[left]
                for other in (core[left] | core[right]) - {left, right}
            )
            for c in witnesses
        )
    kempe = kempe_components(common, all_three, 3)
    assert sorted(map(len, kempe)) == [12, 12]
    vertices = sorted(common)
    signatures = []
    for part in kempe:
        kinds = set()
        for key in part:
            colouring = dict(zip(vertices, key))
            kinds.add((colouring[V] == colouring[A], colouring[V] == colouring[B]))
        signatures.append(kinds)
    assert set(map(frozenset, signatures)) == {
        frozenset({(True, False)}), frozenset({(False, True)})
    }
    print("common deletion: 24 three-colourings in two pure Kempe components of order 12")

    joined = join_triangle(core)
    assert vertex_connectivity_at_least(joined, 7)
    assert not vertex_connectivity_at_least(joined, 8)
    assert is_vertex_critical(joined, 7)
    print("joined host: 7-connected and 7-vertex-critical")

    joined_common = copy_graph(joined)
    for edge in DELETED:
        left, right = tuple(edge)
        remove_edge(joined_common, left, right)
    bags = [
        {9}, {10}, {11}, {0, 1, 2, 4, 5, 8}, {3}, {6}, {7}
    ]
    assert set().union(*bags) == set(joined_common)
    missing_pair = (5, 6)
    required = [
        (left, right)
        for left, right in combinations(range(7), 2)
        if (left, right) != missing_pair
    ]
    verify_minor_model(joined_common, bags, required)
    assert not adjacent_sets(joined_common, bags[5], bags[6])
    # The same model survives deletion of both incident edges at once.
    assert 5 in joined_common[3]
    assert {1, 2} & joined_common[6]
    assert A in joined[B]
    print("spanning labelled K7-minus-edge model: verified")

    separator = {9, 10, 11, 3, 4, 6, 8}
    assert joined[V] == separator
    sides = components(delete_vertices(joined, separator))
    assert {V} in sides and any(part != {V} for part in sides)
    k7_bags = [{9}, {10}, {11}, {0}, {3}, {6}, {1, 4, 5}]
    verify_minor_model(joined, k7_bags)
    print("actual order-seven separator and explicit K7 model: verified")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
