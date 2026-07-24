#!/usr/bin/env python3
"""Independent completeness and certificate checker for the 48 quotients."""

from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


ORDER = 10
Z, P, V = 7, 8, 9
PAIRS = ((0, 1), (2, 3), (4, 5))
CATALOGUE = Path(__file__).with_name(
    "hc7_relative7_planar_deficit_catalogue.json"
)

if not __debug__:
    raise SystemExit("refusing to run with Python optimization enabled")


def root_sets() -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset(
            {6}
            | {
                vertex
                for pair, choice in zip(PAIRS, choices)
                for bit, vertex in enumerate(pair)
                if choice >> bit & 1
            }
        )
        for choices in product((1, 2, 3), repeat=3)
    )


def adjacent(
    x: int,
    y: int,
    a: frozenset[int],
    b: frozenset[int],
    u: frozenset[int],
) -> bool:
    if x > y:
        x, y = y, x
    if y < 7:
        return (x, y) not in PAIRS
    if x >= 7:
        return True
    return x in (u if y == Z else a if y == P else b)


def connected(
    vertices: frozenset[int],
    a: frozenset[int],
    b: frozenset[int],
    u: frozenset[int],
) -> bool:
    if not vertices:
        return False
    reached = {next(iter(vertices))}
    while True:
        expanded = reached | {
            y
            for x in reached
            for y in vertices
            if adjacent(x, y, a, b, u)
        }
        if expanded == reached:
            return reached == vertices
        reached = expanded


def relatively_seven_connected(
    triple: tuple[frozenset[int], frozenset[int], frozenset[int]],
) -> bool:
    a, b, u = triple
    vertices = frozenset(range(ORDER))
    for size in range(7):
        for cut in combinations((0, 1, 2, 3, 4, 5, 6, P, V), size):
            if not connected(vertices - set(cut), a, b, u):
                return False
    return True


def rooted_k4_models() -> tuple[tuple[frozenset[int], ...], ...]:
    empty = frozenset()
    models = set()
    for labels in product(range(5), repeat=7):
        bags = tuple(
            frozenset(x for x, label in enumerate(labels) if label == index)
            for index in range(4)
        )
        if empty in bags or not all(
            connected(bag, empty, empty, empty) for bag in bags
        ):
            continue
        if all(
            any(
                adjacent(x, y, empty, empty, empty)
                for x in bags[i]
                for y in bags[j]
            )
            for i in range(4)
            for j in range(i)
        ):
            models.add(tuple(sorted(bags, key=lambda bag: tuple(sorted(bag)))))
    return tuple(
        sorted(
            models,
            key=lambda model: tuple(tuple(sorted(bag)) for bag in model),
        )
    )


def survivor_triples() -> set[
    tuple[frozenset[int], frozenset[int], frozenset[int]]
]:
    models = rooted_k4_models()
    survivors = set()
    for triple in product(root_sets(), repeat=3):
        if any(
            all(
                bag & triple[0] and bag & triple[1] and bag & triple[2]
                for bag in model
            )
            for model in models
        ):
            continue
        if relatively_seven_connected(triple):
            survivors.add(triple)
    assert len(models) == 644
    return survivors


def expected_hard_records() -> list[list[object]]:
    records = []
    for choices in product((0, 1), repeat=3):
        selected = [pair[choice] for pair, choice in zip(PAIRS, choices)]
        for disagreement in range(3):
            a = set(selected) | {6}
            b = set(selected) | {6}
            b.remove(selected[disagreement])
            b.add(PAIRS[disagreement][1 - choices[disagreement]])

            u = {6, *PAIRS[disagreement]}
            triangle = {6}
            for index, pair in enumerate(PAIRS):
                if index == disagreement:
                    continue
                triangle.add(selected[index])
                u.add(pair[1 - choices[index]])

            roots = {*PAIRS[disagreement], P, V}
            records.append(
                [
                    sorted(a),
                    sorted(b),
                    sorted(u),
                    sorted(triangle),
                    sorted(roots),
                    10,
                ]
            )
    return sorted(records)


def triple_of(record: list[object]) -> tuple[frozenset[int], ...]:
    return tuple(frozenset(part) for part in record[:3])


def check_direct_certificate(record: list[object]) -> None:
    assert len(record) == 4
    assert all(part == sorted(set(part)) for part in record[:3])
    a, b, u = triple_of(record)
    raw_bags = record[3]
    assert len(raw_bags) == 7
    assert all(bag == sorted(set(bag)) for bag in raw_bags)
    bags = tuple(frozenset(bag) for bag in raw_bags)
    assert all(bag for bag in bags)
    assert all(all(0 <= vertex < ORDER for vertex in bag) for bag in bags)
    assert sum(map(len, bags)) == len(set().union(*bags))
    assert all(connected(bag, a, b, u) for bag in bags)
    assert all(
        any(adjacent(x, y, a, b, u) for x in bags[i] for y in bags[j])
        for i in range(7)
        for j in range(i)
    )


def check_host_certificate(record: list[object]) -> None:
    a, b, u = triple_of(record)
    triangle = frozenset(record[3])
    roots = frozenset(record[4])
    deficit = record[5]

    assert len(triangle) == 3
    assert all(adjacent(x, y, a, b, u) for x, y in combinations(triangle, 2))
    assert len(roots) == 4
    assert not triangle & roots
    assert all(
        adjacent(root, vertex, a, b, u)
        for root in roots
        for vertex in triangle
    )
    assert triangle & u == {6}

    remaining = (set(range(7)) | {P, V}) - triangle
    computed = sum(
        sum(adjacent(x, y, a, b, u) for y in triangle) - 1
        for x in remaining
    )
    assert computed == deficit == 10


def fixed_graph6() -> str:
    triple = (
        frozenset((0, 2, 4, 6)),
        frozenset((0, 2, 5, 6)),
        frozenset((1, 3, 4, 5, 6)),
    )
    bits = [
        int(adjacent(x, y, *triple))
        for y in range(1, ORDER)
        for x in range(y)
    ]
    bits.extend([0] * (-len(bits) % 6))
    return "I" + "".join(
        chr(
            63
            + sum(bits[start + offset] << (5 - offset) for offset in range(6))
        )
        for start in range(0, len(bits), 6)
    )


def main() -> None:
    catalogue = json.loads(CATALOGUE.read_text())
    assert set(catalogue) == {"format", "direct_k7", "planar_deficit"}
    assert catalogue["format"] == "hc7-relative7-planar-deficit-v2"
    direct = catalogue["direct_k7"]
    hard = catalogue["planar_deficit"]

    assert hard == expected_hard_records()
    assert len(hard) == len({json.dumps(record) for record in hard}) == 24
    assert len(direct) == len({json.dumps(record) for record in direct}) == 24
    for record in direct:
        check_direct_certificate(record)
    for record in hard:
        check_host_certificate(record)

    survivors = survivor_triples()
    direct_triples = {triple_of(record) for record in direct}
    hard_triples = {triple_of(record) for record in hard}
    assert len(survivors) == 48
    assert direct_triples.isdisjoint(hard_triples)
    assert direct_triples | hard_triples == survivors
    assert fixed_graph6() == "I]~vy}jhw"

    payload = {"direct_k7": direct, "planar_deficit": hard}
    serial = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    print("PASS independent relative-seven certificate check")
    print("survivor_complete=48 direct_K7_models=24 planar_deficit=24")
    print("checked_branch_sets=168 checked_adjacencies=504 deficit=10")
    print("fixed_graph6=I]~vy}jhw")
    print("catalogue_sha256=" + sha256(serial.encode()).hexdigest())


if __name__ == "__main__":
    main()
