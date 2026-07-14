#!/usr/bin/env python3
"""Search the smallest two-component rich-shore static hosts.

This is an adversarial, non-authoritative probe.  The first search fixes all
three open-shore components to single vertices complete to the seven-vertex
boundary.  It then enumerates every boundary graph compatible with the
paired-triangle state and asks whether seven-connectivity and K7-minor
freeness can coexist.  It also checks the decisive limitation of this
template: the exact four-block state extends with the two spare colours, so
the state reflects after a rich-side deletion.

No result from this finite search is used as an unbounded theorem.
"""

from __future__ import annotations

from itertools import combinations

import z3


S = tuple(range(7))
C = 0
BLOCKS = ((1, 2), (3, 4), (5, 6))
PACKETS = (7, 8, 9)  # thin packet, then the two rich components
V = tuple(range(10))


def connected(vertices: frozenset[int], adj: tuple[frozenset[int], ...]) -> bool:
    if not vertices:
        return False
    seen: set[int] = set()
    stack = [next(iter(vertices))]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend((adj[u] & vertices) - seen)
    return seen == vertices


def is_four_connected_boundary(adj: tuple[frozenset[int], ...]) -> bool:
    boundary = frozenset(S)
    if any(len(adj[v]) < 4 for v in S):
        return False
    for size in range(4):
        for deleted in combinations(S, size):
            if not connected(boundary - frozenset(deleted), adj):
                return False
    return True


def partitions_k(items: tuple[int, ...], k: int):
    """Yield unordered set partitions of ``items`` into exactly ``k`` bags."""
    bags: list[list[int]] = []

    def visit(index: int):
        remaining = len(items) - index
        if len(bags) > k or len(bags) + remaining < k:
            return
        if index == len(items):
            if len(bags) == k:
                yield tuple(frozenset(bag) for bag in bags)
            return
        x = items[index]
        for bag in bags:
            bag.append(x)
            yield from visit(index + 1)
            bag.pop()
        if len(bags) < k:
            bags.append([x])
            yield from visit(index + 1)
            bags.pop()

    yield from visit(0)


def k7_model(adj: tuple[frozenset[int], ...]):
    """Return a literal seven-bag clique model, or ``None``."""
    for used_size in range(7, len(V) + 1):
        for used in combinations(V, used_size):
            for bags in partitions_k(used, 7):
                if not all(connected(bag, adj) for bag in bags):
                    continue
                if all(
                    any(v in adj[u] for u in left for v in right)
                    for left, right in combinations(bags, 2)
                ):
                    return bags
    return None


def verify_k7_model(
    bags: tuple[frozenset[int], ...], adj: tuple[frozenset[int], ...]
) -> None:
    assert len(bags) == 7
    assert all(bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    assert all(connected(bag, adj) for bag in bags)
    assert all(
        any(v in adj[u] for u in left for v in right)
        for left, right in combinations(bags, 2)
    )


def host_adjacency(boundary_edges: tuple[tuple[int, int], ...]):
    raw = [set() for _ in V]
    for u, v in boundary_edges:
        raw[u].add(v)
        raw[v].add(u)
    for packet in PACKETS:
        for s in S:
            raw[packet].add(s)
            raw[s].add(packet)
    return tuple(frozenset(row) for row in raw)


def paired_state(boundary_edges: tuple[tuple[int, int], ...]) -> bool:
    edges = {frozenset(e) for e in boundary_edges}
    if any(frozenset(block) in edges for block in BLOCKS):
        return False
    if any(not any(frozenset((C, v)) in edges for v in block) for block in BLOCKS):
        return False
    for left, right in combinations(BLOCKS, 2):
        if not any(frozenset((u, v)) in edges for u in left for v in right):
            return False
    return True


def verify_legal_attainment(adj: tuple[frozenset[int], ...]) -> None:
    # Contract the thin packet with B1.  The following five-colouring of the
    # minor pulls back to the exact paired state on the untouched rich side.
    colours = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, C: 3, 8: 4, 9: 4}
    assert all(colours[u] != colours[v] for u in colours for v in adj[u] if v in colours)
    # The contracted image of {7,1,2} has colour zero.  Its external
    # neighbours are every other boundary literal, all coloured differently.
    cluster = frozenset((7, 1, 2))
    assert connected(cluster, adj)
    outside_neighbours = set().union(*(adj[v] for v in cluster)) - cluster
    assert all(colours[v] != 0 for v in outside_neighbours if v in colours)


