#!/usr/bin/env python3
"""Exact one-bridge classification for the bad six-link quotient.

The fixed graph Q has vertices 0,...,11.  A new vertex w represents one
connected external bridge after contraction and has neighbourhood T in Q.
The script classifies all 2^12 choices of T without third-party packages.
"""

from itertools import combinations


N = 12
FULL = (1 << N) - 1
EDGES: set[tuple[int, int]] = set()


def add_edge(left: int, right: int) -> None:
    EDGES.add((min(left, right), max(left, right)))


# Six-vertex K_5 model: K_4 on 0,1,2,3 and split edge 4--5.
for edge in combinations(range(4), 2):
    add_edge(*edge)
add_edge(4, 5)
for vertex in (0, 1, 2):
    add_edge(vertex, 4)
add_edge(3, 5)

# K_6^- on 6,...,11, with missing edge 10--11.
for edge in combinations(range(6, 12), 2):
    if edge != (10, 11):
        add_edge(*edge)

# The bad perfect matching.
for left, right in enumerate((6, 7, 8, 10, 11, 9)):
    add_edge(left, right)

ADJACENCY = [0] * N
for left, right in EDGES:
    ADJACENCY[left] |= 1 << right
    ADJACENCY[right] |= 1 << left


def components(mask: int) -> tuple[int, ...]:
    answer: list[int] = []
    remaining = mask
    while remaining:
        seen = remaining & -remaining
        frontier = seen
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = ADJACENCY[vertex] & mask & ~seen
            seen |= new
            frontier |= new
        answer.append(seen)
        remaining &= ~seen
    return tuple(answer)


def neighbourhood(mask: int) -> int:
    answer = 0
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        answer |= ADJACENCY[bit.bit_length() - 1]
    return answer & ~mask


CONNECTED: list[int] = []
NEIGHBOURHOOD: dict[int, int] = {}
BY_FIRST = {vertex: [] for vertex in range(N)}
for candidate in range(1, 1 << N):
    if len(components(candidate)) != 1:
        continue
    CONNECTED.append(candidate)
    NEIGHBOURHOOD[candidate] = neighbourhood(candidate)
    first = (candidate & -candidate).bit_length() - 1
    BY_FIRST[first].append(candidate)


def attachment_constraints() -> tuple[set[tuple[int, ...]], int]:
    """Enumerate every six-branch K_6 model left outside the w-branch.

    For one such collection, U is the complement of its six branch sets.
    The branch containing w is {w} union U.  It is connected exactly when
    T meets every component of Q[U].  It is adjacent to another branch B
    either through a Q-edge from U to B or when T meets B.  Thus the
    returned tuple is the exact family of sets that T must hit.
    """

    constraints: set[tuple[int, ...]] = set()
    chosen: list[int] = []
    collection_count = 0

    def record() -> None:
        nonlocal collection_count
        collection_count += 1
        unused = FULL
        for branch in chosen:
            unused ^= branch

        required = list(components(unused))
        for branch in chosen:
            if not (NEIGHBOURHOOD[branch] & unused):
                required.append(branch)

        # If R is contained in R', hitting R already hits R'.
        minimal: list[int] = []
        for requirement in sorted(
            set(required), key=lambda item: (item.bit_count(), item)
        ):
            if not any(old & ~requirement == 0 for old in minimal):
                minimal.append(requirement)
        constraints.add(tuple(minimal))

    def search(available: int) -> None:
        if len(chosen) == 6:
            record()
            return
        if available.bit_count() < 6 - len(chosen):
            return

        first_bit = available & -available
        first = first_bit.bit_length() - 1
        for branch in BY_FIRST[first]:
            if branch & ~available:
                continue
            if any(
                not (NEIGHBOURHOOD[branch] & old) for old in chosen
            ):
                continue
            chosen.append(branch)
            search(available ^ branch)
            chosen.pop()

        # The least available vertex may instead belong to the w-branch.
        search(available ^ first_bit)

    search(FULL)
    return constraints, collection_count


def vertices(mask: int) -> tuple[int, ...]:
    return tuple(vertex for vertex in range(N) if mask & (1 << vertex))


def branch_collections(
    target_count: int,
) -> list[tuple[tuple[int, ...], int]]:
    """All unordered clique-minor branch collections of a fixed order."""

    answer: list[tuple[tuple[int, ...], int]] = []
    chosen: list[int] = []

    def search(available: int) -> None:
        if len(chosen) == target_count:
            answer.append((tuple(chosen), available))
            return
        if available.bit_count() < target_count - len(chosen):
            return

        first_bit = available & -available
        first = first_bit.bit_length() - 1
        for branch in BY_FIRST[first]:
            if branch & ~available:
                continue
            if any(
                not (NEIGHBOURHOOD[branch] & old) for old in chosen
            ):
                continue
            chosen.append(branch)
            search(available ^ branch)
            chosen.pop()
        search(available ^ first_bit)

    search(FULL)
    return answer


def one_bridge_connected(vertices_in_q: int, attachment: int) -> bool:
    return not vertices_in_q or all(
        component & attachment for component in components(vertices_in_q)
    )


