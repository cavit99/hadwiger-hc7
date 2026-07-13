"""Exhaustive certificate for the 5-connected haven-cleaning obstruction.

No third-party packages are used.  The rooted-minor check enumerates all
6^7 assignments of the seven nonroot vertices to five rooted bags or to
the unused class.  This covers every possible rooted K5 model because
each branch set already contains its prescribed root.
"""

from itertools import combinations, product

V = ["T", "S"] + [f"a{i}" for i in range(5)] + [f"b{i}" for i in range(5)]
E: set[frozenset[str]] = set()


def add(x: str, y: str) -> None:
    E.add(frozenset((x, y)))


for i in range(5):
    add("T", f"a{i}")
    add("S", f"b{i}")
    add(f"a{i}", f"a{(i + 1) % 5}")
    add(f"b{i}", f"b{(i + 1) % 5}")
    add(f"a{i}", f"b{i}")
    add(f"a{i}", f"b{(i - 1) % 5}")
add("T", "S")

N = ["T", "S", "a0", "a1", "b0"]
colour = {
    "T": 0, "S": 1, "a0": 2, "a1": 3, "a2": 1, "a3": 2,
    "a4": 1, "b0": 4, "b1": 0, "b2": 3, "b3": 4, "b4": 0,
}
bags = [{"T"}, {"S"}, {"a0", "b0"}, {"a1", "b1"}, {"a3", "a4", "b2"}]
paths = [{"T"}, {"S"}, {"a0"}, {"a1"}, {"b0", "b1", "b2"}]


def adjacent(A: set[str], B: set[str]) -> bool:
    return any(frozenset((x, y)) in E for x in A for y in B)


def connected(A: set[str]) -> bool:
    if not A:
        return False
    seen = {next(iter(A))}
    while True:
        new = seen | {y for x in seen for y in A if frozenset((x, y)) in E}
        if new == seen:
            return seen == A
        seen = new


# Proper rainbow colouring.
assert all(colour[x] != colour[y] for x, y in (tuple(e) for e in E))
assert {colour[x] for x in N} == set(range(5))

# Five-connectivity, hence equality of every haven component below order 5.
for k in range(5):
    for X in combinations(V, k):
        assert connected(set(V) - set(X))

# The displayed K5 model and disjoint transversal linkage.
assert all(connected(B) for B in bags)
assert all(not bags[i] & bags[j] and adjacent(bags[i], bags[j])
           for i in range(5) for j in range(i + 1, 5))
assert all(not paths[i] & paths[j] for i in range(5) for j in range(i + 1, 5))
assert all(connected(P) for P in paths)
assert all(paths[i] & bags[i] for i in range(5))

# Exhaust every N-rooted K5 branch-set assignment.
others = [x for x in V if x not in N]
for assignment in product(range(-1, 5), repeat=len(others)):
    candidate = [{N[i]} for i in range(5)]
    for x, label in zip(others, assignment):
        if label >= 0:
            candidate[label].add(x)
    if all(connected(B) for B in candidate) and all(
        adjacent(candidate[i], candidate[j])
        for i in range(5) for j in range(i + 1, 5)
    ):
        raise AssertionError(f"rooted K5 found: {candidate}")

# Every proper equality partition of H[N] is realised.  Canonical
# partition words and the corresponding colour words use the vertex
# order V displayed above.
partition_witnesses = {
    (0, 1, 1, 2, 0): "011212303042",
    (0, 1, 1, 2, 3): "011212330302",
    (0, 1, 2, 1, 0): "012121303024",
    (0, 1, 2, 1, 3): "012121330304",
    (0, 1, 2, 3, 0): "012312102034",
    (0, 1, 2, 3, 4): "012312140303",
}


def equality_word(values: list[int]) -> tuple[int, ...]:
    labels: dict[int, int] = {}
    answer: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        answer.append(labels[value])
    return tuple(answer)


for boundary_partition, word in partition_witnesses.items():
    witness = {x: int(k) for x, k in zip(V, word)}
    assert all(witness[x] != witness[y] for x, y in (tuple(e) for e in E))
    assert equality_word([witness[x] for x in N]) == boundary_partition

all_proper_boundary_partitions: set[tuple[int, ...]] = set()
for word in product(range(5), repeat=len(N)):
    if all(
        word[i] != word[j]
        for i, j in combinations(range(len(N)), 2)
        if frozenset((N[i], N[j])) in E
    ):
        all_proper_boundary_partitions.add(equality_word(list(word)))
assert set(partition_witnesses) == all_proper_boundary_partitions

independent_sets = {
    frozenset(S)
    for k in range(1, len(N) + 1)
    for S in combinations(N, k)
    if all(frozenset((x, y)) not in E for x, y in combinations(S, 2))
}
realised_traces: set[frozenset[str]] = set()
for word in partition_witnesses.values():
    witness = {x: int(k) for x, k in zip(V, word)}
    for k in range(5):
        trace = frozenset(x for x in N if witness[x] == k)
        if trace:
            realised_traces.add(trace)
assert independent_sets <= realised_traces

print(
    "PASS: all independent traces and model/linkage hold, "
    "but no N-rooted K5 exists"
)
