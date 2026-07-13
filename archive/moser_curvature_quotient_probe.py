#!/usr/bin/env python3
"""Test minimal quotients of the facial curvature profiles.

The shore vertex x is separated from the connected remainder B=D-x;
O is the contracted opposite full shore.  Only contacts forced by fullness
and the stated x-profile are retained, so a positive model is monotone.
"""

from itertools import combinations, product


N = set(range(7))
U = {0, 2, 4, 5, 6}
W, X, BODY, OPP = 7, 8, 9, 10
L = U | {W, 1}
MOSER = {
    frozenset(edge)
    for edge in (
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 2), (1, 6), (2, 6),
        (3, 4), (3, 5), (4, 5), (5, 6),
    )
}


def partitions(items, count):
    items = tuple(items)
    labels = [0]

    def rec(index, maximum):
        if index == len(items):
            if maximum == count - 1:
                bags = [set() for _ in range(count)]
                for item, label in zip(items, labels):
                    bags[label].add(item)
                yield bags
            return
        for label in range(min(maximum + 1, count - 1) + 1):
            labels.append(label)
            yield from rec(index + 1, max(maximum, label))
            labels.pop()

    yield from rec(1, 0)


def connected(bag, edges):
    seen = {next(iter(bag))}
    while True:
        more = {
            y for x in seen for y in bag - seen
            if frozenset((x, y)) in edges
        }
        if not more:
            return seen == bag
        seen |= more


def adjacent(first, second, edges):
    return any(frozenset((x, y)) in edges for x in first for y in second)


def find_model(x_contacts, body_defect):
    edges = set(MOSER)
    edges.add(frozenset((X, BODY)))
    for label in x_contacts:
        edges.add(frozenset((X, label)))
    # Applying the relative cut inequality to D-x gives at least six
    # contacts, so BODY misses at most the displayed one label.  Fullness
    # additionally requires that a missed label be covered by x.
    for label in L - set(body_defect):
        edges.add(frozenset((BODY, label)))
    # The opposite shore is full to S union {b=3}.
    for label in U | {W, 3}:
        edges.add(frozenset((OPP, label)))

    for size in (6, 7):
        for used_n in combinations(sorted(N), size):
            for base in partitions(used_n, 6):
                for assignments in product(range(7), repeat=4):
                    bags = [set(bag) for bag in base]
                    for helper, label in zip((W, X, BODY, OPP), assignments):
                        if label < 6:
                            bags[label].add(helper)
                    if not all(connected(bag, edges) for bag in bags):
                        continue
                    if not all(
                        adjacent(bags[i], bags[j], edges)
                        for i in range(6) for j in range(i)
                    ):
                        continue
                    return bags
    return None


present_pairs = ({0, 2}, {2, 6}, {6, 5}, {5, 4}, {4, 0})
interior_contacts = {W, 1}
interior_failures = []
for defect in (set(), {W}, {1}):
    if find_model(interior_contacts, defect) is None:
        interior_failures.append(defect)
print("interior", "failures", interior_failures)

for pair in present_pairs:
    contacts = set(pair) | {W, 1}
    failures = []
    for defect in (set(), *( {label} for label in contacts )):
        if find_model(contacts, defect) is None:
            failures.append(defect)
    print("ordinary", sorted(map(str, pair)), "failures", failures)

missing_cycle = (0, 5, 2, 4, 6)
for i in range(5):
    u, v = missing_cycle[i], missing_cycle[(i + 1) % 5]
    q = missing_cycle[(i + 3) % 5]
    triple = {u, v, q}
    for extra in ({W}, {1}, {W, 1}):
        contacts = triple | extra
        failures = []
        for defect in (set(), *( {label} for label in contacts )):
            if find_model(contacts, defect) is None:
                failures.append(defect)
        print("triple", sorted(map(str, triple)), sorted(map(str, extra)),
              "failures", failures)
