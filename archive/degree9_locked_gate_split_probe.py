#!/usr/bin/env python3
"""Falsification probe for the balanced degree-nine outer lock.

The only variable data are which side of a split L6 bag carries each
of its three old rooted-model adjacencies.  This script enumerates all
27 distributions and searches exhaustively for a spanning K7 model.
It is a discovery aid, not a proof certificate.
"""

from itertools import product


# 0..5 = h,v,1,2,3,4; 6..10 = U,D,L0,R5,R0.
H, V, X1, X2, X3, X4, U, D, L0, R5, R0 = range(11)
N = 11


def graph(state):
    edges = set()

    def add(a, b):
        if a != b:
            edges.add(tuple(sorted((a, b))))

    # Pure-Moser edges after 5 is absorbed in R5 and 6 in D.
    for x in (X1, X2, X3, X4):
        add(H, x)
        add(V, x)
    add(H, V)
    add(X1, X2)
    add(X3, X4)
    add(D, X1)
    add(D, X2)
    add(R5, X3)
    add(R5, X4)
    add(D, R5)  # edge 56
    add(V, D)
    add(V, R5)

    # Root types and old K4-model edges not incident with L6.
    for left in (U, L0):
        add(left, H)
        add(left, X1)
        add(left, X2)
    for right in (R5, R0):
        add(right, H)
        add(right, X3)
        add(right, X4)
    for a, b in ((L0, R5), (L0, R0), (R5, R0)):
        add(a, b)
    add(U, D)

    # state coordinate: 0=U only, 1=D only, 2=both carry the old edge.
    for target, carrier in zip((L0, R5, R0), state):
        if carrier in (0, 2):
            add(U, target)
        if carrier in (1, 2):
            add(D, target)
    return edges


def find_model(edges):
    adj = [0] * N
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    def connected(block):
        mask = sum(1 << x for x in block)
        reached = mask & -mask
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            x = bit.bit_length() - 1
            new = adj[x] & mask & ~reached
            reached |= new
            frontier |= new
        return reached == mask

    def touches(a, b):
        mb = sum(1 << x for x in b)
        return any(adj[x] & mb for x in a)

    answer = None
    blocks = []

    def visit(x):
        nonlocal answer
        if answer is not None:
            return
        if x == N:
            if len(blocks) != 7:
                return
            if not all(connected(b) for b in blocks):
                return
            if not all(touches(blocks[i], blocks[j])
                       for i in range(7) for j in range(i + 1, 7)):
                return
            answer = tuple(tuple(b) for b in blocks)
            return
        if len(blocks) + N - x < 7:
            return
        for b in blocks:
            b.append(x)
            visit(x + 1)
            b.pop()
        if len(blocks) < 7:
            blocks.append([x])
            visit(x + 1)
            blocks.pop()

    visit(0)
    return answer


for state in product(range(3), repeat=3):
    model = find_model(graph(state))
    print(state, "K7" if model else "open", model or "")
