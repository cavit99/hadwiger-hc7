#!/usr/bin/env python3
"""Finite probe for rooted K5 models in Hegde--Thomas enlargements of PB.

This is research code, not yet a promoted verifier.  It constructs the
pentagonal bipyramid with its planar rotation system and generates all
1-, 3-, and 5-enlargements.  It then searches for a K5 minor rooted at five
*unsplit* vertices of the original pentagonal bipyramid.
"""

from itertools import combinations, product
import sys


BASE = tuple(range(7))
A, B = 0, 1
RIM = tuple(range(2, 7))


def rim(i):
    return RIM[i % 5]


BASE_EDGES = {
    tuple(sorted(e))
    for e in (
        [(A, x) for x in RIM]
        + [(B, x) for x in RIM]
        + [(rim(i), rim(i + 1)) for i in range(5)]
    )
}

# Cyclic neighbour orders in one planar embedding.  Reversal is immaterial.
ROTATION = {
    A: tuple(rim(i) for i in range(5)),
    B: tuple(rim(-i) for i in range(5)),
}
for i in range(5):
    ROTATION[rim(i)] = (A, rim(i + 1), B, rim(i - 1))


def canon_edge(u, v):
    return frozenset((u, v))


def base_graph():
    return set(BASE), {canon_edge(u, v) for u, v in BASE_EDGES}


def adjacent(edges, u, v):
    return canon_edge(u, v) in edges


def connected(edges, vertices):
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        u = todo.pop()
        for v in vertices - seen:
            if adjacent(edges, u, v):
                seen.add(v)
                todo.append(v)
    return seen == vertices


def cyclic_interval(order, subset):
    """Return whether nonempty proper subset is consecutive on the cycle."""
    n = len(order)
    k = len(subset)
    return any({order[(i + j) % n] for j in range(k)} == subset for i in range(n))


def split_partitions(v, conforming):
    order = ROTATION[v]
    neighbors = set(order)
    ans = []
    first = min(neighbors)
    for k in range(2, len(order) - 1):
        for side0_tuple in combinations(order, k):
            side0 = set(side0_tuple)
            side1 = neighbors - side0
            if first not in side0:  # quotient by exchanging the two new ends
                continue
            is_conforming = cyclic_interval(order, side0) and cyclic_interval(order, side1)
            if is_conforming == conforming:
                ans.append((frozenset(side0), frozenset(side1)))
    return ans


def split_vertex(vertices, edges, v, sides):
    x0, x1 = (v, 0), (v, 1)
    out_v = (vertices - {v}) | {x0, x1}
    out_e = {e for e in edges if v not in e}
    out_e.add(canon_edge(x0, x1))
    for i, side in enumerate(sides):
        xi = (v, i)
        for w in side:
            out_e.add(canon_edge(xi, w))
    return out_v, out_e


def split_two(vertices, edges, u, usides, v, vsides):
    """Simultaneously split adjacent u,v; old uv goes between side-0 ends."""
    out_v = (vertices - {u, v}) | {(u, 0), (u, 1), (v, 0), (v, 1)}
    out_e = {e for e in edges if u not in e and v not in e}
    out_e |= {canon_edge((u, 0), (u, 1)), canon_edge((v, 0), (v, 1))}
    out_e.add(canon_edge((u, 0), (v, 0)))
    for i, side in enumerate(usides):
        for w in side - {v}:
            out_e.add(canon_edge((u, i), w))
    for i, side in enumerate(vsides):
        for w in side - {u}:
            out_e.add(canon_edge((v, i), w))
    return out_v, out_e


def rooted_k5_sets(vertices, edges, root_sets):
    root_sets = tuple(frozenset(x) for x in root_sets)
    assert all(root_sets) and all(
        root_sets[i].isdisjoint(root_sets[j])
        for i in range(5) for j in range(i + 1, 5)
    )
    used_roots = set().union(*root_sets)
    others = tuple(vertices - used_roots)
    # Each nonroot is unused (-1) or belongs to one of five rooted bags.
    for assignment in product(range(-1, 5), repeat=len(others)):
        bags = [set(x) for x in root_sets]
        for v, i in zip(others, assignment):
            if i >= 0:
                bags[i].add(v)
        if not all(connected(edges, bag) for bag in bags):
            continue
        if all(
            any(adjacent(edges, u, v) for u in bags[i] for v in bags[j])
            for i in range(5)
            for j in range(i + 1, 5)
        ):
            return tuple(frozenset(bag) for bag in bags)
    return None


def rooted_k5(vertices, edges, roots):
    return rooted_k5_sets(vertices, edges, ({r} for r in roots))


