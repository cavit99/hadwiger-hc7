#!/usr/bin/env python3
"""Verify the minimum degree-eight portal-role-erasure local barrier."""

from itertools import combinations


S = {"p", "q", "i1", "i2", "i3", "t1", "t2", "t3"}
I = {"i1", "i2", "i3"}
T = {"t1", "t2", "t3"}
Q = {"a", "b", "c", "d", "r2", "r3", "s3"}
F = {"x", "y"}
U = {"u"}
V = S | Q | F | U


def edge(v: str, w: str) -> tuple[str, str]:
    require(v != w, "loops are forbidden")
    return tuple(sorted((v, w)))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


EDGES: set[tuple[str, str]] = set()


def add(v: str, w: str) -> None:
    EDGES.add(edge(v, w))


for triangle in (("p", "i2", "t2"), ("q", "i3", "t3")):
    for v, w in combinations(triangle, 2):
        add(v, w)
add("i1", "t1")

for s in S:
    add("u", s)

for v, w in (
    ("c", "a"),
    ("c", "b"),
    ("c", "r2"),
    ("c", "r3"),
    ("c", "s3"),
    ("d", "a"),
    ("d", "b"),
):
    add(v, w)

CONTACTS = {
    "a": {"p", "i1"},
    "b": {"q", "t1"},
    "c": {"i2", "i3", "t2", "t3"},
    "d": {"i1", "t1"},
    "r2": {"i2", "t2"},
    "r3": {"i3"},
    "s3": {"t3"},
}
for v, contacts in CONTACTS.items():
    for s in contacts:
        add(v, s)

add("x", "y")
for s in S - {"q"}:
    add("x", s)
for s in S - {"p"}:
    add("y", s)


def adjacent(v: str, w: str, edges: set[tuple[str, str]] = EDGES) -> bool:
    return v != w and edge(v, w) in edges


def neighbours(v: str, universe: set[str] = V) -> set[str]:
    return {w for w in universe if adjacent(v, w)}


def connected(vertices: set[str], edges: set[tuple[str, str]] = EDGES) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        enlarged = reached | {
            v
            for v in vertices - reached
            if any(adjacent(v, w, edges) for w in reached)
        }
        if enlarged == reached:
            return reached == vertices
        reached = enlarged


def components(vertices: set[str], edges: set[tuple[str, str]] = EDGES) -> list[set[str]]:
    remaining = set(vertices)
    answer: list[set[str]] = []
    while remaining:
        seed = next(iter(remaining))
        component = {seed}
        while True:
            enlarged = component | {
                v
                for v in remaining - component
                if any(adjacent(v, w, edges) for w in component)
            }
            if enlarged == component:
                break
            component = enlarged
        answer.append(component)
        remaining -= component
    return answer


def all_subsets(vertices: set[str]):
    ordered = tuple(sorted(vertices))
    for mask in range(1, 1 << len(ordered)):
        yield {ordered[i] for i in range(len(ordered)) if mask & (1 << i)}


def boundary_contacts(vertices: set[str]) -> set[str]:
    return {s for s in S if any(adjacent(v, s) for v in vertices)}


def proper_colouring(vertices: set[str], colouring: dict[str, int]) -> bool:
    return vertices <= colouring.keys() and all(
        colouring[v] != colouring[w]
        for v, w in EDGES
        if v in vertices and w in vertices
    )


def boundary_partition(colouring: dict[str, int]) -> set[frozenset[str]]:
    return {
        frozenset(s for s in S if colouring[s] == colour)
        for colour in {colouring[s] for s in S}
    }


def path_is_valid(path: tuple[str, ...], colouring: dict[str, int]) -> bool:
    return (
        len(set(path)) == len(path)
        and all(adjacent(v, w) for v, w in zip(path, path[1:]))
        and len({colouring[v] for v in path}) == 2
        and all(colouring[v] != colouring[w] for v, w in zip(path, path[1:]))
        and not (set(path[1:-1]) & S)
    )


