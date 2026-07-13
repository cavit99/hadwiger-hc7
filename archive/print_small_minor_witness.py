#!/usr/bin/env python3
"""Print one exact branch-set witness for a small graph supplied by module."""

import argparse
import importlib


def connected(mask, adjacency):
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


def find(vertices, edges, order):
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}
    adj = [0] * n
    for e in edges:
        x, y = e
        adj[idx[x]] |= 1 << idx[y]
        adj[idx[y]] |= 1 << idx[x]
    masks = [m for m in range(1, 1 << n) if connected(m, adj)]
    masks.sort(key=lambda m: (m.bit_count(), m))
    neigh = [0] * (1 << n)
    for m in range(1, 1 << n):
        bit = m & -m
        neigh[m] = neigh[m - bit] | adj[bit.bit_length() - 1]

    def rec(chosen, candidates, used):
        if len(chosen) == order:
            return chosen
        need = order - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [
                other for other in candidates[pos + 1:]
                if not (other & (used | bag)) and neigh[bag] & other
            ]
            if len(nxt) >= need - 1:
                ans = rec(chosen + [bag], nxt, used | bag)
                if ans:
                    return ans
        return None

    ans = rec([], masks, 0)
    if ans is None:
        return None
    return [[vertices[i] for i in range(n) if mask >> i & 1] for mask in ans]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module")
    parser.add_argument("state", nargs="*", type=int)
    parser.add_argument("--order", type=int, default=7)
    args = parser.parse_args()
    module = importlib.import_module(args.module)
    graph = module.build(tuple(args.state))
    print(find(*graph, args.order))


if __name__ == "__main__":
    main()
