"""Diagnostic: rooted K5 in a W5 repair skeleton with one transit crosslink."""
from itertools import combinations, product
import networkx as nx


def rooted_model(g, roots):
    n = len(g)
    verts = tuple(g)
    candidates = []
    for r in roots:
        others = [v for v in verts if v not in roots and v != r]
        cs = []
        for mask in range(1 << len(others)):
            s = {r} | {others[i] for i in range(len(others)) if mask >> i & 1}
            if nx.is_connected(g.subgraph(s)):
                cs.append(frozenset(s))
        candidates.append(cs)
    order = sorted(range(5), key=lambda i: len(candidates[i]))
    bags = [None] * 5

    def adjacent(a, b):
        return any(g.has_edge(x, y) for x in a for y in b)

    def rec(k, used):
        if k == 5:
            return tuple(bags)
        i = order[k]
        for s in candidates[i]:
            if s & used:
                continue
            if all(bags[j] is None or adjacent(s, bags[j]) for j in range(5)):
                bags[i] = s
                ans = rec(k + 1, used | s)
                if ans:
                    return ans
                bags[i] = None
        return None

    return rec(0, frozenset())


def host(n1, n2, marks1, mark2, cross1, cross2):
    a = [f"a{i}" for i in range(n1)]
    b = [f"b{i}" for i in range(n2)]
    g = nx.Graph()
    g.add_edges_from(zip(a, a[1:]))
    g.add_edges_from(zip(b, b[1:]))
    # rim edges a0-b0-aN-bN-a0 and hub z to all four rim roots
    g.add_edges_from([(a[0], b[0]), (b[0], a[-1]),
                      (a[-1], b[-1]), (b[-1], a[0])])
    g.add_edges_from(("z", x) for x in (a[0], a[-1], b[0], b[-1]))
    g.add_edge(a[cross1], b[cross2])
    roots = tuple(a[i] for i in marks1) + (b[mark2], "z")
    return g, roots


def main():
    bad = []
    total = 0
    for n1, n2 in product(range(3, 7), range(3, 6)):
        for marks1 in combinations(range(n1), 3):
            for mark2 in range(n2):
                for cross1 in marks1:  # transit begins at a first-hit mark
                    for cross2 in range(n2):
                        total += 1
                        g, roots = host(n1, n2, marks1, mark2, cross1, cross2)
                        if not rooted_model(g, roots):
                            bad.append((n1, n2, marks1, mark2, cross1, cross2))
                            if len(bad) >= 20:
                                print("total_prefix", total, "bad", bad)
                                return
    print("total", total, "bad", bad)


if __name__ == "__main__":
    main()
