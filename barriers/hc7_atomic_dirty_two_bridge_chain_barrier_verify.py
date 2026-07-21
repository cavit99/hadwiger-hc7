#!/usr/bin/env python3
"""Verify the canonical dirty two-bridge-chain barrier on the atomic frame."""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations
from typing import Hashable

import networkx as nx


Node = Hashable
CORE = tuple("abcdefg")
SPECIAL = ("h", "p", "q", "r", "s")
DEFECTS = {frozenset(("a", "b")), frozenset(("c", "d"))}


def edge(left: str, right: str) -> frozenset[str]:
    return frozenset((left, right))


def build_graph() -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(CORE + ("x",) + SPECIAL)
    graph.add_edges_from(
        (left, right)
        for left, right in combinations(CORE, 2)
        if edge(left, right) not in DEFECTS
    )
    graph.add_edges_from(("x", vertex) for vertex in "abcd")
    for route in (
        ("f", "h", "g"),
        ("f", "p", "a"),
        ("g", "q", "a"),
        ("a", "r", "s", "c"),
    ):
        graph.remove_edge(route[0], route[-1])
        graph.add_edges_from(zip(route, route[1:]))
    graph.add_edges_from((("e", "h"), ("h", "x"), ("p", "r"), ("s", "q")))
    assert (len(graph), graph.number_of_edges()) == (13, 32)
    assert {vertex: graph.degree(vertex) for vertex in SPECIAL} == {
        "h": 4,
        "p": 3,
        "q": 3,
        "r": 3,
        "s": 3,
    }
    return graph


def spanning_clique_model(
    graph: nx.Graph, order: int
) -> tuple[frozenset[Node], ...] | None:
    """Return an exact spanning clique-minor model, or certify none exists."""

    vertices = tuple(graph)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    rows = [0] * len(vertices)
    for left, right in graph.edges:
        i, j = index[left], index[right]
        rows[i] |= 1 << j
        rows[j] |= 1 << i

    @lru_cache(maxsize=None)
    def connected(mask: int) -> bool:
        reached = mask & -mask
        while True:
            previous = reached
            pending = reached
            while pending:
                bit = pending & -pending
                pending ^= bit
                reached |= rows[bit.bit_length() - 1] & mask
            if reached == previous:
                return reached == mask

    blocks: list[list[int]] = []

    def search(position: int) -> tuple[frozenset[Node], ...] | None:
        if position == len(vertices):
            if len(blocks) != order:
                return None
            masks = tuple(sum(1 << vertex for vertex in block) for block in blocks)
            if not all(connected(mask) for mask in masks):
                return None
            for left, right in combinations(range(order), 2):
                neighbourhood = 0
                pending = masks[left]
                while pending:
                    bit = pending & -pending
                    pending ^= bit
                    neighbourhood |= rows[bit.bit_length() - 1]
                if not neighbourhood & masks[right]:
                    return None
            return tuple(
                frozenset(vertices[position] for position in block)
                for block in blocks
            )

        if len(blocks) + len(vertices) - position < order:
            return None
        for block in blocks:
            block.append(position)
            answer = search(position + 1)
            block.pop()
            if answer is not None:
                return answer
        if len(blocks) < order:
            blocks.append([position])
            answer = search(position + 1)
            blocks.pop()
            if answer is not None:
                return answer
        return None

    return search(0)


def validate_model(
    graph: nx.Graph, model: tuple[tuple[str, ...], ...] | tuple[frozenset[Node], ...]
) -> None:
    branch_sets = tuple(frozenset(branch_set) for branch_set in model)
    assert len(branch_sets) == 7
    assert sum(map(len, branch_sets)) == len(graph)
    assert set().union(*map(set, branch_sets)) == set(graph)
    assert all(nx.is_connected(graph.subgraph(branch_set)) for branch_set in branch_sets)
    for left, right in combinations(branch_sets, 2):
        assert any(graph.has_edge(u, v) for u in left for v in right)


def validate_width_five_decomposition(graph: nx.Graph) -> None:
    """Check the seven displayed bags for ``G-e``."""

    bags = {
        "U": frozenset("bcdfgx"),
        "V": frozenset("acdfgx"),
        "H": frozenset("fghx"),
        "W": frozenset("acfgs"),
        "Q": frozenset("agqs"),
        "R": frozenset("afrs"),
        "P": frozenset("afpr"),
    }
    tree = nx.Graph((left, right) for left, right in ("UV", "UH", "VW", "WQ", "WR", "RP"))
    assert nx.is_tree(tree) and max(map(len, bags.values())) == 6
    assert set().union(*map(set, bags.values())) == set(graph)
    assert all(any({left, right} <= bag for bag in bags.values()) for left, right in graph.edges())
    for vertex in graph:
        containing = {name for name, bag in bags.items() if vertex in bag}
        assert containing and nx.is_connected(tree.subgraph(containing))


