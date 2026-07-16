#!/usr/bin/env python3
"""Deterministic verifier for the eight-terminal carrier trichotomy.

The hand proof is primary.  This script independently checks its finite
orders with the Python standard library and nauty ``geng``.  It enumerates
all labelled C8/K3,5/F8 carrier masks, every simple three-connected graph on
eight vertices, and every choice of the sole nonterminal in every simple
three-connected graph on nine vertices.
"""

from __future__ import annotations

import hashlib
import itertools
import shutil
import subprocess


def graph6_adjacency(line: bytes) -> tuple[int, ...]:
    data = line.strip()
    order = data[0] - 63
    assert 0 <= order <= 62
    bits = []
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


def connected(adjacency: tuple[int, ...], removed: int = 0) -> bool:
    remaining = ((1 << len(adjacency)) - 1) & ~removed
    if not remaining:
        return True
    reached = remaining & -remaining
    while True:
        previous = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            neighbours |= adjacency[bit.bit_length() - 1]
            frontier -= bit
        reached |= neighbours & remaining
        if reached == previous:
            return reached == remaining


def three_connected(adjacency: tuple[int, ...]) -> bool:
    if len(adjacency) < 4:
        return False
    return all(
        connected(adjacency, sum(1 << vertex for vertex in removed))
        for size in range(3)
        for removed in itertools.combinations(range(len(adjacency)), size)
    )


def two_connected_after_deleting(
    adjacency: tuple[int, ...], first: int, second: int
) -> bool:
    removed = (1 << first) | (1 << second)
    if not connected(adjacency, removed):
        return False
    return all(
        connected(adjacency, removed | (1 << vertex))
        for vertex in range(len(adjacency))
        if not (removed >> vertex & 1)
    )


def edges(adjacency: tuple[int, ...]):
    for left in range(len(adjacency)):
        for right in range(left + 1, len(adjacency)):
            if adjacency[left] >> right & 1:
                yield left, right


def delete_edge(
    adjacency: tuple[int, ...], left: int, right: int
) -> tuple[int, ...]:
    answer = list(adjacency)
    answer[left] &= ~(1 << right)
    answer[right] &= ~(1 << left)
    return tuple(answer)


def geng(order: int):
    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("nauty geng was not found on PATH")
    process = subprocess.Popen(
        [executable, "-cq", "-d3", str(order)],
        stdout=subprocess.PIPE,
    )
    assert process.stdout is not None
    for line in process.stdout:
        yield line.strip(), graph6_adjacency(line)
    assert process.wait() == 0


PAIRS = tuple(itertools.combinations(range(8), 2))
PAIR_INDEX = {edge: position for position, edge in enumerate(PAIRS)}


def mask_from_edges(edge_set) -> int:
    return sum(
        1 << PAIR_INDEX[tuple(sorted(edge))]
        for edge in edge_set
    )


def adjacency_mask(adjacency: tuple[int, ...]) -> int:
    return mask_from_edges(edges(adjacency))


def images_of(edge_set) -> frozenset[int]:
    answer = set()
    for image in itertools.permutations(range(8)):
        answer.add(
            mask_from_edges((image[left], image[right]) for left, right in edge_set)
        )
    return frozenset(answer)


def carrier_catalogue():
    cycle_edges = tuple((index, (index + 1) % 8) for index in range(8))
    k35_edges = tuple((left, right) for left in range(5) for right in range(5, 8))
    f8_edges = tuple(
        edge
        for edge in k35_edges
        if edge not in {(0, 5), (1, 6)}
    ) + ((0, 1),)
    cycles = images_of(cycle_edges)
    k35 = images_of(k35_edges)
    f8 = images_of(f8_edges)
    assert len(cycles) == 2520
    assert len(k35) == 56
    assert len(f8) == 3360
    assert not (cycles & k35 or cycles & f8 or k35 & f8)
    return cycles, k35, f8


CYCLES, K35, F8 = carrier_catalogue()
ALL_CARRIERS = CYCLES | K35 | F8

EXPECTED_CARRIER_DIGEST = "159bcbb791299809a3df165123217b6d6084ca58ced87614eaa0c0a8e7fbcb9c"
EXPECTED_ORDER8_DIGEST = "3aa7c2bc965ea0ef0ac670f2efb2e6af9d2b606d07a80a46afbc6c2f12acf70c"
EXPECTED_ORDER9_DIGEST = "01958300b6bd7ad4cadfde77ad55c8a616d17221bb7e796ebba6e0718b97949b"


def contains(mask: int, family: frozenset[int]) -> bool:
    return any(pattern & mask == pattern for pattern in family)


def carrier_kind(mask: int) -> str | None:
    if contains(mask, CYCLES):
        return "C8"
    if contains(mask, K35):
        return "K35"
    if contains(mask, F8):
        return "F8"
    return None


