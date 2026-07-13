"""Verify the strict-surplus unbalanced tree-society counterarchitecture.

This is an interface falsifier, not a counterexample to HC7.
"""

from itertools import combinations

B = {"a", "c", "q1", "q2", "q3"}
P = [f"p{i}" for i in range(1, 6)]
R = [f"z{i}" for i in range(1, 5)]
D = P + R
E = ["u", "v", "r1", "r2"]

edges: set[frozenset[str]] = set()


def add(x: str, *ys: str) -> None:
    for y in ys:
        edges.add(frozenset((x, y)))


# The two tree bags.
for x, y in zip(D, D[1:]):
    add(x, y)
add("u", "v")
add("v", "r1", "r2")

# Boundary rows: P is full, R has the unique defect c.
for x in P:
    add(x, *sorted(B))
for x in R:
    add(x, "a", "q1", "q2", "q3")

# Cross rows.  The three R-portals in E are v,r1,r2.
for x in P:
    add(x, "u", "v")
add("z1", "v", "r1")
add("z2", "v", "r2")
add("z3", "r1", "r2")
add("z4", "v", "r1", "r2")

# Boundary rows of E.  The R-hit vertices are all c-dark.
add("u", "a", "c")
add("v", "q1", "q2", "q3")
add("r1", "a", "q1", "q2", "q3")
add("r2", "a", "q1", "q2", "q3")


def adjacent(x: str, y: str) -> bool:
    return frozenset((x, y)) in edges


def connected(vertices: set[str], tree_vertices: list[str]) -> bool:
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    while True:
        old = len(seen)
        for x in tuple(seen):
            seen.update(y for y in vertices if adjacent(x, y))
        if len(seen) == old:
            return seen == vertices


def open_neighborhood(vertices: set[str]) -> set[str]:
    return {
        y
        for edge in edges
        if edge & vertices
        for y in edge - vertices
    }


def connected_subsets(tree: list[str]):
    for size in range(1, len(tree)):
        for choice in combinations(tree, size):
            subset = set(choice)
            if connected(subset, tree):
                yield subset


assert all(len(open_neighborhood(x)) >= 8 for x in connected_subsets(D))
assert all(len(open_neighborhood(x)) >= 8 for x in connected_subsets(E))

r_portals = {e for e in E if any(adjacent(e, r) for r in R)}
assert r_portals == {"v", "r1", "r2"}
assert len(r_portals) == 3  # m_R+2 for the unique defect c.
assert all(not adjacent(e, "c") for e in r_portals)

# W=uv protects a,c at u and q1,q2,q3 at v.  The off-core R-lobes
# r1,r2 have the common owner defect c.
W = {"u", "v"}
assert all(not adjacent(x, "c") for x in {"r1", "r2"})

# No edge split E=Z|Y has Z meeting R and c while Y retains
# a,c,q1,q2,q3.
exchange_splits = []
for edge in [("u", "v"), ("v", "r1"), ("v", "r2")]:
    reduced = set(edges)
    reduced.remove(frozenset(edge))
    # The components of the four-vertex tree after deleting edge.
    for seed in edge:
        comp = {seed}
        while True:
            old = len(comp)
            for x in tuple(comp):
                comp.update(
                    y for y in E if frozenset((x, y)) in reduced
                )
            if len(comp) == old:
                break
        other = set(E) - comp
        for Z, Y in [(comp, other), (other, comp)]:
            z_has_r = any(z in r_portals for z in Z)
            z_has_c = any(adjacent(z, "c") for z in Z)
            y_full = all(any(adjacent(y, s) for y in Y) for s in B)
            if z_has_r and z_has_c and y_full:
                exchange_splits.append((edge, Z, Y))

assert not exchange_splits

# In the K5^- rotation a,q3,c,D, the central edge has opposite classes
# {a,c} on u and {q3,D} on v: it is a nonrural alternating cut.
assert adjacent("u", "a") and adjacent("u", "c")
assert adjacent("v", "q3") and "v" in r_portals

print("strict surplus=3, minimum proper connected-fragment boundary=8")
print("nonrural owner cut uv; no protected two-bag exchange")
