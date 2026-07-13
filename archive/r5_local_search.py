from itertools import combinations


V = tuple("abcdefgy")
assert len(V) == 8 and len(set(V)) == 8, V

E = set()


def edge(x, y):
    E.add(frozenset((x, y)))


edge("a", "b")
edge("c", "d")
for x, y in [
    ("a", "c"),
    ("a", "e"),
    ("b", "f"),
    ("b", "g"),
    ("c", "e"),
    ("d", "f"),
    ("d", "g"),
    ("e", "f"),
    ("e", "g"),
    ("f", "g"),
]:
    edge(x, y)
for x in "abcdefg":
    edge(x, "y")

N_v = set("abcdefg")


def connected(block):
    if not block:
        return False
    seen = {next(iter(block))}
    while True:
        new = seen | {
            y
            for x in seen
            for y in block - seen
            if frozenset((x, y)) in E
        }
        if new == seen:
            return new == block
        seen = new


def adjacent(a, b):
    return any(frozenset((x, y)) in E for x in a for y in b)


def partitions(seq, k):
    # Canonical unlabeled set partitions into exactly k blocks.
    blocks = []

    def rec(pos):
        if pos == len(seq):
            if len(blocks) == k:
                yield tuple(frozenset(b) for b in blocks)
            return
        remaining = len(seq) - pos
        if len(blocks) > k or len(blocks) + remaining < k:
            return
        x = seq[pos]
        for b in blocks:
            b.add(x)
            yield from rec(pos + 1)
            b.remove(x)
        if len(blocks) < k:
            blocks.append({x})
            yield from rec(pos + 1)
            blocks.pop()

    yield from rec(0)


models = []
partition_count = 0
for size in range(6, len(V) + 1):
    for support in combinations(V, size):
        for P in partitions(support, 6):
            partition_count += 1
            if not all(connected(B) for B in P):
                continue
            if not all(adjacent(P[i], P[j]) for i in range(6) for j in range(i)):
                continue
            s = sum(bool(B & N_v) for B in P)
            sq = sum(len(B) ** 2 for B in P)
            models.append((s, sq, P))

models.sort(key=lambda z: (-z[0], z[1]))
print("vertices", V)
print("edges", len(E))
print("partitions_checked", partition_count)
print("models", len(models))
print("best", models[0][:2] if models else None)
for m in models[:10]:
    print(m)