def two_bridges_connected(
    vertices_in_q: int,
    first_attachment: int,
    second_attachment: int,
    bridge_edge: bool,
) -> bool:
    """Connectivity of Q[U] plus two bridge vertices."""

    q_components = components(vertices_in_q)
    if not q_components:
        return bridge_edge

    component_count = len(q_components)
    first_bridge = component_count
    second_bridge = component_count + 1
    auxiliary = [set() for _ in range(component_count + 2)]
    for index, component in enumerate(q_components):
        if component & first_attachment:
            auxiliary[index].add(first_bridge)
            auxiliary[first_bridge].add(index)
        if component & second_attachment:
            auxiliary[index].add(second_bridge)
            auxiliary[second_bridge].add(index)
    if bridge_edge:
        auxiliary[first_bridge].add(second_bridge)
        auxiliary[second_bridge].add(first_bridge)

    seen = {0}
    frontier = [0]
    while frontier:
        current = frontier.pop()
        for neighbour in auxiliary[current] - seen:
            seen.add(neighbour)
            frontier.append(neighbour)
    return len(seen) == component_count + 2


def has_two_bridge_model(
    first_attachment: int,
    second_attachment: int,
    bridge_edge: bool,
    six_collections: list[tuple[tuple[int, ...], int]],
    five_collections: list[tuple[tuple[int, ...], int]],
) -> bool:
    """Test all spanning models using both new bridge vertices."""

    # The two bridge vertices may lie in one branch set.
    for branches, unused in six_collections:
        if not two_bridges_connected(
            unused, first_attachment, second_attachment, bridge_edge
        ):
            continue
        if all(
            (NEIGHBOURHOOD[branch] & unused)
            or (branch & first_attachment)
            or (branch & second_attachment)
            for branch in branches
        ):
            return True

    # Or they may lie in two different branch sets, leaving five branch
    # sets wholly inside Q.  Partition every unused Q-vertex between the
    # two bridge branch sets.
    for branches, unused in five_collections:
        first_side = unused
        while True:
            second_side = unused ^ first_side
            if one_bridge_connected(
                first_side, first_attachment
            ) and one_bridge_connected(second_side, second_attachment):
                first_neighbourhood = neighbourhood(first_side)
                second_neighbourhood = neighbourhood(second_side)
                bridge_sets_adjacent = (
                    bridge_edge
                    or bool(first_neighbourhood & second_side)
                    or bool(first_attachment & second_side)
                    or bool(second_attachment & first_side)
                )
                if bridge_sets_adjacent and all(
                    (
                        (first_neighbourhood & branch)
                        or (first_attachment & branch)
                    )
                    and (
                        (second_neighbourhood & branch)
                        or (second_attachment & branch)
                    )
                    for branch in branches
                ):
                    return True
            if first_side == 0:
                break
            first_side = (first_side - 1) & unused
    return False


def main() -> None:
    constraints, collection_count = attachment_constraints()
    repairing = {
        attachment
        for attachment in range(1 << N)
        if any(
            all(attachment & requirement for requirement in family)
            for family in constraints
        )
    }
    nonrepairing = set(range(1 << N)) - repairing
    maximal_nonrepairing = {
        attachment
        for attachment in nonrepairing
        if all(
            attachment | (1 << vertex) in repairing
            for vertex in range(N)
            if not attachment & (1 << vertex)
        )
    }

    large_maximal = sorted(
        attachment
        for attachment in maximal_nonrepairing
        if attachment.bit_count() >= 7
    )
    expected = [
        sum(1 << vertex for vertex in (0, 1, 2, 3, 6, 7, 8, 10)),
        sum(1 << vertex for vertex in (0, 1, 2, 4, 6, 7, 8, 11)),
    ]
    assert large_maximal == expected
    assert all(
        attachment.bit_count() < 7
        or any(attachment & ~exception == 0 for exception in expected)
        for attachment in nonrepairing
    )

    print("six_branch_collections", collection_count)
    print("attachment_constraint_types", len(constraints))
    print("repairing_attachment_sets", len(repairing))
    print("nonrepairing_attachment_sets", len(nonrepairing))
    print(
        "maximal_nonrepairing_with_at_least_seven_attachments",
        [vertices(mask) for mask in large_maximal],
    )
    print(
        "smallest_seven_attachment_counterexample",
        (0, 1, 2, 3, 6, 7, 8),
    )

    # If two components have opposite exceptional types, both contracted
    # vertices together always repair the quotient.  It is enough to test
    # the maximal frame and its eight seven-subsets on each side.
    first_frame = set((0, 1, 2, 3, 6, 7, 8, 10))
    second_frame = set((0, 1, 2, 4, 6, 7, 8, 11))
    first_choices = [first_frame] + [
        first_frame - {vertex} for vertex in sorted(first_frame)
    ]
    second_choices = [second_frame] + [
        second_frame - {vertex} for vertex in sorted(second_frame)
    ]
    six_collections = branch_collections(6)
    five_collections = branch_collections(5)
    for bridge_edge in (False, True):
        exceptions = []
        for first in first_choices:
            for second in second_choices:
                if not has_two_bridge_model(
                    sum(1 << vertex for vertex in first),
                    sum(1 << vertex for vertex in second),
                    bridge_edge,
                    six_collections,
                    five_collections,
                ):
                    exceptions.append((tuple(sorted(first)), tuple(sorted(second))))
        print(
            "mixed_type_two_bridge_exceptions_bridge_edge_"
            + str(bridge_edge).lower(),
            len(exceptions),
        )
        assert not exceptions


if __name__ == "__main__":
    main()
