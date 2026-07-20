#!/usr/bin/env python3
"""Verify the singleton-web-cell PB barrier and its chained model."""

from itertools import combinations, product


BASE_CROSS = (
    (1, 0, 2, 1), (0, 0, 4, 0), (0, 0, 4, 1), (0, 1, 4, 0),
    (0, 1, 4, 1), (3, 1, 4, 0), (1, 0, 5, 0), (0, 0, 3, 1),
    (1, 1, 4, 0), (1, 1, 4, 1), (0, 0, 6, 0), (2, 0, 3, 0),
    (2, 0, 3, 1), (2, 1, 3, 0), (0, 0, 2, 0), (4, 1, 5, 0),
    (2, 0, 6, 0), (2, 1, 6, 0), (2, 1, 6, 1), (5, 0, 6, 1),
    (5, 1, 6, 0), (5, 1, 6, 1), (0, 0, 5, 1), (0, 1, 5, 0),
    (0, 1, 5, 1), (1, 0, 6, 1), (1, 0, 3, 0), (1, 0, 3, 1),
    (1, 1, 3, 0), (1, 1, 3, 1),
)

PARTS = (
    frozenset((0, 1)), frozenset((2, 3, 14)), frozenset((4, 5)),
    frozenset((6, 7, 15)), frozenset((8, 9)), frozenset((10, 11)),
    frozenset((12, 13)),
)
RIM = (2, 3, 4, 5, 6)
EDGES = {frozenset((2 * label, 2 * label + 1)) for label in range(7)}
EDGES.update(
    frozenset((2 * left + i, 2 * right + j))
    for left, i, right, j in BASE_CROSS
)
EDGES.update(
    frozenset((14, vertex)) for vertex in (2, 3, 6, 7, 8)
)
EDGES.update(
    frozenset((15, vertex)) for vertex in (2, 3, 5, 6, 14)
)


def adjacent(left: int, right: int) -> bool:
    return left != right and frozenset((left, right)) in EDGES


ADJACENCY = tuple(
    sum(1 << other for other in range(16) if adjacent(vertex, other))
    for vertex in range(16)
)
PART_MASKS = tuple(sum(1 << vertex for vertex in part) for part in PARTS)


def connected_mask(mask: int) -> bool:
    if not mask:
        return False
    reached = mask & -mask
    frontier = reached
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = ADJACENCY[vertex] & mask & ~reached
        reached |= new
        frontier |= new
    return reached == mask


def touches(left: int, right: int) -> bool:
    neighbours = 0
    pending = left
    while pending:
        bit = pending & -pending
        pending ^= bit
        neighbours |= ADJACENCY[bit.bit_length() - 1]
    return bool(neighbours & right)


def valid_model(bags: tuple[int, ...]) -> bool:
    return (
        len(bags) == 5
        and all(connected_mask(bag) for bag in bags)
        and not any(bags[i] & bags[j] for i, j in combinations(range(5), 2))
        and all(touches(bags[i], bags[j]) for i, j in combinations(range(5), 2))
    )


def labels_met(vertices: int, order: tuple[int, ...]) -> set[int]:
    return {label for label in order if touches(vertices, PART_MASKS[label])}


def alternating(order: tuple[int, ...], left: set[int], right: set[int]) -> bool:
    for positions in combinations(range(len(order)), 4):
        labels = tuple(order[position] for position in positions)
        if all(labels[index] in (left if index % 2 == 0 else right)
               for index in range(4)):
            return True
        if all(labels[index] in (right if index % 2 == 0 else left)
               for index in range(4)):
            return True
    return False


def check_no_alternating_split() -> None:
    orders = {0: RIM, 1: (2, 6, 5, 4, 3)}
    for position, label in enumerate(RIM):
        orders[label] = (0, RIM[(position + 1) % 5], 1, RIM[(position - 1) % 5])
    for label, part in enumerate(PART_MASKS):
        anchor = part & -part
        submask = part
        while submask:
            left = submask
            submask = (submask - 1) & part
            right = part ^ left
            if not right or not (left & anchor):
                continue
            if not connected_mask(left) or not connected_mask(right):
                continue
            assert not alternating(
                orders[label], labels_met(left, orders[label]),
                labels_met(right, orders[label]),
            ), (label, left, right)


def connected_subsets(mask: int) -> tuple[int, ...]:
    result = []
    submask = mask
    while submask:
        if connected_mask(submask):
            result.append(submask)
        submask = (submask - 1) & mask
    return tuple(result)


def check_no_adjacent_linkage() -> None:
    for position, first_label in enumerate(RIM):
        second_label = RIM[(position + 1) % 5]
        previous = RIM[(position - 1) % 5]
        following = RIM[(position + 2) % 5]
        subsets = connected_subsets(PART_MASKS[first_label] | PART_MASKS[second_label])
        pole_paths = tuple(
            subset for subset in subsets
            if touches(subset, PART_MASKS[0]) and touches(subset, PART_MASKS[1])
        )
        outer_paths = tuple(
            subset for subset in subsets
            if touches(subset, PART_MASKS[previous])
            and touches(subset, PART_MASKS[following])
        )
        assert not any(not (left & right) for left in pole_paths for right in outer_paths), position


