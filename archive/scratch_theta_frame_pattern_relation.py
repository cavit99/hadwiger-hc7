import itertools


def canon(word):
    mp = {}
    out = []
    for x in word:
        if x not in mp:
            mp[x] = len(mp)
        out.append(mp[x])
    return tuple(out)


patterns = {
    (0, 1, 0, 1): "P4",
    (0, 1, 0, 2): "PA",
    (0, 1, 2, 1): "PB",
    (0, 1, 2, 3): "P0",
}


def ptype(assign, order):
    w = tuple(assign[x] for x in order)
    c = canon(w)
    return patterns.get(c)


A = (0, 1, 5, 2)
B = (1, 0, 5, 2)
relation = set()
states = {}
for vals in itertools.product(range(4), repeat=5):
    a = dict(zip((0, 1, 2, 4, 5), vals))
    # actual boundary edges 04,14,25
    if a[0] == a[4] or a[1] == a[4] or a[2] == a[5]:
        continue
    pa, pb = ptype(a, A), ptype(a, B)
    if pa and pb:
        relation.add((pa, pb))
        states.setdefault((pa, pb), canon(vals))

print(sorted(relation))
P = ["P4", "PA", "PB", "P0"]
for omit_a in [None] + P:
    for omit_b in [None] + P:
        ea = set(P) - ({omit_a} if omit_a else set())
        eb = set(P) - ({omit_b} if omit_b else set())
        ok = [(x, y) for x, y in relation if x in ea and y in eb]
        if not ok:
            print("FAIL", omit_a, omit_b)
