#!/usr/bin/env python3
"""Probe the degree-eight, three-exterior-component quotient.

The quotient has eight boundary vertices and three pairwise nonadjacent
shore vertices.  Shore i sees every boundary vertex except ``miss[i]``.
For a supplied boundary graph, ``find_model`` exhausts all N-meeting K6
models: there are only S(8,6)=266 boundary partitions and 7^3 ways to
place (or omit) the shore vertices.

This is a discovery program, not by itself a proof certificate.
"""

from itertools import combinations, product
import random
import sys

import z3


N = 8
SHORES = (8, 9, 10)
ALL = 11


def partitions_of_selected(selected):
    """Yield canonical partitions of ``selected`` into six blocks."""
    selected = tuple(selected)
    blocks = []

    def rec(pos):
        if pos == len(selected):
            if len(blocks) == 6:
                yield tuple(tuple(b) for b in blocks)
            return
        x = selected[pos]
        # Even putting every remaining point in a new block cannot reach 6.
        if len(blocks) + (len(selected) - pos) < 6:
            return
        # Too many blocks already.
        if len(blocks) > 6:
            return
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
    partition
    for size in range(6, N + 1)
    for selected in combinations(range(N), size)
    for partition in partitions_of_selected(selected)
)
assert len(PARTITIONS) == 462


def make_adjacency(boundary_edges, miss):
    adj = [0] * ALL
    for u, v in boundary_edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    for i, c in enumerate(SHORES):
        for x in range(N):
            if x != miss[i]:
                adj[c] |= 1 << x
                adj[x] |= 1 << c
    return adj


def connected(mask, adj):
    first = (mask & -mask).bit_length() - 1
    seen = 1 << first
    frontier = seen
    while frontier:
        xbit = frontier & -frontier
        frontier -= xbit
        x = xbit.bit_length() - 1
        new = adj[x] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def adjacent(a, b, adj):
    x = a
    while x:
        bit = x & -x
        x -= bit
        v = bit.bit_length() - 1
        if adj[v] & b:
            return True
    return False


def find_model(boundary_edges, miss):
    adj = make_adjacency(boundary_edges, miss)
    for partition in PARTITIONS:
        base = [sum(1 << x for x in block) for block in partition]
        for placement in product(range(-1, 6), repeat=3):
            bags = base[:]
            for i, bag in enumerate(placement):
                if bag >= 0:
                    bags[bag] |= 1 << SHORES[i]
            if not all(connected(b, adj) for b in bags):
                continue
            if all(adjacent(bags[i], bags[j], adj)
                   for i in range(6) for j in range(i + 1, 6)):
                return bags
    return None


EDGE_PAIRS = tuple(combinations(range(N), 2))


def template_clauses(bags, miss):
    """Return monotone boundary-edge clauses making ``bags`` a model.

    Each returned tuple is a disjunction of boundary-edge variables.  Cuts
    or bag adjacencies already witnessed by a fixed shore-boundary edge are
    omitted.  ``None`` means the template can never be a model.
    """

    def edge_kind(u, v):
        if u > v:
            u, v = v, u
        if v < N:
            return (u, v)
        if u >= N:
            return False
        shore_index = v - N
        return u != miss[shore_index]

    clauses = set()

    def require_cross(left, right):
        variables = set()
        for u in left:
            for v in right:
                kind = edge_kind(u, v)
                if kind is True:
                    return True
                if kind is not False:
                    variables.add(kind)
        if not variables:
            return False
        clauses.add(tuple(sorted(variables)))
        return True

    # Connectivity: it is enough to check one orientation of every cut.
    for mask in bags:
        vertices = [v for v in range(ALL) if mask >> v & 1]
        root = vertices[0]
        others = vertices[1:]
        for choice in range(1 << len(others)):
            left = {root}
            left.update(others[k] for k in range(len(others))
                        if choice >> k & 1)
            if len(left) == len(vertices):
                continue
            right = set(vertices) - left
            if not require_cross(left, right):
                return None

    for i in range(6):
        left = {v for v in range(ALL) if bags[i] >> v & 1}
        for j in range(i + 1, 6):
            right = {v for v in range(ALL) if bags[j] >> v & 1}
            if not require_cross(left, right):
                return None
    return tuple(sorted(clauses))