def component_masks(mask: int) -> tuple[int, ...]:
    result = []
    unseen = mask
    while unseen:
        reached = unseen & -unseen
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = ADJACENCY[vertex] & mask & ~reached
            reached |= new
            frontier |= new
        result.append(reached)
        unseen &= ~reached
    return tuple(result)


def simple_paths(column: int, source: int, target: int):
    def visit(path: tuple[int, ...], used: int):
        current = path[-1]
        if current == target:
            yield path
            return
        choices = ADJACENCY[current] & column & ~used
        while choices:
            bit = choices & -choices
            choices ^= bit
            yield from visit(path + (bit.bit_length() - 1,), used | bit)

    yield from visit((source,), 1 << source)


def check_universal_shortest_path_residual() -> int:
    checked = 0
    for position, label in enumerate(RIM):
        column = PART_MASKS[label]
        previous = PART_MASKS[RIM[(position - 1) % 5]]
        following = PART_MASKS[RIM[(position + 1) % 5]]
        sources = tuple(vertex for vertex in PARTS[label]
                        if touches(1 << vertex, PART_MASKS[0]))
        targets = tuple(vertex for vertex in PARTS[label]
                        if touches(1 << vertex, PART_MASKS[1]))
        paths = tuple(
            path for source in sources for target in targets
            for path in simple_paths(column, source, target)
        )
        minimum = min(map(len, paths))
        for path in (candidate for candidate in paths if len(candidate) == minimum):
            checked += 1
            path_mask = sum(1 << vertex for vertex in path)
            for component in component_masks(column ^ path_mask):
                assert not (
                    touches(component, previous) and touches(component, following)
                ), (label, path, component)
    return checked


def oriented_frames():
    for pole_a, pole_b in ((0, 1), (1, 0)):
        for start in range(5):
            for direction in (1, -1):
                rim = tuple(RIM[(start + direction * offset) % 5] for offset in range(5))
                yield pole_a, pole_b, rim


def check_no_two_column_absorption() -> None:
    for pole_a, pole_b, rim in oriented_frames():
        del pole_b
        carrier_vertices = tuple(sorted(PARTS[pole_a] | PARTS[rim[0]]))
        for assignment in product((0, 1, 2), repeat=len(carrier_vertices)):
            first = PART_MASKS[rim[1]]
            second = PART_MASKS[rim[2]]
            for vertex, destination in zip(carrier_vertices, assignment):
                if destination == 1:
                    first |= 1 << vertex
                elif destination == 2:
                    second |= 1 << vertex
            if not connected_mask(first) or not connected_mask(second):
                continue
            assert not (
                touches(first, PART_MASKS[rim[3]])
                and touches(first, PART_MASKS[rim[4]])
                and touches(second, PART_MASKS[rim[4]])
            ), (pole_a, rim, assignment)


def check_web_certificate() -> None:
    t0, t6, t1, t4 = 16, 17, 18, 19
    carrier_edges = {(4, 5), (6, 7), (4, 6), (4, 7), (5, 6)}
    portal_edges = {
        (t0, 4), (t0, 7), (t6, 4), (t6, 5),
        (t1, 5), (t1, 6), (t1, 7), (t4, 7),
    }
    outer_edges = {(t0, t6), (t6, t1), (t1, t4), (t4, t0)}

    carrier = (4, 5, 6, 7)
    assert {
        frozenset(pair) for pair in combinations(carrier, 2) if adjacent(*pair)
    } == {frozenset(edge) for edge in carrier_edges}
    terminal_owners = {t0: 0, t6: 6, t1: 1, t4: 4}
    assert {
        (terminal, vertex)
        for terminal, owner in terminal_owners.items()
        for vertex in carrier
        if touches(1 << vertex, PART_MASKS[owner])
    } == portal_edges

    rib_edges = {frozenset(edge) for edge in carrier_edges | portal_edges | outer_edges}
    faces = (
        (4, 6, 5), (4, 7, 6), (4, t0, 7), (4, t6, t0), (4, 5, t6),
        (5, 6, t1), (5, t1, t6), (6, 7, t1), (7, t0, t4),
        (7, t4, t1), (t0, t6, t1, t4),
    )
    directed = []
    for face in faces:
        directed.extend(zip(face, face[1:] + face[:1]))
    assert len(rib_edges) == 17 and len(faces) == 11
    assert 8 - 17 + 11 == 2
    assert {frozenset(edge) for edge in directed} == rib_edges
    assert len(directed) == 2 * len(rib_edges)
    assert len(set(directed)) == len(directed)
    triangles = {
        frozenset(triple) for triple in combinations((4, 5, 6, 7, t0, t6, t1, t4), 3)
        if all(frozenset(pair) in rib_edges for pair in combinations(triple, 2))
    }
    assert triangles == {frozenset(face) for face in faces[:-1]}
    assert frozenset((5, 6, t1)) in triangles

    # The cell has two literal carrier edges and one terminal edge encoding
    # three literal contacts to owner column C_1.
    assert adjacent(15, 5) and adjacent(15, 6)
    q_without_cell = (PART_MASKS[2] | PART_MASKS[3]) ^ (1 << 15)
    assert {vertex for vertex in range(16)
            if q_without_cell & (1 << vertex) and adjacent(15, vertex)} == {5, 6}
    assert {vertex for vertex in PARTS[1] if adjacent(15, vertex)} == {2, 3, 14}
    assert {
        owner for owner in (0, 6, 1, 4) if touches(1 << 15, PART_MASKS[owner])
    } == {1}
    assert not any(adjacent(15, vertex) for vertex in (4, 7))


