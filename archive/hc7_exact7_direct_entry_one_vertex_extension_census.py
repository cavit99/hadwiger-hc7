#!/usr/bin/env python3
"""Census role-labelled one-vertex extensions of the direct-entry barrier.

The search is deliberately finite and fixed-skeleton.  It retains the
seven-boundary, the displayed colouring on the old vertices, the two full
connected subgraphs in the four-vertex shore, and an exact critical-triangle
response obtained by adding one new outer endpoint.
"""

from itertools import combinations


S = tuple(range(7))
A = ("a1", "a2", "c1", "c2")
B = ("b",)
W = "w"
VERTICES = S + A + B + (W,)
V = 1


def edge(left, right):
    return frozenset((left, right))


BASE_EDGES = {edge(i, (i + 1) % 7) for i in S}
BASE_EDGES.update((edge(0, 2), edge(1, 3)))
BASE_EDGES.update((edge("a1", "a2"), edge("a2", "c1"), edge("c1", "c2")))

CONTACTS = {
    "a1": {0, 1, 4, 5, 6},
    "a2": {2, 3, 4, 5},
    "c1": {0, 2, 5, 6},
    "c2": {1, 2, 3, 4, 5, 6},
    "b": set(S),
}
for vertex, contacts in CONTACTS.items():
    BASE_EDGES.update(edge(vertex, boundary) for boundary in contacts)

COLOUR = {
    0: 4,
    1: 0,
    2: 1,
    3: 4,
    4: 2,
    5: 4,
    6: 3,
    "a1": 1,
    "a2": 3,
    "c1": 2,
    "c2": 5,
    "b": 5,
    W: 0,
}

# One fixed proper five-colouring works for every extension in the A-shore.
FIVE_COLOUR = {
    W: 0,
    "b": 0,
    0: 1,
    "a2": 1,
    "c2": 1,
    2: 2,
    5: 2,
    3: 3,
    "a1": 3,
    "c1": 3,
    1: 4,
    4: 4,
    6: 4,
}

FULL_PAIR = (frozenset(("a1", "a2")), frozenset(("c1", "c2")))
DIRECT_PATH = (4, "a2", "c1", 6)
FIXED_K7_MODEL = (
    frozenset((0, 6, "c1", W)),
    frozenset((1, "a1")),
    frozenset((2, "b")),
    frozenset((3, "c2")),
    frozenset((4,)),
    frozenset((5,)),
    frozenset(("a2",)),
)


def adjacency(edges):
    graph = {vertex: set() for vertex in VERTICES}
    for pair in edges:
        left, right = tuple(pair)
        graph[left].add(right)
        graph[right].add(left)
    return graph


def connected(graph, vertices):
    remaining = set(vertices)
    if not remaining:
        return False
    root = next(iter(remaining))
    seen = {root}
    stack = [root]
    while stack:
        vertex = stack.pop()
        new = graph[vertex] & remaining - seen
        seen.update(new)
        stack.extend(new)
    return seen == remaining


def connectivity_at_least_seven(edges):
    graph = adjacency(edges)
    for size in range(7):
        for deleted in combinations(VERTICES, size):
            remaining = set(VERTICES) - set(deleted)
            if not connected(graph, remaining):
                return False
    return True


def proper(edges, colouring):
    return all(colouring[left] != colouring[right] for left, right in map(tuple, edges))


def bichromatic_component(edges, root, colours):
    graph = adjacency(edges)
    allowed = {vertex for vertex in VERTICES if COLOUR[vertex] in colours}
    seen = {root}
    stack = [root]
    while stack:
        vertex = stack.pop()
        new = graph[vertex] & allowed - seen
        seen.update(new)
        stack.extend(new)
    return seen


def exact_trace(edges, operation_edge, colouring):
    left, right = tuple(operation_edge)
    if colouring[left] != colouring[right]:
        return False
    graph = adjacency(edges)
    common = colouring[left]
    neighbours = (graph[left] | graph[right]) - {left, right}
    return all(colouring[vertex] != common for vertex in neighbours)


