#!/usr/bin/env python3
"""Dependency-free verification of the five-interior split-web architecture."""

from itertools import combinations, product

# Boundary: 0=p1, 1=p2, 2=q1, 3=q2, 4=r1, 5=r2, 6=r3.
BOUNDARY_COLORS = {
    "10": (0, 0, 1, 2, 3, 4, 5),
    "01": (1, 2, 0, 0, 3, 4, 5),
    "11": (0, 0, 1, 1, 2, 3, 4),
}
INTERIOR_EDGES = {
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 2), (1, 4), (2, 3),
}
MASKS = (82, 113, 113, 91, 87)


def normalized_edges(edges):
    return {tuple(sorted(edge)) for edge in edges}


def find_coloring(masks, edges, state, equal_edge=None):
    colors = BOUNDARY_COLORS[state]
    order = len(masks)
    edges = normalized_edges(edges)
    allowed = []
    for mask in masks:
        forbidden = {colors[b] for b in range(7) if mask & (1 << b)}
        allowed.append(tuple(c for c in range(6) if c not in forbidden))
    for assignment in product(range(6), repeat=order):
        if any(assignment[x] not in allowed[x] for x in range(order)):
            continue
        if any(assignment[x] == assignment[y] for x, y in edges):
            continue
        if equal_edge is not None and assignment[equal_edge[0]] != assignment[equal_edge[1]]:
            continue
        return assignment
    return None


def full_graph():
    # Vertices 0..3 are terminals and 4..8 are interior.
    adjacency = [set() for _ in range(9)]
    for p in (0, 1):
        for q in (2, 3):
            adjacency[p].add(q)
            adjacency[q].add(p)
    for x, y in INTERIOR_EDGES:
        adjacency[4 + x].add(4 + y)
        adjacency[4 + y].add(4 + x)
    for x, mask in enumerate(MASKS, start=4):
        for terminal in range(4):
            if mask & (1 << terminal):
                adjacency[x].add(terminal)
                adjacency[terminal].add(x)
    return adjacency


def full_side_graph():
    # Vertices 0..6 are the full adhesion and 7..11 are interior.
    adjacency = [set() for _ in range(12)]
    for x, y in combinations(range(7), 2):
        if {x, y} not in ({0, 1}, {2, 3}):
            adjacency[x].add(y)
            adjacency[y].add(x)
    for x, y in INTERIOR_EDGES:
        adjacency[7 + x].add(7 + y)
        adjacency[7 + y].add(7 + x)
    for x, mask in enumerate(MASKS, start=7):
        for boundary in range(7):
            if mask & (1 << boundary):
                adjacency[x].add(boundary)
                adjacency[boundary].add(x)
    return adjacency


def components_after(adjacency, deleted):
    remaining = set(range(len(adjacency))) - set(deleted)
    components = []
    while remaining:
        root = next(iter(remaining))
        component, stack = {root}, [root]
        remaining.remove(root)
        while stack:
            x = stack.pop()
            for y in adjacency[x] - set(deleted):
                if y in remaining:
                    remaining.remove(y)
                    component.add(y)
                    stack.append(y)
        components.append(component)
    return components


def linkage_exists(adjacency):
    p_paths = []

    def paths(x, target, forbidden, used, path):
        if x == target:
            p_paths.append(tuple(path))
            return
        for y in adjacency[x]:
            if y not in used and y not in forbidden:
                used.add(y)
                path.append(y)
                paths(y, target, forbidden, used, path)
                path.pop()
                used.remove(y)

    paths(0, 1, {2, 3}, {0, 2, 3}, [0])
    for path in p_paths:
        deleted = set(path)
        if 2 in deleted or 3 in deleted:
            continue
        reached, stack = {2}, [2]
        while stack:
            x = stack.pop()
            for y in adjacency[x] - deleted - reached:
                reached.add(y)
                stack.append(y)
        if 3 in reached:
            return True
    return False


