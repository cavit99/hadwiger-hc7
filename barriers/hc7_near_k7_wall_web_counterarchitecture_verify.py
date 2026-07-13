#!/usr/bin/env python3
"""Verify finite members of the non-universal near-K7 wall web.

Run with

    PYTHONPATH=active/runtime/deps python3 \
        barriers/hc7_near_k7_wall_web_counterarchitecture_verify.py

The mathematical note explains why every returned graph is K7-minor-free:
it is a subgraph of K2 join P for a planar graph P.  This script checks the
less transparent assertions (connectivity, the one-complex normalization,
portal multiplicities/properness, and the neutral-row load cap).
"""

from __future__ import annotations

import itertools

import networkx as nx


def geodesic_icosahedron(frequency: int) -> nx.Graph:
    """Return the frequency-f triangular subdivision of the icosahedron."""
    ico = nx.icosahedral_graph()
    faces = [
        tuple(clique)
        for clique in nx.enumerate_all_cliques(ico)
        if len(clique) == 3
    ]
    graph = nx.Graph()

    for i, j, k in faces:
        points: dict[tuple[int, int, int], tuple[tuple[int, int], ...]] = {}
        for a in range(frequency + 1):
            for b in range(frequency + 1 - a):
                c = frequency - a - b
                key = tuple(
                    sorted(
                        (vertex, weight)
                        for vertex, weight in ((i, a), (j, b), (k, c))
                        if weight
                    )
                )
                points[(a, b, c)] = key
                graph.add_node(key)

        for coordinate, vertex in points.items():
            for source in range(3):
                for target in range(3):
                    if source == target or coordinate[source] == 0:
                        continue
                    neighbour_coordinate = list(coordinate)
                    neighbour_coordinate[source] -= 1
                    neighbour_coordinate[target] += 1
                    neighbour = points[tuple(neighbour_coordinate)]
                    graph.add_edge(vertex, neighbour)

    return graph


def find_member(frequency: int) -> dict[str, object] | None:
    planar_core = geodesic_icosahedron(frequency)

    for q3, q4 in planar_core.edges():
        if planar_core.degree(q3) != 6 or planar_core.degree(q4) != 6:
            continue
        common = list(nx.common_neighbors(planar_core, q3, q4))
        if len(common) != 2:
            continue
        a, c = common
        if planar_core.has_edge(a, c):
            continue

        singleton_core = {a, c, q3, q4}
        bag = planar_core.copy()
        bag.remove_nodes_from(singleton_core)
        if nx.node_connectivity(bag) < 3:
            continue

        # u is made nonuniversal precisely on the other neighbours of q3,q4.
        u_holes = (
            set(planar_core.neighbors(q3))
            | set(planar_core.neighbors(q4))
        ) - singleton_core
        if len(u_holes) < 2 or any(planar_core.degree(x) < 6 for x in u_holes):
            continue

        forbidden = singleton_core | u_holes
        candidates = [
            x
            for x in bag
            if x not in forbidden and planar_core.degree(x) >= 6
        ]
        for y1, y2 in itertools.combinations(candidates, 2):
            v_holes = {y1, y2}
            graph = planar_core.copy()
            u = ("u",)
            v = ("v",)
            graph.add_edge(u, v)
            graph.add_edges_from((u, x) for x in planar_core if x not in u_holes)
            graph.add_edges_from((v, x) for x in planar_core if x not in v_holes)
            if nx.node_connectivity(graph) < 7:
                continue

            rows = {
                "F": set(planar_core.neighbors(a)) - singleton_core,
                "C": set(planar_core.neighbors(c)) - singleton_core,
                "Q1": set(bag) - u_holes,
                "Q2": set(bag) - v_holes,
                "Q3": set(planar_core.neighbors(q3)) - singleton_core,
                "Q4": set(planar_core.neighbors(q4)) - singleton_core,
            }
            if len(rows["F"]) < 3 or len(rows["C"]) < 3:
                continue
            if rows["F"] & rows["C"]:
                continue
            if any(
                len(rows[name]) < 2 or len(set(bag) - rows[name]) < 2
                for name in ("Q1", "Q2", "Q3", "Q4")
            ):
                continue
            neutral_load = max(
                sum(x in rows[name] for name in ("Q1", "Q2", "Q3", "Q4"))
                for x in bag
            )
            if neutral_load > 2:
                continue

            return {
                "P": planar_core,
                "G": graph,
                "B": bag,
                "a": a,
                "c": c,
                "q3": q3,
                "q4": q4,
                "u_holes": u_holes,
                "v_holes": v_holes,
                "rows": rows,
                "neutral_load": neutral_load,
            }
    return None


def main() -> None:
    for frequency in (3, 4, 5):
        member = find_member(frequency)
        assert member is not None
        planar_core = member["P"]
        graph = member["G"]
        bag = member["B"]
        rows = member["rows"]
        planar, _ = nx.check_planarity(planar_core)
        assert planar
        print(
            {
                "frequency": frequency,
                "|P|": len(planar_core),
                "tw_lower_bound_scale": frequency,
                "kappa(P)": nx.node_connectivity(planar_core),
                "kappa(B)": nx.node_connectivity(bag),
                "kappa(G)": nx.node_connectivity(graph),
                "row_sizes": {name: len(row) for name, row in rows.items()},
                "u_holes": len(member["u_holes"]),
                "v_holes": len(member["v_holes"]),
                "max_neutral_load": member["neutral_load"],
            }
        )


if __name__ == "__main__":
    main()
