#!/usr/bin/env python3
"""Verify the n=7 fixed-trace edge-rotation barrier."""

from itertools import combinations


def add(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def build():
    k = [("k", i) for i in range(4)]
    j = [("j", i) for i in range(3)]
    s = set(k + j)
    r = [("r", i) for i in range(7)]
    a = ("a", 0)
    adj = {v: set() for v in [a] + k + j + r}
    for u, v in combinations(k, 2):
        add(adj, u, v)
    for i in range(7):
        add(adj, r[i], r[(i + 1) % 7])
    for x in r:
        for y in s:
            add(adj, x, y)
    for y in s:
        add(adj, a, y)
    return adj, a, k, j, r, s


def connected(adj, deleted=frozenset()):
    left = set(adj) - set(deleted)
    if len(left) <= 1:
        return True
    root = next(iter(left))
    seen = {root}
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v in left and v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == left


def connectivity(adj):
    vertices = list(adj)
    for size in range(len(vertices)):
        for cut in combinations(vertices, size):
            if not connected(adj, cut):
                return size
    return len(vertices) - 1


def colourable(adj, q, fixed=None):
    fixed = dict(fixed or {})
    colour = dict(fixed)
    for u, c in fixed.items():
        if c < 0 or c >= q:
            return False
        if any(v in fixed and fixed[v] == c for v in adj[u]):
            return False

    def search():
        if len(colour) == len(adj):
            return dict(colour)
        uncoloured = [v for v in adj if v not in colour]
        u = max(
            uncoloured,
            key=lambda x: (
                len({colour[y] for y in adj[x] if y in colour}),
                len(adj[x]),
            ),
        )
        forbidden = {colour[v] for v in adj[u] if v in colour}
        for c in range(q):
            if c not in forbidden:
                colour[u] = c
                result = search()
                if result is not None:
                    return result
                del colour[u]
        return None

    return search()


def delete_edge(adj, e):
    u, v = e
    out = {x: set(n) for x, n in adj.items()}
    out[u].remove(v)
    out[v].remove(u)
    return out


def contract_edge(adj, e):
    u, v = e
    w = ("contract", repr(u), repr(v))
    out = {x: set() for x in adj if x not in {u, v}}
    out[w] = set()
    for x in adj:
        for y in adj[x]:
            if repr(x) >= repr(y):
                continue
            xx = w if x in {u, v} else x
            yy = w if y in {u, v} else y
            if xx != yy:
                add(out, xx, yy)
    return out


def induced_connected(adj, vertices):
    vertices = set(vertices)
    root = next(iter(vertices))
    seen = {root}
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u] & vertices:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen == vertices


def main():
    g, a, k, j, r, s = build()
    assert len(g) == 15
    assert sum(map(len, g.values())) // 2 == 69
    assert connectivity(g) == 7
    assert colourable(g, 6) is None
    assert colourable(g, 7) is not None

    sigma = {k[i]: i for i in range(4)}
    sigma.update({x: 0 for x in j})

    cycle_edges = [(r[i], r[(i + 1) % 7]) for i in range(7)]
    for e in cycle_edges:
        ge = delete_edge(g, e)
        c = colourable(ge, 6, sigma)
        assert c is not None and c[e[0]] == c[e[1]]
        assert colourable(ge, 5) is None

        gc = contract_edge(g, e)
        assert colourable(gc, 6) is not None
        assert colourable(gc, 5) is None

    e = (r[6], r[0])
    ep = (r[3], r[4])
    d = set(r[:4])
    u = set(r[4:])
    b = {a, *j}
    bags = [b, d, u] + [{x} for x in k]
    assert set().union(*bags) == set(g)
    assert sum(map(len, bags)) == len(g)
    assert all(induced_connected(g, bag) for bag in bags)
    for x, y in combinations(bags, 2):
        assert any(v in g[z] for z in x for v in y)
    for removed in (e, ep):
        h = delete_edge(g, removed)
        for x, y in combinations(bags, 2):
            assert any(v in h[z] for z in x for v in y)

    # With the four boundary colours forbidden, the cycle has the common
    # two-colour list {4,5}; it is the unique vertex-minimal obstruction.
    rset = set(r)
    assert colourable({x: g[x] & rset for x in r}, 2) is None
    for x in r:
        smaller = rset - {x}
        h = {v: g[v] & smaller for v in smaller}
        assert colourable(h, 2) is not None

    print("GREEN fixed-trace edge-rotation barrier")
    print("G: vertices=15 edges=69 connectivity=7 chromatic_number=7")
    print("both edge deletions and contractions: chromatic_number=6, exact Sigma")
    print("spanning K7 model survives either repeated D-U contact deletion")
    print("fixed-trace critical kernel: entire C7 for every deleted cycle edge")


if __name__ == "__main__":
    main()
