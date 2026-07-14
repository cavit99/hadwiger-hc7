#!/usr/bin/env python3
"""Historical discovery probe for the three-packet paired quotient.

The exact unbounded theorem now supersedes this minimal-boundary census.
"""

from itertools import combinations, product


BOUNDARY = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
PACKETS = ("l", "p", "q")
NAMES = BOUNDARY + PACKETS
INDEX = {name: index for index, name in enumerate(NAMES)}
BLOCKS = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))


def named_edge(left: str, right: str) -> tuple[int, int]:
    u, v = INDEX[left], INDEX[right]
    return (u, v) if u < v else (v, u)


def has_k7vee(edges: tuple[tuple[int, int], ...]) -> tuple | None:
    order = len(NAMES)
    adjacency = [0] * order
    for u, v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u

    for size in range(4):
        delete_count = 3 - size
        for forest_indices in combinations(range(len(edges)), size):
            parent = list(range(order))

            def find(vertex: int) -> int:
                while parent[vertex] != vertex:
                    parent[vertex] = parent[parent[vertex]]
                    vertex = parent[vertex]
                return vertex

            touched = 0
            acyclic = True
            for edge_index in forest_indices:
                u, v = edges[edge_index]
                ru, rv = find(u), find(v)
                if ru == rv:
                    acyclic = False
                    break
                parent[ru] = rv
                touched |= (1 << u) | (1 << v)
            if not acyclic:
                continue
            roots = [find(vertex) for vertex in range(order)]
            available = [v for v in range(order) if not (touched >> v & 1)]
            for deleted_vertices in combinations(available, delete_count):
                deleted = set(deleted_vertices)
                bags: dict[int, int] = {}
                for vertex, root in enumerate(roots):
                    if vertex not in deleted:
                        bags[root] = bags.get(root, 0) | (1 << vertex)
                if len(bags) != 7:
                    continue
                branch_sets = tuple(bags.values())
                nonedges = []
                for i, j in combinations(range(7), 2):
                    left, right = branch_sets[i], branch_sets[j]
                    neighbourhood = 0
                    for vertex in range(order):
                        if left >> vertex & 1:
                            neighbourhood |= adjacency[vertex]
                    if not neighbourhood & right:
                        nonedges.append((i, j))
                if len(nonedges) <= 1 or (
                    len(nonedges) == 2 and set(nonedges[0]) & set(nonedges[1])
                ):
                    return forest_indices, deleted_vertices, branch_sets, nonedges
    return None


def main() -> None:
    choices = []
    for block in BLOCKS:
        choices.append(tuple(named_edge("c", vertex) for vertex in block))
    for left, right in combinations(BLOCKS, 2):
        choices.append(tuple(named_edge(u, v) for u in left for v in right))

    fixed = {named_edge(packet, vertex) for packet in PACKETS for vertex in BOUNDARY}
    fixed.add(named_edge("p", "q"))
    failures = []
    witnesses = []
    for selected in product(*choices):
        edges = tuple(sorted(fixed | set(selected)))
        witness = has_k7vee(edges)
        if witness is None:
            failures.append(tuple(selected))
        else:
            witnesses.append(witness)
    print("minimal boundaries", 2**3 * 4**3)
    print("closed", len(witnesses))
    print("failures", len(failures))
    for failure in failures[:20]:
        print(tuple((NAMES[u], NAMES[v]) for u, v in failure))


if __name__ == "__main__":
    main()
