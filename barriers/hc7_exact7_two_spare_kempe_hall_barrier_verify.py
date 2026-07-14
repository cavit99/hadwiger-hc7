#!/usr/bin/env python3
"""Verify the three-connected zero-column Kempe Hall barrier.

Run with an environment containing NetworkX and ``z3-solver``, for example:

    PYTHONPATH=active/runtime/deps python3 \
      barriers/hc7_exact7_two_spare_kempe_hall_barrier_verify.py
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

import networkx as nx
import z3


Vertex = str
Edge = tuple[Vertex, Vertex]

S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
CROSSINGS = tuple(f"v{i}{j}" for i in range(1, 4) for j in range(1, 4))
HORIZONTAL = tuple(f"h{i}{j}" for i in range(1, 4) for j in range(1, 3))
VERTICAL = tuple(f"g{i}{j}" for i in range(1, 3) for j in range(1, 4))
FACES = tuple(f"f{i}{j}" for i in range(1, 3) for j in range(1, 3))
C = (*CROSSINGS, *HORIZONTAL, *VERTICAL, *FACES)


def require(condition: bool, message: str) -> None:
    """Keep proof checks active under ``python -O``."""
    if not condition:
        raise RuntimeError(message)


def edge(left: Vertex, right: Vertex) -> Edge:
    require(left != right, "loops are forbidden")
    return tuple(sorted((left, right)))


COLOUR: dict[Vertex, int] = {
    "a1": 1,
    "t1": 1,
    "a2": 2,
    "t2": 2,
    "a3": 3,
    "t3": 3,
    "c": 4,
}
COLOUR.update({vertex: 6 for vertex in CROSSINGS})
COLOUR.update({vertex: 1 for vertex in HORIZONTAL})
COLOUR.update({vertex: 3 for vertex in VERTICAL})
COLOUR.update({vertex: 2 for vertex in FACES})

E_C: set[Edge] = set()
for i in range(1, 4):
    for j in range(1, 3):
        E_C.add(edge(f"v{i}{j}", f"h{i}{j}"))
        E_C.add(edge(f"h{i}{j}", f"v{i}{j + 1}"))
for i in range(1, 3):
    for j in range(1, 4):
        E_C.add(edge(f"v{i}{j}", f"g{i}{j}"))
        E_C.add(edge(f"g{i}{j}", f"v{i + 1}{j}"))
for i in range(1, 3):
    for j in range(1, 3):
        face = f"f{i}{j}"
        rim = (
            f"v{i}{j}",
            f"h{i}{j}",
            f"v{i}{j + 1}",
            f"g{i}{j + 1}",
            f"v{i + 1}{j + 1}",
            f"h{i + 1}{j}",
            f"v{i + 1}{j}",
            f"g{i}{j}",
        )
        E_C.update(edge(face, vertex) for vertex in rim)

CONTACTS: dict[Vertex, frozenset[Vertex]] = {
    "a1": frozenset(f"v{i}1" for i in range(1, 4)),
    "t1": frozenset(f"v{i}3" for i in range(1, 4)),
    "a3": frozenset(f"v1{j}" for j in range(1, 4)),
    "t3": frozenset(f"v3{j}" for j in range(1, 4)),
    "a2": frozenset(("v11",)),
    "t2": frozenset(("v33",)),
    "c": frozenset(("v12",)),
}

E_S = {
    edge("c", "a1"),
    edge("c", "a2"),
    edge("c", "a3"),
    edge("a1", "a2"),
    edge("a1", "a3"),
    edge("a2", "a3"),
}
E_CONTACT = {
    edge(literal, portal)
    for literal, portals in CONTACTS.items()
    for portal in portals
}
E_ALL = frozenset(E_C | E_S | E_CONTACT)


def graph(vertices: tuple[Vertex, ...], edges: set[Edge] | frozenset[Edge]) -> nx.Graph:
    answer = nx.Graph()
    answer.add_nodes_from(vertices)
    answer.add_edges_from(edges)
    return answer


def faces(embedding: nx.PlanarEmbedding) -> list[tuple[Vertex, ...]]:
    seen: set[tuple[Vertex, Vertex]] = set()
    answer: list[tuple[Vertex, ...]] = []
    for left, right in embedding.edges():
        if (left, right) not in seen:
            answer.append(tuple(embedding.traverse_face(left, right, seen)))
    return answer


def rotations(word: tuple[Vertex, ...]) -> set[tuple[Vertex, ...]]:
    return {word[index:] + word[:index] for index in range(len(word))}


def path_is_valid(path: tuple[Vertex, ...], edges: set[Edge] | frozenset[Edge]) -> bool:
    return len(path) == len(set(path)) and all(
        edge(left, right) in edges for left, right in zip(path, path[1:])
    )


def kempe_success(duty: int, spare: int) -> bool:
    shore = graph((*S, *C), E_ALL)
    allowed = {vertex for vertex in shore if COLOUR[vertex] in {duty, spare}}
    return not nx.has_path(shore.subgraph(allowed), f"a{duty}", f"t{duty}")


class RootedK4Solver:
    """Complete connected-bag encoding of the named rooted expansion."""

    def __init__(self) -> None:
        self.index = {vertex: index for index, vertex in enumerate(C)}
        order = len(C)
        self.member = [
            [z3.Bool(f"member_{index}_{bag}") for bag in range(4)]
            for index in range(order)
        ]
        self.root = [
            [z3.Bool(f"root_{index}_{bag}") for bag in range(4)]
            for index in range(order)
        ]
        self.depth = [
            [z3.Int(f"depth_{index}_{bag}") for bag in range(4)]
            for index in range(order)
        ]
        self.solver = z3.Solver()

        neighbours: dict[Vertex, list[Vertex]] = defaultdict(list)
        for left, right in E_C:
            neighbours[left].append(right)
            neighbours[right].append(left)

        for index in range(order):
            self.solver.add(
                z3.PbLe([(self.member[index][bag], 1) for bag in range(4)], 1)
            )

        for bag in range(4):
            self.solver.add(
                z3.PbEq([(self.root[index][bag], 1) for index in range(order)], 1)
            )
            for index, vertex in enumerate(C):
                self.solver.add(0 <= self.depth[index][bag])
                self.solver.add(self.depth[index][bag] < order)
                self.solver.add(
                    z3.Implies(
                        self.root[index][bag],
                        z3.And(self.member[index][bag], self.depth[index][bag] == 0),
                    )
                )
                lower_neighbour = z3.Or(
                    *[
                        z3.And(
                            self.member[self.index[other]][bag],
                            self.depth[self.index[other]][bag]
                            < self.depth[index][bag],
                        )
                        for other in neighbours[vertex]
                    ]
                )
                self.solver.add(
                    z3.Implies(
                        z3.And(
                            self.member[index][bag],
                            z3.Not(self.root[index][bag]),
                        ),
                        z3.And(self.depth[index][bag] >= 1, lower_neighbour),
                    )
                )

    def contact(self, bag: int, literal: Vertex) -> None:
        self.solver.add(
            z3.Or(*[self.member[self.index[v]][bag] for v in CONTACTS[literal]])
        )

    def pairwise_adjacent(self) -> None:
        for first, second in combinations(range(4), 2):
            witnesses = []
            for left, right in E_C:
                witnesses.extend(
                    (
                        z3.And(
                            self.member[self.index[left]][first],
                            self.member[self.index[right]][second],
                        ),
                        z3.And(
                            self.member[self.index[right]][first],
                            self.member[self.index[left]][second],
                        ),
                    )
                )
            self.solver.add(z3.Or(*witnesses))

    def exclude_impossible_roots(self) -> None:
        # Every connected traced H_i can be rooted at one of its assigned
        # first-side contacts.  H_2 has the unique first-side portal v11.
        for vertex in C:
            index = self.index[vertex]
            if vertex not in CONTACTS["a1"]:
                self.solver.add(z3.Not(self.root[index][1]))
            if vertex != "v11":
                self.solver.add(z3.Not(self.root[index][2]))
            if vertex not in CONTACTS["a3"]:
                self.solver.add(z3.Not(self.root[index][3]))


def main() -> None:
    require(set(COLOUR) == set((*S, *C)), "colouring domain is wrong")
    require(all(COLOUR[u] != COLOUR[v] for u, v in E_ALL), "improper colouring")
    boundary_classes: dict[int, set[Vertex]] = defaultdict(set)
    for literal in S:
        boundary_classes[COLOUR[literal]].add(literal)
    require(
        {frozenset(value) for value in boundary_classes.values()}
        == {
            frozenset(("a1", "t1")),
            frozenset(("a2", "t2")),
            frozenset(("a3", "t3")),
            frozenset(("c",)),
        },
        "wrong boundary equality partition",
    )
    require(all(edge(f"a{i}", f"t{i}") not in E_S for i in range(1, 4)), "a block is not independent")
    require(
        all(edge("c", f"a{i}") in E_S for i in range(1, 4))
        and all(
            edge(f"a{i}", f"a{j}") in E_S
            for i, j in combinations(range(1, 4), 2)
        ),
        "boundary block-adjacency witnesses are missing",
    )

    page = graph(C, E_C)
    planar, embedding = nx.check_planarity(page)
    require(planar, "the page is not planar")
    require(nx.node_connectivity(page) == 3, "the page is not exactly three-connected")
    require(all(CONTACTS[literal] for literal in S), "the page is not S-full")

    selected = ("v21", "v11", "v12", "v23", "v33", "v32")
    all_duty_portals = set().union(
        *(CONTACTS[literal] for literal in S if literal != "c")
    )
    common_faces = [
        face for face in faces(embedding) if all_duty_portals <= set(face)
    ]
    require(len(common_faces) == 1, "selected portals do not have one common face")
    filtered = tuple(v for v in common_faces[0] if v in set(selected))
    allowed_orders = rotations(selected) | rotations(tuple(reversed(selected)))
    require(filtered in allowed_orders, "selected portal order is wrong")

    reversal = (
        ("v21", "f21", "v32"),
        ("v11", "f11", "v22", "f22", "v33"),
        ("v12", "f12", "v23"),
    )
    require(all(path_is_valid(path, E_C) for path in reversal), "bad reversal path")
    require(
        all(set(first).isdisjoint(second) for first, second in combinations(reversal, 2)),
        "reversal paths are not disjoint",
    )

    expected_success = {
        (1, 5): True,
        (1, 6): False,
        (3, 5): True,
        (3, 6): False,
    }
    observed_success = {
        test: kempe_success(*test) for test in expected_success
    }
    require(observed_success == expected_success, "wrong two-spare success matrix")

    rows = tuple(
        ("a1", f"v{i}1", f"h{i}1", f"v{i}2", f"h{i}2", f"v{i}3", "t1")
        for i in range(1, 4)
    )
    columns = tuple(
        ("a3", f"v1{j}", f"g1{j}", f"v2{j}", f"g2{j}", f"v3{j}", "t3")
        for j in range(1, 4)
    )
    require(all(path_is_valid(path, E_ALL) for path in (*rows, *columns)), "bad lock path")
    require(
        all({COLOUR[v] for v in path} == {1, 6} for path in rows),
        "a row is not a 1/6 lock",
    )
    require(
        all({COLOUR[v] for v in path} == {3, 6} for path in columns),
        "a column is not a 3/6 lock",
    )
    row_interiors = tuple(set(path[1:-1]) for path in rows)
    require(
        all(first.isdisjoint(second) for first, second in combinations(row_interiors, 2)),
        "row locks are not internally disjoint",
    )
    require(
        not any(
            all(set(pair) & interior for interior in row_interiors)
            for pair in combinations(C, 2)
        ),
        "two interior vertices hit all row locks",
    )

    # The four artificial stars certify the alternating disk obstruction to
    # two disjoint original-duty carriers.
    augmented = page.copy()
    terminal_order = ("A1", "A3", "T1", "T3")
    terminal_contacts = {
        "A1": CONTACTS["a1"],
        "A3": CONTACTS["a3"],
        "T1": CONTACTS["t1"],
        "T3": CONTACTS["t3"],
    }
    for terminal, portals in terminal_contacts.items():
        augmented.add_node(terminal)
        augmented.add_edges_from((terminal, portal) for portal in portals)
    augmented_planar, augmented_embedding = nx.check_planarity(augmented)
    require(augmented_planar, "the artificial-terminal society is not planar")
    terminal_faces = [
        face
        for face in faces(augmented_embedding)
        if set(terminal_order) <= set(face)
    ]
    require(len(terminal_faces) == 1, "artificial terminals are not cofacial")
    terminal_face_order = tuple(
        vertex for vertex in terminal_faces[0] if vertex in set(terminal_order)
    )
    require(
        terminal_face_order
        in rotations(terminal_order) | rotations(tuple(reversed(terminal_order))),
        "artificial terminals do not alternate",
    )

    rooted = RootedK4Solver()
    rooted.contact(1, "a1")
    rooted.contact(1, "t3")
    rooted.contact(2, "a2")
    rooted.contact(2, "t2")
    rooted.contact(3, "a3")
    rooted.contact(3, "t1")
    rooted.solver.add(
        z3.Or(
            *[
                rooted.member[rooted.index[portal]][bag]
                for portal in CONTACTS["c"]
                for bag in range(4)
            ]
        )
    )
    rooted.pairwise_adjacent()
    rooted.exclude_impossible_roots()
    rooted.solver.set(timeout=60_000)
    require(rooted.solver.check() == z3.unsat, "a rooted-K4 expansion exists or solve timed out")

    print("GREEN: exact paired state and proper six-colouring")
    print("GREEN: planar three-connected common-face page and literal reversal")
    print("GREEN: success graph has the zero spare-column {6}")
    print("GREEN: no two-vertex row-lock transversal")
    print("GREEN: alternating society forbids two disjoint original-duty carriers")
    print("GREEN: no reversed rooted-K4 expansion")


if __name__ == "__main__":
    main()
