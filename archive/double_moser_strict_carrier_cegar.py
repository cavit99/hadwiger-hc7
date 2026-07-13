#!/usr/bin/env python3
"""Search small strict-relative double-Moser carrier obstructions.

This is a discovery probe, not a proof certificate.  Z3 generates contact
profiles with no two disjoint rooted carriers and no relative boundary of
order at most seven.  An exact branch-set search tests the resulting full
double-Moser quotient for K7 and blocks every superprofile of a positive
instance.
"""

from itertools import combinations
from z3 import And, Bool, Not, Or, PbGe, PbLe, Solver, is_true, sat


LABELS = ("a", "b", "x1", "x2", "x3", "x4", "p", "q")


def connected(mask, adjacency, order):
    if not mask:
        return False
    reached = mask & -mask
    while True:
        expanded = reached
        for vertex in range(order):
            if reached >> vertex & 1:
                expanded |= adjacency[vertex] & mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def find_k7(order, edges):
    adjacency = [0] * order
    for left, right in edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    neighbours = [0] * (1 << order)
    connected_sets = []
    for mask in range(1, 1 << order):
        low = mask & -mask
        vertex = low.bit_length() - 1
        neighbours[mask] = neighbours[mask ^ low] | adjacency[vertex]
        reached = low
        while True:
            expanded = reached | (neighbours[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected_sets.append(mask)
    connected_sets.sort(key=lambda mask: (mask.bit_count(), mask))
    answer = []

    def search(start, used):
        if len(answer) == 7:
            return tuple(answer)
        for index in range(start, len(connected_sets)):
            bag = connected_sets[index]
            if bag & used:
                continue
            if any(not (neighbours[bag] & old) for old in answer):
                continue
            answer.append(bag)
            result = search(index + 1, used | bag)
            if result:
                return result
            answer.pop()
        return None

    return search(0, 0)


def quotient_edges(order, shore_edges, contacts):
    # u,v,x1,x2,x3,x4,a,b,p,q followed by R.
    u, v, x1, x2, x3, x4, a, b, p, q = range(10)
    edges = set()

    def add(left, right):
        edges.add(tuple(sorted((left, right))))

    add(u, v)
    for vertex in (x1, x2, x3, x4, p, q):
        add(u, vertex)
    for vertex in (x1, x2, x3, x4, a, b):
        add(v, vertex)
    for left, right in ((x1, x2), (x3, x4), (a, b), (p, q)):
        add(left, right)
    for vertex in (x1, x2):
        add(a, vertex)
        add(q, vertex)
    for vertex in (x3, x4):
        add(b, vertex)
        add(p, vertex)
    for left, right in shore_edges:
        add(10 + left, 10 + right)
    boundary_index = {label: index for index, label in enumerate(LABELS, 6)}
    # Correct the first six labels: x1..x4 occupy 2..5, a,b occupy 6,7.
    boundary_index.update({"a": a, "b": b, "x1": x1, "x2": x2,
                           "x3": x3, "x4": x4, "p": p, "q": q})
    for label, mask in contacts.items():
        for vertex in range(order):
            if mask >> vertex & 1:
                add(boundary_index[label], 10 + vertex)
    return edges


def search_shore(name, order, shore_edges, maximum_contacts=28,
                 iteration_limit=500):
    adjacency = [0] * order
    for left, right in shore_edges:
        adjacency[left] |= 1 << right
        adjacency[right] |= 1 << left
    variables = [[Bool(f"{name}_{label}_{vertex}") for vertex in range(order)]
                 for label in LABELS]
    solver = Solver()
    for row in variables:
        solver.add(Or(*row))
    # The old outer vertices need at least three R-neighbours in a
    # contraction-critical host.
    solver.add(PbGe([(value, 1) for value in variables[0]], 3))
    solver.add(PbGe([(value, 1) for value in variables[1]], 3))
    solver.add(PbLe([(value, 1) for row in variables for value in row],
                    maximum_contacts))

    whole = (1 << order) - 1
    for subset in range(1, whole):
        frontier = 0
        for vertex in range(order):
            if subset >> vertex & 1:
                frontier |= adjacency[vertex]
        frontier_size = (frontier & ~subset).bit_count()
        hits = [Or(*(variables[label][vertex]
                     for vertex in range(order) if subset >> vertex & 1))
                for label in range(8)]
        solver.add(PbGe([(hit, 1) for hit in hits], 8 - frontier_size))

    connected_sets = [mask for mask in range(1, 1 << order)
                      if connected(mask, adjacency, order)]
    for left in connected_sets:
        for right in connected_sets:
            if left & right:
                continue
            left_hits = [Or(*(variables[label][vertex]
                              for vertex in range(order)
                              if left >> vertex & 1))
                         for label in (0, 4, 5)]
            right_hits = [Or(*(variables[label][vertex]
                               for vertex in range(order)
                               if right >> vertex & 1))
                          for label in (1, 2, 3)]
            solver.add(Not(And(*(left_hits + right_hits))))

    for iteration in range(iteration_limit):
        if solver.check() != sat:
            print(name, "unsat after", iteration, "positive profiles")
            return None
        model = solver.model()
        contacts = {}
        true_variables = []
        for label_index, label in enumerate(LABELS):
            mask = 0
            for vertex, variable in enumerate(variables[label_index]):
                if is_true(model.eval(variable)):
                    mask |= 1 << vertex
                    true_variables.append(variable)
            contacts[label] = mask
        if iteration % 100 == 0:
            print(name, "testing", iteration, contacts, flush=True)
        edges = quotient_edges(order, shore_edges, contacts)
        minor = find_k7(10 + order, edges)
        if minor is None:
            print(name, "K7-free candidate", contacts)
            return contacts
        # K7-minor existence is monotone, so block this profile and every
        # contact superprofile.
        solver.add(Or(*(Not(variable) for variable in true_variables)))
    print(name, "iteration limit reached")
    return None


def main():
    search_shore("c4", 4, ((0, 1), (1, 2), (2, 3), (3, 0)), 28)
    search_shore("diamond", 4,
                 ((0, 1), (1, 2), (2, 3), (3, 0), (0, 2)), 26)
    search_shore("k4", 4, tuple(combinations(range(4), 2)), 24)


if __name__ == "__main__":
    main()
