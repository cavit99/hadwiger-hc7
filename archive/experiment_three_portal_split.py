"""Enumerate minimal three-pair connected-cut obstructions on small 2-connected graphs."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

import networkx as nx


def connected_cuts(graph: nx.Graph) -> list[int]:
    """Return one bit mask for each unordered connected bipartition."""
    n = graph.number_of_nodes()
    vertices = list(range(n))
    cuts: list[int] = []
    # Require vertex 0 on the first shore to quotient by complementation.
    for mask in range(1, 1 << n):
        if not (mask & 1) or mask == (1 << n) - 1:
            continue
        left = [v for v in vertices if mask & (1 << v)]
        right = [v for v in vertices if not mask & (1 << v)]
        if nx.is_connected(graph.subgraph(left)) and nx.is_connected(graph.subgraph(right)):
            cuts.append(mask)
    return cuts


def demand_type(edges: tuple[tuple[int, int], ...]) -> str:
    demand = nx.Graph()
    demand.add_edges_from(edges)
    degrees = sorted(dict(demand.degree()).values(), reverse=True)
    if not nx.is_bipartite(demand):
        return "nonbipartite"
    return f"bipartite:{degrees}:c{nx.number_connected_components(demand)}"


def list_colourable(graph: nx.Graph, portals: tuple[int, int, int], selected: int | None) -> bool:
    """Test the maximally foot-restricted contraction lists."""
    n = graph.number_of_nodes()
    lists: list[set[int]] = []
    for vertex in range(n):
        allowed = {3}  # contraction colour alpha
        for colour, portal in enumerate(portals):
            if not (portal & (1 << vertex)):
                allowed.add(colour)
        if selected is not None and not (portals[selected] & (1 << vertex)):
            allowed.discard(selected)
        lists.append(allowed)

    colours = [-1] * n

    def search(left: set[int]) -> bool:
        if not left:
            return True
        vertex = min(
            left,
            key=lambda x: len(lists[x] - {colours[y] for y in graph[x] if colours[y] >= 0}),
        )
        forbidden = {colours[y] for y in graph[vertex] if colours[y] >= 0}
        for colour in lists[vertex] - forbidden:
            colours[vertex] = colour
            if search(left - {vertex}):
                return True
        colours[vertex] = -1
        return False

    return search(set(range(n)))


def portal_triple_search(max_order: int = 6) -> None:
    """Seek a no-split three-class society with an uncolourable exact list state."""
    checked = 0
    obstructions = 0
    for raw in nx.graph_atlas_g():
        n = raw.number_of_nodes()
        if n < 3 or n > max_order or not nx.is_biconnected(raw):
            continue
        graph = nx.convert_node_labels_to_integers(raw)
        cuts = connected_cuts(graph)
        full = (1 << n) - 1
        subsets = [mask for mask in range(1, full) if mask.bit_count() >= 2]
        split_cuts = {
            mask: {
                cut
                for cut in cuts
                if (mask & cut) and (mask & (full ^ cut))
            }
            for mask in subsets
        }
        for portals in combinations(subsets, 3):
            checked += 1
            if split_cuts[portals[0]] & split_cuts[portals[1]] & split_cuts[portals[2]]:
                continue
            obstructions += 1
            host = graph.copy()
            host.add_nodes_from(range(n, n + 3))
            host.add_edges_from(combinations(range(n, n + 3), 2))
            for colour, portal in enumerate(portals):
                host.add_edges_from((n + colour, vertex) for vertex in range(n) if portal & (1 << vertex))
            if nx.node_connectivity(host) < 4:
                continue
            for selected in (None, 0, 1, 2):
                if not list_colourable(graph, portals, selected):
                    print(
                        "UNCOLOURABLE THREE-CLASS OBSTRUCTION",
                        "n=", n,
                        "G=", sorted(graph.edges()),
                        "portals=", portals,
                        "selected=", selected,
                    )
                    return
    print("three-class search: no uncolourable obstruction", "checked=", checked, "no-split=", obstructions)


def main() -> None:
    counts: Counter[str] = Counter()
    examples: dict[str, tuple[nx.Graph, tuple[tuple[int, int], ...]]] = {}
    by_order: defaultdict[int, Counter[str]] = defaultdict(Counter)

    for raw in nx.graph_atlas_g():
        n = raw.number_of_nodes()
        if n < 3 or n > 7 or not nx.is_biconnected(raw):
            continue
        graph = nx.convert_node_labels_to_integers(raw)
        cuts = connected_cuts(graph)
        pairs = list(combinations(range(n), 2))
        crossed = {
            pair: {mask for mask in cuts if bool(mask & (1 << pair[0])) != bool(mask & (1 << pair[1]))}
            for pair in pairs
        }
        for triple in combinations(pairs, 3):
            if crossed[triple[0]] & crossed[triple[1]] & crossed[triple[2]]:
                continue
            kind = demand_type(triple)
            counts[kind] += 1
            by_order[n][kind] += 1
            examples.setdefault(kind, (graph.copy(), triple))

    print("obstruction demand types")
    for kind, count in counts.most_common():
        graph, triple = examples[kind]
        print(kind, count, "n=", graph.number_of_nodes(), "G=", sorted(graph.edges()), "pairs=", triple)
    print("by order")
    for n in sorted(by_order):
        print(n, dict(by_order[n]))
    portal_triple_search()


if __name__ == "__main__":
    main()