def verify_singleton_reflection_colouring(adj: tuple[frozenset[int], ...]) -> None:
    # All three open-shore vertices use the same fifth colour.  Deleting one
    # rich singleton is therefore a proper rich-side minor whose colouring
    # pulls back to the thin closed shore with equality partition exactly Pi.
    colours = {
        1: 0,
        2: 0,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        C: 3,
        7: 4,
        8: 4,
        9: 4,
    }
    assert all(
        colours[u] != colours[v]
        for u in colours
        for v in adj[u]
        if v in colours
    )


def search_singletons() -> None:
    forbidden = {frozenset(block) for block in BLOCKS}
    allowed = tuple(
        e for e in combinations(S, 2) if frozenset(e) not in forbidden
    )
    paired_count = 0
    four_connected_count = 0
    k7_free = []
    first_model = None
    for mask in range(1 << len(allowed)):
        boundary_edges = tuple(
            allowed[i] for i in range(len(allowed)) if mask >> i & 1
        )
        if not paired_state(boundary_edges):
            continue
        paired_count += 1
        adj = host_adjacency(boundary_edges)
        boundary_adj = tuple(frozenset(adj[v] & frozenset(S)) for v in V)
        if not is_four_connected_boundary(boundary_adj):
            continue
        four_connected_count += 1
        # For three independent universal packet vertices, four-connectivity
        # of H is equivalent to seven-connectivity of the host.  We still
        # verify the host directly for cuts of order below seven.
        assert all(
            connected(frozenset(V) - frozenset(deleted), adj)
            for size in range(7)
            for deleted in combinations(V, size)
        )
        verify_legal_attainment(adj)
        verify_singleton_reflection_colouring(adj)
        model = k7_model(adj)
        if model is None:
            k7_free.append(boundary_edges)
            break
        verify_k7_model(model, adj)
        if first_model is None:
            first_model = (boundary_edges, model)
    print("singleton packets: paired boundary graphs", paired_count)
    print("singleton packets: seven-connected hosts", four_connected_count)
    print("singleton packets: K7-minor-free hosts", len(k7_free))
    print("singleton packets: every host reflects Pi by rich-side deletion")
    if first_model is not None:
        print("first K7 model", first_model[1])
    if k7_free:
        print("first K7-free boundary", k7_free[0])


def minimum_cut_below_seven(
    vertices: tuple[int, ...], adj: tuple[frozenset[int], ...]
):
    universe = frozenset(vertices)
    for size in range(7):
        for deleted_tuple in combinations(vertices, size):
            deleted = frozenset(deleted_tuple)
            remaining = universe - deleted
            if not connected(remaining, adj):
                first = next(iter(remaining))
                component = {first}
                stack = [first]
                while stack:
                    u = stack.pop()
                    for v in adj[u] & remaining:
                        if v not in component:
                            component.add(v)
                            stack.append(v)
                return deleted, frozenset(component), remaining - component
    return None