def paired_rooted_k5(vertices, edges, left, right):
    """Find five disjoint clique-model bags, each meeting left and right."""
    order = tuple(sorted(vertices, key=repr))
    n = len(order)
    candidates = []
    for mask in range(1, 1 << n):
        bag = {order[i] for i in range(n) if mask & (1 << i)}
        if bag & left and bag & right and connected(edges, bag):
            candidates.append((mask, frozenset(bag)))
    # Canonical order by bit mask removes bag permutations.
    def rec(start, used, chosen):
        if len(chosen) == 5:
            return tuple(bag for _, bag in chosen)
        for k in range(start, len(candidates)):
            mask, bag = candidates[k]
            if mask & used:
                continue
            if not all(any(adjacent(edges, u, v) for u in bag for v in old)
                       for _, old in chosen):
                continue
            ans = rec(k + 1, used | mask, chosen + [(mask, bag)])
            if ans is not None:
                return ans
        return None
    return rec(0, 0, [])


def find_unsplit_rooted_k5(vertices, edges, split_labels):
    unsplit = tuple(v for v in BASE if v not in split_labels)
    for roots in combinations(unsplit, 5):
        model = rooted_k5(vertices, edges, roots)
        if model is not None:
            return roots, model
    return None


def find_fibre_rooted_k5(vertices, edges, split_labels):
    """Root five bags at all vertices descended from five base labels."""
    fibres = {
        v: ({(v, 0), (v, 1)} if v in split_labels else {v})
        for v in BASE
    }
    for labels in combinations(BASE, 5):
        model = rooted_k5_sets(vertices, edges, (fibres[v] for v in labels))
        if model is not None:
            return labels, model
    return None


def oriented_partition(v, partition, required_side0):
    p, q = partition
    if required_side0 in p:
        return p, q
    return q, p


def main():
    vertices, edges = base_graph()
    families = []

    # Type 1: every nonedge is nonconfluent because all disks are triangles.
    type1 = []
    for u, v in combinations(BASE, 2):
        if not adjacent(edges, u, v):
            e1 = set(edges) | {canon_edge(u, v)}
            type1.append(((u, v), vertices, e1, set()))
    families.append(("type-1", type1))

    type3 = []
    for v in BASE:
        for sides in split_partitions(v, conforming=False):
            v3, e3 = split_vertex(vertices, edges, v, sides)
            type3.append(((v, sides), v3, e3, {v}))
    families.append(("type-3", type3))

    # Exact type-5 family.  If uv has facial thirds x,y, splitting u along
    # the uvx face means v and x go to opposite new ends; splitting v along
    # the uvy face means u and y go to opposite new ends (or swap x,y).
    type5 = []
    for u, v in BASE_EDGES:
        common = sorted((set(ROTATION[u]) & set(ROTATION[v])))
        assert len(common) == 2
        for up in split_partitions(u, conforming=True):
            usides = oriented_partition(u, up, v)
            for vp in split_partitions(v, conforming=True):
                vsides = oriented_partition(v, vp, u)
                valid_face_assignment = any(
                    x in usides[1] and y in vsides[1]
                    for x, y in (common, tuple(reversed(common)))
                )
                if not valid_face_assignment:
                    continue
                v5, e5 = split_two(vertices, edges, u, usides, v, vsides)
                e5.add(canon_edge((u, 1), (v, 1)))
                type5.append(((u, v, usides, vsides), v5, e5, {u, v}))
    families.append(("type-5", type5))

    for name, instances in families:
        failures = []
        fibre_failures = []
        ordinary_failures = []
        sample = None
        for spec, vs, es, split_labels in instances:
            witness = find_unsplit_rooted_k5(vs, es, split_labels)
            fibre_witness = find_fibre_rooted_k5(vs, es, split_labels)
            ordinary_witness = next(
                (
                    rooted_k5(vs, es, roots)
                    for roots in combinations(vs, 5)
                    if rooted_k5(vs, es, roots) is not None
                ),
                None,
            )
            if witness is None:
                failures.append(spec)
            elif sample is None:
                sample = (spec, witness)
            if fibre_witness is None:
                fibre_failures.append(spec)
            if ordinary_witness is None:
                ordinary_failures.append(spec)
        print(
            f"{name}: instances={len(instances)} "
            f"unsplit-root failures={len(failures)} "
            f"whole-fibre-root failures={len(fibre_failures)} "
            f"ordinary-K5 failures={len(ordinary_failures)}"
        )
        if sample is not None:
            print(f"  sample={sample}")
        if failures:
            print(f"  first_failure={failures[0]}")
        if fibre_failures:
            print(f"  first_fibre_failure={fibre_failures[0]}")

        if name == "type-5" and "--paired" in sys.argv:
            paired_tests = 0
            paired_failures = []
            for spec, vs, es, split_labels in instances:
                u, v = sorted(split_labels)
                common_contacts = set(BASE) - split_labels
                for lu, ru, lv, rv in product(range(2), repeat=4):
                    left = common_contacts | {(u, lu), (v, lv)}
                    right = common_contacts | {(u, ru), (v, rv)}
                    paired_tests += 1
                    if paired_rooted_k5(vs, es, left, right) is None:
                        paired_failures.append((spec, lu, ru, lv, rv))
            print(
                f"  paired-endpoint tests={paired_tests} "
                f"failures={len(paired_failures)}"
            )
            if paired_failures:
                print(f"  first_paired_failure={paired_failures[0]}")


if __name__ == "__main__":
    main()
