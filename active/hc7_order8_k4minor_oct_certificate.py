#!/usr/bin/env python3
"""Generate certificates for the order-eight K4-minor/OCT dichotomy.

The exact finite statement checked is:

    Every simple graph on eight vertices either has an odd-cycle
    transversal of size at most two or contains a K4 minor.

Consequently every eight-vertex K4-minor-free graph has an odd-cycle
transversal of size at most two.

Nauty's ``geng -q 8`` supplies one representative of every isomorphism
class of simple eight-vertex graphs.  For each representative this script
emits either:

* ``OCT`` and a set of at most two vertices whose deletion is bipartite; or
* ``K4`` and four disjoint connected branch sets that are pairwise adjacent.

Invocation:

    python3 active/hc7_order8_k4minor_oct_certificate.py

To retain the canonical certificate as a file:

    python3 active/hc7_order8_k4minor_oct_certificate.py \
        --output /tmp/hc7-order8-k4minor-oct.cert

The companion checker validates the certificate without using this
script's witness-search routines.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import shutil
import subprocess
from pathlib import Path


ORDER = 8
ALL_VERTICES = (1 << ORDER) - 1
EXPECTED_GRAPHS = 12_346
EXPECTED_OCT = 8_876
EXPECTED_K4 = 3_470
EXPECTED_SHA256 = "a15a855eb45886eccac037642266ff47532f490301fc6fff9a495b07f923912e"


def decode_graph6(code: str) -> tuple[int, ...]:
    """Decode a short graph6 string as adjacency bitsets."""

    values = [ord(char) - 63 for char in code.strip()]
    if not values or values[0] != ORDER:
        raise ValueError(f"expected an order-{ORDER} graph6 code: {code!r}")
    bits: list[int] = []
    for value in values[1:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    adjacency = [0] * ORDER
    position = 0
    for right in range(1, ORDER):
        for left in range(right):
            if bits[position]:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
            position += 1
    return tuple(adjacency)


def graph6_catalogue() -> list[tuple[str, tuple[int, ...]]]:
    """Return the complete canonical order-eight catalogue from nauty."""

    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("nauty's `geng` executable is required")
    result = subprocess.run(
        [executable, "-q", str(ORDER)],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    catalogue = [
        (line, decode_graph6(line))
        for line in result.stdout.splitlines()
        if line and not line.startswith(">")
    ]
    if len(catalogue) != EXPECTED_GRAPHS:
        raise RuntimeError(
            f"expected {EXPECTED_GRAPHS} graph6 records, got {len(catalogue)}"
        )
    if len({code for code, _ in catalogue}) != EXPECTED_GRAPHS:
        raise RuntimeError("geng returned duplicate graph6 records")
    return sorted(catalogue)


def bipartite_after_deleting(
    adjacency: tuple[int, ...], deleted: int
) -> bool:
    colours = [-1] * ORDER
    for root in range(ORDER):
        if deleted >> root & 1 or colours[root] >= 0:
            continue
        colours[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            neighbours = adjacency[vertex] & ~deleted
            while neighbours:
                bit = neighbours & -neighbours
                neighbours ^= bit
                other = bit.bit_length() - 1
                if colours[other] < 0:
                    colours[other] = colours[vertex] ^ 1
                    stack.append(other)
                elif colours[other] == colours[vertex]:
                    return False
    return True


def find_oct(adjacency: tuple[int, ...]) -> int | None:
    """Return the lexicographically first OCT mask of size at most two."""

    for size in range(3):
        for vertices in itertools.combinations(range(ORDER), size):
            deleted = sum(1 << vertex for vertex in vertices)
            if bipartite_after_deleting(adjacency, deleted):
                return deleted
    return None


def connected(adjacency: tuple[int, ...], vertices: int) -> bool:
    if not vertices:
        return False
    reached = vertices & -vertices
    while True:
        old = reached
        frontier = reached
        neighbours = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        reached |= neighbours & vertices
        if reached == old:
            return reached == vertices


def adjacent(
    adjacency: tuple[int, ...], first: int, second: int
) -> bool:
    vertices = first
    while vertices:
        bit = vertices & -vertices
        vertices ^= bit
        if adjacency[bit.bit_length() - 1] & second:
            return True
    return False


def find_k4_model(
    adjacency: tuple[int, ...],
) -> tuple[int, int, int, int] | None:
    """Find four disjoint, connected, pairwise adjacent branch sets."""

    connected_sets = tuple(
        mask
        for mask in range(1, ALL_VERTICES + 1)
        if connected(adjacency, mask)
    )
    for first_index, first in enumerate(connected_sets):
        for second_index in range(first_index + 1, len(connected_sets)):
            second = connected_sets[second_index]
            if first & second or not adjacent(adjacency, first, second):
                continue
            for third_index in range(second_index + 1, len(connected_sets)):
                third = connected_sets[third_index]
                if (
                    third & (first | second)
                    or not adjacent(adjacency, first, third)
                    or not adjacent(adjacency, second, third)
                ):
                    continue
                for fourth in connected_sets[third_index + 1 :]:
                    if (
                        fourth & (first | second | third)
                        or not adjacent(adjacency, first, fourth)
                        or not adjacent(adjacency, second, fourth)
                        or not adjacent(adjacency, third, fourth)
                    ):
                        continue
                    return first, second, third, fourth
    return None


def record(code: str, adjacency: tuple[int, ...]) -> tuple[str, str]:
    oct_mask = find_oct(adjacency)
    if oct_mask is not None:
        return "OCT", f"{code}\tOCT\t{oct_mask:02x}"
    model = find_k4_model(adjacency)
    if model is None:
        raise AssertionError(
            f"counterexample: graph6={code} has neither required witness"
        )
    encoded = ",".join(f"{branch_set:02x}" for branch_set in model)
    return "K4", f"{code}\tK4\t{encoded}"


def main() -> None:
    if not __debug__:
        raise SystemExit("certificate checks require normal Python mode (without -O)")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="path for the generated canonical certificate",
    )
    arguments = parser.parse_args()

    records: list[str] = []
    counts = {"OCT": 0, "K4": 0}
    for code, adjacency in graph6_catalogue():
        kind, line = record(code, adjacency)
        counts[kind] += 1
        records.append(line)

    payload = ("\n".join(records) + "\n").encode("ascii")
    digest = hashlib.sha256(payload).hexdigest()
    assert counts == {"OCT": EXPECTED_OCT, "K4": EXPECTED_K4}
    assert digest == EXPECTED_SHA256

    header = (
        "# hc7 order-eight K4-minor/OCT certificate v1\n"
        f"# graphs={EXPECTED_GRAPHS} oct={EXPECTED_OCT} k4={EXPECTED_K4}\n"
        f"# records_sha256={EXPECTED_SHA256}\n"
    )
    if arguments.output is not None:
        arguments.output.write_bytes(header.encode("ascii") + payload)
    print(f"graphs {EXPECTED_GRAPHS}")
    print(f"oct_witnesses {EXPECTED_OCT}")
    print(f"k4_witnesses {EXPECTED_K4}")
    print(f"records_sha256 {digest}")
    if arguments.output is not None:
        print(f"certificate {arguments.output}")
    print("PASS")


if __name__ == "__main__":
    main()