def verify_rotation(adjacency):
    rotation = {
        0: [2, 8, 5, 6, 7, 3],
        1: [2, 3, 7, 4, 8],
        2: [0, 1, 8],
        3: [1, 0, 7],
        4: [7, 6, 5, 8, 1],
        5: [4, 6, 0, 8],
        6: [5, 4, 7, 0],
        7: [3, 0, 6, 4, 1],
        8: [5, 0, 2, 1, 4],
    }
    assert all(set(rotation[x]) == adjacency[x] for x in range(9))
    directed = {(x, y) for x in range(9) for y in adjacency[x]}
    seen, faces = set(), []
    while directed - seen:
        start = next(iter(directed - seen))
        x, y = start
        face = []
        while (x, y) not in seen:
            seen.add((x, y))
            face.append(x)
            around_y = rotation[y]
            # Keep the face on the left: predecessor of x in clockwise order.
            z = around_y[(around_y.index(x) - 1) % len(around_y)]
            x, y = y, z
        assert (x, y) == start
        faces.append(face)
    edge_count = sum(len(neighbours) for neighbours in adjacency) // 2
    assert 9 - edge_count + len(faces) == 2
    assert any(len(face) == 4 and set(face) == {0, 1, 2, 3} for face in faces)


def main():
    internal_degree = [0] * 5
    for x, y in INTERIOR_EDGES:
        internal_degree[x] += 1
        internal_degree[y] += 1
    assert [internal_degree[x] + MASKS[x].bit_count() for x in range(5)] == [7] * 5
    assert MASKS[0] | MASKS[1] | MASKS[2] | MASKS[3] | MASKS[4] == 127

    assert find_coloring(MASKS, INTERIOR_EDGES, "10") is not None
    assert find_coloring(MASKS, INTERIOR_EDGES, "01") is not None
    assert find_coloring(MASKS, INTERIOR_EDGES, "11") is None

    adjacency = full_graph()
    assert not linkage_exists(adjacency)
    # Three-connectivity and the stronger no terminal-free <=3-cut property.
    for size in range(3):
        for deleted in combinations(range(9), size):
            assert len(components_after(adjacency, deleted)) == 1
    for size in range(4):
        for deleted in combinations(range(9), size):
            for component in components_after(adjacency, deleted):
                assert component & {0, 1, 2, 3}
    verify_rotation(adjacency)

    # The locally transition-critical architecture is nevertheless excluded
    # by this explicit K7-model in the full side graph.
    side_adjacency = full_side_graph()
    branch_sets = ({0}, {2}, {4}, {5}, {6}, {1, 3}, {8, 11})
    for branch in branch_sets:
        assert len(components_after(side_adjacency, set(range(12)) - branch)) == 1
    for i, first in enumerate(branch_sets):
        for second in branch_sets[i + 1:]:
            assert any(y in side_adjacency[x] for x in first for y in second)

    # Every internal one-step minor creates state 11.
    for deleted in range(5):
        vertices = [x for x in range(5) if x != deleted]
        index = {x: i for i, x in enumerate(vertices)}
        masks = tuple(MASKS[x] for x in vertices)
        edges = {
            (index[x], index[y])
            for x, y in INTERIOR_EDGES
            if deleted not in (x, y)
        }
        coloring = find_coloring(masks, edges, "11")
        assert coloring is not None
        seen = {
            coloring[index[y]]
            for y in vertices
            if tuple(sorted((deleted, y))) in INTERIOR_EDGES
        }
        seen |= {
            BOUNDARY_COLORS["11"][b]
            for b in range(7)
            if MASKS[deleted] & (1 << b)
        }
        assert seen == set(range(6))

    for x, y in INTERIOR_EDGES:
        deleted_edges = INTERIOR_EDGES - {(x, y)}
        coloring = find_coloring(MASKS, deleted_edges, "11", equal_edge=(x, y))
        assert coloring is not None
        for endpoint in (x, y):
            seen = {
                coloring[z]
                for z in range(5)
                if tuple(sorted((endpoint, z))) in deleted_edges
            }
            seen |= {
                BOUNDARY_COLORS["11"][b]
                for b in range(7)
                if MASKS[endpoint] & (1 << b)
            }
            assert set(range(6)) - {coloring[endpoint]} <= seen

        # Contract y into x.
        vertices = [z for z in range(5) if z != y]
        index = {z: i for i, z in enumerate(vertices)}
        masks = tuple(
            MASKS[x] | MASKS[y] if z == x else MASKS[z]
            for z in vertices
        )
        contracted_edges = set()
        for a, b in INTERIOR_EDGES:
            aa = x if a == y else a
            bb = x if b == y else b
            if aa != bb:
                contracted_edges.add(tuple(sorted((index[aa], index[bb]))))
        assert find_coloring(masks, contracted_edges, "11") is not None

    print("verified order-5 local architecture and its explicit K7-model")


if __name__ == "__main__":
    main()
