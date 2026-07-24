#!/usr/bin/env python3
"""Exhaustive verifier for the sharp relative-seven quotient closure."""

from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


ORDER = 10
Z, P, V = 7, 8, 9
PAIRS = ((0, 1), (2, 3), (4, 5))
NONEDGES = set(PAIRS)
CATALOGUE = Path(__file__).with_name(
    "hc7_relative7_planar_deficit_catalogue.json"
)

if not __debug__:
    raise SystemExit("refusing to run with Python optimization enabled")


def root_sets() -> tuple[int, ...]:
    result = []
    for choices in product((1, 2, 3), repeat=3):
        mask = 1 << 6
        for (x, y), choice in zip(PAIRS, choices):
            if choice & 1:
                mask |= 1 << x
            if choice & 2:
                mask |= 1 << y
        result.append(mask)
    return tuple(result)


def build(a: int, b: int, u: int) -> tuple[int, ...]:
    adjacency = [0] * ORDER

    def add(x: int, y: int) -> None:
        adjacency[x] |= 1 << y
        adjacency[y] |= 1 << x

    for x, y in combinations(range(7), 2):
        if (x, y) not in NONEDGES:
            add(x, y)
    for x in range(7):
        if u >> x & 1:
            add(Z, x)
        if a >> x & 1:
            add(P, x)
        if b >> x & 1:
            add(V, x)
    add(Z, P)
    add(Z, V)
    add(P, V)
    return tuple(adjacency)


def connected(adjacency: tuple[int, ...], mask: int) -> bool:
    if not mask:
        return True
    reached = mask & -mask
    while True:
        expanded = reached
        scan = reached
        while scan:
            bit = scan & -scan
            scan -= bit
            expanded |= adjacency[bit.bit_length() - 1]
        expanded &= mask
        if expanded == reached:
            return reached == mask
        reached = expanded


def relatively_seven_connected(adjacency: tuple[int, ...]) -> bool:
    full = (1 << ORDER) - 1
    nonmarkers = tuple(x for x in range(ORDER) if x != Z)
    for size in range(7):
        for cut in combinations(nonmarkers, size):
            cutmask = sum(1 << x for x in cut)
            if not connected(adjacency, full ^ cutmask):
                return False
    return True


def colourable(adjacency: tuple[int, ...], number: int) -> bool:
    order = sorted(
        range(ORDER), key=lambda x: adjacency[x].bit_count(), reverse=True
    )
    colours = [-1] * ORDER

    def search(at: int) -> bool:
        if at == ORDER:
            return True
        vertex = order[at]
        blocked = {
            colours[x]
            for x in range(ORDER)
            if adjacency[vertex] >> x & 1 and colours[x] >= 0
        }
        for colour in range(number):
            if colour in blocked:
                continue
            colours[vertex] = colour
            if search(at + 1):
                return True
            colours[vertex] = -1
        return False

    return search(0)


def clique_minor_certificate(
    adjacency: tuple[int, ...], order: int
) -> tuple[int, ...] | None:
    assignment = [-2] * ORDER

    def valid() -> tuple[int, ...] | None:
        bags = tuple(sorted(
            sum(
                1 << x
                for x, label in enumerate(assignment)
                if label == bag
            )
            for bag in range(order)
        ))
        if any(not bag or not connected(adjacency, bag) for bag in bags):
            return None
        if not all(
            any(
                adjacency[x] & bags[j]
                for x in range(ORDER)
                if bags[i] >> x & 1
            )
            for i in range(order)
            for j in range(i)
        ):
            return None
        return bags

    def search(at: int, used: int) -> tuple[int, ...] | None:
        if used + ORDER - at < order:
            return None
        if at == ORDER:
            return valid() if used == order else None
        assignment[at] = -1
        found = search(at + 1, used)
        if found is not None:
            return found
        for label in range(min(used + 1, order)):
            assignment[at] = label
            found = search(at + 1, max(used, label + 1))
            if found is not None:
                return found
        return None

    return search(0, 0)


def rooted_k4_models() -> tuple[tuple[int, ...], ...]:
    adjacency = build(0, 0, 0)
    models = set()
    # Labels 0,...,3 are branch sets and label 4 means unused.
    for labels in product(range(5), repeat=7):
        bags = tuple(
            sum(1 << x for x, label in enumerate(labels) if label == i)
            for i in range(4)
        )
        if any(not bag or not connected(adjacency, bag) for bag in bags):
            continue
        if not all(
            any(
                adjacency[x] & bags[j]
                for x in range(7)
                if bags[i] >> x & 1
            )
            for i in range(4)
            for j in range(i)
        ):
            continue
        models.add(tuple(sorted(bags)))
    return tuple(sorted(models))


