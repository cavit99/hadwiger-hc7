#!/usr/bin/env python3
"""Exhaustively verify the seven-boundary pair-bicycle completion.

The graph atlas supplies every unlabelled graph on seven vertices.  For
each triangle-free graph, enumerate all 3^7 assignments of the pair lists
12, 13, 23.  Whenever every colour has support at least four and the list
instance is uncolourable, verify an anchored K4 in the literal auxiliary
graph consisting of the boundary plus the carrier triangle.
"""

from __future__ import annotations

from itertools import combinations, product

import networkx as nx


PAIR_LISTS = (0b011, 0b101, 0b110)


def triangle_free(graph: nx.Graph) -> bool:
    return not any(nx.triangles(graph).values())


def colourable(graph: nx.Graph, lists: tuple[int, ...]) -> bool:
    order = sorted(graph, key=lambda v: (-graph.degree[v], lists[v]))
    colour: dict[int, int] = {}

    def extend(position: int) -> bool:
        if position == len(order):
            return True
        vertex = order[position]
        forbidden = {
            colour[neighbour]
            for neighbour in graph[vertex]
            if neighbour in colour
        }
        for candidate in range(3):
            if lists[vertex] & (1 << candidate) and candidate not in forbidden:
                colour[vertex] = candidate
                if extend(position + 1):
                    return True
                del colour[vertex]
        return False

    return extend(0)


def anchored_k4(graph: nx.Graph, lists: tuple[int, ...]) -> bool:
    """Find four bags, one chosen boundary root per bag, using carriers only."""

    def adjacent(left: tuple[str, int], right: tuple[str, int]) -> bool:
        if left[0] == right[0] == "c":
            return left != right
        if left[0] == right[0] == "s":
            return graph.has_edge(left[1], right[1])
        if left[0] == "c":
            left, right = right, left
        return bool(lists[left[1]] & (1 << right[1]))

    def connected(bag: list[tuple[str, int]]) -> bool:
        seen = {bag[0]}
        stack = [bag[0]]
        while stack:
            vertex = stack.pop()
            for neighbour in bag:
                if neighbour not in seen and adjacent(vertex, neighbour):
                    seen.add(neighbour)
                    stack.append(neighbour)
        return len(seen) == len(bag)

    for roots in combinations(range(7), 4):
        # Each carrier goes into one of the four bags, or is unused (index 4).
        for assignment in product(range(5), repeat=3):
            bags = [[("s", roots[index])] for index in range(4)]
            for carrier, bag_index in enumerate(assignment):
                if bag_index < 4:
                    bags[bag_index].append(("c", carrier))
            if not all(connected(bag) for bag in bags):
                continue
            if all(
                any(adjacent(x, y) for x in bags[a] for y in bags[b])
                for a, b in combinations(range(4), 2)
            ):
                return True
    return False


def verify_template_bags() -> None:
    templates = {
        "T2": ("01 03 05 12 23 34 45", (3, 5, 6, 3, 5, 6), ((0, 1, 2), (1, 0), (2,), (3,))),
        "T4": ("01 05 16 23 26 34 46 56", (3, 5, 3, 5, 6, 6, 6), ((0, 0), (1, 1, 2), (2,), (3,))),
        "T5": ("01 04 12 23 25 36 45 56", (3, 3, 5, 6, 5, 5, 3), ((0, 0, 2), (1, 1), (2,), (3,))),
        "T6": ("01 05 06 12 23 34 36 45", (3, 5, 5, 3, 6, 6, 3), ((0, 0), (1, 1, 2), (2,), (3,))),
        "T10a": ("01 05 06 12 23 26 34 45 46", (3, 5, 6, 3, 5, 6, 3), ((0, 1, 2), (1, 0), (2,), (3,))),
        "T10b": ("01 05 06 12 23 26 34 45 46", (3, 5, 6, 3, 5, 6, 5), ((0, 1, 2), (1, 0), (2,), (3,))),
        "T10c": ("01 05 06 12 23 26 34 45 46", (3, 5, 6, 3, 5, 6, 6), ((0, 1, 2), (1, 0), (2,), (3,))),
    }
    for name, (edge_text, lists, encoded_bags) in templates.items():
        graph = nx.Graph()
        graph.add_nodes_from(range(len(lists)))
        graph.add_edges_from((int(edge[0]), int(edge[1])) for edge in edge_text.split())
        assert anchored_k4(graph, lists), name

        # Pin the exact bags printed in the theorem.  The first integer in
        # each tuple is its boundary root; later integers are zero-based
        # carrier indices.
        bags = [
            [("s", encoded[0]), *(("c", carrier) for carrier in encoded[1:])]
            for encoded in encoded_bags
        ]

        def adjacent(left: tuple[str, int], right: tuple[str, int]) -> bool:
            if left[0] == right[0] == "c":
                return left != right
            if left[0] == right[0] == "s":
                return graph.has_edge(left[1], right[1])
            if left[0] == "c":
                left, right = right, left
            return bool(lists[left[1]] & (1 << right[1]))

        for bag in bags:
            auxiliary = nx.Graph()
            auxiliary.add_nodes_from(bag)
            auxiliary.add_edges_from(
                (x, y) for x, y in combinations(bag, 2) if adjacent(x, y)
            )
            assert nx.is_connected(auxiliary), (name, bag)
        assert all(
            any(adjacent(x, y) for x in bags[a] for y in bags[b])
            for a, b in combinations(range(4), 2)
        ), name


def verify_full_list_refinements() -> None:
    templates = {
        "T7": (3, 5, 3, 3, 6, 7, 3),
        "T8": (7, 3, 3, 3, 3, 5, 5),
        "T9": (7, 7, 3, 3, 3, 3, 3),
        "T10": (3, 5, 6, 3, 5, 6, 7),
    }
    surviving: dict[str, int] = {}
    for name, template in templates.items():
        full_vertices = [v for v, mask in enumerate(template) if mask == 7]
        count = 0
        for replacements in product(PAIR_LISTS, repeat=len(full_vertices)):
            refined = list(template)
            for vertex, mask in zip(full_vertices, replacements, strict=True):
                refined[vertex] = mask
            if all(
                sum(bool(mask & (1 << colour)) for mask in refined) >= 4
                for colour in range(3)
            ):
                count += 1
        surviving[name] = count
    assert surviving == {"T7": 0, "T8": 0, "T9": 0, "T10": 3}, surviving


def main() -> None:
    graph_count = 0
    supported_assignments = 0
    uncolourable_assignments = 0
    for graph in nx.graph_atlas_g():
        if len(graph) != 7 or not triangle_free(graph):
            continue
        graph_count += 1
        for lists in product(PAIR_LISTS, repeat=7):
            if any(
                sum(bool(mask & (1 << colour)) for mask in lists) < 4
                for colour in range(3)
            ):
                continue
            supported_assignments += 1
            if colourable(graph, lists):
                continue
            uncolourable_assignments += 1
            assert anchored_k4(graph, lists), (
                nx.to_graph6_bytes(graph, header=False).strip(),
                lists,
            )

    verify_template_bags()
    verify_full_list_refinements()
    assert graph_count == 107, graph_count
    print("VERIFIED")
    print(f"triangle_free_graphs={graph_count}")
    print(f"support_ge_4_pair_assignments={supported_assignments}")
    print(f"uncolourable_assignments={uncolourable_assignments}")
    print("all_uncolourable_assignments_have_anchored_K4=True")
    print("template_rows_checked=7")
    print("full_list_refinements=T7:0,T8:0,T9:0,T10:3")


if __name__ == "__main__":
    main()
