#!/usr/bin/env python3
"""Search small 4-connected planar quotients for a 5-chromatic edge split."""

from itertools import product

import networkx as nx


def k_colorable(graph, k):
    vertices = sorted(graph, key=lambda v: graph.degree(v), reverse=True)
    colour = {}

    def search(i):
        if i == len(vertices):
            return True
        # DSATUR-style dynamic choice among uncoloured vertices.
        uncoloured = vertices[i:]
        v = max(uncoloured,
                key=lambda x: (len({colour[y] for y in graph[x]
                                    if y in colour}), graph.degree(x)))
        j = vertices.index(v, i)
        vertices[i], vertices[j] = vertices[j], vertices[i]
        forbidden = {colour[y] for y in graph[v] if y in colour}
        for c in range(k):
            if c not in forbidden:
                colour[v] = c
                if search(i + 1):
                    return True
                del colour[v]
        vertices[i], vertices[j] = vertices[j], vertices[i]
        return False

    return search(0)


def split_vertex(graph, d, states):
    out = graph.copy()
    nbrs = list(graph[d])
    out.remove_node(d)
    u = max(graph.nodes) + 1
    v = u + 1
    out.add_edge(u, v)
    for x, state in zip(nbrs, states):
        if state in (0, 2):
            out.add_edge(u, x)
        if state in (1, 2):
            out.add_edge(v, x)
    return out, u, v


def main():
    quotients = []
    for q in nx.graph_atlas_g():
        if len(q) < 5 or not nx.is_connected(q):
            continue
        if nx.node_connectivity(q) < 4 or not nx.check_planarity(q)[0]:
            continue
        quotients.append(q)

    # The atlas stops at seven vertices.  Add the first natural
    # four-connected nontriangulated candidates: the square antiprism and
    # every one-edge deletion of the icosahedron.
    anti = nx.Graph()
    anti.add_nodes_from(range(8))
    for i in range(4):
        anti.add_edge(i, (i + 1) % 4)
        anti.add_edge(4 + i, 4 + (i + 1) % 4)
        anti.add_edge(i, 4 + i)
        anti.add_edge(i, 4 + ((i - 1) % 4))
    if nx.node_connectivity(anti) >= 4 and nx.check_planarity(anti)[0]:
        quotients.append(anti)

    ico = nx.icosahedral_graph()
    for edge in list(ico.edges()):
        q = ico.copy()
        q.remove_edge(*edge)
        if nx.node_connectivity(q) >= 4 and nx.check_planarity(q)[0]:
            quotients.append(q)

    tested = 0
    survivors = []
    for q in quotients:
        planar, embedding = nx.check_planarity(q)
        seen_darts = set()
        faces = []
        for a, b in embedding.edges():
            if (a, b) in seen_darts:
                continue
            face = embedding.traverse_face(a, b, seen_darts)
            faces.append(face)
        for d in q:
            long_faces = [face for face in faces if d in face and len(face) >= 4]
            if not long_faces:
                continue
            degree = q.degree(d)
            for states in product(range(3), repeat=degree):
                # Both split ends must retain an old neighbour.
                if all(s == 1 for s in states) or all(s == 0 for s in states):
                    continue
                j, u, v = split_vertex(q, d, states)
                tested += 1
                if nx.node_connectivity(j) < 4:
                    continue
                if k_colorable(j, 4):
                    continue
                # In a seven-connected triangle extension, every core
                # degree-four vertex is complete to T.  The distributed
                # residue permits only the three other cofacial roots to
                # have that status.
                admissible_faces = []
                for face in long_faces:
                    roots = set(face) - {d}
                    if len(roots) < 3:
                        continue
                    low = {x for x in j if j.degree(x) == 4}
                    if low <= roots:
                        admissible_faces.append(face)
                if not admissible_faces:
                    continue
                survivors.append((q, d, states, j, u, v))
                print("FOUND quotient", nx.to_graph6_bytes(q, header=False).strip(),
                      "split", d, states,
                      "expanded", nx.to_graph6_bytes(j, header=False).strip())
                print("root face", admissible_faces[0])
                print("Q edges", sorted(q.edges()))
                print("J edges", sorted(j.edges()))
                return
    print("tested", tested, "splits over", len(quotients),
          "atlas quotients; no 5-chromatic 4-connected expansion")


if __name__ == "__main__":
    main()
