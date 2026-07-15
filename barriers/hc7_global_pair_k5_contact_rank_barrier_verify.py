#!/usr/bin/env python3
"""Verify the K5-contact-rank stall in K2 joined to the icosahedron.

The checker is dependency-free.  For every eligible adjacent pair ``p,q``
(all edges except the edge between the two universal vertices), it searches
all connected branch sets of order at most three.  This is enough to exclude
a five-bag model of total order at most seven and to find the displayed
optimal models of total order eight.
"""

from itertools import combinations


TOP, BOTTOM = 10, 11
APEX_A, APEX_B = 12, 13
VERTICES = frozenset(range(14))


def edge(a, b):
    return tuple(sorted((a, b)))


I_EDGES = set()
for i in range(5):
    I_EDGES.update(
        {
            edge(TOP, i),
            edge(BOTTOM, 5 + i),
            edge(i, (i + 1) % 5),
            edge(5 + i, 5 + (i + 1) % 5),
            edge(i, 5 + i),
            edge(i, 5 + (i - 1) % 5),
        }
    )

G_EDGES = set(I_EDGES)
for apex in (APEX_A, APEX_B):
    for vertex in range(12):
        G_EDGES.add(edge(apex, vertex))
G_EDGES.add(edge(APEX_A, APEX_B))


def adjacent(a, b):
    return edge(a, b) in G_EDGES


def connected(vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        vertex = todo.pop()
        for neighbour in vertices - seen:
            if adjacent(vertex, neighbour):
                seen.add(neighbour)
                todo.append(neighbour)
    return seen == vertices


def touch(left, right):
    return any(adjacent(a, b) for a in left for b in right)


def verify_connectivity():
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            assert connected(VERTICES - set(deleted))


def candidates(pair, maximum_bag_order):
    remaining = sorted(VERTICES - set(pair))
    values = []
    for size in range(1, maximum_bag_order + 1):
        for branch_set in combinations(remaining, size):
            branch_set = frozenset(branch_set)
            if connected(branch_set):
                p, q = pair
                values.append(
                    (
                        branch_set,
                        any(adjacent(p, vertex) for vertex in branch_set),
                        any(adjacent(q, vertex) for vertex in branch_set),
                    )
                )
    return values


def find_model(pair, order_bound):
    # Five nonempty bags of total order <= 8 have individual order <= 4.
    values = candidates(pair, order_bound - 4)

    def search(start, chosen, used, total_order, common, covered):
        if len(chosen) == 5:
            if common == 4 and covered == 5:
                return tuple(values[index] for index in chosen)
            return None
        if total_order + 5 - len(chosen) > order_bound:
            return None
        for index in range(start, len(values)):
            branch_set, p_contact, q_contact = values[index]
            new_order = total_order + len(branch_set)
            if new_order + 4 - len(chosen) > order_bound:
                continue
            if used & branch_set:
                continue
            if any(not touch(branch_set, values[old][0]) for old in chosen):
                continue
            answer = search(
                index + 1,
                [*chosen, index],
                used | branch_set,
                new_order,
                common + int(p_contact and q_contact),
                covered + int(p_contact or q_contact),
            )
            if answer is not None:
                return answer
        return None

    return search(0, [], frozenset(), 0, 0, 0)


def verify_rank_stall():
    eligible = sorted(G_EDGES - {edge(APEX_A, APEX_B)})
    witnesses = {}
    for pair in eligible:
        # A smaller model with the same first two coordinates would beat the
        # claimed rank.  This search is exhaustive because every bag in a
        # five-bag model of total order <= 7 has order at most three.
        assert find_model(pair, 7) is None
        witness = find_model(pair, 8)
        assert witness is not None
        witnesses[pair] = witness

    assert len(eligible) == 54

    # Check the compact representatives displayed in the note.  The search
    # is free to return a different witness of the same optimum.
    displayed = {
        edge(APEX_A, 0): (
            frozenset({1}),
            frozenset({2}),
            frozenset({APEX_B}),
            frozenset({3, TOP}),
            frozenset({5, 6, 7}),
        ),
        edge(0, 1): (
            frozenset({2}),
            frozenset({APEX_A}),
            frozenset({APEX_B}),
            frozenset({3, TOP}),
            frozenset({5, 6, 7}),
        ),
    }
    for pair, model in displayed.items():
        assert sum(map(len, model)) == 8
        assert all(connected(branch_set) for branch_set in model)
        assert all(
            not (model[first] & model[second])
            and touch(model[first], model[second])
            for first in range(5)
            for second in range(first + 1, 5)
        )
        p, q = pair
        contacts = [
            (
                any(adjacent(p, vertex) for vertex in branch_set),
                any(adjacent(q, vertex) for vertex in branch_set),
            )
            for branch_set in model
        ]
        assert sum(a and b for a, b in contacts) == 4
        assert sum(a or b for a, b in contacts) == 5


if __name__ == "__main__":
    verify_connectivity()
    verify_rank_stall()
    print(
        "GREEN: every eligible adjacent-pair orbit attains contact rank "
        "(4,5,-8), while the hidden terminal pair is the two apices"
    )
