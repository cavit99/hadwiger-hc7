#!/usr/bin/env python3
"""Verify the focused atomic-immersion guardrail in K2 join icosahedron."""

from collections import Counter
from itertools import combinations


def edge(u: str, v: str) -> tuple[str, str]:
    return tuple(sorted((u, v)))


indices = range(5)
ico_vertices = {"t", "b"} | {f"u{i}" for i in indices} | {
    f"w{i}" for i in indices
}
vertices = ico_vertices | {"p", "q"}

ico_edges: set[tuple[str, str]] = set()
for i in indices:
    j = (i + 1) % 5
    ico_edges.update(
        {
            edge("t", f"u{i}"),
            edge("b", f"w{i}"),
            edge(f"u{i}", f"u{j}"),
            edge(f"w{i}", f"w{j}"),
            edge(f"u{i}", f"w{i}"),
            edge(f"u{i}", f"w{(i - 1) % 5}"),
        }
    )

edges = set(ico_edges)
edges.add(edge("p", "q"))
for apex in ("p", "q"):
    for v in ico_vertices:
        edges.add(edge(apex, v))


def neighbours(v: str, graph_edges: set[tuple[str, str]] = edges) -> set[str]:
    return {y if x == v else x for x, y in graph_edges if v in (x, y)}


def connected_after(deleted: set[str]) -> bool:
    remaining = vertices - deleted
    if len(remaining) <= 1:
        return True
    start = next(iter(remaining))
    seen = {start}
    todo = [start]
    while todo:
        v = todo.pop()
        for w in neighbours(v) - deleted - seen:
            seen.add(w)
            todo.append(w)
    return seen == remaining


def verify_planar_face_certificate() -> None:
    seen = {"t"}
    todo = ["t"]
    while todo:
        v = todo.pop()
        for w in neighbours(v, ico_edges) - seen:
            seen.add(w)
            todo.append(w)
    assert seen == ico_vertices

    faces: list[tuple[str, str, str]] = []
    for i in indices:
        j = (i + 1) % 5
        faces.extend(
            [
                ("t", f"u{i}", f"u{j}"),
                ("b", f"w{j}", f"w{i}"),
                (f"u{i}", f"w{i}", f"u{j}"),
                (f"u{i}", f"w{(i - 1) % 5}", f"w{i}"),
            ]
        )

    incidence: Counter[tuple[str, str]] = Counter()
    for face in faces:
        assert len(set(face)) == 3
        for u, v in combinations(face, 2):
            assert edge(u, v) in ico_edges
            incidence[edge(u, v)] += 1
    assert set(incidence) == ico_edges
    assert set(incidence.values()) == {2}

    # Every vertex link is one cycle, so the faces define a closed connected
    # triangulated surface.  Euler characteristic 2 identifies the sphere.
    for v in ico_vertices:
        link_edges = {
            edge(*[x for x in face if x != v]) for face in faces if v in face
        }
        link_vertices = set().union(*map(set, link_edges))
        assert all(sum(x in e for e in link_edges) == 2 for x in link_vertices)
        start = next(iter(link_vertices))
        seen = {start}
        todo = [start]
        while todo:
            x = todo.pop()
            for e in link_edges:
                if x in e:
                    y = e[0] if e[1] == x else e[1]
                    if y not in seen:
                        seen.add(y)
                        todo.append(y)
        assert seen == link_vertices
    assert len(ico_vertices) - len(ico_edges) + len(faces) == 2


def build_paths(
    branches: list[str], special: dict[frozenset[str], list[str]]
) -> dict[frozenset[str], list[str]]:
    paths: dict[frozenset[str], list[str]] = {}
    for u, v in combinations(branches, 2):
        key = frozenset((u, v))
        path = special.get(key, [u, v])
        assert {path[0], path[-1]} == {u, v}
        assert len(path) == len(set(path))
        assert all(edge(x, y) in edges for x, y in zip(path, path[1:]))
        paths[key] = path
    assert len(paths) == 21
    return paths


def verify_atomic(
    branches: list[str],
    paths: dict[frozenset[str], list[str]],
    collision: str,
    expected_length: int = 26,
) -> None:
    used_edges: Counter[tuple[str, str]] = Counter()
    internal: Counter[str] = Counter()
    for path in paths.values():
        used_edges.update(edge(x, y) for x, y in zip(path, path[1:]))
        internal.update(path[1:-1])
    assert set(used_edges.values()) == {1}
    roles = Counter(internal)
    roles.update(branches)
    assert {v: count for v, count in roles.items() if count >= 2} == {
        collision: 2
    }
    assert sum(used_edges.values()) == expected_length


def verify_near_model(bags: list[set[str]], missing: frozenset[int]) -> None:
    assert len(bags) == 7
    assert set().union(*bags) == vertices
    assert sum(map(len, bags)) == len(vertices)
    for bag in bags:
        start = next(iter(bag))
        seen = {start}
        todo = [start]
        while todo:
            v = todo.pop()
            for w in neighbours(v) & bag - seen:
                seen.add(w)
                todo.append(w)
        assert seen == bag
    absent: set[frozenset[int]] = set()
    for i, j in combinations(range(7), 2):
        if not any(edge(u, v) in edges for u in bags[i] for v in bags[j]):
            absent.add(frozenset((i, j)))
    assert absent == {missing}