def check_no_five_owner_model() -> None:
    connected = {mask for mask in range(1, 1 << 16) if connected_mask(mask)}
    neighbours = [0] * (1 << 16)
    for mask in range(1, 1 << 16):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask ^ bit] | ADJACENCY[bit.bit_length() - 1]

    examined = positive = 0
    for owners in combinations(range(7), 5):
        bags = [PART_MASKS[label] for label in owners]
        remaining = tuple(
            vertex for label in range(7) if label not in owners for vertex in sorted(PARTS[label])
        )
        for assignment in product(range(6), repeat=len(remaining)):
            examined += 1
            candidate = bags.copy()
            for vertex, destination in zip(remaining, assignment):
                if destination < 5:
                    candidate[destination] |= 1 << vertex
            if any(not bag or bag not in connected for bag in candidate):
                continue
            if any(not (neighbours[candidate[i]] & candidate[j])
                   for i, j in combinations(range(5), 2)):
                continue
            positive += 1
    assert (examined, positive) == (137_376, 0)


def check_models_and_owners() -> None:
    clique = (2, 3, 6, 14, 15)
    assert all(adjacent(left, right) for left, right in combinations(clique, 2))

    bags_as_vertices = (
        (0, 1), (4, 5), (2, 7), (3, 8, 15), (9, 10, 11, 12, 13),
    )
    bags = tuple(sum(1 << vertex for vertex in bag) for bag in bags_as_vertices)
    assert valid_model(bags)
    root_a = sum(1 << vertex for vertex in (0, 3, 4, 7, 8, 10, 12))
    root_b = sum(1 << vertex for vertex in (1, 2, 5, 9, 11, 13, 15))
    assert all((root_a & part).bit_count() == 1 for part in PART_MASKS)
    assert all((root_b & part).bit_count() == 1 for part in PART_MASKS)
    assert not (root_a & root_b)
    assert all(bag & root_a and bag & root_b for bag in bags)

    check_no_five_owner_model()
    four_owner = (1, 48, 3458, 12288, 16908)
    assert valid_model(four_owner)
    owner_labels = (None, 2, 5, 6, 1)
    for bag, label in zip(four_owner, owner_labels):
        if label is not None:
            assert PART_MASKS[label] & bag == PART_MASKS[label]


def main() -> None:
    assert len(EDGES) == 47
    assert set().union(*PARTS) == set(range(16))
    assert sum(map(len, PARTS)) == 16
    assert all(connected_mask(mask) for mask in PART_MASKS)

    expected_contacts = {
        frozenset((pole, rim)) for pole in (0, 1) for rim in RIM
    } | {
        frozenset((RIM[index], RIM[(index + 1) % 5])) for index in range(5)
    }
    actual_contacts = {
        frozenset((left, right)) for left, right in combinations(range(7), 2)
        if touches(PART_MASKS[left], PART_MASKS[right])
    }
    assert actual_contacts == expected_contacts

    full = (1 << 16) - 1
    for size in range(5):
        for deleted in combinations(range(16), size):
            removed = sum(1 << vertex for vertex in deleted)
            assert connected_mask(full ^ removed), deleted
    assert len(tuple(vertex for vertex in range(16) if adjacent(15, vertex))) == 5

    check_web_certificate()
    shortest_residual_paths = check_universal_shortest_path_residual()
    check_no_alternating_split()
    check_no_adjacent_linkage()
    check_no_two_column_absorption()
    check_models_and_owners()
    print(
        "singleton web-cell PB barrier: PASS "
        "order=16 size=47 connectivity=5 five_owner_models=0 "
        f"maximum_distinct_owner_bags=4 shortest_residual_paths={shortest_residual_paths}"
    )


if __name__ == "__main__":
    main()
