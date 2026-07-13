"""Search robust Fabila-Monroy--Wood packet-crosslink templates.

The packet carriers are represented by private degree-two vertices.  A
template consists of a cycle using the two carriers of one packet and an
opposite linkage using the two carriers of a second packet.  Any
intersections between the two packet systems are harmless by FMW Lemma 7;
only the two paths within the second packet must remain disjoint.
"""

from __future__ import annotations

from itertools import combinations

import networkx as nx


MISSING = {(0, 2), (0, 3), (0, 5), (1, 2), (1, 5), (2, 4), (4, 5)}
MODE_A = ((0, 3), (1, 2), (4, 5))
MODE_B = ((0, 3), (1, 5), (2, 4))


def boundary() -> nx.Graph:
    graph = nx.complete_graph(7)
    graph.remove_edges_from(MISSING)
    return graph


def packet_graph(graph: nx.Graph, packet: tuple[tuple[int, int], tuple[int, int]], prefix: str) -> nx.Graph:
    answer = graph.copy()
    for index, (left, right) in enumerate(packet):
        node = f"{prefix}{index}"
        answer.add_edges_from(((left, node), (node, right)))
    return answer


def canonical_cycle_order(cycle: list[object], roots: set[int]) -> tuple[int, ...]:
    order = tuple(vertex for vertex in cycle if vertex in roots)
    assert len(order) == 4
    return order


def connected_partition(graph: nx.Graph, remaining: set[int], roots: tuple[int, ...]):
    first = min(remaining)
    for size in range(1, len(remaining)):
        for raw in combinations(remaining, size):
            left = set(raw)
            right = remaining - left
            if first not in left:
                continue
            if not nx.is_connected(graph.subgraph(left)) or not nx.is_connected(graph.subgraph(right)):
                continue
            if not any(graph.has_edge(x, y) for x in left for y in right):
                continue
            if not all(
                any(graph.has_edge(root, x) for x in left)
                and any(graph.has_edge(root, y) for y in right)
                for root in roots
            ):
                continue
            yield tuple(sorted(left)), tuple(sorted(right))


def search(packet_a, packet_b):
    graph = boundary()
    augmented_a = packet_graph(graph, packet_a, "A")
    roots = set(packet_a[0] + packet_a[1])
    cycles = []
    for cycle in nx.simple_cycles(augmented_a.to_directed(), length_bound=10):
        if len(cycle) < 4 or "A0" not in cycle or "A1" not in cycle:
            continue
        if set(vertex for vertex in cycle if isinstance(vertex, int)) & roots != roots:
            continue
        # Directed enumeration duplicates undirected cycles; simplicity is all we need.
        if len(set(cycle)) != len(cycle):
            continue
        order = canonical_cycle_order(cycle, roots)
        if order not in [item[1] for item in cycles]:
            cycles.append((cycle, order))

    augmented_b = packet_graph(graph, packet_b, "B")
    for cycle, order in cycles:
        for rotation in range(4):
            cyclic = order[rotation:] + order[:rotation]
            for reversed_order in (cyclic, (cyclic[0], cyclic[3], cyclic[2], cyclic[1])):
                opposite = ((reversed_order[0], reversed_order[2]), (reversed_order[1], reversed_order[3]))
                for assignment in (packet_b, packet_b[::-1]):
                    candidates = []
                    for (source, target), demand in zip(opposite, assignment):
                        carrier = "B0" if demand == packet_b[0] else "B1"
                        candidates.append([
                            path
                            for path in nx.all_simple_paths(augmented_b, source, target, cutoff=9)
                            if carrier in path
                            and ("B1" if carrier == "B0" else "B0") not in path
                        ])
                    for first in candidates[0]:
                        for second in candidates[1]:
                            if set(first) & set(second):
                                continue
                            used = {
                                vertex
                                for vertex in cycle + first + second
                                if isinstance(vertex, int)
                            }
                            remaining = set(range(7)) - used
                            if len(remaining) < 2:
                                continue
                            for left, right in connected_partition(graph, remaining, reversed_order):
                                return {
                                    "cycle": cycle,
                                    "order": reversed_order,
                                    "linkage": (first, second),
                                    "reserve": (left, right),
                                }
    return None


def main() -> None:
    for packet_a in combinations(MODE_A, 2):
        for packet_b in combinations(MODE_B, 2):
            result = search(packet_a, packet_b)
            print(packet_a, packet_b, result)


if __name__ == "__main__":
    main()
