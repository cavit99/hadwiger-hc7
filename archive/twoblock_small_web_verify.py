#!/usr/bin/env python3
"""Exhaustive replay for the sharp HC7 two-block web on <=3 interior vertices.

Boundary order:
    0=p1, 1=p2, 2=q1, 3=q2, 4=r1, 5=r2, 6=r3.
"""

from itertools import combinations, product

BOUNDARY_ORDER = 7
COLORS = range(6)
STATE_COLORS = {
    "10": (0, 0, 1, 2, 3, 4, 5),
    "01": (1, 2, 0, 0, 3, 4, 5),
    "11": (0, 0, 1, 1, 2, 3, 4),
}


def connected(order, edges):
    adjacency = [set() for _ in range(order)]
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    reached = {0}
    stack = [0]
    while stack:
        x = stack.pop()
        for y in adjacency[x] - reached:
            reached.add(y)
            stack.append(y)
    return len(reached) == order


def state_extends(order, edges, masks, state):
    boundary_colors = STATE_COLORS[state]
    lists = []
    for mask in masks:
        forbidden = {
            boundary_colors[i]
            for i in range(BOUNDARY_ORDER)
            if mask & (1 << i)
        }
        lists.append(tuple(c for c in COLORS if c not in forbidden))

    adjacency = [set() for _ in range(order)]
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)

    assignment = [-1] * order
    ordering = sorted(range(order), key=lambda x: len(lists[x]))

    def search(depth):
        if depth == order:
            return True
        x = ordering[depth]
        for color in lists[x]:
            if all(assignment[y] != color for y in adjacency[x]):
                assignment[x] = color
                if search(depth + 1):
                    return True
                assignment[x] = -1
        return False

    return search(0)


def pair_linkage_exists(order, edges, masks):
    """Test disjoint p1-p2 and q1-q2 paths, excluding R from the host."""

    total = 4 + order
    adjacency = [set() for _ in range(total)]
    # Boundary K_{2,2}.
    for p in (0, 1):
        for q in (2, 3):
            adjacency[p].add(q)
            adjacency[q].add(p)
    for x, y in edges:
        x += 4
        y += 4
        adjacency[x].add(y)
        adjacency[y].add(x)
    for x, mask in enumerate(masks, start=4):
        for terminal in range(4):
            if mask & (1 << terminal):
                adjacency[x].add(terminal)
                adjacency[terminal].add(x)

    paths = []

    def enumerate_paths(x, target, used, path):
        if x == target:
            paths.append(tuple(path))
            return
        for y in adjacency[x]:
            if y not in used:
                used.add(y)
                path.append(y)
                enumerate_paths(y, target, used, path)
                path.pop()
                used.remove(y)

    enumerate_paths(0, 1, {0}, [0])
    for path in paths:
        forbidden = set(path)
        if 2 in forbidden or 3 in forbidden:
            continue
        reached = {2}
        stack = [2]
        while stack:
            x = stack.pop()
            for y in adjacency[x]:
                if y not in forbidden and y not in reached:
                    reached.add(y)
                    stack.append(y)
        if 3 in reached:
            return True
    return False


def main():
    xor_masks = (
        sum(1 << i for i in (1, 3, 4, 5, 6)),
        sum(1 << i for i in (0, 2, 4, 5, 6)),
    )
    assert state_extends(2, [(0, 1)], xor_masks, "10")
    assert state_extends(2, [(0, 1)], xor_masks, "01")
    assert not state_extends(2, [(0, 1)], xor_masks, "11")
    assert not pair_linkage_exists(2, [(0, 1)], xor_masks)
    assert min(mask.bit_count() + 1 for mask in xor_masks) == 6
    print("XOR gadget replayed: split states yes, joint state no, minimum degree 6")

    for order in (1, 2, 3):
        possible_edges = list(combinations(range(order), 2))
        tested = split_obstructions = unlinked_obstructions = 0

        for edge_bits in range(1 << len(possible_edges)):
            edges = [
                edge
                for i, edge in enumerate(possible_edges)
                if edge_bits & (1 << i)
            ]
            if not connected(order, edges):
                continue

            internal_degree = [0] * order
            for x, y in edges:
                internal_degree[x] += 1
                internal_degree[y] += 1

            mask_choices = [
                tuple(
                    mask
                    for mask in range(1 << BOUNDARY_ORDER)
                    if mask.bit_count() + internal_degree[x] >= 7
                )
                for x in range(order)
            ]

            for masks in product(*mask_choices):
                # Inclusion-minimality of the contact separator makes
                # every boundary vertex adjacent to this distinguished side.
                union_mask = 0
                for mask in masks:
                    union_mask |= mask
                if union_mask != 127:
                    continue
                tested += 1
                if not state_extends(order, edges, masks, "10"):
                    continue
                if not state_extends(order, edges, masks, "01"):
                    continue
                if state_extends(order, edges, masks, "11"):
                    continue
                split_obstructions += 1
                if pair_linkage_exists(order, edges, masks):
                    continue
                unlinked_obstructions += 1
                raise AssertionError(
                    f"surviving order-{order} web: edges={edges}, masks={masks}"
                )

        print(
            f"order {order}: tested {tested}, "
            f"split/no-joint={split_obstructions}, "
            f"split/no-joint/unlinked={unlinked_obstructions}"
        )


if __name__ == "__main__":
    main()