def z3_k7_model(adj: tuple[frozenset[int], ...]):
    n = len(adj)
    x = [[z3.Bool(f"x_{b}_{v}") for v in range(n)] for b in range(7)]
    root = [[z3.Bool(f"root_{b}_{v}") for v in range(n)] for b in range(7)]
    rank = [[z3.Int(f"rank_{b}_{v}") for v in range(n)] for b in range(7)]
    solver = z3.Solver()
    for v in range(n):
        solver.add(z3.PbLe([(x[b][v], 1) for b in range(7)], 1))
    signatures = []
    for b in range(7):
        solver.add(z3.Or(x[b]))
        solver.add(z3.PbEq([(root[b][v], 1) for v in range(n)], 1))
        signatures.append(z3.Sum([2**v * z3.If(x[b][v], 1, 0) for v in range(n)]))
        for v in range(n):
            solver.add(z3.Implies(root[b][v], x[b][v]))
            solver.add(z3.Implies(root[b][v], rank[b][v] == 0))
            solver.add(z3.Implies(z3.Not(x[b][v]), rank[b][v] == -1))
            solver.add(
                z3.Implies(
                    z3.And(x[b][v], z3.Not(root[b][v])),
                    z3.And(
                        rank[b][v] >= 1,
                        rank[b][v] < n,
                        z3.Or(
                            [
                                z3.And(x[b][u], rank[b][u] < rank[b][v])
                                for u in adj[v]
                            ]
                        ),
                    ),
                )
            )
    for b in range(6):
        solver.add(signatures[b] < signatures[b + 1])
    for left, right in combinations(range(7), 2):
        solver.add(
            z3.Or(
                [
                    z3.And(x[left][u], x[right][v])
                    for u in range(n)
                    for v in adj[u]
                ]
            )
        )
    if solver.check() != z3.sat:
        return None
    model = solver.model()
    return tuple(
        frozenset(v for v in range(n) if z3.is_true(model.eval(x[b][v])))
        for b in range(7)
    )


def subset_k7_model(adj: tuple[frozenset[int], ...]):
    """Exact branch-set clique search, ordered toward small bags."""
    n = len(adj)
    adjmask = tuple(sum(1 << u for u in row) for row in adj)

    def subset_connected(mask: int) -> bool:
        start = mask & -mask
        seen = start
        frontier = start
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            v = bit.bit_length() - 1
            new = adjmask[v] & mask & ~seen
            seen |= new
            frontier |= new
        return seen == mask

    candidates = []
    for mask in range(1, 1 << n):
        if subset_connected(mask):
            exterior = 0
            scan = mask
            while scan:
                bit = scan & -scan
                scan -= bit
                exterior |= adjmask[bit.bit_length() - 1]
            candidates.append((mask, exterior))
    candidates.sort(key=lambda item: (item[0].bit_count(), item[0]))

    def visit(
        selected: tuple[int, ...],
        used: int,
        available: list[tuple[int, int]],
    ):
        need = 7 - len(selected)
        if need == 0:
            return selected
        if n - used.bit_count() < need or len(available) < need:
            return None
        for index, (mask, exterior) in enumerate(available):
            if mask & used:
                continue
            following = [
                item
                for item in available[index + 1 :]
                if not (item[0] & (used | mask)) and bool(item[0] & exterior)
            ]
            answer = visit(selected + (mask,), used | mask, following)
            if answer is not None:
                return answer
        return None

    masks = visit((), 0, candidates)
    if masks is None:
        return None
    return tuple(
        frozenset(v for v in range(n) if mask >> v & 1) for mask in masks
    )