# Static boundary and degree-eight interface.
boundary_components = {frozenset(component) for component in components(S)}
require(
    boundary_components
    == {
        frozenset({"p", "i2", "t2"}),
        frozenset({"q", "i3", "t3"}),
        frozenset({"i1", "t1"}),
    },
    "wrong compact boundary",
)
independence_number = max(
    len(A)
    for A in all_subsets(S)
    if all(not adjacent(v, w) for v, w in combinations(A, 2))
)
require(independence_number == 3, "boundary independence number is not three")
require(neighbours("u") == S, "u must have degree eight with neighbourhood S")
outside_components = {frozenset(component) for component in components(Q | F)}
require(outside_components == {frozenset(Q), frozenset(F)}, "wrong two shores")
require(boundary_contacts(Q) == S, "Q is not boundary-full")
require(boundary_contacts(F) == S, "F is not boundary-full")


# Fixed opposite boundary partitions and the bilateral odd path cycle.
merged = {s: 0 for s in I} | {s: 1 for s in T} | {"p": 2, "q": 2}
merged |= {"a": 3, "b": 3, "c": 2, "d": 2, "r2": 3, "r3": 1, "s3": 0}
split = {s: 0 for s in I} | {s: 1 for s in T} | {"p": 2, "q": 3}
split |= {"x": 3, "y": 2}
require(proper_colouring(S | Q, merged), "merged Q-shore colouring is improper")
require(proper_colouring(S | F, split), "split F-shore colouring is improper")
require(
    boundary_partition(merged)
    == {frozenset(I), frozenset(T), frozenset({"p", "q"})},
    "wrong merged boundary partition",
)
require(
    boundary_partition(split)
    == {frozenset(I), frozenset(T), frozenset({"p"}), frozenset({"q"})},
    "wrong split boundary partition",
)
P_Q = ("p", "a", "c", "b", "q")
P_F = ("p", "x", "y", "q")
require(path_is_valid(P_Q, merged), "invalid merged-shore path")
require(path_is_valid(P_F, split), "invalid split-shore path")
cycle_edges = {
    edge(v, w)
    for path in (P_Q, P_F)
    for v, w in zip(path, path[1:])
}
cycle_vertices = set(P_Q) | set(P_F)
require(len(cycle_edges) == 7 and len(cycle_vertices) == 7, "path union is not a 7-cycle")
require(
    all(sum(edge(v, w) in cycle_edges for w in cycle_vertices - {v}) == 2 for v in cycle_vertices),
    "path union is not a simple cycle",
)


# Four incidence splits and the absence of a two-defect residual component.
q_residual = components(Q - set(P_Q[1:-1]))
expected_q_residual = {
    frozenset({"d"}),
    frozenset({"r2"}),
    frozenset({"r3"}),
    frozenset({"s3"}),
}
require({frozenset(C) for C in q_residual} == expected_q_residual, "wrong Q residual")
require(not (F - set(P_F[1:-1])), "the F path should fill its shore")
for block in (I, T):
    seen_parts = {
        frozenset(boundary_contacts(C) & block)
        for C in q_residual
        if boundary_contacts(C) & block
    }
    require(len(seen_parts) >= 2, f"{sorted(block)} does not split in Q")
require(
    all(len(S - boundary_contacts(C)) != 2 for C in q_residual),
    "unexpected two-defect Q residual component",
)


# Exhaustive universal connector--carrier intersection in each shore.
def root_connectors(shore: set[str]) -> list[set[str]]:
    return [
        R
        for R in all_subsets(shore)
        if connected(R)
        and any(adjacent(v, "p") for v in R)
        and any(adjacent(v, "q") for v in R)
    ]


def carriers(shore: set[str], block: set[str]) -> list[set[str]]:
    return [R for R in all_subsets(shore) if connected(R | block)]


entanglement_counts: list[tuple[str, int, int]] = []
for shore_name, shore in (("Q", Q), ("F", F)):
    roots = root_connectors(shore)
    require(roots, f"no root connector in {shore_name}")
    for block_name, block in (("I", I), ("T", T)):
        block_carriers = carriers(shore, block)
        require(block_carriers, f"no {block_name}-carrier in {shore_name}")
        require(
            all(not root.isdisjoint(carrier) for root in roots for carrier in block_carriers),
            f"disjoint root connector and {block_name}-carrier in {shore_name}",
        )
        entanglement_counts.append((shore_name + block_name, len(roots), len(block_carriers)))


