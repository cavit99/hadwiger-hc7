#!/usr/bin/env python3
"""Symbolic CEGIS for crossed order-six frames without a w-absorber.

The solver imposes every local seven-connectivity inequality, the terminal
degree inequality, full attachment, and all-edge-blocked contraction status.
For one internal shore type and one C5 frame it additionally requires the two
missing-edge paths to be vertex-disjoint.  Monotone absorber certificates are
then excluded until either a genuine crossed/no-absorber attachment is found
or the formula becomes UNSAT.
"""

from __future__ import annotations

import argparse
import json

import z3

from moser_order6_absorber_probe import (
    A,
    FRAMES,
    L,
    MISSING,
    ROOTS,
    adjacent,
    b,
    connected,
    d,
    find_absorber_masks,
    graph_edges,
    vertices,
)
from portal_k6k1_probe import AttachmentSolver, TYPES


def components(mask: int, fedges: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    unseen = {i for i in range(6) if mask & (1 << i)}
    answer = []
    while unseen:
        comp = {next(iter(unseen))}
        while True:
            more = {
                y
                for x in comp
                for y in unseen - comp
                if tuple(sorted((x, y))) in fedges
            }
            if not more:
                break
            comp |= more
        unseen -= comp
        answer.append(tuple(sorted(comp)))
    return answer


def block_connected_formula(x, fedges, mask: int, endpoints: tuple[int, int]):
    """Connectivity after collapsing fixed components of D[mask]."""
    if not mask:
        return z3.BoolVal(False)
    endpoint_bits = tuple(L.index(endpoint) for endpoint in endpoints)
    comps = components(mask, fedges)
    incidence = {
        (c, p): z3.Or(*(x[i][endpoint_bits[p]] for i in comp))
        for c, comp in enumerate(comps)
        for p in range(2)
    }
    conditions = [
        z3.Or(*(incidence[c, p] for c in range(len(comps)))) for p in range(2)
    ]
    conditions.extend(
        z3.Or(incidence[c, 0], incidence[c, 1]) for c in range(len(comps))
    )
    conditions.append(z3.Or(*(
        z3.And(incidence[c, 0], incidence[c, 1]) for c in range(len(comps))
    )))
    return z3.And(*conditions)


def crossing_formula(x, fedges, frame: tuple[int, int]):
    e, f = (MISSING[index] for index in frame)
    choices = []
    for mask_e in range(1, 1 << 6):
        conn_e = block_connected_formula(x, fedges, mask_e, e)
        available = ((1 << 6) - 1) ^ mask_e
        mask_f = available
        while mask_f:
            choices.append(z3.And(
                conn_e, block_connected_formula(x, fedges, mask_f, f)
            ))
            mask_f = (mask_f - 1) & available
    return z3.Or(*choices)


def certificate_valid(record: dict, frame: tuple[int, int], cert) -> bool:
    mask_e, mask_f, mask_w = cert
    if mask_e & mask_f or mask_e & mask_w or mask_f & mask_w:
        return False
    edges = graph_edges(record)
    e, f = (MISSING[index] for index in frame)
    leftover = next(root for root in ROOTS if root not in e + f)
    block_e = vertices(mask_e) | {b(e[0]), b(e[1])}
    block_f = vertices(mask_f) | {b(f[0]), b(f[1])}
    block_w = vertices(mask_w) | {b("w")}
    if not all(connected(block, edges) for block in (block_e, block_f, block_w)):
        return False
    targets = (block_e, block_f, {b(leftover)}, {b(A)})
    return adjacent(block_e, block_f, edges) and all(
        adjacent(block_w, target, edges) for target in targets
    )


def record_from(name, fedges, instance) -> dict:
    return {
        "type": name,
        "internal_edges": [list(edge) for edge in sorted(fedges)],
        "aw": instance.aw,
        "rows": list(instance.rows),
    }


def minimize_support(record, frame, cert):
    keys = []
    if record["aw"]:
        keys.append(("aw",))
    for i, row in enumerate(record["rows"]):
        for bit in range(7):
            if row & (1 << bit):
                keys.append(("x", i, bit))

    def reduced(keep):
        rows = [0] * 6
        aw = False
        for key in keep:
            if key[0] == "aw":
                aw = True
            else:
                rows[key[1]] |= 1 << key[2]
        return {
            "type": record["type"],
            "internal_edges": record["internal_edges"],
            "aw": aw,
            "rows": rows,
        }

    keep = list(keys)
    for key in list(keys):
        trial = [item for item in keep if item != key]
        if certificate_valid(reduced(trial), frame, cert):
            keep = trial
    assert certificate_valid(reduced(keep), frame, cert)
    return tuple(keep)


def solve(name: str, frame: tuple[int, int], limit: int) -> dict:
    fedges = TYPES[name]
    solver = AttachmentSolver(fedges, blocked_only=True)
    solver.solver.add(crossing_formula(solver.x, fedges, frame))
    supports = []
    for iteration in range(limit):
        instance = solver.next()
        if instance is None:
            return {"status": "unsat", "supports": supports}
        record = record_from(name, fedges, instance)
        crossed, cert = find_absorber_masks(record, frame)
        assert crossed
        if cert is None:
            return {
                "status": "sat",
                "supports": supports,
                "survivor": {"aw": instance.aw, "rows": list(instance.rows)},
            }
        support = minimize_support(record, frame, cert)
        assert support
        supports.append({"required": [list(key) for key in support], "masks": list(cert)})
        solver.exclude_support(support)
        if iteration and iteration % 100 == 0:
            print(name, frame, iteration, flush=True)
    return {"status": "limit", "supports": supports}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--types", nargs="*", default=[])
    parser.add_argument("--limit", type=int, default=10000)
    parser.add_argument("--output", default="moser_order6_absorber_cegis.json")
    args = parser.parse_args()
    names = args.types or list(TYPES)
    archive = {"format": 1, "types": {}}
    for name in names:
        archive["types"][name] = {}
        for frame in FRAMES:
            result = solve(name, frame, args.limit)
            archive["types"][name][f"{frame[0]}-{frame[1]}"] = result
            print(name, frame, result["status"], len(result["supports"]), flush=True)
        with open(args.output, "w", encoding="utf-8") as target:
            json.dump(archive, target, indent=2)


if __name__ == "__main__":
    main()