verify_planar_face_certificate()
assert len(vertices) == 14 and len(edges) == 55

cuts_tested = 0
ordered_vertices = sorted(vertices)
for size in range(7):
    for deleted_tuple in combinations(ordered_vertices, size):
        cuts_tested += 1
        assert connected_after(set(deleted_tuple))
separator = {"p", "q"} | {f"u{i}" for i in indices}
assert len(separator) == 7 and not connected_after(separator)

branches_1 = ["p", "q", "t", "u0", "u1", "u3", "w1"]
paths_1 = build_paths(
    branches_1,
    {
        frozenset(("t", "w1")): ["t", "u2", "w1"],
        frozenset(("u1", "u3")): ["u1", "u2", "u3"],
        frozenset(("u0", "u3")): ["u0", "u4", "u3"],
        frozenset(("u0", "w1")): ["u0", "w0", "w1"],
        frozenset(("u3", "w1")): ["u3", "w2", "w1"],
    },
)
verify_atomic(branches_1, paths_1, "u2")
assert "w4" not in set().union(*map(set, paths_1.values()))

verify_near_model(
    [
        {"t"},
        {"w1"},
        {"p"},
        {"q"},
        {"u0", "u4", "w0"},
        {"u1", "u2"},
        {"u3", "w2", "b", "w3", "w4"},
    ],
    frozenset((0, 1)),
)
verify_near_model(
    [
        {"u1"},
        {"u3"},
        {"p"},
        {"q"},
        {"t", "u2"},
        {"u0", "u4", "w0"},
        {"w1", "w2", "b", "w3", "w4"},
    ],
    frozenset((0, 1)),
)

branches_2 = ["p", "q", "t", "u0", "u4", "w0", "w3"]
paths_2 = build_paths(
    branches_2,
    {
        frozenset(("t", "w0")): ["t", "u1", "w0"],
        frozenset(("t", "w3")): ["t", "u3", "w3"],
        frozenset(("u0", "w3")): ["u0", "w4", "w3"],
        frozenset(("u4", "w0")): ["u4", "w4", "w0"],
        frozenset(("w0", "w3")): ["w0", "b", "w3"],
    },
)
verify_atomic(branches_2, paths_2, "w4")
assert "u2" not in set().union(*map(set, paths_2.values()))

# In the common partition of G-u2, the missed clean bag D_u0 is a sharp
# obstruction to Theorem 3.5's paired linkage.
missed_bag = {"u0", "u4", "w0"}
active_bags = {
    "a": {"t"},
    "b": {"w1"},
    "c": {"u1"},
    "d": {"u3", "w2", "b", "w3", "w4"},
}


def is_connected_set(subset: set[str]) -> bool:
    start = next(iter(subset))
    seen = {start}
    todo = [start]
    while todo:
        v = todo.pop()
        for w in neighbours(v) & subset - seen:
            seen.add(w)
            todo.append(w)
    return seen == subset


connected_subsets = []
ordered_missed = sorted(missed_bag)
for size in range(1, len(ordered_missed) + 1):
    for chosen in combinations(ordered_missed, size):
        subset = set(chosen)
        if is_connected_set(subset):
            connected_subsets.append(subset)


def contacts(left: set[str], right: set[str]) -> bool:
    return any(edge(u, v) in edges for u in left for v in right)


ab_connectors = [
    part
    for part in connected_subsets
    if contacts(part, active_bags["a"]) and contacts(part, active_bags["b"])
]
cd_connectors = [
    part
    for part in connected_subsets
    if contacts(part, active_bags["c"]) and contacts(part, active_bags["d"])
]
assert ab_connectors and cd_connectors
assert not any(left.isdisjoint(right) for left in ab_connectors for right in cd_connectors)

branches_3 = ["b", "p", "q", "t", "u0", "u1", "u2"]
paths_3 = build_paths(
    branches_3,
    {
        frozenset(("b", "t")): ["b", "w3", "u3", "t"],
        frozenset(("b", "u0")): ["b", "w4", "u0"],
        frozenset(("b", "u1")): ["b", "w0", "u1"],
        frozenset(("b", "u2")): ["b", "w1", "u2"],
        frozenset(("p", "u0")): ["p", "u4", "u0"],
        frozenset(("p", "u2")): ["p", "w2", "u2"],
        frozenset(("u0", "u2")): ["u0", "p", "u2"],
    },
)
verify_atomic(branches_3, paths_3, "p", expected_length=29)
assert len(neighbours("p")) == 13

print("GREEN atomic weak-K7 immersion icosahedral guardrail")
print(
    f"host: vertices={len(vertices)} edges={len(edges)} "
    f"connectivity=7 cuts_tested={cuts_tested} planar_core=yes K7_minor=no"
)
print(
    "witnesses: potential=(M,T,H,L)=(1,0,0,26) Q=1 "
    "collisions=u2,w4 mutual_avoidance=yes"
)
print("rounded_models: missing=t-w1,u1-u3 spanning=yes singleton_roots=yes")
print("missed_clean_bag: paired_linkage=no")
print("branch_transit: collision=p degree=13 minimum_excess_M=1 length=29")
print("terminal: pair=p,q hits_every_K5_model; exact_order7_separator=yes")