def relabelled_terminal_data(
    adjacency: tuple[int, ...], root: int
) -> tuple[tuple[int, ...], int, int]:
    old_terminals = tuple(vertex for vertex in range(9) if vertex != root)
    image = {old: new for new, old in enumerate(old_terminals)}
    terminal_adjacency = [0] * 8
    terminal_mask = 0
    for old_left, old_right in edges(adjacency):
        if root in (old_left, old_right):
            continue
        left, right = image[old_left], image[old_right]
        terminal_adjacency[left] |= 1 << right
        terminal_adjacency[right] |= 1 << left
        terminal_mask |= 1 << PAIR_INDEX[tuple(sorted((left, right)))]
    neighbour_mask = sum(
        1 << image[old]
        for old in old_terminals
        if adjacency[root] >> old & 1
    )
    return tuple(terminal_adjacency), terminal_mask, neighbour_mask


def theta_exception(
    terminal_adjacency: tuple[int, ...], neighbour_mask: int
) -> tuple[int, ...] | None:
    degree_two = tuple(
        vertex
        for vertex in range(8)
        if terminal_adjacency[vertex].bit_count() == 2
    )
    branch = tuple(vertex for vertex in range(8) if vertex not in degree_two)
    if len(degree_two) != 6 or len(branch) != 2:
        return None
    degree_two_mask = sum(1 << vertex for vertex in degree_two)
    branch_mask = sum(1 << vertex for vertex in branch)
    if neighbour_mask & degree_two_mask != degree_two_mask:
        return None
    matching_edges = []
    for vertex in degree_two:
        internal = terminal_adjacency[vertex] & degree_two_mask
        outside = terminal_adjacency[vertex] & branch_mask
        if internal.bit_count() != 1 or outside.bit_count() != 1:
            return None
        mate = (internal & -internal).bit_length() - 1
        if vertex < mate:
            matching_edges.append((vertex, mate))
    if len(matching_edges) != 3:
        return None
    for left, right in matching_edges:
        left_branch = terminal_adjacency[left] & branch_mask
        right_branch = terminal_adjacency[right] & branch_mask
        if left_branch == right_branch:
            return None
    return degree_two


def owner_mask(terminal_mask: int, neighbour_mask: int, owner: int) -> int:
    answer = terminal_mask
    for other in range(8):
        if other != owner and neighbour_mask >> other & 1:
            answer |= 1 << PAIR_INDEX[tuple(sorted((owner, other)))]
    return answer


def digest(lines) -> str:
    payload = "\n".join(sorted(lines)).encode()
    return hashlib.sha256(payload).hexdigest()


def verify_order_eight():
    total = three = minimal = 0
    records = []
    failures = []
    minimal_profile: dict[int, int] = {}
    for code, adjacency in geng(8):
        total += 1
        if not three_connected(adjacency):
            continue
        three += 1
        mask = adjacency_mask(adjacency)
        kind = carrier_kind(mask)
        if kind is None:
            failures.append(code.decode())
        records.append(f"{code.decode()}:{kind}")
        if any(
            three_connected(delete_edge(adjacency, left, right))
            for left, right in edges(adjacency)
        ):
            continue
        minimal += 1
        edge_count = mask.bit_count()
        minimal_profile[edge_count] = minimal_profile.get(edge_count, 0) + 1
    assert not failures
    assert (total, three, minimal) == (2589, 2388, 18)
    assert minimal_profile == {12: 4, 13: 11, 14: 2, 15: 1}
    return total, three, minimal, minimal_profile, digest(records)


def verify_order_nine():
    total = three = rooted = theta = 0
    records = []
    failures = []
    exact_families = set()
    for code, adjacency in geng(9):
        total += 1
        if not three_connected(adjacency):
            continue
        three += 1
        for root in range(9):
            if any(
                two_connected_after_deleting(adjacency, root, neighbour)
                for neighbour in range(9)
                if adjacency[root] >> neighbour & 1
            ):
                continue
            rooted += 1
            terminal_adjacency, terminal_mask, neighbour_mask = relabelled_terminal_data(
                adjacency, root
            )
            exact_families.add((terminal_mask, neighbour_mask))
            if contains(terminal_mask, CYCLES):
                kind = "C8"
            else:
                owners = theta_exception(terminal_adjacency, neighbour_mask)
                if owners is None:
                    failures.append((code.decode(), root, "not-theta"))
                    continue
                theta += 1
                bad_owners = tuple(
                    owner
                    for owner in owners
                    if not contains(owner_mask(terminal_mask, neighbour_mask, owner), CYCLES)
                )
                if bad_owners:
                    failures.append((code.decode(), root, bad_owners))
                    continue
                kind = "theta"
            records.append(
                f"{code.decode()}:{root}:{terminal_mask:07x}:{neighbour_mask:02x}:{kind}"
            )
    assert not failures
    assert (total, three, rooted, theta) == (84242, 80890, 97, 6)
    return total, three, rooted, theta, len(exact_families), digest(records)


def main() -> None:
    catalogue_digest = digest(f"{mask:07x}" for mask in ALL_CARRIERS)
    assert catalogue_digest == EXPECTED_CARRIER_DIGEST
    order_eight = verify_order_eight()
    order_nine = verify_order_nine()
    assert order_eight[-1] == EXPECTED_ORDER8_DIGEST
    assert order_nine[-1] == EXPECTED_ORDER9_DIGEST
    print("carrier_counts", len(CYCLES), len(K35), len(F8), len(ALL_CARRIERS))
    print("carrier_digest", catalogue_digest)
    print("order8", order_eight)
    print("order9", order_nine)
    print("PASS")


if __name__ == "__main__":
    main()
