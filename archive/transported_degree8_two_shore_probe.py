#!/usr/bin/env python3
"""Discovery probe for the transported degree-eight two-shore quotient.

The boundary has eight vertices.  Shore f misses 7 (=w), and shore r
misses at most one boundary vertex.  We ask whether alpha(boundary)<=3
and a prescribed boundary clique P already force an N-meeting K6.

This is only an invariant finder; no output is used as a proof.
"""

from itertools import combinations, product
import z3

N = 8
SHORES = (8, 9)
ALL = 10
PAIRS = tuple(combinations(range(N), 2))


def partitions_of_selected(selected):
    selected = tuple(selected)
    blocks = []
    def rec(pos):
        if pos == len(selected):
            if len(blocks) == 6:
                yield tuple(tuple(b) for b in blocks)
            return
        if len(blocks) + len(selected) - pos < 6:
            return
        x = selected[pos]
        for i in range(len(blocks)):
            blocks[i].append(x)
            yield from rec(pos + 1)
            blocks[i].pop()
        if len(blocks) < 6:
            blocks.append([x])
            yield from rec(pos + 1)
            blocks.pop()
    yield from rec(0)


PARTITIONS = tuple(
    p for size in range(6, N + 1)
    for chosen in combinations(range(N), size)
    for p in partitions_of_selected(chosen)
)


def clauses_for(bags, misses):
    clauses = set()
    def edge_kind(a, b):
        if a > b:
            a, b = b, a
        if b < N:
            return (a, b)
        if a >= N:
            return False
        return a != misses[b - N]
    def require(left, right):
        opts = set()
        for a in left:
            for b in right:
                kind = edge_kind(a, b)
                if kind is True:
                    return True
                if kind is not False:
                    opts.add(kind)
        if not opts:
            return False
        clauses.add(tuple(sorted(opts)))
        return True
    for bag in bags:
        verts = [x for x in range(ALL) if bag >> x & 1]
        root, tail = verts[0], verts[1:]
        for bits in range(1 << len(tail)):
            left = {root} | {tail[i] for i in range(len(tail)) if bits >> i & 1}
            if len(left) == len(verts):
                continue
            if not require(left, set(verts) - left):
                return None
    for i, j in combinations(range(6), 2):
        left = {x for x in range(ALL) if bags[i] >> x & 1}
        right = {x for x in range(ALL) if bags[j] >> x & 1}
        if not require(left, right):
            return None
    return tuple(clauses)


def solve(p_size, second_miss):
    e = {p: z3.Bool("e_%d_%d" % p) for p in PAIRS}
    s = z3.Solver()
    for four in combinations(range(N), 4):
        s.add(z3.Or(*(e[p] for p in combinations(four, 2))))
    for p in combinations(range(p_size), 2):
        s.add(e[p])
    misses = (7, second_miss)
    # The old body D-u is full to the original boundary S.  Hence if the
    # residual shore itself misses a vertex of P, that label has a literal
    # representative among w and the y-vertices in U-P.
    if second_miss < p_size:
        s.add(z3.Or(*(e[tuple(sorted((second_miss, x)))]
                      for x in range(p_size, N))))
    templates = 0
    for part in PARTITIONS:
        base = [sum(1 << x for x in b) for b in part]
        for placement in product(range(-1, 6), repeat=2):
            bags = base[:]
            for i, at in enumerate(placement):
                if at >= 0:
                    bags[at] |= 1 << SHORES[i]
            cs = clauses_for(bags, misses)
            if cs is None:
                continue
            templates += 1
            s.add(z3.Or(*(z3.Not(z3.Or(*(e[p] for p in c))) for c in cs)))
    ans = s.check()
    print("p", p_size, "miss", second_miss, "templates", templates, ans)
    if ans == z3.sat:
        m = s.model()
        print([p for p in PAIRS if z3.is_true(m[e[p]])])


def solve_one_shore(p_size):
    """Add the exact local degree bounds present when R is empty."""
    e = {p: z3.Bool("o_%d_%d" % p) for p in PAIRS}
    s = z3.Solver()
    for four in combinations(range(N), 4):
        s.add(z3.Or(*(e[p] for p in combinations(four, 2))))
    for p in combinations(range(p_size), 2):
        s.add(e[p])
    # label 7 is w; the other non-P labels are the private y-vertices.
    s.add(z3.PbGe([(e[tuple(sorted((7, x)))], 1)
                   for x in range(N) if x != 7], 6))
    for y in range(p_size, 7):
        s.add(z3.PbGe([(e[tuple(sorted((y, x)))], 1)
                       for x in range(N) if x != y], 5))
    # D-u remains full to P, so each P-label has a representative in L.
    for p in range(p_size):
        s.add(z3.Or(*(e[(p,x)] for x in range(p_size,N))))
    misses=(7,)
    templates=0
    for part in PARTITIONS:
        base=[sum(1<<x for x in b) for b in part]
        for at in range(-1,6):
            bags=base[:]
            if at>=0: bags[at]|=1<<8
            # clauses_for expects two shores; inline by adding an omitted
            # dummy second shore to no bag and an arbitrary miss.
            cs=clauses_for(bags,(7,0))
            if cs is None: continue
            templates+=1
            s.add(z3.Or(*(z3.Not(z3.Or(*(e[p] for p in c))) for c in cs)))
    ans=s.check(); print('one p',p_size,'templates',templates,ans)
    if ans==z3.sat:
        m=s.model(); print([p for p in PAIRS if z3.is_true(m[e[p]])])


if __name__ == "__main__":
    for p in (2, 3, 4):
        solve(p, 6)
