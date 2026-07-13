#!/usr/bin/env python3
"""Exact simultaneous-state test on the rank-(2,2) two-R-torso host.

For six nonempty portal classes P_0,...,P_5 on the fixed eight-vertex
host, the program encodes actual connected carriers.  It proves that the
following four conditions are inconsistent:

* the six portal classes have an SDR;
* for i=0,1,2 there are no disjoint carriers for e_i and e_{i+3};
* one shore owns both frames in each of two opposite frame pairs.

No outward-lock or three-linkage exclusion is imposed.  Thus the result
is stronger than the full local state test on this particular host.

The SMT formula is quantifier-free.  Every possible nonempty connected
vertex mask and every ordered disjoint pair of such masks is generated
directly from the host graph.  All three choices of two owned opposite
frame pairs are checked, so no label-symmetry assumption is hidden.
"""

from __future__ import annotations

import itertools
import subprocess

import networkx as nx

from c6_rank_four_leaf_counterexample import graph


def disjunction(parts: list[str]) -> str:
    if not parts:
        return "false"
    if len(parts) == 1:
        return parts[0]
    return f"(or {' '.join(parts)})"


def conjunction(parts: list[str]) -> str:
    if not parts:
        return "true"
    if len(parts) == 1:
        return parts[0]
    return f"(and {' '.join(parts)})"


class Encoding:
    def __init__(self) -> None:
        self.host = graph()
        self.vertices = tuple(self.host)
        self.order = len(self.vertices)
        self.connected_masks = tuple(
            mask
            for mask in range(1, 1 << self.order)
            if nx.is_connected(
                self.host.subgraph(
                    self.vertices[index]
                    for index in range(self.order)
                    if mask >> index & 1
                )
            )
        )
        self.disjoint_pairs = tuple(
            (first, second)
            for first in self.connected_masks
            for second in self.connected_masks
            if not first & second
        )

    def meets(self, label: int, mask: int) -> str:
        return disjunction(
            [
                f"p_{label}_{index}"
                for index in range(self.order)
                if mask >> index & 1
            ]
        )

    def carries(self, edge: tuple[int, int], mask: int) -> str:
        return conjunction(
            [self.meets(edge[0], mask), self.meets(edge[1], mask)]
        )

    def linkage(self, first_edge: tuple[int, int],
                second_edge: tuple[int, int]) -> str:
        return disjunction(
            [
                conjunction(
                    [self.carries(first_edge, first),
                     self.carries(second_edge, second)]
                )
                for first, second in self.disjoint_pairs
            ]
        )

    def formula(
        self,
        owned_pairs: tuple[int, ...] = (),
        *,
        sdr: bool,
        antipodal_indices: tuple[int, ...] = (0, 1, 2),
        owned_frames: tuple[int, ...] | None = None,
    ) -> str:
        lines = ["(set-logic QF_LIA)"]
        for label in range(6):
            for index in range(self.order):
                lines.append(f"(declare-fun p_{label}_{index} () Bool)")

            if sdr:
                lines.extend(
                    (
                        f"(declare-fun r_{label} () Int)",
                        f"(assert (and (<= 0 r_{label}) "
                        f"(< r_{label} {self.order})))",
                        "(assert "
                        + disjunction(
                            [
                                f"(and (= r_{label} {index}) "
                                f"p_{label}_{index})"
                                for index in range(self.order)
                            ]
                        )
                        + ")",
                    )
                )
            else:
                lines.append(
                    "(assert "
                    + disjunction(
                        [f"p_{label}_{index}" for index in range(self.order)]
                    )
                    + ")"
                )

        if sdr:
            lines.append(
                "(assert (distinct "
                + " ".join(f"r_{label}" for label in range(6))
                + "))"
            )

        # Three antipodal missing-edge linkages are absent.
        for index in antipodal_indices:
            first = (index, (index + 1) % 6)
            second = ((index + 3) % 6, (index + 4) % 6)
            lines.append(f"(assert (not {self.linkage(first, second)}))")

        # Opposite frame pair j consists of frames j and j+3.
        if owned_frames is None:
            owned_frames = tuple(
                frame for pair in owned_pairs for frame in (pair, pair + 3)
            )
        for frame in owned_frames:
            first = ((frame - 2) % 6, (frame - 1) % 6)
            second = ((frame + 2) % 6, (frame + 3) % 6)
            lines.append(f"(assert {self.linkage(first, second)})")

        lines.append("(check-sat)")
        return "\n".join(lines)


def solve(formula: str) -> str:
    result = subprocess.run(
        ("z3", "-in"),
        input=formula,
        text=True,
        capture_output=True,
        check=True,
        timeout=120,
    )
    assert not result.stderr
    return result.stdout.strip()


def main() -> None:
    encoding = Encoding()
    assert len(encoding.connected_masks) == 167
    assert len(encoding.disjoint_pairs) == 2270

    # The SDR is genuinely doing work: the coarse state without it exists.
    coarse = solve(encoding.formula((0, 1), sdr=False))
    assert coarse == "sat"

    outcomes = {}
    for owned in itertools.combinations(range(3), 2):
        outcome = solve(encoding.formula(owned, sdr=True))
        outcomes[owned] = outcome
        assert outcome == "unsat"

    normalized_frames = (0, 1, 3, 4)
    omit_antipodal = {
        omitted: solve(
            encoding.formula(
                sdr=True,
                antipodal_indices=tuple(
                    index for index in range(3) if index != omitted
                ),
                owned_frames=normalized_frames,
            )
        )
        for omitted in range(3)
    }
    omit_frame = {
        omitted: solve(
            encoding.formula(
                sdr=True,
                owned_frames=tuple(
                    frame for frame in normalized_frames if frame != omitted
                ),
            )
        )
        for omitted in normalized_frames
    }
    assert set(omit_antipodal.values()) == {"sat"}
    assert set(omit_frame.values()) == {"sat"}

    print("vertices", encoding.vertices)
    print("connected carrier masks", len(encoding.connected_masks))
    print("ordered disjoint carrier pairs", len(encoding.disjoint_pairs))
    print("without SDR", coarse)
    print("with SDR, two owned opposite frame pairs", outcomes)
    print("omit one antipodal exclusion", omit_antipodal)
    print("omit one owned frame", omit_frame)


if __name__ == "__main__":
    main()