def certificate_type(remainder: nx.Graph, certificate: nx.Graph) -> str:
    """Validate a literal Kuratowski subdivision and return its core type."""

    assert set(certificate) <= set(remainder)
    assert all(remainder.has_edge(u, v) for u, v in certificate.edges())
    assert nx.is_connected(certificate)
    branch = {vertex for vertex in certificate if certificate.degree(vertex) != 2}
    assert branch
    unused = {edge(u, v) for u, v in certificate.edges()}
    pairs: list[frozenset[str]] = []
    for start in branch:
        for neighbour in certificate[start]:
            first = edge(start, neighbour)
            if first not in unused:
                continue
            unused.remove(first)
            previous, current = start, neighbour
            while current not in branch:
                assert certificate.degree(current) == 2
                following = next(vertex for vertex in certificate[current] if vertex != previous)
                step = edge(current, following)
                assert step in unused
                unused.remove(step)
                previous, current = current, following
            assert current != start
            pairs.append(edge(start, current))
    assert not unused and len(pairs) == len(set(pairs))
    core = nx.Graph()
    core.add_nodes_from(branch)
    core.add_edges_from(tuple(pair) for pair in pairs)
    if nx.is_isomorphic(core, nx.complete_graph(5)):
        return "TK5"
    assert nx.is_isomorphic(core, nx.complete_bipartite_graph(3, 3))
    return "TK3,3"


