#!/usr/bin/env python3
"""Verify the first-entry packet-minimality barrier."""

from functools import lru_cache
from itertools import combinations


S = tuple(range(7))
A = ("a1", "a2", "c1", "c2")
B = ("b",)
VERTICES = S + A + B


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def edge(u, v):
    return frozenset((u, v))


EDGES = {edge(i, (i + 1) % 7) for i in S}
EDGES.update((edge(0, 2), edge(1, 3)))
EDGES.update((edge("a1", "a2"), edge("a2", "c1"), edge("c1", "c2")))

CONTACTS = {
    "a1": {0, 1, 4, 5, 6},
    "a2": {2, 3, 4, 5},
    "c1": {0, 2, 5, 6},
    "c2": {1, 2, 3, 4, 5, 6},
    "b": set(S),
}
for vertex, contacts in CONTACTS.items():
    EDGES.update(edge(vertex, s) for s in contacts)

INDEX = {vertex: index for index, vertex in enumerate(VERTICES)}
N = len(VERTICES)
ALL = (1 << N) - 1
ADJ = [0] * N
for e in EDGES:
    require(len(e) == 2, "loop in edge set")
    u, v = tuple(e)
    ADJ[INDEX[u]] |= 1 << INDEX[v]
    ADJ[INDEX[v]] |= 1 << INDEX[u]


def mask(vertices):
    result = 0
    for vertex in vertices:
        result |= 1 << INDEX[vertex]
    return result


@lru_cache(None)
def connected(vertex_mask):
    if not vertex_mask:
        return False
    seen = vertex_mask & -vertex_mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        index = bit.bit_length() - 1
        new = ADJ[index] & vertex_mask & ~seen
        seen |= new
        frontier |= new
    return seen == vertex_mask


@lru_cache(None)
def neighbours(vertex_mask):
    result = 0
    remaining = vertex_mask
    while remaining:
        bit = remaining & -remaining
        remaining -= bit
        result |= ADJ[bit.bit_length() - 1]
    return result & ~vertex_mask


def verify_connectivity():
    for size in range(6):
        for deleted in combinations(VERTICES, size):
            require(connected(ALL ^ mask(deleted)), f"cut below six: {deleted}")
    cut = {0, 2, 5, 6, "a2", "c2"}
    require(not connected(ALL ^ mask(cut)), "displayed six-cut does not disconnect")


def has_spanning_k7_model():
    """Search all canonical connected seven-part partitions."""

    def search(remaining, chosen, parts_left):
        if parts_left == 1:
            return connected(remaining) and all(
                neighbours(remaining) & part for part in chosen
            )
        if remaining.bit_count() < parts_left:
            return False

        pivot = remaining & -remaining
        part = remaining
        while part:
            rest = remaining ^ part
            if (
                part & pivot
                and rest.bit_count() >= parts_left - 1
                and connected(part)
                and all(neighbours(part) & old for old in chosen)
                and search(rest, chosen + (part,), parts_left - 1)
            ):
                return True
            part = (part - 1) & remaining
        return False

    return search(ALL, tuple(), 7)


def verify_colouring_and_packets():
    colours = {
        1: 0,
        4: 0,
        6: 0,
        2: 1,
        5: 1,
        0: 2,
        3: 3,
        "a1": 3,
        "a2": 2,
        "c1": 3,
        "c2": 2,
        "b": 4,
    }
    for e in EDGES:
        u, v = tuple(e)
        require(colours[u] != colours[v], f"monochromatic edge {sorted(e, key=str)}")

    p1 = {"a1", "a2"}
    p2 = {"c1", "c2"}
    for packet in (p1, p2):
        require(connected(mask(packet)), f"disconnected packet {packet}")
        met = {s for s in S if neighbours(mask(packet)) & mask((s,))}
        require(met == set(S), f"packet is not boundary-full: {packet}")
    require(neighbours(mask(p1)) & mask(p2), "packets are not adjacent")
    for vertex in A:
        met = {s for s in S if edge(vertex, s) in EDGES}
        require(met != set(S), f"full singleton {vertex}")

    path = (0, "a1", "a2", 3)
    for u, v in zip(path, path[1:]):
        require(edge(u, v) in EDGES, f"missing path edge {u}-{v}")
    require(
        {colours[v] for v in path} == {colours[0], colours[3]},
        "displayed path is not bichromatic",
    )
    two_colour_vertices = {
        vertex for vertex in VERTICES if colours[vertex] in {colours[0], colours[3]}
    }
    require(two_colour_vertices == {0, 3, *A}, "unexpected two-colour vertex")
    require(edge(0, 3) not in EDGES, "boundary endpoints are adjacent")
    require(
        not any(edge(0, vertex) in EDGES and edge(vertex, 3) in EDGES for vertex in A),
        "a bichromatic path has fewer than two internal vertices",
    )


def main():
    require(len(VERTICES) == 12, "wrong vertex count")
    require(len(EDGES) == 38, "wrong edge count")
    require(all(edge(a, b) not in EDGES for a in A for b in B), "shore edge present")
    verify_connectivity()
    verify_colouring_and_packets()
    require(not has_spanning_k7_model(), "unexpected K7 minor")
    print("GREEN first-entry packet-minimality barrier")
    print("vertices=12 edges=38 connectivity=6 K7_minor=no")


if __name__ == "__main__":
    main()
