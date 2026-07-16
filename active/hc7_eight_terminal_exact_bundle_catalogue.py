#!/usr/bin/env python3
"""Generate the exact labelled eight-terminal kernel bundles.

This is a deterministic discovery/certificate generator, not a proof of the
structural terminal-kernel theorem.  It needs only Python's standard library
and Brendan McKay's ``geng`` executable from nauty.

The eight terminals have fixed labels 0,...,7.  A terminal graph is encoded
by the 28-bit mask on lexicographically ordered terminal pairs.  For a
nine-vertex kernel with extra vertex x, an exact template is

    (terminal_mask << 8) | N_T(x).

Its legal owner family consists of all terminal quotients obtained by
contracting x into one actual neighbour.  The catalogue therefore represents
the quantifier ``for every exact template K, there exists an owner w in
N_K(x)``; it never substitutes one universal owner.

The normalized order-ten branch is generated separately from the analytic
C8/AABBAABB classification.  Its census is a check of that normal form, not
an exhaustive proof that every irreducible order-ten kernel has the form.
"""

from __future__ import annotations

import collections
import hashlib
import itertools
import shutil
import subprocess


TERMINALS = tuple(range(8))
PAIRS = tuple(itertools.combinations(TERMINALS, 2))
PAIR_INDEX = {edge: position for position, edge in enumerate(PAIRS)}
PERMUTATIONS = tuple(itertools.permutations(TERMINALS))