def valid_response_pair(edges, outer):
    first = edge(V, W)
    second = edge(V, outer)
    if first not in edges or second not in edges or edge(W, outer) not in edges:
        return False

    # The first response is a colouring of G-first.
    if not proper(edges - {first}, COLOUR):
        return False

    alpha = COLOUR[V]
    beta = COLOUR[outer]
    common_deletion = edges - {first, second}
    component = bichromatic_component(common_deletion, W, {alpha, beta})
    if component != {W, outer}:
        return False

    switched = dict(COLOUR)
    switched[W] = beta
    switched[outer] = alpha
    if not proper(edges - {second}, switched):
        return False

    return exact_trace(edges - {first}, first, COLOUR) and exact_trace(
        edges - {second}, second, switched
    )


def is_boundary_full(vertices, edges):
    return all(
        any(edge(vertex, boundary) in edges for vertex in vertices)
        for boundary in S
    )


def adjacent_sets(left, right, edges):
    return any(edge(x, y) in edges for x in left for y in right)


def verify_model(edges, bags):
    graph = adjacency(edges)
    if set().union(*map(set, bags)) != set(VERTICES):
        return False
    if sum(map(len, bags)) != len(VERTICES):
        return False
    if not all(connected(graph, bag) for bag in bags):
        return False
    return all(adjacent_sets(left, right, edges) for left, right in combinations(bags, 2))


def extensions(side, outer):
    mandatory = {edge(V, W), edge(W, outer)}
    if side == "A":
        optional = [
            vertex
            for vertex in S + A
            if vertex not in {V, outer} and COLOUR[vertex] != COLOUR[W]
        ]
    else:
        # The new vertex lies with b, so separation forbids all A contacts.
        optional = [vertex for vertex in S if vertex != V]

    for size in range(len(optional) + 1):
        for selected in combinations(optional, size):
            yield BASE_EDGES | mandatory | {edge(W, vertex) for vertex in selected}


def neighbourhood(edges):
    return frozenset(next(iter(pair - {W})) for pair in edges if W in pair)


def main():
    # The only old outer endpoints in the same open shore that are adjacent
    # to v are a1,c2 on the A-side and b on the B-side.
    roles = (("A", "a1"), ("A", "c2"), ("B", "b"))
    expected = {
        ("A", "a1"): (512, 256, 4, 4),
        ("A", "c2"): (512, 512, 4, 3),
        ("B", "b"): (64, 64, 0, 0),
    }

    all_seven_connected = []
    for side, outer in roles:
        raw = responses = seven_connected = strict = 0
        for edges in extensions(side, outer):
            raw += 1
            if not valid_response_pair(edges, outer):
                continue
            responses += 1
            if not connectivity_at_least_seven(edges):
                continue
            seven_connected += 1

            # The old direct path and two selected full subgraphs survive.
            if not all(edge(x, y) in edges for x, y in zip(DIRECT_PATH, DIRECT_PATH[1:])):
                raise RuntimeError("direct path was lost")
            if not all(is_boundary_full(part, edges) for part in FULL_PAIR):
                raise RuntimeError("selected full subgraph was lost")

            same_shore_strict = not is_boundary_full({W}, edges)
            if same_shore_strict:
                strict += 1

            if side == "A" and not proper(edges, FIVE_COLOUR):
                raise RuntimeError("fixed five-colouring failed")
            if not verify_model(edges, FIXED_K7_MODEL):
                raise RuntimeError("fixed K7 model failed")
            all_seven_connected.append((side, outer, neighbourhood(edges), same_shore_strict))

        observed = (raw, responses, seven_connected, strict)
        if observed != expected[(side, outer)]:
            raise RuntimeError(f"wrong census for {(side, outer)}: {observed}")
        print(
            f"role={side}/{outer}: candidates={raw} responses={responses} "
            f"seven_connected={seven_connected} strict_same_shore={strict}"
        )

    if len(all_seven_connected) != 8:
        raise RuntimeError("wrong role-labelled seven-connected total")
    if len({contacts for _, _, contacts, _ in all_seven_connected}) != 6:
        raise RuntimeError("wrong unlabelled host total")

    print("seven-connected role-labelled extensions=8 distinct_hosts=6")
    print("strict direct-entry extensions=7")
    print("all seven-connected extensions: fixed spanning K7 model=yes")
    print("all A-shore extensions: fixed five-colouring=yes")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
