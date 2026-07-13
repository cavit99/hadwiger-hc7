from itertools import combinations, product
from random import Random


# Vertices: apex v=0, C={y}=1, saturated bag {a,b}={2,3},
# and four two-vertex contact bags.
v, y, a, b = range(4)
bags = ((4, 5), (6, 7), (8, 9), (10, 11))
targets = tuple(x for bag in bags for x in bag)
vertices = tuple(range(12))
h_vertices = tuple(range(1, 12))

# v has exactly seven neighbours: a,b, one root in each target bag, and
# a second root in the first target bag.
roots = (a, b, 4, 5, 6, 8, 10)
nonroots = tuple(x for x in h_vertices if x not in roots)


def add(E, x, z):
    E.add((min(x, z), max(x, z)))


def base_edges():
    E = set()
    for x in roots:
        add(E, v, x)
    add(E, a, b)
    add(E, a, y)
    add(E, b, y)
    # Saturated target partition: a owns bags 0,1; b owns bags 2,3.
    for x in bags[0] + bags[1]:
        add(E, a, x)
    for x in bags[2] + bags[3]:
        add(E, b, x)
    for bag in bags:
        add(E, *bag)
        # Make y adjacent to both vertices; this only helps connectivity.
        for x in bag:
            add(E, y, x)
    return E


cross_pairs = tuple(
    (x, z)
    for i in range(4)
    for j in range(i + 1, 4)
    for x in bags[i]
    for z in bags[j]
)


def neighbourhoods(E):
    N = [set() for _ in vertices]
    for x, z in E:
        N[x].add(z)
        N[z].add(x)
    return N


def connected_after_deleting(N, deleted):
    rem = set(vertices) - deleted
    if not rem:
        return True
    seen = {next(iter(rem))}
    while True:
        new = seen | {z for x in seen for z in N[x] & rem}
        if new == seen:
            return new == rem
        seen = new


def seven_connected(E):
    N = neighbourhoods(E)
    if min(map(len, N)) < 7:
        return False
    for k in range(1, 7):
        for cut in combinations(vertices, k):
            if not connected_after_deleting(N, set(cut)):
                return False
    return True


def set_partitions(items, k):
    blocks = []

    def rec(pos):
        if pos == len(items):
            if len(blocks) == k:
                yield tuple(tuple(block) for block in blocks)
            return
        x = items[pos]
        for block in blocks:
            block.append(x)
            yield from rec(pos + 1)
            block.pop()
        if len(blocks) < k:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


root_partitions = []
for used in combinations(roots, 6):
    root_partitions.append(tuple((x,) for x in used))
for P in set_partitions(roots, 6):
    root_partitions.append(P)


def has_six_contact_model(E):
    N = neighbourhoods(E)

    def conn(B):
        B = set(B)
        seen = {next(iter(B))}
        while True:
            new = seen | {z for x in seen for z in N[x] & B}
            if new == seen:
                return new == B
            seen = new

    for root_partition in root_partitions:
        used_roots = {x for block in root_partition for x in block}
        free = nonroots + tuple(x for x in roots if x not in used_roots)
        # Assignment 0..5 puts a free vertex in a branch set; 6 leaves it unused.
        for assignment in product(range(7), repeat=len(free)):
            B = [set(block) for block in root_partition]
            for x, dest in zip(free, assignment):
                if dest < 6:
                    B[dest].add(x)
            if not all(conn(block) for block in B):
                continue
            if all(any(z in N[x] for x in B[i] for z in B[j])
                   for i in range(6) for j in range(i)):
                return tuple(frozenset(block) for block in B)
    return None


def original_model_ok(E):
    P = ((a, b),) + bags + ((y,),)
    N = neighbourhoods(E)
    return all(any(z in N[x] for x in P[i] for z in P[j])
               for i in range(6) for j in range(i))


def random_search(seed=0, trials=100000):
    rng = Random(seed)
    base = base_edges()
    for trial in range(trials):
        # Fairly dense cross-bag graph is needed for minimum degree seven.
        p = rng.uniform(0.45, 0.9)
        E = set(base)
        for edge in cross_pairs:
            if rng.random() < p:
                add(E, *edge)
        if not original_model_ok(E):
            continue
        if not seven_connected(E):
            continue
        model = has_six_contact_model(E)
        if model is None:
            print("FOUND", trial, sorted(E))
            return E
        if trial % 1000 == 0:
            print("connected_with_model", trial, model)
    print("none", trials)
    return None


if __name__ == "__main__":
    random_search()