def graph6_adjacency(line: bytes) -> tuple[int, ...]:
    """Decode an order-at-most-62 graph6 line into adjacency bitsets."""

    data = line.strip()
    assert data and data[0] != ord(">")
    order = data[0] - 63
    assert 0 <= order <= 62
    bits: list[int] = []
    for value in data[1:]:
        value -= 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * order
    position = 0
    for right in range(1, order):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def geng(order: int):
    """Yield connected, minimum-degree-three unlabelled graphs."""

    if shutil.which("geng") is None:
        raise SystemExit("nauty's `geng` executable is required")
    process = subprocess.Popen(
        ["geng", "-cq", "-d3", str(order)],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    for line in process.stdout:
        yield graph6_adjacency(line)
    if process.wait() != 0:
        raise RuntimeError(f"geng failed at order {order}")


def edges(adjacency: tuple[int, ...]):
    for left in range(len(adjacency)):
        for right in range(left + 1, len(adjacency)):
            if adjacency[left] >> right & 1:
                yield left, right


def connected(adjacency: tuple[int, ...], removed: int = 0) -> bool:
    remaining = ((1 << len(adjacency)) - 1) & ~removed
    if not remaining:
        return True
    reached = remaining & -remaining
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adjacency[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == old:
            return reached == remaining


def three_connected(adjacency: tuple[int, ...]) -> bool:
    if len(adjacency) < 4:
        return False
    return all(
        connected(adjacency, sum(1 << vertex for vertex in removed))
        for size in range(3)
        for removed in itertools.combinations(range(len(adjacency)), size)
    )


def delete_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    answer = list(adjacency)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def contract_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    if left > right:
        left, right = right, left
    assert adjacency[left] >> right & 1
    image = tuple(
        left if vertex == right else vertex - (vertex > right)
        for vertex in range(len(adjacency))
    )
    answer = [0] * (len(adjacency) - 1)
    for old_left, old_right in edges(adjacency):
        new_left, new_right = image[old_left], image[old_right]
        if new_left == new_right:
            continue
        if new_left > new_right:
            new_left, new_right = new_right, new_left
        answer[new_left] |= 1 << new_right
        answer[new_right] |= 1 << new_left
    return tuple(answer)


def contractible(adjacency: tuple[int, ...], left: int, right: int) -> bool:
    return three_connected(contract_edge(adjacency, left, right))


def terminal_mask(
    adjacency: tuple[int, ...], terminals: tuple[int, ...], image: tuple[int, ...]
) -> int:
    labels = dict(zip(terminals, image))
    return sum(
        1 << PAIR_INDEX[tuple(sorted((labels[left], labels[right])))]
        for left, right in edges(adjacency)
        if left in labels and right in labels
    )


def sha256_fixed_width(items, width: int) -> str:
    digest = hashlib.sha256()
    for item in items:
        digest.update(int(item).to_bytes(width, "big"))
    return digest.hexdigest()


def encoded_family(family: tuple[int, ...]) -> bytes:
    assert len(family) < 256
    return bytes([len(family)]) + b"".join(
        mask.to_bytes(4, "big") for mask in family
    )


def sha256_families(families) -> str:
    digest = hashlib.sha256()
    for family in families:
        digest.update(encoded_family(family))
    return digest.hexdigest()


def owner_family_one_extra(template: int) -> tuple[int, ...]:
    base_mask, neighbours = template >> 8, template & 0xFF
    outcomes = set()
    for owner in TERMINALS:
        if not (neighbours >> owner & 1):
            continue
        quotient = base_mask
        for other in TERMINALS:
            if other != owner and neighbours >> other & 1:
                quotient |= 1 << PAIR_INDEX[tuple(sorted((owner, other)))]
        outcomes.add(quotient)
    return tuple(sorted(outcomes))


def order_eight_catalogue():
    unlabelled = []
    for adjacency in geng(8):
        if not three_connected(adjacency):
            continue
        if any(
            three_connected(delete_edge(adjacency, left, right))
            for left, right in edges(adjacency)
        ):
            continue
        unlabelled.append(adjacency)
    assert len(unlabelled) == 18

    masks = {
        terminal_mask(adjacency, TERMINALS, image)
        for adjacency in unlabelled
        for image in PERMUTATIONS
    }
    masks = tuple(sorted(masks))
    assert len(masks) == 196_976
    return unlabelled, masks


def order_nine_catalogue():
    rooted_occurrences = []
    occurrence_edge_profile = collections.Counter()
    occurrence_degree_profile = collections.Counter()
    for adjacency in geng(9):
        if not three_connected(adjacency):
            continue
        for extra in range(9):
            neighbours = tuple(
                vertex
                for vertex in range(9)
                if adjacency[extra] >> vertex & 1
            )
            if any(contractible(adjacency, extra, vertex) for vertex in neighbours):
                continue
            rooted_occurrences.append((adjacency, extra))
            occurrence_edge_profile[sum(1 for _ in edges(adjacency))] += 1
            occurrence_degree_profile[len(neighbours)] += 1
    assert len(rooted_occurrences) == 97

    templates = set()
    for adjacency, extra in rooted_occurrences:
        terminals = tuple(vertex for vertex in range(9) if vertex != extra)
        neighbour_positions = tuple(
            position
            for position, vertex in enumerate(terminals)
            if adjacency[extra] >> vertex & 1
        )
        for image in PERMUTATIONS:
            base_mask = terminal_mask(adjacency, terminals, image)
            neighbour_mask = sum(1 << image[position] for position in neighbour_positions)
            templates.add((base_mask << 8) | neighbour_mask)
    templates = tuple(sorted(templates))
    assert len(templates) == 2_408_280

    # Deduplication by an identical set of owner quotients is logically safe
    # for forall-template/exists-owner composition.  In this census the map is
    # injective, but the code checks rather than assumes that fact.
    families = {owner_family_one_extra(template) for template in templates}
    assert len(families) == len(templates)
    families = tuple(sorted(families))
    return (
        rooted_occurrences,
        occurrence_edge_profile,
        occurrence_degree_profile,
        templates,
        families,
    )


def labelled_cycles() -> tuple[tuple[tuple[int, int], ...], ...]:
    answer = set()
    for tail in itertools.permutations(range(1, 8)):
        cycle = (0,) + tail
        if cycle[1] > cycle[-1]:
            continue
        answer.add(
            tuple(
                sorted(
                    tuple(sorted((cycle[index], cycle[(index + 1) % 8])))
                    for index in range(8)
                )
            )
        )
    assert len(answer) == 2520
    return tuple(sorted(answer))


def owner_family_two_extras(template: int) -> tuple[int, ...]:
    base_mask = template >> 8
    first = template & 0xFF
    second = 0xFF ^ first
    outcomes = set()
    for owner_first in TERMINALS:
        if not (first >> owner_first & 1):
            continue
        for owner_second in TERMINALS:
            if not (second >> owner_second & 1):
                continue
            quotient = base_mask
            for owner, neighbours in ((owner_first, first), (owner_second, second)):
                for other in TERMINALS:
                    if other != owner and neighbours >> other & 1:
                        quotient |= 1 << PAIR_INDEX[tuple(sorted((owner, other)))]
            outcomes.add(quotient)
    return tuple(sorted(outcomes))


def order_ten_normal_form_catalogue():
    """Generate, but do not prove, the C8/AABBAABB normal form."""

    templates = set()
    for cycle_edges in labelled_cycles():
        cycle_adjacency = [set() for _ in TERMINALS]
        for left, right in cycle_edges:
            cycle_adjacency[left].add(right)
            cycle_adjacency[right].add(left)
        cycle = [0]
        previous = None
        current = 0
        while len(cycle) < 8:
            choices = sorted(
                cycle_adjacency[current]
                - ({previous} if previous is not None else set())
            )
            following = min(choices) if previous is None else choices[0]
            cycle.append(following)
            previous, current = current, following
        base_mask = sum(1 << PAIR_INDEX[edge] for edge in cycle_edges)
        for shift in range(4):
            first = sum(
                1 << cycle[index]
                for index in range(8)
                if ((index - shift) % 4) in (0, 1)
            )
            templates.add((base_mask << 8) | first)
    templates = tuple(sorted(templates))
    assert len(templates) == 10_080
    families = tuple(
        sorted({owner_family_two_extras(template) for template in templates})
    )
    assert len(families) == 5_040
    assert all(len(family) == 16 for family in families)
    return templates, families


def main() -> None:
    unlabelled8, masks8 = order_eight_catalogue()
    print("order8_unlabelled", len(unlabelled8))
    print("order8_labelled", len(masks8))
    print(
        "order8_unlabelled_edge_profile",
        dict(
            sorted(
                collections.Counter(
                    sum(1 for _ in edges(adjacency)) for adjacency in unlabelled8
                ).items()
            )
        ),
    )
    print(
        "order8_labelled_edge_profile",
        dict(sorted(collections.Counter(mask.bit_count() for mask in masks8).items())),
    )
    print("order8_digest", sha256_fixed_width(masks8, 4), flush=True)

    rooted9, edge9, degree9, templates9, families9 = order_nine_catalogue()
    print("order9_rooted_occurrences", len(rooted9))
    print("order9_occurrence_edge_profile", dict(sorted(edge9.items())))
    print("order9_occurrence_degree_profile", dict(sorted(degree9.items())))
    print("order9_templates", len(templates9))
    print(
        "order9_template_edge_profile",
        dict(
            sorted(
                collections.Counter(
                    (template >> 8).bit_count() + (template & 0xFF).bit_count()
                    for template in templates9
                ).items()
            )
        ),
    )
    print(
        "order9_template_degree_profile",
        dict(
            sorted(
                collections.Counter(
                    (template & 0xFF).bit_count() for template in templates9
                ).items()
            )
        ),
    )
    print("order9_template_digest", sha256_fixed_width(templates9, 8))
    print("order9_owner_families", len(families9))
    print(
        "order9_family_size_profile",
        dict(sorted(collections.Counter(map(len, families9)).items())),
    )
    print("order9_family_digest", sha256_families(families9), flush=True)

    templates10, families10 = order_ten_normal_form_catalogue()
    print("order10_normal_form_templates", len(templates10))
    print("order10_template_digest", sha256_fixed_width(templates10, 8))
    print("order10_owner_families", len(families10))
    print(
        "order10_family_size_profile",
        dict(sorted(collections.Counter(map(len, families10)).items())),
    )
    print("order10_family_digest", sha256_families(families10))


if __name__ == "__main__":
    main()
