"""Probe the full/full unique-interface quotient over K7-(C6+K1)."""

from contact_order7_sixedge_web_probe import generic_minor_model


S = tuple(range(7))
RIM = tuple(range(6))
Z = 6
H, X, Y = 7, 8, 9


def norm(a, b):
    return tuple(sorted((a, b)))


edges = set()
for i in RIM:
    for j in RIM:
        if i < j and (i - j) % 6 not in (1, 5):
            edges.add((i, j))
for i in RIM:
    edges.add(norm(Z, i))
for s in S:
    for helper in (H, X, Y):
        edges.add(norm(s, helper))
edges.add(norm(X, Y))

model = generic_minor_model(10, edges, 7)
assert model is not None
decoded = tuple(
    tuple(v for v in range(10) if mask & (1 << v)) for mask in model
)
print(decoded)

# One canonical certificate is
# {c0}|{c2}|{c4}|{z}|H|{X,c1}|{Y,c3}.
expected = ({0}, {2}, {4}, {6}, {7}, {8, 1}, {9, 3})
assert all(any(set(block) == bag for block in decoded) for bag in expected)
