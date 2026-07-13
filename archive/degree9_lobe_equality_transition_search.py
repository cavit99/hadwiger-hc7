#!/usr/bin/env python3
"""Search order-at-most-two full shores at the cone-P6 lobe adhesion."""

from itertools import combinations, product


S = tuple(range(7))  # 0 is r; 1,...,6 are the ordered spine vertices.
BOUNDARY_EDGES = {
    frozenset((0, i)) for i in range(1, 7)
} | {
    frozenset((i, i + 1)) for i in range(1, 6)
}


def partitions(items):
    if not items:
        yield ()
        return
    x, *rest = items
    for p in partitions(rest):
        yield ((x,),) + p
        for i in range(len(p)):
            yield p[:i] + (tuple(sorted(p[i] + (x,))),) + p[i + 1 :]


ALL_PARTITIONS = {
    tuple(sorted(tuple(sorted(block)) for block in p))
    for p in partitions(list(S))
}


def independent(block):
    return all(frozenset(pair) not in BOUNDARY_EDGES
               for pair in combinations(block, 2))


STATES = []
for partition in ALL_PARTITIONS:
    if len(partition) <= 6 and all(independent(block) for block in partition):
        colors = [None] * 7
        for color, block in enumerate(partition):
            for vertex in block:
                colors[vertex] = color
        STATES.append((tuple(colors), partition))
STATES = tuple(STATES)
ALL_BITS = (1 << len(STATES)) - 1


def available(neighbors, colors):
    forbidden = 0
    for x in neighbors:
        forbidden |= 1 << colors[x]
    return 0b111111 & ~forbidden


def family(predicate):
    bits = 0
    for i, (colors, _) in enumerate(STATES):
        if predicate(colors):
            bits |= 1 << i
    return bits


def one_extends(neighbors, colors):
    return bool(available(neighbors, colors))


def two_extends(na, nb, colors, adjacent=True):
    aa = available(na, colors)
    bb = available(nb, colors)
    if not aa or not bb:
        return False
    if not adjacent:
        return True
    return not (aa == bb and aa & (aa - 1) == 0)


def single_signature():
    neighbors = frozenset(S)
    original = family(lambda c: one_extends(neighbors, c))
    operated = [("del_vertex", ALL_BITS)]
    for x in S:
        reduced = neighbors - {x}
        operated.append((f"del_w_{x}", family(
            lambda c, reduced=reduced: one_extends(reduced, c))))

        def contraction(colors, x=x):
            return all(colors[y] != colors[x] for y in neighbors if y != x)

        operated.append((f"con_w_{x}", family(contraction)))
    return {
        "order": 1,
        "na": neighbors,
        "nb": frozenset(),
        "E": original,
        "new": tuple((name, bits & ~original) for name, bits in operated),
    }


def two_signature(na, nb):
    na, nb = frozenset(na), frozenset(nb)
    original = family(lambda c: two_extends(na, nb, c, True))
    operated = [
        ("del_a", family(lambda c: one_extends(nb, c))),
        ("del_b", family(lambda c: one_extends(na, c))),
        ("del_ab", family(lambda c: two_extends(na, nb, c, False))),
        ("con_ab", family(lambda c: one_extends(na | nb, c))),
    ]
    for side, own, other in (("a", na, nb), ("b", nb, na)):
        for x in sorted(own):
            reduced = own - {x}
            if side == "a":
                deletion = family(
                    lambda c, reduced=reduced: two_extends(reduced, nb, c, True)
                )
            else:
                deletion = family(
                    lambda c, reduced=reduced: two_extends(na, reduced, c, True)
                )
            operated.append((f"del_{side}_{x}", deletion))

            def contraction(colors, own=own, other=other, x=x):
                color = colors[x]
                if any(colors[y] == color for y in own if y != x):
                    return False
                return bool(available(other, colors) & ~(1 << color))

            operated.append((f"con_{side}_{x}", family(contraction)))
    return {
        "order": 2,
        "na": na,
        "nb": nb,
        "E": original,
        "new": tuple((name, bits & ~original) for name, bits in operated),
    }


def candidates():
    result = []
    one = single_signature()
    if all(bits for _, bits in one["new"]):
        result.append(one)
    seen = set()
    for choices in product((1, 2, 3), repeat=7):
        na = frozenset(x for x, choice in zip(S, choices) if choice & 1)
        nb = frozenset(x for x, choice in zip(S, choices) if choice & 2)
        key = min((tuple(sorted(na)), tuple(sorted(nb))),
                  (tuple(sorted(nb)), tuple(sorted(na))))
        if key in seen:
            continue
        seen.add(key)
        sig = two_signature(na, nb)
        if all(bits for _, bits in sig["new"]):
            result.append(sig)
    return result


def transitions_into(piece, other):
    return all(bits & other["E"] for _, bits in piece["new"])


def describe(piece):
    return piece["order"], sorted(piece["na"]), sorted(piece["nb"])


def main():
    print("proper boundary states", len(STATES))
    pieces = candidates()
    print("individually operation-critical full pieces", len(pieces))
    disjoint = 0
    for i, first in enumerate(pieces):
        for second in pieces[i:]:
            if first["E"] & second["E"]:
                continue
            disjoint += 1
            if transitions_into(first, second) and transitions_into(second, first):
                print("TRANSITION PAIR", describe(first), describe(second))
                return
    print("no order-at-most-two transition pair; disjoint pairs", disjoint)


if __name__ == "__main__":
    main()
