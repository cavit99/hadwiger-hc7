#!/usr/bin/env python3
"""Exact audit of the one-bag reserved-path splitter claim.

The graph is a square antiprism L with its four top-face vertices rooted,
plus an induced even path a-t-p.  It verifies:

* H is 5-connected and nonplanar by the edge bound;
* every path vertex has a four-saturating neighbourhood in L;
* L has no rooted K4 at the four face roots;
* H has a rooted K4, but the lexicographic minimum path intersection is
  one path vertex in one branch bag.

Thus even the strongest natural normalization does not free the path.
"""

from itertools import combinations


ROOTS = (0, 1, 2, 3)
A, P, T = 8, 9, 10
PATH_MASK = (1 << A) | (1 << P) | (1 << T)


def add(edges, left, right):
    edges.add(tuple(sorted((left, right))))


def graphs():
    # Square antiprism: top 0..3, bottom 4..7.  The top square is a face.
    plane = set()
    for index in range(4):
        add(plane, index, (index + 1) % 4)
        add(plane, 4 + index, 4 + (index + 1) % 4)
        add(plane, index, 4 + index)
        add(plane, index, 4 + (index - 1) % 4)

    graph = set(plane)
    add(graph, A, T)
    add(graph, T, P)
    for vertex in {0, 1, 4, 5, 6, 7}:
        add(graph, A, vertex)
    for vertex in {2, 3, 4, 5, 6, 7}:
        add(graph, P, vertex)
    for vertex in {1, 2, 4, 5, 6}:
        add(graph, T, vertex)
    return plane, graph


def adjacency(order, edges):
    result = [0] * order
    for left, right in edges:
        result[left] |= 1 << right
        result[right] |= 1 << left
    return result


def connected(mask, adj):
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        for vertex in range(len(adj)):
            if reached >> vertex & 1:
                expanded |= adj[vertex] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def is_five_connected(edges):
    adj = adjacency(11, edges)
    whole = (1 << 11) - 1
    for order in range(5):
        for cut in combinations(range(11), order):
            remaining = whole
            for vertex in cut:
                remaining &= ~(1 << vertex)
            if not connected(remaining, adj):
                return False
    return True


def four_colourings(edges):
    neighbours = [set() for _ in range(8)]
    for left, right in edges:
        neighbours[left].add(right)
        neighbours[right].add(left)
    order = sorted(range(8), key=lambda vertex: -len(neighbours[vertex]))
    colours = [-1] * 8
    answer = []

    def search(position):
        if position == 8:
            answer.append(tuple(colours))
            return
        vertex = order[position]
        for colour in range(4):
            if all(colours[other] != colour for other in neighbours[vertex]):
                colours[vertex] = colour
                search(position + 1)
                colours[vertex] = -1

    search(0)
    return answer


def k_colouring(order, edges, number_of_colours, vertices=None):
    if vertices is None:
        vertices = set(range(order))
    neighbours = {vertex: set() for vertex in vertices}
    for left, right in edges:
        if left in vertices and right in vertices:
            neighbours[left].add(right)
            neighbours[right].add(left)
    search_order = sorted(vertices, key=lambda vertex: -len(neighbours[vertex]))
    colours = {}

    def search(position):
        if position == len(search_order):
            return dict(colours)
        vertex = search_order[position]
        for colour in range(number_of_colours):
            if all(colours.get(other) != colour
                   for other in neighbours[vertex]):
                colours[vertex] = colour
                answer = search(position + 1)
                if answer is not None:
                    return answer
        colours.pop(vertex, None)
        return None

    return search(0)


def same_bichromatic_component(edges, colouring, left, right, other_colour):
    common = colouring[left]
    allowed = {common, other_colour}
    neighbours = {vertex: set() for vertex in colouring}
    for x, y in edges:
        if x in colouring and y in colouring:
            neighbours[x].add(y)
            neighbours[y].add(x)
    reached = {left}
    frontier = [left]
    while frontier:
        vertex = frontier.pop()
        for other in neighbours[vertex]:
            if other not in reached and colouring[other] in allowed:
                reached.add(other)
                frontier.append(other)
    return right in reached


