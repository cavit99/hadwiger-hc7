#!/usr/bin/env python3
"""Exact census for vertex splits of the pentagonal bipyramid.

No third-party package is used.  A K5 minor is sought by exhaustive
enumeration of five pairwise disjoint, pairwise adjacent connected masks.
"""

from itertools import combinations, product


X, Y, BOTH = 0, 1, 2


def has_crossing(word):
    """Return whether four cyclic positions have alternating clone access."""
    sees_x = lambda i: word[i] in (X, BOTH)
    sees_y = lambda i: word[i] in (Y, BOTH)
    for a, b, c, d in combinations(range(len(word)), 4):
        if sees_x(a) and sees_y(b) and sees_x(c) and sees_y(d):
            return True
        if sees_y(a) and sees_x(b) and sees_y(c) and sees_x(d):
            return True
    return False


def split_graph(kind, word):
    """Return `(vertices, edges)`; `word` is in the planar cyclic order."""
    poles = ("p", "q")
    rim = tuple(f"c{i}" for i in range(5))
    edges = set()
    for i in range(5):
        edges.add(tuple(sorted((rim[i], rim[(i + 1) % 5]))))
    for pole in poles:
        for c in rim:
            edges.add(tuple(sorted((pole, c))))

    if kind == "pole":
        old = "p"
        neighbours = rim
    else:
        old = "c0"
        # This is the cyclic order around c0 in the fixed embedding.
        neighbours = ("c1", "p", "c4", "q")

    vertices = [v for v in poles + rim if v != old] + ["x", "y"]
    edges = {e for e in edges if old not in e}
    edges.add(("x", "y"))
    for vertex, mark in zip(neighbours, word):
        if mark in (X, BOTH):
            edges.add(tuple(sorted(("x", vertex))))
        if mark in (Y, BOTH):
            edges.add(tuple(sorted(("y", vertex))))
    return vertices, edges


def exact_k5_minor(vertices, edges):
    """Return one exact K5 branch-set model, or `None`."""
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adjacency = [0] * n
    for u, v in edges:
        i, j = index[u], index[v]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    connected = []
    external_neighbours = {}
    for mask in range(1, 1 << n):
        reached = mask & -mask
        while True:
            enlarged = reached
            work = reached
            while work:
                bit = work & -work
                work -= bit
                enlarged |= adjacency[bit.bit_length() - 1] & mask
            if enlarged == reached:
                break
            reached = enlarged
        if reached != mask:
            continue
        connected.append(mask)
        neighbours = 0
        work = mask
        while work:
            bit = work & -work
            work -= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        external_neighbours[mask] = neighbours

    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def extend(chosen, start):
        if len(chosen) == 5:
            return chosen
        for position in range(start, len(connected)):
            mask = connected[position]
            if any(mask & old for old in chosen):
                continue
            if any(not (external_neighbours[mask] & old) for old in chosen):
                continue
            answer = extend(chosen + [mask], position + 1)
            if answer is not None:
                return answer
        return None

    return extend([], 0)


def swapped(word):
    return tuple(Y if x == X else X if x == Y else BOTH for x in word)


def pole_canonical(word):
    images = []
    for direction in (1, -1):
        for offset in range(5):
            images.append(
                tuple(word[(direction * i + offset) % 5] for i in range(5))
            )
    return min(images + [swapped(image) for image in images])


def rim_canonical(word):
    # On (c1,p,c4,q), the stabilizer independently swaps the two poles and
    # the two rim neighbours.
    images = []
    for swap_rim in (False, True):
        for swap_poles in (False, True):
            permutation = [0, 1, 2, 3]
            if swap_rim:
                permutation[0], permutation[2] = permutation[2], permutation[0]
            if swap_poles:
                permutation[1], permutation[3] = permutation[3], permutation[1]
            images.append(tuple(word[permutation[i]] for i in range(4)))
    return min(images + [swapped(image) for image in images])


def rooted_canonical(kind, word, root_word):
    """Canonicalize while coupling clone interchange across all contacts."""
    images = []
    if kind == "pole":
        for direction in (1, -1):
            for offset in range(5):
                column_image = tuple(
                    word[(direction * i + offset) % 5] for i in range(5)
                )
                images.append(column_image + root_word)
                images.append(column_image + root_word[::-1])
    else:
        for swap_rim in (False, True):
            for swap_poles in (False, True):
                permutation = [0, 1, 2, 3]
                if swap_rim:
                    permutation[0], permutation[2] = permutation[2], permutation[0]
                if swap_poles:
                    permutation[1], permutation[3] = permutation[3], permutation[1]
                column_image = tuple(word[permutation[i]] for i in range(4))
                images.append(column_image + root_word)
                images.append(column_image + root_word[::-1])
    return min(images + [swapped(image) for image in images])