def three_rooted_k4_free(
    a: int,
    b: int,
    u: int,
    models: tuple[tuple[int, ...], ...],
) -> bool:
    return not any(
        all(bag & a and bag & b and bag & u for bag in model)
        for model in models
    )


def vertices(mask: int) -> list[int]:
    return [x for x in range(7) if mask >> x & 1]


def certificates(
    triple: tuple[int, int, int],
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    a, b, u = triple
    adjacency = build(a, b, u)
    fixed = set(range(7)) | {P, V}
    result = []
    for triangle in combinations(range(7), 3):
        if not all(
            adjacency[x] >> y & 1 for x, y in combinations(triangle, 2)
        ):
            continue
        if sum(u >> x & 1 for x in triangle) > 1:
            continue
        common = tuple(
            x
            for x in sorted(fixed - set(triangle))
            if all(adjacency[x] >> y & 1 for y in triangle)
        )
        for roots in combinations(common, 4):
            remaining = fixed - set(triangle)
            deficit = sum(
                sum(adjacency[x] >> y & 1 for y in triangle) - 1
                for x in remaining
            )
            if deficit <= 11:
                result.append((triangle, roots, deficit))
    return tuple(result)


def record(
    triple: tuple[int, int, int],
    certificate: tuple[tuple[int, ...], tuple[int, ...], int],
) -> list[object]:
    triangle, roots, deficit = certificate
    return [
        vertices(triple[0]),
        vertices(triple[1]),
        vertices(triple[2]),
        list(triangle),
        list(roots),
        deficit,
    ]


def direct_record(
    triple: tuple[int, int, int], bags: tuple[int, ...]
) -> list[object]:
    return [
        vertices(triple[0]),
        vertices(triple[1]),
        vertices(triple[2]),
        [
            [x for x in range(ORDER) if bag >> x & 1]
            for bag in bags
        ],
    ]


def graph6(adjacency: tuple[int, ...]) -> str:
    bits = [
        adjacency[x] >> y & 1
        for y in range(1, ORDER)
        for x in range(y)
    ]
    bits.extend([0] * (-len(bits) % 6))
    payload = "".join(
        chr(
            63
            + sum(bits[start + offset] << (5 - offset) for offset in range(6))
        )
        for start in range(0, len(bits), 6)
    )
    return chr(ORDER + 63) + payload


def main() -> None:
    roots = root_sets()
    models = rooted_k4_models()
    assert len(roots) == 27
    assert len(models) == 644

    model_free = 0
    relative = []
    for triple in product(roots, repeat=3):
        if not three_rooted_k4_free(*triple, models):
            continue
        model_free += 1
        adjacency = build(*triple)
        if relatively_seven_connected(adjacency):
            relative.append(triple)

    assert model_free == 912
    assert len(relative) == 48

    direct = []
    hard = []
    for triple in relative:
        adjacency = build(*triple)
        assert not colourable(adjacency, 5)
        assert colourable(adjacency, 6)
        model = clique_minor_certificate(adjacency, 7)
        if model is None:
            hard.append(triple)
        else:
            direct.append((triple, model))

    assert len(direct) == 24
    assert len(hard) == 24

    hard_records = []
    for triple in hard:
        found = certificates(triple)
        assert len(found) == 1
        assert found[0][2] == 10
        hard_records.append(record(triple, found[0]))
    hard_records.sort()
    direct_records = sorted(
        direct_record(triple, model) for triple, model in direct
    )

    catalogue = json.loads(CATALOGUE.read_text())
    assert catalogue["format"] == "hc7-relative7-planar-deficit-v2"
    assert catalogue["direct_k7"] == direct_records
    assert catalogue["planar_deficit"] == hard_records

    fixed = (
        sum(1 << x for x in (0, 2, 4, 6)),
        sum(1 << x for x in (0, 2, 5, 6)),
        sum(1 << x for x in (1, 3, 4, 5, 6)),
    )
    assert fixed in hard
    assert graph6(build(*fixed)) == "I]~vy}jhw"

    payload = {
        "direct_k7": direct_records,
        "planar_deficit": hard_records,
    }
    serial = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    print("PASS relative-seven planar-deficit exhaustive verification")
    print("root_sets=27 rooted_K4_models=644 triple_model_free=912")
    print("relative_survivors=48 direct_K7=24 hard=24")
    print("explicit_K7_minor_models=24 checked_adjacencies=504")
    print("unique_planar_deficit_certificates=24 deficit=10")
    print("fixed_graph6=I]~vy}jhw")
    print("catalogue_sha256=" + sha256(serial.encode()).hexdigest())


if __name__ == "__main__":
    main()
