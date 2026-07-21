#!/usr/bin/env python3
"""Verify the deleted-colour rooted-K4 contact-concentration barrier."""

from itertools import combinations, product


E, Q = 0, 1
P = (2, 3, 4, 5)
R = (6, 7, 8, 9)
W = (10, 11, 12, 13)
T = (14, 15, 16, 17)
V = tuple(range(18))
U = (E,) + R


def build_edges():
    edges = set()

    def add(left, right):
        edges.add(tuple(sorted((left, right))))

    edges.update(tuple(sorted(edge)) for edge in combinations(W, 2))
    edges.update(tuple(sorted(edge)) for edge in combinations(T, 2))
    add(W[0], T[1])
    for vertex in W + T + R:
        add(Q, vertex)
    for vertex in T:
        add(E, vertex)
    for index in range(4):
        add(P[index], T[index])
        add(P[index], R[index])
        for other in range(4):
            if index != other:
                add(R[index], W[other])
    add(R[0], R[1])
    add(R[2], R[3])
    return edges


EDGES = build_edges()
ADJ = {vertex: set() for vertex in V}
for left, right in EDGES:
    ADJ[left].add(right)
    ADJ[right].add(left)

FIXED = {E: 0, Q: 0, **{vertex: 0 for vertex in P}}
for index in range(4):
    for vertex in (R[index], W[index], T[index]):
        FIXED[vertex] = index + 1


def is_connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    start = min(vertices)
    seen = {start}
    stack = [start]
    while stack:
        vertex = stack.pop()
        for neighbour in sorted((ADJ[vertex] & vertices) - seen):
            seen.add(neighbour)
            stack.append(neighbour)
    return seen == vertices


def adjacent(left, right):
    right = set(right)
    return any(ADJ[vertex] & right for vertex in left)


def distance(start, target, allowed):
    allowed = set(allowed)
    frontier = {start}
    seen = {start}
    length = 0
    while frontier:
        if target in frontier:
            return length
        next_frontier = set()
        for vertex in frontier:
            next_frontier.update((ADJ[vertex] & allowed) - seen)
        seen.update(next_frontier)
        frontier = next_frontier
        length += 1
    return None


def is_path(path):
    return len(set(path)) == len(path) and all(
        tuple(sorted(edge)) in EDGES for edge in zip(path, path[1:])
    )


def count_five_colourings():
    order = sorted(V, key=lambda vertex: (-len(ADJ[vertex]), vertex))
    colour = {}
    total = 0
    colourful = 0

    def extend(position):
        nonlocal total, colourful
        if position == len(order):
            total += 1
            colourful += len({colour[root] for root in U}) == 5
            return

        vertex = order[position]
        forbidden = {colour[nbr] for nbr in ADJ[vertex] if nbr in colour}
        for value in range(5):
            if value not in forbidden:
                colour[vertex] = value
                extend(position + 1)
        colour.pop(vertex, None)

    extend(0)
    return total, colourful


def is_rooted_k4(bags):
    return all(is_connected(bag) for bag in bags) and all(
        adjacent(bags[left], bags[right])
        for left, right in combinations(range(4), 2)
    )


def contact_count(root, bags):
    """Count bags meeting N_{H_root}(root), equivalently adjacent to root."""
    return sum(bool(ADJ[root] & set(bag)) for bag in bags)


def count_rooted_k4_models():
    nonroots = W + T
    count = 0
    maximum_contacts = 0
    for owners in product(range(5), repeat=len(nonroots)):
        bags = [{R[index]} for index in range(4)]
        for vertex, owner in zip(nonroots, owners):
            if owner < 4:
                bags[owner].add(vertex)
        if not is_rooted_k4(bags):
            continue
        count += 1
        contacts = sum(bool(set(bag) & set(T)) for bag in bags)
        maximum_contacts = max(maximum_contacts, contacts)
    return count, maximum_contacts


def verify_fixed_routing():
    assert all(FIXED[left] != FIXED[right] for left, right in EDGES)
    literal_root_edges = {
        edge for edge in EDGES if set(edge) <= set(U)
    }
    assert literal_root_edges == {
        tuple(sorted((R[0], R[1]))),
        tuple(sorted((R[2], R[3]))),
    }

    for left, right in combinations(U, 2):
        colours = {FIXED[left], FIXED[right]}
        allowed = {vertex for vertex in V if FIXED[vertex] in colours}
        assert distance(left, right, allowed) is not None

    path_ea = (E, T[0], P[0], R[0])
    path_bc = (R[1], W[2], W[1], R[2])
    assert is_path(path_ea) and is_path(path_bc)
    assert set(path_ea).isdisjoint(path_bc)
    for path in (path_ea, path_bc):
        colours = {FIXED[path[0]], FIXED[path[-1]]}
        allowed = {vertex for vertex in V if FIXED[vertex] in colours}
        assert set(path) <= allowed
        assert distance(path[0], path[-1], allowed) == len(path) - 1 == 3


def verify_displayed_models():
    contact_model = [
        {R[0], W[1]},
        {R[1], W[2]},
        {R[2], W[3]},
        {R[3], W[0], T[1]},
    ]
    assert is_rooted_k4(contact_model)
    assert sum(bool(set(bag) & set(T)) for bag in contact_model) == 1

    k5_model = [
        {E, T[0], Q},
        {R[0], W[1]},
        {R[1], W[2]},
        {R[2], W[3]},
        {R[3], W[0]},
    ]
    assert all(is_connected(bag) for bag in k5_model)
    assert all(
        adjacent(k5_model[left], k5_model[right])
        for left, right in combinations(range(5), 2)
    )


def verify_contact_vector(maximum_e_contacts):
    maxima = [maximum_e_contacts]
    for deleted_index in range(4):
        remaining = [index for index in range(4) if index != deleted_index]
        bags = [{E, Q, T[remaining[0]]}]
        bags.extend(
            {R[index], W[remaining[(position + 1) % 3]]}
            for position, index in enumerate(remaining)
        )

        deleted_colour = FIXED[R[deleted_index]]
        assert all(
            FIXED[vertex] != deleted_colour
            for bag in bags
            for vertex in bag
        )
        assert [next(root for root in U if root in bag) for bag in bags] == [
            E,
            *(R[index] for index in remaining),
        ]
        assert is_rooted_k4(bags)
        contacts = contact_count(R[deleted_index], bags)
        assert contacts == 4
        maxima.append(contacts)

    assert tuple(maxima) == (1, 4, 4, 4, 4)
    return tuple(maxima)


def main():
    verify_fixed_routing()

    total, colourful = count_five_colourings()
    assert (total, colourful) == (253_200, 253_200)
    print(f"five_colourings={total} colourful_on_U={colourful}")
    print("routing_pairs=10 designated_paths=shortest_disjoint")

    model_count, maximum_contacts = count_rooted_k4_models()
    assert (model_count, maximum_contacts) == (927, 1)
    contact_vector = verify_contact_vector(maximum_contacts)
    vector_text = ",".join(str(value) for value in contact_vector)
    print(
        f"rooted_K4_models={model_count} "
        f"maximum_contact_vector_e_r1_r2_r3_r4=({vector_text})"
    )

    verify_displayed_models()
    print("explicit_U_rooted_K5=PASS")
    print(
        "scope=fixed-deletion contact shortcut only; "
        "existential deletion survives"
    )


if __name__ == "__main__":
    main()
