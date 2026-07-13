"""Enumerate the degree-7 local helper minor obstruction.

For every unlabeled seven-vertex graph F in NetworkX's graph atlas with
omega(F) <= 2, put N = complement(F).  Thus alpha(N) <= 2.  Add m
independent helper vertices, each complete to N, and test whether the
resulting graph has a K6 model every branch set of which meets N.

This is a finite discovery/audit script, not a substitute for a hand proof.
"""

from itertools import combinations

import networkx as nx


def partitions(sequence, parts):
    """Canonical unlabeled partitions of sequence into exactly parts blocks."""
    blocks = []

    def rec(position):
        if position == len(sequence):
            if len(blocks) == parts:
                yield tuple(frozenset(block) for block in blocks)
            return
        remaining = len(sequence) - position
        if len(blocks) + remaining < parts:
            return
        vertex = sequence[position]
        for block in blocks:
            block.add(vertex)
            yield from rec(position + 1)
            block.remove(vertex)
        if len(blocks) < parts:
            blocks.append({vertex})
            yield from rec(position + 1)
            blocks.pop()

    yield from rec(0)


def connected(graph, block):
    return len(block) == 1 or nx.is_connected(graph.subgraph(block))


def adjacent(graph, first, second):
    return any(graph.has_edge(x, y) for x in first for y in second)


def has_n_meeting_k6(graph, neighborhood):
    vertices = tuple(graph.nodes())
    for size in range(6, len(vertices) + 1):
        for support in combinations(vertices, size):
            for model in partitions(support, 6):
                if not all(block & neighborhood for block in model):
                    continue
                if not all(connected(graph, block) for block in model):
                    continue
                if all(
                    adjacent(graph, model[i], model[j])
                    for i in range(6)
                    for j in range(i)
                ):
                    return True, model
    return False, None


def clique_number(graph):
    return max((len(clique) for clique in nx.find_cliques(graph)), default=0)


def main():
    seven_vertex_graphs = [
        graph for graph in nx.graph_atlas_g() if graph.number_of_nodes() == 7
    ]
    complements = [graph for graph in seven_vertex_graphs if clique_number(graph) <= 2]
    print("triangle_free_complements", len(complements))
    for helpers in (1, 2, 3):
        obstructions = []
        for complement in complements:
            complement = nx.convert_node_labels_to_integers(complement)
            neighborhood_graph = nx.complement(complement)
            local = neighborhood_graph.copy()
            neighborhood = frozenset(range(7))
            for index in range(helpers):
                helper = 7 + index
                local.add_node(helper)
                local.add_edges_from((helper, vertex) for vertex in neighborhood)
            exists, _ = has_n_meeting_k6(local, neighborhood)
            if not exists:
                code = nx.to_graph6_bytes(complement, header=False).decode().strip()
                obstructions.append(code)
        print("helpers", helpers, "obstructions", len(obstructions), obstructions)


if __name__ == "__main__":
    main()
