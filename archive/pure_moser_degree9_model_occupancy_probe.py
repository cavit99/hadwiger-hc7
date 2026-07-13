#!/usr/bin/env python3
"""Exact small-minor probe for a rooted K4 with possible 5/6 occupancy.

The four abstract B vertices form a K4, see h, and each has a root
complete to H1 or H2.  Boundary vertices 5 and 6 may be outside the
model or already contained in one of the four bags.  We contract assigned
vertices into their bag and test every resulting quotient for K7.
"""

from itertools import combinations, product


def connected(mask: int, adjacency: list[int]) -> bool:
    reached = mask & -mask
    while True:
        nxt = reached
        bits = reached
        while bits:
            bit = bits & -bits
            bits -= bit
            nxt |= adjacency[bit.bit_length() - 1] & mask
        if nxt == reached:
            return reached == mask
        reached = nxt


def has_k7(vertices: tuple[str, ...], edges: set[frozenset[str]]) -> bool:
    n = len(vertices)
    index = {x: i for i, x in enumerate(vertices)}
    adjacency = [0] * n
    for edge in edges:
        x, y = edge
        adjacency[index[x]] |= 1 << index[y]
        adjacency[index[y]] |= 1 << index[x]
    connected_masks = [
        mask for mask in range(1, 1 << n) if connected(mask, adjacency)
    ]
    neighbours = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask - bit] | adjacency[bit.bit_length()-1]
    connected_masks.sort(key=lambda m: (m.bit_count(), m))

    def search(chosen: int, candidates: list[int], used: int) -> bool:
        if chosen == 7:
            return True
        need = 7 - chosen
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [
                other for other in candidates[pos + 1 :]
                if not (other & (used | bag)) and neighbours[bag] & other
            ]
            if len(nxt) >= need - 1 and search(chosen + 1, nxt, used | bag):
                return True
        return False

    return search(0, connected_masks, 0)


def make_graph(types: tuple[int, ...], owner5: int, owner6: int):
    # owner -1 means boundary vertex remains outside all rooted bags.
    bnodes = tuple(f"B{i}" for i in range(4))
    vertices = ["v", "h", "1", "2", "3", "4", *bnodes]
    if owner5 < 0:
        vertices.append("5")
    if owner6 < 0:
        vertices.append("6")
    vertices = tuple(vertices)
    edges: set[frozenset[str]] = set()

    def image(x: str) -> str:
        if x == "5" and owner5 >= 0:
            return bnodes[owner5]
        if x == "6" and owner6 >= 0:
            return bnodes[owner6]
        return x

    def add(x: str, y: str):
        x, y = image(x), image(y)
        if x != y:
            edges.add(frozenset((x, y)))

    for x in ("h", "1", "2", "3", "4", "5", "6"):
        add("v", x)
    for x, y in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "5"), ("4", "5"), ("5", "6"),
    ):
        add(x, y)
    for i, j in combinations(range(4), 2):
        add(bnodes[i], bnodes[j])
    for i, side in enumerate(types):
        add("h", bnodes[i])
        for x in (("1", "2") if side == 0 else ("3", "4")):
            add(bnodes[i], x)
    return vertices, edges


def main() -> None:
    negative = []
    owners = range(-1, 4)
    for types in product((0, 1), repeat=4):
        for owner5, owner6 in product(owners, repeat=2):
            vertices, edges = make_graph(types, owner5, owner6)
            if not has_k7(vertices, edges):
                negative.append((types, owner5, owner6))
    print("negative", len(negative), "of", 16 * 25)
    for row in negative[:100]:
        print(row)


if __name__ == "__main__":
    main()
