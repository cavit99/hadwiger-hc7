#!/usr/bin/env python3
"""Falsify the singleton q2--q2 robust-carrier candidate.

Input is a graph6 stream (normally ``geng -q -d4 n``).  For every
4-connected graph and every ordered choice

    alpha,beta,a1,a2,b1,b2

of six distinct terminals, test the four disjoint connected-carrier
patterns in Theorem 5 of ``results/hc7_near_k7_rotation_edge.md``.

The implementation uses the equivalent unordered formulation.  For two
disjoint terminal triples A and B, let a pair p in B be *bad from A* when
there are no disjoint connected vertex sets containing A and p.  The four
patterns all fail for some labelling precisely when the bad-pair graph on
B has a vertex of degree two and, symmetrically, the bad-pair graph on A
has a vertex of degree two.
"""

from __future__ import annotations

import argparse
import itertools
import sys
from collections.abc import Iterable

import networkx as nx


def components(graph: nx.Graph, mask: int) -> tuple[int, ...]:
    """Return component masks in the subgraph induced by ``mask``."""
    answer: list[int] = []
    unseen = mask
    while unseen:
        seed = unseen & -unseen
        reached = seed
        frontier = seed
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            neighbours = 0
            for neighbour in graph[vertex]:
                neighbours |= 1 << neighbour
            new = neighbours & mask & ~reached
            reached |= new
            frontier |= new
        answer.append(reached)
        unseen &= ~reached
    return tuple(answer)


def is_four_connected(graph: nx.Graph) -> bool:
    """Exact 4-connectivity test by deleting at most three vertices."""
    n = len(graph)
    if n < 5 or min(dict(graph.degree()).values(), default=0) < 4:
        return False
    full = (1 << n) - 1
    vertices = range(n)
    for order in range(4):
        for deleted in itertools.combinations(vertices, order):
            mask = full
            for vertex in deleted:
                mask ^= 1 << vertex
            if len(components(graph, mask)) != 1:
                return False
    return True


class CarrierOracle:
    """Cache exact disjoint connected-carrier queries for one graph."""

    def __init__(self, graph: nx.Graph) -> None:
        self.graph = graph
        self.n = len(graph)
        self.full = (1 << self.n) - 1
        self._component_cache: dict[int, tuple[int, ...]] = {}
        self._connected_cache: dict[int, bool] = {}
        self._carrier_cache: dict[tuple[int, int], bool] = {}

    def component_masks(self, mask: int) -> tuple[int, ...]:
        if mask not in self._component_cache:
            self._component_cache[mask] = components(self.graph, mask)
        return self._component_cache[mask]

    def connected(self, mask: int) -> bool:
        if mask not in self._connected_cache:
            self._connected_cache[mask] = (
                mask != 0 and len(self.component_masks(mask)) == 1
            )
        return self._connected_cache[mask]

    def has_disjoint_carriers(self, first: int, second: int) -> bool:
        """Whether disjoint connected sets can contain the two masks."""
        if first & second:
            return False
        # The relation is symmetric; canonicalization halves the cache.
        key = tuple(sorted((first, second)))
        if key in self._carrier_cache:
            return self._carrier_cache[key]

        optional = self.full & ~(first | second)
        chosen = optional
        while True:
            left = first | chosen
            if self.connected(left):
                remainder = self.full & ~left
                if any(
                    component & second == second
                    for component in self.component_masks(remainder)
                ):
                    self._carrier_cache[key] = True
                    return True
            if chosen == 0:
                break
            chosen = (chosen - 1) & optional

        self._carrier_cache[key] = False
        return False


def mask_of(vertices: Iterable[int]) -> int:
    mask = 0
    for vertex in vertices:
        mask |= 1 << vertex
    return mask


def common_bad_pair_vertex(
    oracle: CarrierOracle, triple: tuple[int, int, int], other: tuple[int, int, int]
) -> int | None:
    """Return a vertex incident with two carrier-failing pairs, if any."""
    triple_mask = mask_of(triple)
    bad_pairs = {
        frozenset(pair)
        for pair in itertools.combinations(other, 2)
        if not oracle.has_disjoint_carriers(triple_mask, mask_of(pair))
    }
    for vertex in other:
        incident = sum(vertex in pair for pair in bad_pairs)
        if incident == 2:
            return vertex
    return None