POSITIVE_MODELS: dict[frozenset[str], tuple[tuple[str, ...], ...]] = {
    edge("h", "p"): (("a", "q"), ("c", "r", "s"), ("d", "f"), ("e",), ("g",), ("b", "x"), ("h", "p")),
    edge("h", "q"): (("a", "p", "r"), ("c", "s"), ("d", "g"), ("e",), ("f",), ("b", "x"), ("h", "q")),
    edge("h", "r"): (("a", "p", "q"), ("c", "s"), ("d", "f"), ("e",), ("g",), ("b", "x"), ("h", "r")),
    edge("b", "p"): (("a", "p", "q", "r", "s"), ("c", "f"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
    edge("d", "p"): (("a", "q", "x"), ("c", "p", "r", "s"), ("d",), ("e",), ("f", "h"), ("g",), ("b",)),
    edge("g", "p"): (("a", "c", "q", "r", "s"), ("d",), ("e",), ("f", "p"), ("g",), ("b",), ("h", "x")),
    edge("p", "q"): (("a", "c", "r", "s"), ("d",), ("e",), ("f", "p", "q"), ("g",), ("b",), ("h", "x")),
    edge("b", "q"): (("a", "p", "q", "r", "s"), ("c", "f"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
    edge("d", "q"): (("a", "p", "r", "x"), ("c", "q", "s"), ("d",), ("e",), ("f",), ("g", "h"), ("b",)),
    edge("f", "q"): (("a", "c", "p", "r", "s"), ("d",), ("e",), ("f", "q"), ("g",), ("b",), ("h", "x")),
    edge("b", "r"): (("a", "p", "q", "r", "s"), ("c", "f"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
    edge("d", "r"): (("a", "f", "p", "q"), ("c", "r", "s"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
    edge("g", "r"): (("a", "c", "q", "s"), ("d",), ("e",), ("f", "p", "r"), ("g",), ("b",), ("h", "x")),
    edge("b", "s"): (("a", "p", "q", "r", "s"), ("c", "f"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
    edge("d", "s"): (("a", "f", "p", "q", "r"), ("c", "s"), ("d",), ("e",), ("g",), ("b",), ("h", "x")),
}


NEGATIVE_COVERS: dict[str, tuple[frozenset[str], ...]] = {
    "c-star": tuple(edge(vertex, "c") for vertex in "hpqr"),
    "x-star-plus-hb": tuple(edge(vertex, "x") for vertex in "pqr") + (edge("h", "b"),),
    "cross-plus-hd": (edge("q", "r"), edge("r", "f"), edge("h", "d")),
    "s-star": tuple(edge("s", vertex) for vertex in "aefghpx"),
    "e-star-plus-ha": tuple(edge("e", vertex) for vertex in "pqrs") + (edge("h", "a"),),
}


def verify_saturation(graph: nx.Graph) -> dict[str, tuple[list[str], list[str]]]:
    incident_nonedges = {
        edge(vertex, other)
        for vertex in SPECIAL
        for other in graph
        if vertex != other and not graph.has_edge(vertex, other)
    }
    assert set(POSITIVE_MODELS) <= incident_nonedges
    for added, model in POSITIVE_MODELS.items():
        augmented = graph.copy()
        augmented.add_edge(*tuple(added))
        validate_model(augmented, model)

    covered = set().union(*map(set, NEGATIVE_COVERS.values()))
    assert covered == incident_nonedges - set(POSITIVE_MODELS)
    for name, additions in NEGATIVE_COVERS.items():
        augmented = graph.copy()
        augmented.add_edges_from(tuple(added) for added in additions)
        if name == "x-star-plus-hb":
            assert spanning_clique_model(augmented, 7) is None
        else:
            augmented.remove_node("e")
            assert spanning_clique_model(augmented, 6) is None

    table: dict[str, tuple[list[str], list[str]]] = {}
    for vertex in SPECIAL:
        nonneighbours = sorted(set(graph) - {vertex} - set(graph[vertex]))
        terminal = [u for u in nonneighbours if edge(vertex, u) in POSITIVE_MODELS]
        surviving = [u for u in nonneighbours if edge(vertex, u) not in POSITIVE_MODELS]
        table[vertex] = terminal, surviving
    return table


def verify_object_deletion_nonplanarity(graph: nx.Graph) -> Counter[str]:
    """Check every deletion of at most two vertex-or-edge objects."""

    edge_objects = tuple(
        edge(left, right) for left, right in sorted(tuple(sorted(pair)) for pair in graph.edges())
    )
    objects: tuple[str | frozenset[str], ...] = tuple(graph) + edge_objects
    assert len(objects) == 45 and len(set(objects)) == 45

    certificates: Counter[str] = Counter()
    cases = 0
    for size in range(3):
        for deleted in combinations(objects, size):
            remainder = graph.copy()
            remainder.remove_nodes_from(obj for obj in deleted if isinstance(obj, str))
            remainder.remove_edges_from(
                tuple(obj) for obj in deleted if isinstance(obj, frozenset)
            )
            planar, certificate = nx.check_planarity(remainder, counterexample=True)
            assert not planar
            certificates[certificate_type(remainder, certificate)] += 1
            cases += 1
    assert cases == 1036
    assert certificates == Counter({"TK5": 449, "TK3,3": 587})
    return certificates


def main() -> None:
    graph = build_graph()

    connectivity_cases = 0
    for size in range(3):
        for deleted in combinations(tuple(graph), size):
            remainder = graph.copy()
            remainder.remove_nodes_from(deleted)
            assert nx.is_connected(remainder)
            connectivity_cases += 1
    cut = set(graph["p"])
    remainder = graph.copy()
    remainder.remove_nodes_from(cut)
    assert len(cut) == 3 and not nx.is_connected(remainder)

    clique = ("b", "d", "e", "f")
    assert all(graph.has_edge(left, right) for left, right in combinations(clique, 2))
    colouring = {
        "a": 1, "b": 3, "c": 2, "d": 2, "e": 0, "f": 1, "g": 1,
        "h": 2, "p": 0, "q": 2, "r": 2, "s": 0, "x": 0,
    }
    assert all(colouring[left] != colouring[right] for left, right in graph.edges())

    k6_remainder = graph.copy()
    k6_remainder.remove_node("e")
    validate_width_five_decomposition(k6_remainder)
    assert spanning_clique_model(k6_remainder, 6) is None

    certificates = verify_object_deletion_nonplanarity(graph)
    table = verify_saturation(graph)

    print("GREEN atomic dirty two-bridge-chain barrier")
    print("host: vertices=13 edges=32 connectivity=3 chromatic=4 K7_minor=no")
    print(f"connectivity_checks={connectivity_cases} cut=N(p)={sorted(cut)}")
    print("K7_exclusion=G-e width-5 decomposition and no spanning K6 model")
    print(
        "object_deletion_nonplanar=yes objects=45 cases=1036 "
        f"kuratowski={dict(sorted(certificates.items()))}"
    )
    for vertex in SPECIAL:
        terminal, surviving = table[vertex]
        print(f"saturation_{vertex}: K7={','.join(terminal)} survives={','.join(surviving)}")
    print("two_apex_subdivision_exclusion=yes")


if __name__ == "__main__":
    main()
