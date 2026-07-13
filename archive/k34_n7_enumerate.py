"""Finite discovery enumeration for the sparse |C|=7 K3+K4 cell.

This is a search aid, not a mathematical proof.  It enumerates unlabelled
12/13-edge graphs C and row-symmetric A/B incidence systems in the two
sparse density cells.  It tests single-A helper pairs first, then Dirac's
degree-seven neighbourhood condition and seven-connectivity on failures.
"""

from collections import defaultdict
from itertools import combinations, combinations_with_replacement

import networkx as nx


U = tuple(range(7))
USET = frozenset(U)
SETS3 = tuple(frozenset(x) for x in combinations(U, 3))
SETS4 = tuple(frozenset(x) for x in combinations(U, 4))
SETS5 = tuple(frozenset(x) for x in combinations(U, 5))


def sums(rows):
    return tuple(sum(x in row for row in rows) for x in U)


def row_systems(row_types):
    """Generate row-multisets, preserving blocks of unequal row sizes."""
    if row_types == (3, 3, 3, 3):
        for ids in combinations_with_replacement(range(len(SETS3)), 4):
            yield tuple(SETS3[i] for i in ids)
    elif row_types == (4, 4, 4):
        for ids in combinations_with_replacement(range(len(SETS4)), 3):
            yield tuple(SETS4[i] for i in ids)
    elif row_types == (5, 4, 4):
        for big in SETS5:
            for ids in combinations_with_replacement(range(len(SETS4)), 2):
                yield (big, SETS4[ids[0]], SETS4[ids[1]])
    elif row_types == (4, 3, 3, 3):
        for big in SETS4:
            for ids in combinations_with_replacement(range(len(SETS3)), 3):
                yield (big,) + tuple(SETS3[i] for i in ids)
    else:
        raise ValueError(row_types)


def helper_pair(graph, components, a_rows, b_rows):
    candidates = []
    for mask in range(1, 1 << 7):
        part = frozenset(x for x in U if (mask >> x) & 1)
        if not all(part & row for row in b_rows):
            continue
        roots = {
            i
            for i, row in enumerate(a_rows)
            if all(component & row for component in components[part])
        }
        if roots:
            candidates.append((part, roots))
    for i, (first, roots1) in enumerate(candidates):
        for second, roots2 in candidates[i + 1 :]:
            if first & second:
                continue
            if any(x != y for x in roots1 for y in roots2):
                return first, second
    return None


def host(graph, a_rows, b_rows):
    g = nx.Graph()
    g.add_nodes_from(range(16))
    # C=0..6, A=7..9, B=10..13, v=14; node 15 is not used.
    g.remove_node(15)
    g.add_edges_from(graph.edges())
    g.add_edges_from(combinations(range(7, 10), 2))
    g.add_edges_from(combinations(range(10, 14), 2))
    g.add_edges_from((14, x) for x in range(7, 14))
    for i, row in enumerate(a_rows, 7):
        g.add_edges_from((i, x) for x in row)
    for i, row in enumerate(b_rows, 10):
        g.add_edges_from((i, x) for x in row)
    return g


def dirac_ok(g):
    for x in g:
        if g.degree(x) != 7:
            continue
        neighbours = tuple(g[x])
        for triple in combinations(neighbours, 3):
            if g.subgraph(triple).number_of_edges() == 0:
                return False
    return True


def dirac_c_ok(graph, a_rows, b_rows):
    """Fast necessary Dirac check on the six/seven degree-seven C vertices."""
    adjacency = [0] * 14
    for x, y in graph.edges():
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    for x, y in combinations(range(7, 10), 2):
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    for x, y in combinations(range(10, 14), 2):
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    for i, row in enumerate(a_rows, 7):
        for x in row:
            adjacency[i] |= 1 << x
            adjacency[x] |= 1 << i
    for i, row in enumerate(b_rows, 10):
        for x in row:
            adjacency[i] |= 1 << x
            adjacency[x] |= 1 << i
    for x in U:
        if adjacency[x].bit_count() != 7:
            continue
        neighbours = [y for y in range(14) if (adjacency[x] >> y) & 1]
        for y, z, w in combinations(neighbours, 3):
            if not (
                ((adjacency[y] >> z) & 1)
                or ((adjacency[y] >> w) & 1)
                or ((adjacency[z] >> w) & 1)
            ):
                return False
    return True


def main():
    b3333 = defaultdict(list)
    for rows in row_systems((3, 3, 3, 3)):
        b3333[sums(rows)].append(rows)
    b4333 = defaultdict(list)
    for rows in row_systems((4, 3, 3, 3)):
        b4333[sums(rows)].append(rows)
    a_systems = {
        pattern: [(rows, sums(rows)) for rows in row_systems(pattern)]
        for pattern in ((4, 4, 4), (5, 4, 4))
    }

    c_graphs = {
        q: [
            nx.convert_node_labels_to_integers(g)
            for g in nx.graph_atlas_g()
            if len(g) == 7 and g.number_of_edges() == q and nx.is_connected(g)
        ]
        for q in (12, 13)
    }
    print("C counts", {q: len(gs) for q, gs in c_graphs.items()}, flush=True)

    totals = defaultdict(int)
    examples = {}
    for p, q in ((24, 13), (25, 12)):
        for graph in c_graphs[q]:
            components = {}
            for mask in range(1, 1 << 7):
                part = frozenset(x for x in U if (mask >> x) & 1)
                components[part] = tuple(
                    frozenset(c) for c in nx.connected_components(graph.subgraph(part))
                )
            degree_c = tuple(graph.degree(x) for x in U)
            patterns = [((4, 4, 4), b3333, None)] if p == 24 else [
                ((5, 4, 4), b3333, None),
                ((4, 4, 4), b4333, None),
            ]
            high_vertices = U if p == 24 else (None,)
            for high in high_vertices:
                target = tuple(
                    7 + (1 if p == 24 and x == high else 0) - degree_c[x]
                    for x in U
                )
                if min(target) < 0:
                    continue
                for a_pattern, b_index, _ in patterns:
                    for a_rows, a_sums in a_systems[a_pattern]:
                        residual = tuple(target[x] - a_sums[x] for x in U)
                        if min(residual) < 0:
                            continue
                        for b_rows in b_index.get(residual, ()):
                            totals[p, "feasible"] += 1
                            if not dirac_c_ok(graph, a_rows, b_rows):
                                totals[p, "dirac_fail"] += 1
                                continue
                            totals[p, "dirac"] += 1
                            if helper_pair(graph, components, a_rows, b_rows):
                                totals[p, "dirac_helper"] += 1
                                continue
                            totals[p, "dirac_nohelper"] += 1
                            g = host(graph, a_rows, b_rows)
                            if not dirac_ok(g):
                                totals[p, "dirac_boundary_fail"] += 1
                                continue
                            connectivity = nx.node_connectivity(g)
                            if connectivity < 7:
                                totals[p, "dirac_nohelper_kfail"] += 1
                                continue
                            totals[p, "obstruction"] += 1
                            examples[p] = {
                                "C": nx.to_graph6_bytes(graph, header=False).decode().strip(),
                                "A": [sorted(x) for x in a_rows],
                                "B": [sorted(x) for x in b_rows],
                                "degrees": dict(g.degree()),
                                "connectivity": connectivity,
                                "edges": sorted(g.edges()),
                            }
                            print("OBSTRUCTION", p, examples[p], flush=True)
                            return
        print("case", p, dict((k[1], v) for k, v in totals.items() if k[0] == p), flush=True)
    print("totals", dict(totals), flush=True)


if __name__ == "__main__":
    main()