def common_bad_pair_vertices(
    oracle: CarrierOracle, triple: tuple[int, int, int], other: tuple[int, int, int]
) -> tuple[int, ...]:
    """All vertices incident with both failing pairs in the other triple."""
    triple_mask = mask_of(triple)
    bad_pairs = {
        frozenset(pair)
        for pair in itertools.combinations(other, 2)
        if not oracle.has_disjoint_carriers(triple_mask, mask_of(pair))
    }
    return tuple(
        vertex
        for vertex in other
        if sum(vertex in pair for pair in bad_pairs) == 2
    )


def counterexample_terminal_tuples(graph: nx.Graph) -> Iterable[tuple[int, ...]]:
    """Yield every robust tuple, modulo swaps inside the two demand pairs."""
    oracle = CarrierOracle(graph)
    vertices = tuple(graph)
    for first in itertools.combinations(vertices, 3):
        outside = tuple(vertex for vertex in vertices if vertex not in first)
        for second in itertools.combinations(outside, 3):
            alphas = common_bad_pair_vertices(oracle, second, first)
            if not alphas:
                continue
            betas = common_bad_pair_vertices(oracle, first, second)
            for alpha in alphas:
                a1, a2 = (vertex for vertex in first if vertex != alpha)
                for beta in betas:
                    b1, b2 = (vertex for vertex in second if vertex != beta)
                    yield alpha, beta, a1, a2, b1, b2


def counterexample_terminals(graph: nx.Graph) -> tuple[int, ...] | None:
    """Return alpha,beta,a1,a2,b1,b2 if all four patterns fail."""
    return next(iter(counterexample_terminal_tuples(graph)), None)


def canonical_cycle(cycle: Iterable[int]) -> tuple[int, ...]:
    sequence = tuple(cycle)
    candidates = []
    for oriented in (sequence, tuple(reversed(sequence))):
        for offset in range(len(sequence)):
            candidates.append(oriented[offset:] + oriented[:offset])
    return min(candidates)


def facial_cycles(graph: nx.Graph) -> set[tuple[int, ...]] | None:
    planar, embedding = nx.check_planarity(graph)
    if not planar:
        return None
    marked: set[tuple[int, int]] = set()
    faces: set[tuple[int, ...]] = set()
    for u, v in embedding.edges:
        for start in ((u, v), (v, u)):
            if start not in marked:
                faces.add(canonical_cycle(embedding.traverse_face(*start, marked)))
    return faces


def is_crossed_double_face_book(
    faces: set[tuple[int, ...]] | None, terminals: tuple[int, ...]
) -> bool:
    """Whether two alternating quadrilateral faces share alpha--beta."""
    if faces is None:
        return False
    alpha, beta, a1, a2, b1, b2 = terminals
    a_vertices = (a1, a2)
    b_vertices = (b1, b2)
    for b_order in (b_vertices, tuple(reversed(b_vertices))):
        expected = {
            canonical_cycle((b_order[0], alpha, beta, a_vertices[0])),
            canonical_cycle((b_order[1], alpha, beta, a_vertices[1])),
        }
        if expected <= faces:
            return True
    return False


def shared_one_counterexample_terminals(graph: nx.Graph) -> tuple[int, ...] | None:
    """Return alpha,beta,c,a,b for the |D cap E|=1 singleton variant.

    Here D={c,a}, E={c,b}.  Two of the four robust patterns are impossible
    for the trivial reason that both disjoint carriers would have to contain
    the same singleton c.  The two genuinely testable patterns are

        {alpha,c,a} versus {beta,b}, and
        {alpha,a} versus {beta,c,b}.
    """
    oracle = CarrierOracle(graph)
    for alpha, beta, common, old_only, new_only in itertools.permutations(
        graph, 5
    ):
        first = oracle.has_disjoint_carriers(
            mask_of((alpha, common, old_only)), mask_of((beta, new_only))
        )
        second = oracle.has_disjoint_carriers(
            mask_of((alpha, old_only)), mask_of((beta, common, new_only))
        )
        if not first and not second:
            return alpha, beta, common, old_only, new_only
    return None


def shared_two_counterexample_terminals(graph: nx.Graph) -> tuple[int, ...] | None:
    """Return any alpha,beta,c1,c2 for the D=E singleton variant.

    Every one of the four patterns is then impossible: each asks two
    vertex-disjoint carriers to contain the same singleton portal c1 or c2.
    This mode records that connectivity alone has no content in this cell.
    """
    if len(graph) < 4:
        return None
    return tuple(itertools.islice(graph, 4))


