#!/usr/bin/env python3
"""Search order-three portal pieces for the first transition survivor."""

from itertools import product
import random

from degree8_transition_gadget_search import (
    STATES, candidates, transition_ok, N, Z,
)


HOOD_AVAIL = {}
COLORABLE = {}


def hood_availability(hood):
    hood = frozenset(hood)
    if hood not in HOOD_AVAIL:
        values = []
        for colors, _, _ in STATES:
            forbidden = 0
            for x in hood:
                forbidden |= 1 << colors[x]
            values.append(0b111111 & ~forbidden)
        HOOD_AVAIL[hood] = tuple(values)
    return HOOD_AVAIL[hood]


def list_colorable(masks, internal_edges):
    key = (masks, tuple(sorted(internal_edges)))
    if key in COLORABLE:
        return COLORABLE[key]
    choices = [tuple(color for color in range(6) if mask >> color & 1)
               for mask in masks]
    answer = False
    if all(choices):
        for assignment in product(*choices):
            if all(assignment[u] != assignment[v] for u, v in internal_edges):
                answer = True
                break
    COLORABLE[key] = answer
    return answer


def extension_family(vertex_count, internal_edges, neighborhoods,
                     extra_boundary_edges=()):
    internal_edges = {tuple(sorted(edge)) for edge in internal_edges}
    extra_boundary_edges = tuple(extra_boundary_edges)
    avail_columns = [hood_availability(hood) for hood in neighborhoods]
    bits = 0
    for state_index, (colors, _, _) in enumerate(STATES):
        if any(colors[x] == colors[y] for x, y in extra_boundary_edges):
            continue
        masks = tuple(column[state_index] for column in avail_columns)
        if list_colorable(masks, internal_edges):
            bits |= 1 << state_index
    return bits


def delete_vertex(vertex_count, internal_edges, neighborhoods, deleted):
    keep = [x for x in range(vertex_count) if x != deleted]
    relabel = {old: new for new, old in enumerate(keep)}
    edges = {(relabel[u], relabel[v]) for u, v in internal_edges
             if u != deleted and v != deleted}
    hoods = [neighborhoods[old] for old in keep]
    return len(keep), edges, hoods, ()


def contract_internal(vertex_count, internal_edges, neighborhoods, edge):
    u, v = edge
    keep = [x for x in range(vertex_count) if x != v]
    relabel = {old: new for new, old in enumerate(keep)}
    merged_old = u
    hoods = []
    for old in keep:
        if old == merged_old:
            hoods.append(frozenset(neighborhoods[u] | neighborhoods[v]))
        else:
            hoods.append(neighborhoods[old])
    edges = set()
    for a, b in internal_edges:
        if (a, b) == tuple(sorted(edge)):
            continue
        aa = u if a == v else a
        bb = u if b == v else b
        if aa != bb:
            edges.add(tuple(sorted((relabel[aa], relabel[bb]))))
    return vertex_count - 1, edges, hoods, ()


def contract_boundary(vertex_count, internal_edges, neighborhoods,
                      interior, boundary):
    keep = [x for x in range(vertex_count) if x != interior]
    relabel = {old: new for new, old in enumerate(keep)}
    hoods = []
    for old in keep:
        hood = set(neighborhoods[old])
        if tuple(sorted((old, interior))) in internal_edges:
            hood.add(boundary)
        hoods.append(frozenset(hood))
    edges = {(relabel[u], relabel[v]) for u, v in internal_edges
             if u != interior and v != interior}
    extras = tuple((boundary, x) for x in neighborhoods[interior]
                   if x != boundary)
    return vertex_count - 1, edges, hoods, extras


def order3_signature(internal_edges, neighborhoods):
    internal_edges = {tuple(sorted(edge)) for edge in internal_edges}
    neighborhoods = tuple(frozenset(hood) for hood in neighborhoods)
    base = extension_family(3, internal_edges, neighborhoods)
    operated = []

    for vertex in range(3):
        data = delete_vertex(3, internal_edges, neighborhoods, vertex)
        operated.append((f"del_v{vertex}", extension_family(*data)))

    for edge in sorted(internal_edges):
        deleted_edges = internal_edges - {edge}
        operated.append((f"del_e{edge}",
                         extension_family(3, deleted_edges, neighborhoods)))
        data = contract_internal(3, internal_edges, neighborhoods, edge)
        operated.append((f"con_e{edge}", extension_family(*data)))

    for vertex in range(3):
        for boundary in sorted(neighborhoods[vertex]):
            reduced = list(neighborhoods)
            reduced[vertex] = frozenset(set(reduced[vertex]) - {boundary})
            operated.append((f"del_{vertex}_{boundary}",
                             extension_family(3, internal_edges, reduced)))
            data = contract_boundary(3, internal_edges, neighborhoods,
                                     vertex, boundary)
            operated.append((f"con_{vertex}_{boundary}",
                             extension_family(*data)))

    return {
        "order": 3,
        "edges": tuple(sorted(internal_edges)),
        "hoods": neighborhoods,
        "E": base,
        "new": tuple((name, result & ~base) for name, result in operated),
    }


def random_piece(required, rng):
    hoods = [set(), set(), set()]
    for x in required:
        subset = rng.randrange(1, 8)
        for vertex in range(3):
            if subset >> vertex & 1:
                hoods[vertex].add(x)
    edges = ((0, 1), (1, 2)) if rng.randrange(2) == 0 \
        else ((0, 1), (0, 2), (1, 2))
    return order3_signature(edges, hoods)


def find_with_large(large, small_a, small_b, position):
    for first in small_a:
        for second in small_b:
            pieces = [None, None, None]
            pieces[position] = large
            pieces[(position + 1) % 3] = first
            pieces[(position + 2) % 3] = second
            if pieces[0]["E"] & pieces[1]["E"] & pieces[2]["E"]:
                continue
            if all(transition_ok(pieces[i], pieces[(i + 1) % 3],
                                 pieces[(i + 2) % 3]) for i in range(3)):
                return tuple(pieces)
    return None


def main():
    branch_required = tuple(x for x in range(9) if x not in (0, 1))
    d_required = tuple(x for x in range(8) if x != 0)
    small_branch = candidates(branch_required)
    small_d = candidates(d_required)
    rng = random.Random(20260711)

    critical_branch = critical_d = 0
    for iteration in range(500):
        large_branch = random_piece(branch_required, rng)
        if all(bits for _, bits in large_branch["new"]):
            critical_branch += 1
            found = find_with_large(large_branch, small_branch, small_d, 0)
            if found:
                print("ORDER3 SURVIVOR branch", iteration)
                for label, piece in zip(("R1", "R2", "D"), found):
                    print(label, piece.get("edges"), piece.get("hoods"),
                          piece.get("na"), piece.get("nb"))
                return

        large_d = random_piece(d_required, rng)
        if all(bits for _, bits in large_d["new"]):
            critical_d += 1
            found = find_with_large(large_d, small_branch, small_branch, 2)
            if found:
                print("ORDER3 SURVIVOR D", iteration)
                for label, piece in zip(("R1", "R2", "D"), found):
                    print(label, piece.get("edges"), piece.get("hoods"),
                          piece.get("na"), piece.get("nb"))
                return
        if iteration and iteration % 100 == 0:
            print("sampled", iteration, "critical", critical_branch, critical_d)
    print("no random survivor; critical order3 samples",
          critical_branch, critical_d)


if __name__ == "__main__":
    main()
