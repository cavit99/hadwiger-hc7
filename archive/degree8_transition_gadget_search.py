#!/usr/bin/env python3
"""Search for concrete two-vertex pieces satisfying all portal transitions."""

from itertools import product

from degree8_cutvertex_exact_transfer_probe import (
    PARTITIONS, full_adjacency, independent, MISS_TYPES, N, Z,
)


BOUNDARY_EDGES = [
    (0, 1), (0, 7), (1, 7),
    (2, 4), (4, 5), (3, 5), (3, 6), (2, 6),
    (2, Z),
]
MISS_TYPE = MISS_TYPES[0]
ADJ = full_adjacency(BOUNDARY_EDGES, MISS_TYPE)


def states():
    result = []
    for partition in PARTITIONS:
        if not independent(partition, ADJ):
            continue
        colors = [None] * 9
        for color, block in enumerate(partition):
            for vertex in block:
                colors[vertex] = color
        result.append((tuple(colors), len(partition), partition))
    return tuple(result)


STATES = states()
ALL_STATE_BITS = (1 << len(STATES)) - 1


def available(neighbors, colors):
    forbidden = 0
    for x in neighbors:
        forbidden |= 1 << colors[x]
    return 0b111111 & ~forbidden


def two_extends(na, nb, colors, adjacent=True):
    aa = available(na, colors)
    bb = available(nb, colors)
    if not aa or not bb:
        return False
    if not adjacent:
        return True
    return not (aa == bb and aa & (aa - 1) == 0)


def single_extends(neighbors, colors):
    return bool(available(neighbors, colors))


def family(predicate):
    bits = 0
    for index, (colors, _, _) in enumerate(STATES):
        if predicate(colors):
            bits |= 1 << index
    return bits


def signature(na, nb):
    na, nb = frozenset(na), frozenset(nb)
    original = family(lambda c: two_extends(na, nb, c, True))
    operated = []

    # Delete either internal vertex; delete/contract their edge.
    operated.append(("del_a", family(lambda c: single_extends(nb, c))))
    operated.append(("del_b", family(lambda c: single_extends(na, c))))
    operated.append(("del_ab", family(lambda c: two_extends(na, nb, c, False))))
    operated.append(("con_ab", family(
        lambda c: single_extends(na | nb, c))))

    for side, own, other in (("a", na, nb), ("b", nb, na)):
        for x in sorted(own):
            reduced = own - {x}
            if side == "a":
                deletion = family(lambda c, r=reduced: two_extends(r, nb, c, True))
            else:
                deletion = family(lambda c, r=reduced: two_extends(na, r, c, True))
            operated.append((f"del_{side}_{x}", deletion))

            def contraction(colors, own=own, other=other, x=x):
                cx = colors[x]
                # Contracting the interior endpoint onto boundary label x
                # adds x--y for every other boundary neighbor y.
                if any(colors[y] == cx for y in own if y != x):
                    return False
                # The surviving interior endpoint is adjacent to the merged
                # x through the internal edge.
                return bool(available(other, colors) & ~(1 << cx))

            operated.append((f"con_{side}_{x}", family(contraction)))

    new = tuple((name, result & ~original) for name, result in operated)
    return {
        "order": 2,
        "na": na,
        "nb": nb,
        "E": original,
        "new": new,
    }


def single_signature(neighbors):
    neighbors = frozenset(neighbors)
    original = family(lambda c: single_extends(neighbors, c))
    operated = [("del_vertex", ALL_STATE_BITS)]
    for x in sorted(neighbors):
        reduced = neighbors - {x}
        operated.append((f"del_w_{x}", family(
            lambda c, r=reduced: single_extends(r, c))))

        def contraction(colors, neighbors=neighbors, x=x):
            cx = colors[x]
            return all(colors[y] != cx for y in neighbors if y != x)

        operated.append((f"con_w_{x}", family(contraction)))
    return {
        "order": 1,
        "na": neighbors,
        "nb": frozenset(),
        "E": original,
        "new": tuple((name, result & ~original)
                     for name, result in operated),
    }


def candidates(required):
    required = tuple(required)
    seen = set()
    result = []
    single = single_signature(required)
    if all(bits for _, bits in single["new"]):
        result.append(single)
    for choices in product((1, 2, 3), repeat=len(required)):
        na = frozenset(x for x, choice in zip(required, choices) if choice & 1)
        nb = frozenset(x for x, choice in zip(required, choices) if choice & 2)
        key = min((tuple(sorted(na)), tuple(sorted(nb))),
                  (tuple(sorted(nb)), tuple(sorted(na))))
        if key in seen:
            continue
        seen.add(key)
        sig = signature(na, nb)
        if all(bits for _, bits in sig["new"]):
            result.append(sig)
    return result


def transition_ok(piece, other_a, other_b):
    common = other_a["E"] & other_b["E"] & ~piece["E"]
    return common and all(bits & common for _, bits in piece["new"])


def main():
    # Exact-defect type 01,01 for the branches and defect 0 for D.
    branch_required = tuple(x for x in range(9) if x not in (0, 1))
    d_required = tuple(x for x in range(8) if x != 0)
    branch = candidates(branch_required)
    dpieces = candidates(d_required)
    print("independent low states", len(STATES))
    print("fully operation-critical two-vertex candidates:",
          len(branch), "branch", len(dpieces), "D")

    checked = 0
    for r1 in branch:
        for r2 in branch:
            pair = r1["E"] & r2["E"]
            if not pair:
                continue
            for d in dpieces:
                checked += 1
                if r1["E"] & r2["E"] & d["E"]:
                    continue
                if not transition_ok(r1, r2, d):
                    continue
                if not transition_ok(r2, r1, d):
                    continue
                if not transition_ok(d, r1, r2):
                    continue
                print("TRANSITION ARCHITECTURE")
                for label, piece in (("R1", r1), ("R2", r2), ("D", d)):
                    print(label, "order", piece["order"],
                          sorted(piece["na"]), sorted(piece["nb"]))
                return
    print("no two-vertex architecture; triples checked", checked)


if __name__ == "__main__":
    main()
