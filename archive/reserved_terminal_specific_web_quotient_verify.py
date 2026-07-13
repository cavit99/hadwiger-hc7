#!/usr/bin/env python3
"""Exact conservative crossing quotients for the Moser reserved connector."""

from __future__ import annotations

import itertools


def minor_model(n: int, edges: set[tuple[int, int]], k: int):
    adjacency = [0] * n
    for x, y in edges:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x
    neighbour_union = [0] * (1 << n)
    connected: list[int] = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        x = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[x]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def rec(chosen: list[int], candidates: list[int], used: int):
        if len(chosen) == k:
            return tuple(chosen)
        needed = k - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [
                other for other in candidates[pos + 1 :]
                if not other & (used | bag)
                and neighbour_union[bag] & other
            ]
            if len(nxt) >= needed - 1:
                answer = rec(chosen + [bag], nxt, used | bag)
                if answer is not None:
                    return answer
        return None

    return rec([], connected, 0)


def e(x: int, y: int) -> tuple[int, int]:
    return (x, y) if x < y else (y, x)


def main() -> None:
    # Pure Moser labels: repeated pair a=1,b=3 and U={0,2,4,5,6}.
    moser = {
        e(x, y)
        for x, y in {
            (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
            (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
        }
    }
    u = {0, 2, 4, 5, 6}
    a, b, w, v, helper, xpiece, ypiece = 1, 3, 7, 8, 9, 10, 11
    order = (0, 2, 6, 5, 4)  # present C5 / pentagram order
    base = moser | {e(v, z) for z in range(7)}

    checked = 0
    for side, opposite_terminal in (("a", b), ("b", a)):
        common = base | {e(helper, z) for z in u | {w, opposite_terminal}}
        for i, r, j, s in itertools.combinations(range(5), 4):
            first = (order[i], order[j])
            second = (order[r], order[s])
            graph = (
                common
                | {e(xpiece, ypiece)}
                | {e(xpiece, z) for z in first}
                | {e(ypiece, z) for z in second}
            )
            assert minor_model(12, graph, 6) is not None
            assert minor_model(12, graph, 7) is None
            checked += 1
            print(side, first, second, "eta=6")
    assert checked == 10
    print("verified 10 terminal-specific crossing quotients: all eta=6, none eta=7")


if __name__ == "__main__":
    main()