def prove_pattern(miss, certificate_path=None):
    variables = {e: z3.Bool("e_%d_%d" % e) for e in EDGE_PAIRS}
    solver = z3.Solver()
    for four in combinations(range(N), 4):
        solver.add(z3.Or(*(variables[e] for e in combinations(four, 2))))

    # Exclude every usable three-anchor coloring S|T|P.  If all three
    # blocks are independent, the star v+S and the two exterior components
    # outside a retained side connect T and P, respectively; the resulting
    # proper-minor colorings glue across all three sides.
    seen_anchor_partitions = set()
    for colors in product(range(3), repeat=N):
        if set(colors) != {0, 1, 2}:
            continue
        blocks = tuple(tuple(x for x in range(N) if colors[x] == c)
                       for c in range(3))
        # Swapping the two component-connected blocks changes nothing.
        key = (blocks[0],) + tuple(sorted((blocks[1], blocks[2])))
        if key in seen_anchor_partitions:
            continue
        seen_anchor_partitions.add(key)
        good = True
        bsets = [set(b) for b in blocks]
        for i in range(3):
            j, k = [x for x in range(3) if x != i]
            if not ((miss[j] not in bsets[1] and miss[k] not in bsets[2])
                    or (miss[j] not in bsets[2]
                        and miss[k] not in bsets[1])):
                good = False
                break
        if not good:
            continue
        internal = [variables[tuple(sorted(e))]
                    for block in blocks for e in combinations(block, 2)]
        # At least one same-block edge: otherwise this anchor partition
        # would close the counterexample.
        solver.add(z3.Or(*internal))

    # Also exclude four-anchor partitions S|T|P|{w}.  Here v connects S,
    # the two shores outside a retained side connect T and P, and w is an
    # already connected singleton forced to a fourth color by adjacency to
    # all three contracted anchor images.
    seen_four_anchor = set()

    def boundary_cross_expr(left, right):
        terms = [variables[tuple(sorted((x, y)))]
                 for x in left for y in right if x != y]
        return z3.Or(*terms) if terms else z3.BoolVal(False)

    for w in range(N):
        rest = [x for x in range(N) if x != w]
        for colors_tail in product(range(3), repeat=len(rest)):
            if set(colors_tail) != {0, 1, 2}:
                continue
            blocks = tuple(tuple(x for x, c in zip(rest, colors_tail)
                                 if c == color)
                           for color in range(3))
            key = (blocks[0],) + tuple(sorted((blocks[1], blocks[2]))) + ((w,),)
            if key in seen_four_anchor:
                continue
            seen_four_anchor.add(key)

            independent = z3.And(*(
                z3.Not(variables[tuple(sorted(e))])
                for block in blocks for e in combinations(block, 2)
            ))
            side_terms = []
            for i in range(3):
                j, k = [x for x in range(3) if x != i]
                assignment_terms = []
                for first, second in ((j, k), (k, j)):
                    if miss[first] in blocks[1] or miss[second] in blocks[2]:
                        continue
                    if (any(x != miss[first] for x in blocks[2])
                            or any(x != miss[second] for x in blocks[1])):
                        bd = z3.BoolVal(True)
                    else:
                        bd = boundary_cross_expr(blocks[1], blocks[2])
                    wb = (z3.BoolVal(True) if w != miss[first]
                          else boundary_cross_expr((w,), blocks[1]))
                    wd = (z3.BoolVal(True) if w != miss[second]
                          else boundary_cross_expr((w,), blocks[2]))
                    assignment_terms.append(z3.And(bd, wb, wd))
                side_terms.append(z3.Or(*assignment_terms))
            closure = z3.And(independent, *side_terms)
            solver.add(z3.Not(closure))

    certificate = []
    while solver.check() == z3.sat:
        model = solver.model()
        edges = [e for e, variable in variables.items()
                 if z3.is_true(model.eval(variable, model_completion=True))]
        bags = find_model(edges, miss)
        if bags is None:
            print("genuine quotient counterexample", miss, edges)
            return False
        clauses = template_clauses(bags, miss)
        assert clauses is not None
        certificate.append(tuple(bags))
        valid = z3.And(*(z3.Or(*(variables[e] for e in clause))
                         for clause in clauses))
        solver.add(z3.Not(valid))
        if len(certificate) % 100 == 0:
            print("pattern", miss, "templates", len(certificate))

    print("UNSAT pattern", miss, "templates", len(certificate))
    if certificate_path:
        with open(certificate_path, "w", encoding="utf-8") as stream:
            stream.write(repr({"miss": miss, "bags": certificate}) + "\n")
    return True


