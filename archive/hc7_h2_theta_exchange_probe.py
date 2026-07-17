#!/usr/bin/env python3
"""Exhaustive labelled probe for the h=2 endpoint-rigid theta exchange.

This is an active proof-discovery script, not a promoted theorem.

The audited mixed-shore normalization has boundary

    S = {s,x,r1,r2,a,b,c,d},

where s is universal in S and S-{s,x} is the theta graph consisting of
the edge r1-r2 and the two length-three paths r1-b-a-r2 and
r1-d-c-r2.  A support-six K5 model has two singleton rows in U, two
singleton boundary rows w1,w2, and the edge row {v,t}.  Two components of
V-v have distinct missed contacts in {s,w1,w2}.

Seven-connectivity supplies two disjoint paths from the U rows to two
distinct vertices of S-{s,t,w1,w2}.  We contract each stopped path into
its U row and contract each of the two components of V-v.  Only forced
edges are retained.  Thus a K7 model found below lifts literally to the
host graph.

The script checks every legal placement of t,w1,w2, both exact choices for
the optional v-w contact, all three unordered pairs of distinct missed
labels, and every possible pair of Menger terminals.  It verifies the three
explicit branch-set constructions in the hand proof (the endpoint-matching
case and its two Hall-failure forms) using only the Python standard library.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


THETA = ("r1", "r2", "a", "b", "c", "d")
BOUNDARY = ("s", "x") + THETA
THETA_EDGES = {
    frozenset(edge)
    for edge in (
        ("r1", "r2"),
        ("r1", "b"),
        ("b", "a"),
        ("a", "r2"),
        ("r1", "d"),
        ("d", "c"),
        ("c", "r2"),
    )
}


def edge(left: str, right: str) -> frozenset[str]:
    assert left != right
    return frozenset((left, right))


def adjacent(edges: set[frozenset[str]], left: str, right: str) -> bool:
    return edge(left, right) in edges


@dataclass(frozen=True)
class Case:
    t: str
    w1: str
    w2: str
    v_meets_t_neighbour: bool | None
    missed1: str
    missed2: str
    anchor1: str
    anchor2: str

    @property
    def defect(self) -> str:
        met = sum(
            edge(self.t, w) in THETA_EDGES for w in (self.w1, self.w2)
        )
        if met == 0:
            return "(2,2,0)"
        return "(2,1,1)" if self.v_meets_t_neighbour else "(3,1,0)"


def legal_placements():
    for w1, w2 in combinations(THETA, 2):
        if edge(w1, w2) not in THETA_EDGES:
            continue
        for t in THETA:
            if t in (w1, w2):
                continue
            contacts = tuple(w for w in (w1, w2) if edge(t, w) in THETA_EDGES)
            if len(contacts) == 2:
                continue  # t must miss at least one boundary singleton row
            variants = (None,) if len(contacts) == 0 else (False, True)
            for variant in variants:
                yield t, w1, w2, variant


def build(case: Case) -> tuple[tuple[str, ...], set[frozenset[str]]]:
    # R1,R2 are the two U singleton rows after their disjoint stopped
    # anchor paths have been contracted into them.  The anchor terminal is
    # consequently removed from the remaining boundary.
    remaining_boundary = tuple(
        vertex for vertex in BOUNDARY if vertex not in (case.anchor1, case.anchor2)
    )
    vertices = ("R1", "R2", "v", "C1", "C2") + remaining_boundary
    edges: set[frozenset[str]] = set()

    # Exact forced boundary graph.  No unproved x--theta edge is inserted.
    edges.update(e for e in THETA_EDGES if e <= set(remaining_boundary))
    for vertex in remaining_boundary:
        if vertex != "s":
            edges.add(edge("s", vertex))

    # Original K5 row adjacencies, plus the boundary contacts inherited by
    # the contracted anchor path terminal.
    edges.add(edge("R1", "R2"))
    for row, terminal in (("R1", case.anchor1), ("R2", case.anchor2)):
        for vertex in (case.w1, case.w2, case.t):
            edges.add(edge(row, vertex))
        edges.add(edge(row, "s"))
        for vertex in THETA:
            if vertex in remaining_boundary and edge(terminal, vertex) in THETA_EDGES:
                edges.add(edge(row, vertex))
        # Each component meets every possible anchor terminal because its
        # missed contact is in {s,w1,w2}.
        edges.add(edge(row, "C1"))
        edges.add(edge(row, "C2"))

    # Exact edge-row contacts.  v meets each singleton missed by t; when t
    # meets exactly one w, the optional redundant v contact distinguishes
    # defect (2,1,1) from (3,1,0).
    edges.add(edge("v", case.t))
    for w in (case.w1, case.w2):
        if edge(case.t, w) not in THETA_EDGES:
            edges.add(edge("v", w))
        elif case.v_meets_t_neighbour:
            edges.add(edge("v", w))

    # Contracted components of V-v.  They are anticomplete to one another,
    # meet v, and meet exactly the seven non-missed boundary vertices.
    for component, missed in (("C1", case.missed1), ("C2", case.missed2)):
        edges.add(edge(component, "v"))
        for vertex in remaining_boundary:
            if vertex != missed:
                edges.add(edge(component, vertex))

    assert all(e <= set(vertices) for e in edges)
    return vertices, edges


def endpoint_contacts(
    boundary_vertex: str,
    t: str,
    edges: set[frozenset[str]],
) -> frozenset[str]:
    return frozenset(
        endpoint
        for endpoint in ("v", t)
        if adjacent(edges, endpoint, boundary_vertex)
    )


def explicit_model(
    case: Case,
    edges: set[frozenset[str]],
) -> tuple[str, tuple[tuple[str, ...], ...]]:
    """Return the matching/Hall branch-set construction from the hand proof."""
    contacts1 = endpoint_contacts(case.missed1, case.t, edges)
    contacts2 = endpoint_contacts(case.missed2, case.t, edges)
    assert contacts1 and contacts2

    # Distinct representatives of the two missed-contact sets.
    for endpoint1, endpoint2 in (("v", case.t), (case.t, "v")):
        if endpoint1 in contacts1 and endpoint2 in contacts2:
            return "matching", (
                ("R1",),
                ("R2",),
                ("C1", endpoint1),
                ("C2", endpoint2),
                ("s",),
                (case.w1,),
                (case.w2,),
            )

    # Hall failure forces two identical singleton contact sets.
    assert contacts1 == contacts2 and len(contacts1) == 1
    common_endpoint = next(iter(contacts1))
    free = tuple(
        vertex
        for vertex in BOUNDARY
        if vertex not in ("s", case.t, case.w1, case.w2, case.anchor1, case.anchor2)
    )
    assert free
    r = free[0]

    component_for = {case.missed1: "C1", case.missed2: "C2"}
    if common_endpoint == "v":
        # Both missing labels are w1,w2.  Orient them exactly as Form A.
        assert {case.missed1, case.missed2} == {case.w1, case.w2}
        return "hall-v", (
            ("R1",),
            ("R2",),
            (component_for[case.w1],),
            (case.t,),
            ("s",),
            (component_for[case.w2], r),
            ("v", case.w2),
        )

    # One missing label is s and the other is the unique w met by t.
    assert common_endpoint == case.t
    assert "s" in component_for
    missed_w = next(label for label in component_for if label != "s")
    other_w = next(w for w in (case.w1, case.w2) if w != missed_w)
    return "hall-t", (
        ("R1",),
        ("R2",),
        (component_for["s"],),
        (other_w,),
        (missed_w,),
        (component_for[missed_w], case.t),
        ("s", r),
    )


def verify_model(
    vertices: tuple[str, ...],
    edges: set[frozenset[str]],
    bags: tuple[tuple[str, ...], ...],
) -> None:
    flat = [v for bag in bags for v in bag]
    assert len(bags) == 7 and all(bags)
    assert len(flat) == len(set(flat)) and set(flat) <= set(vertices)
    for bag in bags:
        reached = {bag[0]}
        while True:
            new = reached | {
                v for v in bag if any(edge(v, u) in edges for u in reached if u != v)
            }
            if new == reached:
                break
            reached = new
        assert reached == set(bag), bag
    for left, right in combinations(bags, 2):
        assert any(edge(u, v) in edges for u in left for v in right), (left, right)


def main() -> None:
    cases = 0
    construction_counts = {"matching": 0, "hall-v": 0, "hall-t": 0}
    defect_counts: dict[str, int] = {}

    for t, w1, w2, variant in legal_placements():
        free = tuple(vertex for vertex in BOUNDARY if vertex not in ("s", t, w1, w2))
        for missed1, missed2 in combinations(("s", w1, w2), 2):
            for anchor1, anchor2 in combinations(free, 2):
                case = Case(t, w1, w2, variant, missed1, missed2, anchor1, anchor2)
                vertices, edges = build(case)
                construction, model = explicit_model(case, edges)
                verify_model(vertices, edges, model)
                cases += 1
                construction_counts[construction] += 1
                defect_counts[case.defect] = defect_counts.get(case.defect, 0) + 1

    print(f"cases={cases}")
    print("failures=0")
    for name in sorted(defect_counts):
        print("defect", name, defect_counts[name])
    for name in ("matching", "hall-v", "hall-t"):
        print("construction", name, construction_counts[name])


if __name__ == "__main__":
    main()