def census(kind, degree, canonical):
    k5_count = 0
    planar_count = 0
    all_orbits = set()
    planar_orbits = set()
    for word in product((X, Y, BOTH), repeat=degree):
        crossing = has_crossing(word)
        model = exact_k5_minor(*split_graph(kind, word))
        assert (model is not None) == crossing, (kind, word, model)
        orbit = canonical(word)
        all_orbits.add(orbit)
        if crossing:
            k5_count += 1
        else:
            planar_count += 1
            planar_orbits.add(orbit)
    print(
        f"{kind}: assignments={3 ** degree} k5={k5_count} "
        f"planar={planar_count} orbits={len(all_orbits)} "
        f"planar_orbits={len(planar_orbits)}"
    )


def rooted_orbit_census(kind, degree):
    orbits = {}
    for word in product((X, Y, BOTH), repeat=degree):
        for roots in product((X, Y, BOTH), repeat=2):
            key = rooted_canonical(kind, word, roots)
            previous = orbits.setdefault(key, has_crossing(word))
            assert previous == has_crossing(word)
    positive = sum(orbits.values())
    print(
        f"root-distributed {kind}: orbits={len(orbits)} k7={positive} "
        f"surviving={len(orbits) - positive}"
    )


def pb_edges():
    edges = set()
    for i in range(5):
        edges.add(tuple(sorted((f"c{i}", f"c{(i + 1) % 5}"))))
    for pole in ("p", "q"):
        for i in range(5):
            edges.add(tuple(sorted((pole, f"c{i}"))))
    return edges


def is_facial_flip(missing, deleted):
    missing = set(missing)
    deleted = set(deleted)
    if missing == {"p", "q"}:
        if not all(v.startswith("c") for v in deleted):
            return False
        i, j = sorted(int(v[1:]) for v in deleted)
        return (j - i) % 5 in (1, 4)

    if not all(v.startswith("c") for v in missing):
        return False
    i, j = sorted(int(v[1:]) for v in missing)
    if (j - i) % 5 not in (2, 3):
        return False
    if (j - i) % 5 == 2:
        middle = f"c{(i + 1) % 5}"
    else:
        middle = f"c{(j + 1) % 5}"
    return len(deleted & {"p", "q"}) == 1 and middle in deleted


def one_edge_exchange_census():
    vertices = ["p", "q"] + [f"c{i}" for i in range(5)]
    edges = pb_edges()
    missing = {
        tuple(sorted((u, v)))
        for u, v in combinations(vertices, 2)
        if tuple(sorted((u, v))) not in edges
    }
    checked = 0
    for added in missing:
        for deleted in edges:
            model = exact_k5_minor(vertices, (edges | {added}) - {deleted})
            assert (model is None) == is_facial_flip(added, deleted), (
                added,
                deleted,
                model,
            )
            checked += 1
    print(f"one-edge exchanges={checked}: diagonal-flip criterion PASS")

    # Two independent safe flips at one rim target remain planar/K5-free.
    first = tuple(sorted(("c0", "c2")))
    second = tuple(sorted(("c0", "c3")))
    safe = 0
    for pole_1 in ("p", "q"):
        for pole_2 in ("p", "q"):
            deleted_1 = tuple(sorted((pole_1, "c1")))
            deleted_2 = tuple(sorted((pole_2, "c4")))
            graph = (edges | {first, second}) - {deleted_1, deleted_2}
            assert exact_k5_minor(vertices, graph) is None
            safe += 1
    print(f"simultaneous safe rim flips={safe}: all K5-free")

    # A pole-edge flip becomes terminal after every possible second contact.
    pole_edge = tuple(sorted(("p", "q")))
    deleted_rim = tuple(sorted(("c0", "c1")))
    base = (edges | {pole_edge}) - {deleted_rim}
    second_contacts = (missing - {pole_edge}) | {deleted_rim}
    for contact in second_contacts:
        assert exact_k5_minor(vertices, base | {contact}) is not None, contact
    print(
        f"pole safe exchange plus second contact={len(second_contacts)}: all K5"
    )


def main():
    census("pole", 5, pole_canonical)
    census("rim", 4, rim_canonical)
    rooted_orbit_census("pole", 5)
    rooted_orbit_census("rim", 4)
    one_edge_exchange_census()
    print("pentagonal-bipyramid vertex-split classification: PASS")


if __name__ == "__main__":
    main()