def alpha_at_most_three(edges):
    eset = {tuple(sorted(e)) for e in edges}
    return all(any(tuple(sorted(e)) in eset for e in combinations(s, 2))
               for s in combinations(range(N), 4))


def two_triples_and_edge(edges):
    eset = {tuple(sorted(e)) for e in edges}
    universe = set(range(N))
    for s in combinations(range(N), 3):
        if any(tuple(sorted(e)) in eset for e in combinations(s, 2)):
            continue
        rest = universe - set(s)
        for t in combinations(sorted(rest), 3):
            if any(tuple(sorted(e)) in eset for e in combinations(t, 2)):
                continue
            pair = tuple(sorted(rest - set(t)))
            if pair in eset:
                return (s, t, pair)
    return None


def three_anchor_partition(edges, miss):
    """Find S|T|P usable by the star plus the two deleted shores.

    Block 0 is connected through v.  For each retained shore i, the other
    two shores must be assignable to blocks 1 and 2 without missing a
    vertex of their assigned block.
    """
    eset = {tuple(sorted(e)) for e in edges}
    for colors in product(range(3), repeat=N):
        if set(colors) != {0, 1, 2}:
            continue
        if any(colors[u] == colors[v] for u, v in eset):
            continue
        blocks = [set(x for x in range(N) if colors[x] == c)
                  for c in range(3)]
        good = True
        for i in range(3):
            j, k = [x for x in range(3) if x != i]
            if not ((miss[j] not in blocks[1] and miss[k] not in blocks[2])
                    or (miss[j] not in blocks[2]
                        and miss[k] not in blocks[1])):
                good = False
                break
        if good:
            return tuple(tuple(sorted(b)) for b in blocks)
    return None


def four_anchor_partition(edges, miss):
    """Find S|T|P|{w} yielding four prescribed boundary colors."""
    eset = {tuple(sorted(e)) for e in edges}

    def has_edge(left, right):
        return any(tuple(sorted((x, y))) in eset for x in left for y in right)

    for w in range(N):
        rest = [x for x in range(N) if x != w]
        for colors_tail in product(range(3), repeat=len(rest)):
            if set(colors_tail) != {0, 1, 2}:
                continue
            blocks = [set() for _ in range(3)]
            for x, c in zip(rest, colors_tail):
                blocks[c].add(x)
            if any(has_edge(block, block) for block in blocks):
                continue
            good = True
            for i in range(3):
                j, k = [x for x in range(3) if x != i]
                side_good = False
                for first, second in ((j, k), (k, j)):
                    # first connects T=blocks[1], second connects P=blocks[2]
                    if miss[first] in blocks[1] or miss[second] in blocks[2]:
                        continue
                    bd = (any(x != miss[first] for x in blocks[2])
                          or any(x != miss[second] for x in blocks[1])
                          or has_edge(blocks[1], blocks[2]))
                    wb = (w != miss[first]
                          or has_edge({w}, blocks[1]))
                    wd = (w != miss[second]
                          or has_edge({w}, blocks[2]))
                    if bd and wb and wd:
                        side_good = True
                        break
                if not side_good:
                    good = False
                    break
            if good:
                return (tuple(sorted(blocks[0])),
                        tuple(sorted(blocks[1])),
                        tuple(sorted(blocks[2])), (w,))
    return None


def random_boundary(p=0.35):
    while True:
        edges = [(i, j) for i in range(N) for j in range(i + 1, N)
                 if random.random() < p]
        if alpha_at_most_three(edges):
            return edges


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "prove":
        pattern_index = int(sys.argv[2])
        patterns = ((0, 0, 0), (0, 0, 1), (0, 1, 2))
        miss = patterns[pattern_index]
        path = "degree8_three_shore_certificate_%d.txt" % pattern_index
        raise SystemExit(0 if prove_pattern(miss, path) else 1)
    patterns = ((0, 0, 0), (0, 0, 1), (0, 1, 2))
    for trial in range(1000):
        edges = random_boundary(random.uniform(0.3, 0.75))
        for miss in patterns:
            model = find_model(edges, miss)
            if model is None:
                decomposition = three_anchor_partition(edges, miss)
                if decomposition is None:
                    print("STRONG COUNTEREXAMPLE", miss, edges)
                    return
                print("direct-model obstruction covered by trace gluing",
                      miss, decomposition)
        if trial % 25 == 0:
            print("checked", trial)
    print("no random counterexample")


if __name__ == "__main__":
    main()