# The same terminal-free positive lobe in both completions.
K = {"a", "b", "r2", "r3", "s3"}
C = {"c"}
I_nominees = {"p": "a", "q": "b", "i1": "d", "i2": "r2", "i3": "r3"}
T_nominees = {"p": "a", "q": "b", "t1": "d", "t2": "r2", "t3": "s3"}


def completed_edges(nominees: dict[str, str], block: set[str]) -> set[tuple[str, str]]:
    answer = {e for e in EDGES if e[0] in Q and e[1] in Q}
    root_p = nominees["p"]
    root_q = nominees["q"]
    answer.add(edge(root_p, root_q))
    for label in block:
        terminal = nominees[label]
        answer.add(edge(terminal, root_p))
        answer.add(edge(terminal, root_q))
    return answer


for name, nominees, block in (("I", I_nominees, I), ("T", T_nominees, T)):
    require(len(set(nominees.values())) == 5, f"{name} nominees are not distinct")
    require(
        all(adjacent(vertex, label) for label, vertex in nominees.items()),
        f"{name} nominee is outside its portal set",
    )
    completion_components = {
        frozenset(component)
        for component in components(Q - K, completed_edges(nominees, block))
    }
    require(completion_components == {frozenset(C), frozenset({"d"})}, f"wrong {name} cut")
    require(C.isdisjoint(nominees.values()), f"C is not terminal-free for {name}")

require(neighbours("c", Q) == K, "wrong internal lobe boundary")
require(boundary_contacts(C) == {"i2", "i3", "t2", "t3"}, "wrong lobe contacts")
full_lobe_boundary = neighbours("c")
require(len(full_lobe_boundary) == 9, "positive lobe boundary is not nine")
require(len(S - boundary_contacts(C)) == 4, "positive lobe defect is not four")
require(V - (C | full_lobe_boundary), "lobe boundary is not an actual separation")


# Exhaust all disjoint adjacent connected pairs in Q.
connected_subsets = [A for A in all_subsets(Q) if connected(A)]
candidate_pairs = 0
maximum_common_contacts = 0
for index, A in enumerate(connected_subsets):
    for B in connected_subsets[index + 1 :]:
        if A & B:
            continue
        if not any(adjacent(v, w) for v in A for w in B):
            continue
        candidate_pairs += 1
        maximum_common_contacts = max(
            maximum_common_contacts,
            len(boundary_contacts(A) & boundary_contacts(B)),
        )
require(maximum_common_contacts < 6, "a forbidden common-near-full pair exists")


# Explicitly certify the failed global hypothesis.
require(neighbours("r3") == {"c", "i3"}, "unexpected low-degree witness")
global_five_colouring = {
    "c": 0,
    "u": 0,
    "y": 0,
    "x": 1,
    "i3": 2,
    "t2": 2,
    "i2": 3,
    "t3": 3,
    "t1": 2,
    "i1": 3,
    "q": 1,
    "p": 4,
    "b": 3,
    "a": 1,
    "d": 0,
    "r2": 1,
    "s3": 1,
    "r3": 1,
}
require(proper_colouring(V, global_five_colouring), "displayed global five-colouring is improper")

print("GREEN degree8 portal role-erasure local barrier")
print(
    "boundary: order=8 alpha=3; shores=(7,2); bilateral_cycle=7; "
    "Q_residual_components=4 two_defect=0"
)
print(
    "entanglement: "
    + " ".join(f"{name}=({roots},{block_carriers})" for name, roots, block_carriers in entanglement_counts)
)
print(
    f"common_lobe: internal_boundary={len(K)} full_boundary={len(full_lobe_boundary)} "
    f"defect={len(S - boundary_contacts(C))}; connected_subsets={len(connected_subsets)} "
    f"adjacent_disjoint_pairs={candidate_pairs} max_common_contacts={maximum_common_contacts}"
)
print("scope: not seven-connected; globally five-colourable; no critical entering-edge responses")
