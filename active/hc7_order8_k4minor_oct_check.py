#!/usr/bin/env python3
"""Independently check the order-eight K4-minor/OCT certificate.

This checker does not search for witnesses and imports no code from the
generator.  It separately obtains nauty's complete order-eight graph6
catalogue, decodes each graph into an edge set, and directly validates the
recorded OCT or four-branch-set certificate.

Invocation:

    python3 active/hc7_order8_k4minor_oct_check.py

To check an existing certificate instead:

    python3 active/hc7_order8_k4minor_oct_check.py \
        /tmp/hc7-order8-k4minor-oct.cert
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ORDER = 8
EXPECTED_GRAPHS = 12_346
EXPECTED_OCT = 8_876
EXPECTED_K4 = 3_470
EXPECTED_SHA256 = "a15a855eb45886eccac037642266ff47532f490301fc6fff9a495b07f923912e"


def catalogue_codes() -> set[str]:
    executable = shutil.which("geng")
    if executable is None:
        raise SystemExit("nauty's `geng` executable is required")
    result = subprocess.run(
        [executable, "-q", str(ORDER)],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    codes = {
        line
        for line in result.stdout.splitlines()
        if line and not line.startswith(">")
    }
    if len(codes) != EXPECTED_GRAPHS:
        raise AssertionError(
            f"expected {EXPECTED_GRAPHS} catalogue entries, got {len(codes)}"
        )
    return codes


def graph6_edges(code: str) -> set[tuple[int, int]]:
    """Decode graph6 directly as an unordered edge set."""

    data = [ord(character) - 63 for character in code]
    if not data or data[0] != ORDER:
        raise AssertionError(f"not an order-{ORDER} graph6 code: {code!r}")
    bits = [
        (value >> shift) & 1
        for value in data[1:]
        for shift in range(5, -1, -1)
    ]
    pairs = [
        (left, right)
        for right in range(1, ORDER)
        for left in range(right)
    ]
    return {edge for edge, bit in zip(pairs, bits, strict=False) if bit}


def neighbours(
    vertex: int, edges: set[tuple[int, int]], allowed: set[int]
) -> set[int]:
    answer = set()
    for left, right in edges:
        if left == vertex and right in allowed:
            answer.add(right)
        elif right == vertex and left in allowed:
            answer.add(left)
    return answer


def connected(vertices: set[int], edges: set[tuple[int, int]]) -> bool:
    if not vertices:
        return False
    reached = {min(vertices)}
    while True:
        expanded = reached | set().union(
            *(neighbours(vertex, edges, vertices) for vertex in reached)
        )
        if expanded == reached:
            return reached == vertices
        reached = expanded


def validate_oct(
    code: str, payload: str, edges: set[tuple[int, int]]
) -> None:
    deleted_mask = int(payload, 16)
    if deleted_mask >= 1 << ORDER or deleted_mask.bit_count() > 2:
        raise AssertionError(f"{code}: invalid OCT mask {payload}")
    remaining = {
        vertex
        for vertex in range(ORDER)
        if not (deleted_mask >> vertex) & 1
    }
    colours: dict[int, int] = {}
    for root in sorted(remaining):
        if root in colours:
            continue
        colours[root] = 0
        queue = [root]
        while queue:
            vertex = queue.pop()
            for other in neighbours(vertex, edges, remaining):
                if other not in colours:
                    colours[other] = 1 - colours[vertex]
                    queue.append(other)
                elif colours[other] == colours[vertex]:
                    raise AssertionError(
                        f"{code}: deletion mask {payload} is not an OCT"
                    )


def validate_k4(
    code: str, payload: str, edges: set[tuple[int, int]]
) -> None:
    masks = [int(item, 16) for item in payload.split(",")]
    if len(masks) != 4 or any(
        mask <= 0 or mask >= 1 << ORDER for mask in masks
    ):
        raise AssertionError(f"{code}: invalid K4 branch-set encoding")
    if any(
        masks[first] & masks[second]
        for first in range(4)
        for second in range(first + 1, 4)
    ):
        raise AssertionError(f"{code}: K4 branch sets are not disjoint")
    branch_sets = [
        {vertex for vertex in range(ORDER) if mask >> vertex & 1}
        for mask in masks
    ]
    if not all(connected(branch_set, edges) for branch_set in branch_sets):
        raise AssertionError(f"{code}: a K4 branch set is disconnected")
    for first in range(4):
        for second in range(first + 1, 4):
            if not any(
                tuple(sorted((left, right))) in edges
                for left in branch_sets[first]
                for right in branch_sets[second]
            ):
                raise AssertionError(
                    f"{code}: K4 branch sets {first},{second} are nonadjacent"
                )


def check_certificate(certificate: Path) -> None:
    lines = certificate.read_text(encoding="ascii").splitlines()
    records = [line for line in lines if line and not line.startswith("#")]
    payload = ("\n".join(records) + "\n").encode("ascii")
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise AssertionError(
            f"certificate digest {digest} != {EXPECTED_SHA256}"
        )

    catalogue = catalogue_codes()
    seen: set[str] = set()
    counts = {"OCT": 0, "K4": 0}
    for line in records:
        fields = line.split("\t")
        if len(fields) != 3:
            raise AssertionError(f"malformed certificate line: {line!r}")
        code, kind, witness = fields
        if code in seen or code not in catalogue:
            raise AssertionError(f"duplicate or unknown graph6 code: {code}")
        seen.add(code)
        edges = graph6_edges(code)
        if kind == "OCT":
            validate_oct(code, witness, edges)
        elif kind == "K4":
            validate_k4(code, witness, edges)
        else:
            raise AssertionError(f"{code}: unknown witness kind {kind!r}")
        counts[kind] += 1

    if seen != catalogue:
        raise AssertionError(
            f"certificate misses {len(catalogue - seen)} catalogue entries"
        )
    if counts != {"OCT": EXPECTED_OCT, "K4": EXPECTED_K4}:
        raise AssertionError(f"unexpected witness counts: {counts}")

    print(f"graphs {len(seen)}")
    print(f"oct_witnesses {counts['OCT']}")
    print(f"k4_witnesses {counts['K4']}")
    print(f"records_sha256 {digest}")
    print("PASS")


def main() -> None:
    if not __debug__:
        raise SystemExit("certificate checks require normal Python mode (without -O)")

    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path, nargs="?")
    arguments = parser.parse_args()

    if arguments.certificate is not None:
        check_certificate(arguments.certificate)
        return

    generator = Path(__file__).with_name(
        "hc7_order8_k4minor_oct_certificate.py"
    )
    with tempfile.TemporaryDirectory(prefix="hc7-order8-oct-") as temporary:
        certificate = Path(temporary) / "certificate.txt"
        subprocess.run(
            [
                sys.executable,
                str(generator),
                "--output",
                str(certificate),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        check_certificate(certificate)


if __name__ == "__main__":
    main()