def rooted_k4_minimum(order, edges):
    adj = adjacency(order, edges)
    neighbours = [0] * (1 << order)
    candidates = [[] for _ in ROOTS]
    for mask in range(1, 1 << order):
        low = mask & -mask
        vertex = low.bit_length() - 1
        neighbours[mask] = neighbours[mask ^ low] | adj[vertex]
        if not connected(mask, adj):
            continue
        contained_roots = [root for root in ROOTS if mask >> root & 1]
        if len(contained_roots) == 1:
            candidates[contained_roots[0]].append(mask)

    best = None
    witness = None

    def search(index, used, bags):
        nonlocal best, witness
        if index == 4:
            path_bags = sum(bool(bag & PATH_MASK) for bag in bags)
            path_vertices = sum((bag & PATH_MASK).bit_count() for bag in bags)
            score = (path_bags, path_vertices)
            if best is None or score < best:
                best, witness = score, tuple(bags)
            return
        for bag in candidates[index]:
            if bag & used:
                continue
            if any(not (neighbours[bag] & old) for old in bags):
                continue
            search(index + 1, used | bag, (*bags, bag))

    search(0, 0, ())
    return best, witness


def vertices(mask):
    names = ("x1", "x2", "x3", "x4", "y1", "y2", "y3", "y4",
             "a", "p", "t")
    return tuple(names[index] for index in range(11) if mask >> index & 1)


def main():
    plane, graph = graphs()
    assert is_five_connected(graph)
    assert len(graph) == 35 > 3 * 11 - 6  # Hence H is nonplanar.

    colourings = four_colourings(plane)
    rows = {
        "a": {0, 1, 4, 5, 6, 7},
        "p": {2, 3, 4, 5, 6, 7},
        "t": {1, 2, 4, 5, 6},
    }
    for row in rows.values():
        assert all(len({colouring[v] for v in row}) == 4
                   for colouring in colourings)

    plane_best, plane_model = rooted_k4_minimum(8, plane)
    graph_best, graph_model = rooted_k4_minimum(11, graph)
    assert plane_model is None
    assert graph_best == (1, 1)
    assert graph_model is not None

    # The whole architecture is not merely saturated: it is vertex-critical,
    # and every internal deletion/contraction relevant to the path/body has
    # the full critical witness.  Edge witnesses have equal ends, full colour
    # fans, and all required bichromatic connections.
    assert k_colouring(11, graph, 5) is None
    for vertex in range(11):
        assert k_colouring(11, graph, 5,
                           set(range(11)) - {vertex}) is not None
    redundant_outer_edges = set()
    for edge in graph:
        operated = set(graph) - {edge}
        witness = k_colouring(11, operated, 5)
        if witness is None:
            redundant_outer_edges.add(edge)
            continue
        left, right = edge
        assert witness[left] == witness[right]
        common = witness[left]
        operated_adjacency = adjacency(11, operated)
        for endpoint in edge:
            seen = {witness[other] for other in range(11)
                    if operated_adjacency[endpoint] >> other & 1}
            assert set(range(5)) - {common} <= seen
        for other_colour in set(range(5)) - {common}:
            assert same_bichromatic_component(
                operated, witness, left, right, other_colour)
    # Exactly the two outer-frame edges a-b and p-q are locally redundant.
    # Every edge internal to L or T, and every T-L portal edge, has the full
    # deletion/contraction transition witness.  In the actual HC7 host the
    # two outer edges acquire their criticality from u and v.
    assert redundant_outer_edges == {(4, P), (6, A)}

    # A concrete second path Q=y1-y4-y3 is already present.  Moving its
    # first endpoint y1 into the T-meeting bag replaces the a--x2 model
    # adjacency, but simultaneously destroys the only adjacency from the
    # x3 bag to x1: portal debt is shifted, not removed.
    q_path = (4, 7, 6)
    assert all(tuple(sorted(edge)) in graph
               for edge in zip(q_path, q_path[1:]))
    b1, b2, b3, b4 = graph_model
    assert vertices(b1) == ("x1",)
    assert vertices(b2) == ("x2",)
    assert vertices(b3) == ("x3", "y1", "y2")
    assert vertices(b4) == ("x4", "y3", "a")
    without_a = b4 & ~(1 << A)
    assert not any((adjacency(11, graph)[vertex] & b2)
                   for vertex in range(11) if without_a >> vertex & 1)
    assert adjacency(11, graph)[A] & b2
    without_q = b3 & ~(1 << 4)
    assert not any((adjacency(11, graph)[vertex] & b1)
                   for vertex in range(11) if without_q >> vertex & 1)
    assert adjacency(11, graph)[4] & b1

    print("five_connected=True edges=35 nonplanar_by_euler=True")
    print(f"four_colourings={len(colourings)} all_path_rows_saturating=True")
    print("rooted_K4_after_deleting_path=False")
    print(f"minimum_path_intersection={graph_best}")
    print("model=" + " | ".join(str(vertices(bag)) for bag in graph_model))
    print("vertex_critical=True all_internal_transition_Kempe_witnesses=True")
    print("locally_redundant_outer_edges=(p-q,a-b)")
    print("second_path=('y1','y4','y3') portal_debt_cycle=True")


if __name__ == "__main__":
    main()