def read_graphs(stream: Iterable[bytes]) -> Iterable[nx.Graph]:
    for line in stream:
        line = line.strip()
        if not line or line.startswith(b">"):
            continue
        graph = nx.from_graph6_bytes(line)
        # graph6 labels are already 0,...,n-1, but make this invariant explicit.
        yield nx.convert_node_labels_to_integers(graph, ordering="sorted")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int)
    parser.add_argument("--progress", type=int, default=10000)
    parser.add_argument(
        "--variant",
        choices=("distinct4", "shared1", "shared2"),
        default="distinct4",
    )
    parser.add_argument(
        "--classify-all",
        action="store_true",
        help="scan the full stream and classify every counterexample graph",
    )
    parser.add_argument(
        "--seek-rural-exception",
        action="store_true",
        help="stop only at a nonplanar or non-double-book robust tuple",
    )
    args = parser.parse_args()

    examined = 0
    four_connected = 0
    counterexample_graphs = 0
    planar_counterexample_graphs = 0
    nonplanar_counterexample_graphs = 0
    robust_terminal_tuples = 0
    nonbook_terminal_tuples = 0
    first_nonplanar: dict | None = None
    first_nonbook: dict | None = None
    for graph in read_graphs(sys.stdin.buffer):
        examined += 1
        if args.limit is not None and examined > args.limit:
            break
        if not is_four_connected(graph):
            continue
        four_connected += 1
        if args.variant == "distinct4":
            terminals = counterexample_terminals(graph)
        elif args.variant == "shared1":
            terminals = shared_one_counterexample_terminals(graph)
        else:
            terminals = shared_two_counterexample_terminals(graph)
        if terminals is not None:
            record = {
                    "result": "COUNTEREXAMPLE",
                    "graph6": nx.to_graph6_bytes(graph, header=False).decode().strip(),
                    "order": len(graph),
                    "size": graph.number_of_edges(),
                    "connectivity": nx.node_connectivity(graph),
                    "planar": nx.check_planarity(graph)[0],
                    "edges": sorted(tuple(sorted(edge)) for edge in graph.edges),
                    "terminals": terminals,
                    "variant": args.variant,
                    "examined": examined,
                    "four_connected_examined": four_connected,
                }
            if args.seek_rural_exception:
                if args.variant != "distinct4":
                    raise SystemExit("--seek-rural-exception requires --variant distinct4")
                faces = facial_cycles(graph)
                planar = faces is not None
                exception = next(
                    (
                        robust_tuple
                        for robust_tuple in counterexample_terminal_tuples(graph)
                        if not planar
                        or not is_crossed_double_face_book(faces, robust_tuple)
                    ),
                    None,
                )
                if exception is not None:
                    print(
                        record
                        | {
                            "result": "RURAL_EXCEPTION",
                            "terminals": exception,
                            "planar": planar,
                        }
                    )
                    return
                continue
            if not args.classify_all:
                print(record)
                return
            counterexample_graphs += 1
            planar, _ = nx.check_planarity(graph)
            if planar:
                planar_counterexample_graphs += 1
            else:
                nonplanar_counterexample_graphs += 1
                if first_nonplanar is None:
                    first_nonplanar = record
            if args.variant == "distinct4":
                faces = facial_cycles(graph)
                for robust_tuple in counterexample_terminal_tuples(graph):
                    robust_terminal_tuples += 1
                    if not is_crossed_double_face_book(faces, robust_tuple):
                        nonbook_terminal_tuples += 1
                        if first_nonbook is None:
                            first_nonbook = record | {"terminals": robust_tuple}
        if args.progress and examined % args.progress == 0:
            print(
                {"progress": examined, "four_connected": four_connected},
                file=sys.stderr,
            )

    summary = {
            "result": "NONE",
            "examined": examined,
            "four_connected_examined": four_connected,
        }
    if args.classify_all:
        summary |= {
            "result": "CLASSIFICATION",
            "counterexample_graphs": counterexample_graphs,
            "planar_counterexample_graphs": planar_counterexample_graphs,
            "nonplanar_counterexample_graphs": nonplanar_counterexample_graphs,
            "robust_terminal_tuples_mod_pair_swaps": robust_terminal_tuples,
            "nonbook_terminal_tuples": nonbook_terminal_tuples,
            "first_nonplanar": first_nonplanar,
            "first_nonbook": first_nonbook,
        }
    if args.seek_rural_exception:
        summary["result"] = "NO_RURAL_EXCEPTION"
    print(summary)


if __name__ == "__main__":
    main()