def search_k2_components(candidate_limit: int = 200) -> None:
    """CEGAR search with a singleton thin packet and two rich K2s."""
    # 0..6 are S, 7 is the thin singleton, 8--9 and 10--11 are rich K2s.
    vertices = tuple(range(12))
    forbidden = {frozenset(block) for block in BLOCKS}
    h_edges = tuple(e for e in combinations(S, 2) if frozenset(e) not in forbidden)
    contact_edges = tuple((u, s) for u in (8, 9, 10, 11) for s in S)
    optional_edges = h_edges + contact_edges
    variables = {e: z3.Bool(f"e_{e[0]}_{e[1]}") for e in optional_edges}
    solver = z3.Solver()

    # Every rich K2 is S-full, and every endpoint has at least six boundary
    # neighbours because its only internal neighbour contributes one degree.
    for u in (8, 9, 10, 11):
        solver.add(z3.PbGe([(variables[(u, s)], 1) for s in S], 6))
    for s in S:
        solver.add(z3.Or(variables[(8, s)], variables[(9, s)]))
        solver.add(z3.Or(variables[(10, s)], variables[(11, s)]))
    # Each component contributes exactly one packet.  In a K2 the only way
    # to pack two full connected subgraphs is for both singleton endpoints to
    # be S-full.
    solver.add(
        z3.Not(
            z3.And(
                *[variables[(8, s)] for s in S],
                *[variables[(9, s)] for s in S],
            )
        )
    )
    solver.add(
        z3.Not(
            z3.And(
                *[variables[(10, s)] for s in S],
                *[variables[(11, s)] for s in S],
            )
        )
    )

    # Literal paired-state adjacencies.
    for block in BLOCKS:
        solver.add(z3.Or([variables[tuple(sorted((C, v)))] for v in block]))
    for left, right in combinations(BLOCKS, 2):
        solver.add(
            z3.Or(
                [variables[tuple(sorted((u, v)))] for u in left for v in right]
            )
        )

    # Minimum degree seven at boundary vertices.  The thin singleton supplies
    # one fixed neighbour there.
    for s in S:
        incident = [variables[e] for e in optional_edges if s in e]
        solver.add(z3.PbGe([(v, 1) for v in incident], 6))

    fixed_edges = {tuple(sorted((7, s))) for s in S} | {(8, 9), (10, 11)}

    def adjacency_from_model(model):
        raw = [set() for _ in vertices]
        for u, v in fixed_edges:
            raw[u].add(v)
            raw[v].add(u)
        for e, variable in variables.items():
            if z3.is_true(model.eval(variable)):
                u, v = e
                raw[u].add(v)
                raw[v].add(u)
        return tuple(frozenset(row) for row in raw)

    def edge_expression(u: int, v: int):
        e = tuple(sorted((u, v)))
        if e in fixed_edges:
            return z3.BoolVal(True)
        if e in variables:
            return variables[e]
        reversed_e = (e[1], e[0])
        return variables.get(reversed_e, z3.BoolVal(False))

    def verify_k2_reflection_colouring(adj: tuple[frozenset[int], ...]) -> None:
        colours = {
            1: 0,
            2: 0,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            C: 3,
            7: 4,
            8: 4,
            9: 5,
            10: 4,
            11: 5,
        }
        assert all(
            colours[u] != colours[v]
            for u in colours
            for v in adj[u]
            if v in colours
        )

        # The same palette, after contracting the thin singleton with B1,
        # witnesses legal attainment on the untouched rich closed shore.
        cluster = frozenset((7, 1, 2))
        assert connected(cluster, adj)
        minor_colours = {0: 3, 3: 1, 4: 1, 5: 2, 6: 2, 8: 4, 9: 5, 10: 4, 11: 5}
        assert all(
            minor_colours[u] != minor_colours[v]
            for u in minor_colours
            for v in adj[u]
            if v in minor_colours
        )
        outside_neighbours = set().union(*(adj[v] for v in cluster)) - cluster
        assert all(
            minor_colours[v] != 0
            for v in outside_neighbours
            if v in minor_colours
        )

        # Exact packet vector: the thin singleton is one full packet; each
        # rich K2 is full but cannot split into two full singleton packets.
        assert adj[7] & frozenset(S) == frozenset(S)
        for u, v in ((8, 9), (10, 11)):
            assert (adj[u] | adj[v]) & frozenset(S) == frozenset(S)
            assert not (
                adj[u] & frozenset(S) == frozenset(S)
                and adj[v] & frozenset(S) == frozenset(S)
            )

    def symbolic_connected(bag: frozenset[int]):
        if len(bag) == 1:
            return z3.BoolVal(True)
        anchor = min(bag)
        others = tuple(sorted(bag - {anchor}))
        cut_edges = []
        # One shore of every unordered cut contains ``anchor``.
        for mask in range(1 << len(others)):
            left = {anchor} | {
                others[i] for i in range(len(others)) if mask >> i & 1
            }
            if len(left) == len(bag):
                continue
            right = set(bag) - left
            cut_edges.append(
                z3.Or([edge_expression(u, v) for u in left for v in right])
            )
        return z3.And(cut_edges)

    def symbolic_model_valid(bags: tuple[frozenset[int], ...]):
        connected_bags = [symbolic_connected(bag) for bag in bags]
        adjacent_pairs = [
            z3.Or([edge_expression(u, v) for u in left for v in right])
            for left, right in combinations(bags, 2)
        ]
        return z3.And(connected_bags + adjacent_pairs)

    checked = 0
    connectivity_clauses = 0
    while checked < candidate_limit and solver.check() == z3.sat:
        model = solver.model()
        adj = adjacency_from_model(model)
        cut = minimum_cut_below_seven(vertices, adj)
        if cut is not None:
            _, left, right = cut
            crossing = [
                variable
                for (u, v), variable in variables.items()
                if (u in left and v in right) or (u in right and v in left)
            ]
            assert crossing
            solver.add(z3.Or(crossing))
            connectivity_clauses += 1
            continue
        checked += 1
        verify_k2_reflection_colouring(adj)
        k7 = subset_k7_model(adj)
        if k7 is None:
            print("K2 packets: K7-free seven-connected candidate found")
            print("edges", sum(len(row) for row in adj) // 2)
            print("boundary edges", [e for e in h_edges if e[1] in adj[e[0]]])
            print("contacts", [e for e in contact_edges if e[1] in adj[e[0]]])
            return
        verify_k7_model(k7, adj)
        # Exclude this entire branch-set model, including every alternative
        # internal route and every alternative adjacency edge.  If the graph
        # solver becomes UNSAT after finitely many such exclusions, that is an
        # exact finite certificate that every host in this template has a K7
        # minor; it is stronger than merely sampling graph assignments.
        solver.add(z3.Not(symbolic_model_valid(k7)))
        if checked <= 3:
            print("K2 packets: candidate", checked, "contains K7", k7)
    print("K2 packets: distinct K7 models excluded", checked)
    print("K2 packets: connectivity clauses learned", connectivity_clauses)
    print("K2 packets: every checked host reflects Pi by rich-side deletion")
    if solver.check() == z3.unsat:
        print("K2 packets: exact template UNSAT without K7")
    else:
        print("K2 packets: no K7-free candidate found in bounded search")


def search_triangle_thin_singleton_rich(candidate_limit: int = 1000) -> None:
    """Search the first template that can genuinely obstruct Pi-extension.

    The thin shore is a triangle.  Every triangle vertex sees the singleton
    ``c`` and at least one literal in each paired block, so an exact-Pi
    colouring leaves it only the same two spare colours.  Hence Pi cannot
    extend across the thin shore.  The rich shore consists of two universal
    singleton packets.
    """

    vertices = tuple(range(12))
    thin = (7, 8, 9)
    rich = (10, 11)
    forbidden = {frozenset(block) for block in BLOCKS}
    h_edges = tuple(e for e in combinations(S, 2) if frozenset(e) not in forbidden)
    contact_edges = tuple((s, u) for u in thin for s in S)
    optional_edges = h_edges + contact_edges
    variables = {e: z3.Bool(f"t_{e[0]}_{e[1]}") for e in optional_edges}
    fixed_edges = {
        *combinations(thin, 2),
        *((s, u) for u in rich for s in S),
    }
    solver = z3.Solver()

    for u in thin:
        contacts = [variables[(s, u)] for s in S]
        solver.add(z3.PbGe([(value, 1) for value in contacts], 5))
        solver.add(z3.Not(z3.And(contacts)))
        solver.add(variables[(C, u)])
        for block in BLOCKS:
            solver.add(z3.Or([variables[(s, u)] for s in block]))
    for s in S:
        solver.add(z3.Or([variables[(s, u)] for u in thin]))

    for block in BLOCKS:
        solver.add(z3.Or([variables[tuple(sorted((C, v)))] for v in block]))
    for left, right in combinations(BLOCKS, 2):
        solver.add(
            z3.Or(
                [variables[tuple(sorted((u, v)))] for u in left for v in right]
            )
        )

    # Each boundary literal already has the two rich singleton neighbours.
    for s in S:
        incident = [value for e, value in variables.items() if s in e]
        solver.add(z3.PbGe([(value, 1) for value in incident], 5))

    def adjacency_from_model(model):
        raw = [set() for _ in vertices]
        for u, v in fixed_edges:
            raw[u].add(v)
            raw[v].add(u)
        for (u, v), value in variables.items():
            if z3.is_true(model.eval(value)):
                raw[u].add(v)
                raw[v].add(u)
        return tuple(frozenset(row) for row in raw)

    def edge_expression(u: int, v: int):
        e = tuple(sorted((u, v)))
        if e in fixed_edges:
            return z3.BoolVal(True)
        return variables.get(e, z3.BoolVal(False))

    def symbolic_connected(bag: frozenset[int]):
        if len(bag) == 1:
            return z3.BoolVal(True)
        anchor = min(bag)
        others = tuple(sorted(bag - {anchor}))
        clauses = []
        for mask in range(1 << len(others)):
            left = {anchor} | {
                others[i] for i in range(len(others)) if mask >> i & 1
            }
            if len(left) == len(bag):
                continue
            right = set(bag) - left
            clauses.append(
                z3.Or([edge_expression(u, v) for u in left for v in right])
            )
        return z3.And(clauses)

    def symbolic_model_valid(bags: tuple[frozenset[int], ...]):
        return z3.And(
            [symbolic_connected(bag) for bag in bags]
            + [
                z3.Or([edge_expression(u, v) for u in left for v in right])
                for left, right in combinations(bags, 2)
            ]
        )

    models_excluded = 0
    connectivity_clauses = 0
    while models_excluded < candidate_limit and solver.check() == z3.sat:
        model = solver.model()
        adj = adjacency_from_model(model)
        cut = minimum_cut_below_seven(vertices, adj)
        if cut is not None:
            _, left, right = cut
            crossing = [
                value
                for (u, v), value in variables.items()
                if (u in left and v in right) or (u in right and v in left)
            ]
            assert crossing
            solver.add(z3.Or(crossing))
            connectivity_clauses += 1
            continue

        # Exact packet vector (1,2).
        boundary = frozenset(S)
        assert all((adj[u] & boundary) != boundary for u in thin)
        assert set().union(*(set(adj[u] & boundary) for u in thin)) == set(S)
        assert all(adj[u] & boundary == boundary for u in rich)

        # Legal attainment: delete thin vertex 7, colour the remaining thin
        # edge with the two spare colours, and give both rich singletons one
        # of those colours.
        colours = {0: 3, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 2, 8: 4, 9: 5, 10: 4, 11: 4}
        assert all(
            colours[u] != colours[v]
            for u in colours
            for v in adj[u]
            if v in colours
        )

        # Nonreflection is literal: every thin vertex is adjacent to at
        # least one member of each of the four exact Pi blocks, so all three
        # vertices would need the same two non-boundary colours.
        for u in thin:
            assert C in adj[u]
            assert all(any(s in adj[u] for s in block) for block in BLOCKS)

        k7 = subset_k7_model(adj)
        if k7 is None:
            print("triangle thin: K7-free nonreflecting candidate found")
            print("edges", sum(len(row) for row in adj) // 2)
            print("boundary edges", [e for e in h_edges if e[1] in adj[e[0]]])
            print("thin contacts", [e for e in contact_edges if e[1] in adj[e[0]]])
            print("connectivity clauses learned", connectivity_clauses)
            return
        verify_k7_model(k7, adj)
        models_excluded += 1
        solver.add(z3.Not(symbolic_model_valid(k7)))
        if models_excluded <= 3:
            print("triangle thin: candidate", models_excluded, "contains K7", k7)

    print("triangle thin: distinct K7 models excluded", models_excluded)
    print("triangle thin: connectivity clauses learned", connectivity_clauses)
    if solver.check() == z3.unsat:
        print("triangle thin: exact template UNSAT without K7")
    else:
        print("triangle thin: bounded search found no K7-free host")


if __name__ == "__main__":
    search_singletons()
    search_k2_components(candidate_limit=20)
    search_triangle_thin_singleton_rich(candidate_limit=2000)
