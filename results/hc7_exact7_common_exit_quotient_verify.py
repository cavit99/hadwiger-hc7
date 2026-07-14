#!/usr/bin/env python3
"""Proof-producing finite audit of the common-exit gate quotient.

The quotient retains seven literal boundary vertices, the three literal gate
vertices, the descended lobe, selected sibling lobes, and the two old full
packets.  A quotient model lifts literally by expanding a lobe or packet
vertex to the connected set that it represents.

The script performs three exhaustive checks.

1. Three siblings: all 20 multisets of missing A-labels and all 512 minimal
   paired-triangle boundary witnesses.  No gate-to-boundary edge is used.
2. Two distinct missing labels with nonadjacent common A-labels: all four
   symmetry types, all compatible minimal boundary witnesses, and all nine
   placements of the two gate contacts forced by old-component fullness.
3. Two equal missing labels: all three symmetry types, all 512 minimal
   boundaries, and all nine forced-contact placements.

The default audit is solver-free.  It checks a frozen catalogue of literal
branch-set templates, each consisting of seven branch sets of order at most
three plus a conjunction of required optional boundary/gate edges.  Every
template is checked by ordinary graph routines against only its advertised
edges.  Use --show-templates to print the catalogue.

The optional --regenerate mode invokes Z3 to rediscover and compress a
catalogue.  Regeneration is a discovery audit; the frozen catalogue and the
solver-free checker are the proof-producing certificate.

This is a finite quotient certificate, not a proof of state preservation or
of a global descent measure.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement, permutations, product
from typing import Iterable

try:
    from .hc7_exact7_common_exit_quotient_templates import FROZEN_TEMPLATES
except ImportError:
    from hc7_exact7_common_exit_quotient_templates import FROZEN_TEMPLATES


z3 = None


def require_z3() -> None:
    """Load the optional discovery dependency only in regeneration mode."""

    global z3
    if z3 is not None:
        return
    try:
        import z3 as z3_module
    except ImportError as error:
        raise SystemExit(
            "--regenerate requires the optional z3-solver package"
        ) from error
    z3 = z3_module


Vertex = str
Edge = tuple[Vertex, Vertex]
Bag = frozenset[Vertex]


S = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
A = frozenset({"c", "a1", "a2", "a3"})
T = frozenset({"t1", "t2", "t3"})
X = ("x1", "x2", "x3")
PAIRS = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))
P, Q, K = "p", "q", "k"
TARGET = 7
MAX_BAG_ORDER = 3
GATE_RENAMINGS = tuple(dict(zip(X, image)) for image in permutations(X))
EXPECTED_TEMPLATE_COUNTS = {
    "three-sibling": 21,
    "hard-two-sibling": 20,
    "equal-two-sibling": 17,
}


def edge(left: Vertex, right: Vertex) -> Edge:
    assert left != right
    return tuple(sorted((left, right)))


PAIR_NONEDGES = frozenset(edge(*pair) for pair in PAIRS)
BOUNDARY_UNIVERSE = tuple(
    edge(left, right)
    for left, right in combinations(S, 2)
    if edge(left, right) not in PAIR_NONEDGES
)


def minimal_boundaries() -> tuple[frozenset[Edge], ...]:
    """Choose one literal witness for each paired-triangle requirement."""

    groups: list[tuple[Edge, ...]] = []
    for pair in PAIRS:
        groups.append(tuple(edge("c", endpoint) for endpoint in pair))
    for first, second in combinations(PAIRS, 2):
        groups.append(tuple(edge(left, right) for left in first for right in second))
    answer = tuple(frozenset(choice) for choice in product(*groups))
    assert len(answer) == 2**3 * 4**3 == 512
    assert len(set(answer)) == len(answer)
    return answer


MINIMAL_BOUNDARIES = minimal_boundaries()


@dataclass(frozen=True)
class Case:
    family: str
    missing: tuple[Vertex, ...]
    boundary: frozenset[Edge]
    gate_contacts: frozenset[Edge] = frozenset()

    @property
    def siblings(self) -> tuple[Vertex, ...]:
        return tuple(f"j{index + 1}" for index in range(len(self.missing)))

    @property
    def lobes(self) -> tuple[Vertex, ...]:
        return (K, *self.siblings)

    @property
    def vertices(self) -> tuple[Vertex, ...]:
        return (*S, *X, *self.lobes, P, Q)

    @property
    def structural_edges(self) -> frozenset[Edge]:
        answer: set[Edge] = set()
        for gate in X:
            for lobe in self.lobes:
                answer.add(edge(gate, lobe))
        for label in A:
            answer.add(edge(K, label))
        for sibling, missing_label in zip(self.siblings, self.missing):
            answer.add(edge(sibling, "t1"))
            for label in A - {missing_label}:
                answer.add(edge(sibling, label))
        for packet in (P, Q):
            for label in S:
                answer.add(edge(packet, label))
        return frozenset(answer)

    @property
    def optional_edges(self) -> frozenset[Edge]:
        return self.boundary | self.gate_contacts

    @property
    def edges(self) -> frozenset[Edge]:
        return self.structural_edges | self.optional_edges


def three_sibling_cases() -> tuple[Case, ...]:
    """Three siblings suffice for every case with at least three siblings."""

    answer = []
    for missing in combinations_with_replacement(sorted(A), 3):
        for boundary in MINIMAL_BOUNDARIES:
            answer.append(Case("three-sibling", missing, boundary))
    assert len(answer) == 20 * 512 == 10_240
    return tuple(answer)


# With common exit t1, swapping the second and third paired duties leaves
# four orbits of unordered distinct missing-label pairs.
HARD_MISSING_TYPES = (
    ("c", "a1"),
    ("c", "a2"),
    ("a1", "a2"),
    ("a2", "a3"),
)
EQUAL_MISSING_TYPES = ("c", "a1", "a2")


def hard_two_sibling_cases() -> tuple[Case, ...]:
    """Enumerate the distinct-missing/nonadjacent-common-label residue."""

    answer = []
    for missing in HARD_MISSING_TYPES:
        common = tuple(sorted(A - set(missing)))
        common_edge = edge(*common)
        for boundary in MINIMAL_BOUNDARIES:
            if common_edge in boundary:
                continue
            # The three lobes see only A union {t1}.  In the old paired
            # application C is S-full, so t2 and t3 have literal neighbours
            # in X.  It is enough to retain one such edge for each label.
            for gate_for_t2, gate_for_t3 in product(X, repeat=2):
                contacts = frozenset(
                    {
                        edge(gate_for_t2, "t2"),
                        edge(gate_for_t3, "t3"),
                    }
                )
                answer.append(Case("hard-two-sibling", missing, boundary, contacts))
    assert len(answer) == 11_520
    return tuple(answer)


def equal_two_sibling_cases() -> tuple[Case, ...]:
    """Enumerate the three symmetry types with one repeated missing label."""

    answer = []
    for missing_label in EQUAL_MISSING_TYPES:
        missing = (missing_label, missing_label)
        for boundary in MINIMAL_BOUNDARIES:
            for gate_for_t2, gate_for_t3 in product(X, repeat=2):
                contacts = frozenset(
                    {
                        edge(gate_for_t2, "t2"),
                        edge(gate_for_t3, "t3"),
                    }
                )
                answer.append(Case("equal-two-sibling", missing, boundary, contacts))
    assert len(answer) == 3 * 512 * 9 == 13_824
    return tuple(answer)


def neighbours(vertices: Iterable[Vertex], edges: frozenset[Edge]) -> dict[Vertex, set[Vertex]]:
    answer = {vertex: set() for vertex in vertices}
    for left, right in edges:
        answer[left].add(right)
        answer[right].add(left)
    return answer


def connected(bag: Bag, edges: frozenset[Edge]) -> bool:
    if not bag:
        return False
    adjacency = neighbours(bag, frozenset(e for e in edges if set(e) <= set(bag)))
    reached: set[Vertex] = set()
    stack = [next(iter(bag))]
    while stack:
        vertex = stack.pop()
        if vertex in reached:
            continue
        reached.add(vertex)
        stack.extend(adjacency[vertex] - reached)
    return reached == set(bag)


def bags_adjacent(left: Bag, right: Bag, edges: frozenset[Edge]) -> bool:
    return any(edge(u, v) in edges for u in left for v in right)


def verify_literal_model(
    vertices: tuple[Vertex, ...],
    edges: frozenset[Edge],
    bags: tuple[Bag, ...],
) -> None:
    """Check a literal K7 branch-set model against the supplied edges."""

    assert len(bags) == TARGET
    assert all(1 <= len(bag) <= MAX_BAG_ORDER for bag in bags)
    assert all(bag <= set(vertices) for bag in bags)
    assert all(left.isdisjoint(right) for left, right in combinations(bags, 2))
    assert all(connected(bag, edges) for bag in bags)
    assert all(
        bags_adjacent(left, right, edges)
        for left, right in combinations(bags, 2)
    )


def verify_model(case: Case, bags: tuple[Bag, ...]) -> None:
    """Independently check a literal K7 branch-set model in one case."""

    verify_literal_model(case.vertices, case.edges, bags)


def verify_case_hypotheses(case: Case) -> None:
    """Check the exact quotient hypotheses, independently of Z3."""

    # Proper paired-triangle state and its six required adjacencies.
    assert case.boundary.isdisjoint(PAIR_NONEDGES)
    assert all(any(edge("c", endpoint) in case.boundary for endpoint in pair) for pair in PAIRS)
    assert all(
        any(edge(u, v) in case.boundary for u in first for v in second)
        for first, second in combinations(PAIRS, 2)
    )

    # Exact lobe supports and literal gate incidence.
    adjacency = neighbours(case.vertices, case.edges)
    assert adjacency[K] & set(S) == set(A)
    assert adjacency[K] & set(X) == set(X)
    for sibling, missing_label in zip(case.siblings, case.missing):
        expected = {"t1"} | (set(A) - {missing_label})
        assert adjacency[sibling] & set(S) == expected
        assert adjacency[sibling] & set(X) == set(X)
    assert all(
        not adjacency[left] & set(case.lobes)
        for left in case.lobes
    )

    # The two old packet vertices are disjoint, mutually nonadjacent, and
    # complete to the old literal boundary.
    assert edge(P, Q) not in case.edges
    assert adjacency[P] & set(S) == set(S)
    assert adjacency[Q] & set(S) == set(S)

    if case.family in {"hard-two-sibling", "equal-two-sibling"}:
        assert len(case.missing) == 2
        assert any(edge(gate, "t2") in case.gate_contacts for gate in X)
        assert any(edge(gate, "t3") in case.gate_contacts for gate in X)
        component = set(X) | set(case.lobes)
        assert set().union(*(adjacency[v] & set(S) for v in component)) == set(S)

    if case.family == "hard-two-sibling":
        assert len(set(case.missing)) == 2
        common = tuple(sorted(A - set(case.missing)))
        assert edge(*common) not in case.boundary
    if case.family == "equal-two-sibling":
        assert len(set(case.missing)) == 1


def canonical_bags(bags: Iterable[Bag]) -> tuple[Bag, ...]:
    """Sort branch sets by their resource content and then boundary content."""

    resource_order = {name: index for index, name in enumerate((*X, K, "j1", "j2", "j3", P, Q))}
    boundary_order = {name: index for index, name in enumerate(S)}

    def key(bag: Bag) -> tuple[tuple[int, ...], tuple[int, ...], tuple[str, ...]]:
        resources = tuple(sorted(resource_order[v] for v in bag if v in resource_order))
        boundary = tuple(sorted(boundary_order[v] for v in bag if v in boundary_order))
        return resources, boundary, tuple(sorted(bag))

    return tuple(sorted((frozenset(bag) for bag in bags), key=key))


class MinorSolver:
    """Incremental exact K7-minor solver for one missing-label pattern."""

    def __init__(self, exemplar: Case):
        require_z3()
        self.vertices = exemplar.vertices
        self.index = {vertex: index for index, vertex in enumerate(self.vertices)}
        self.structural = exemplar.structural_edges
        optional = set(BOUNDARY_UNIVERSE)
        if exemplar.family in {"hard-two-sibling", "equal-two-sibling"}:
            optional.update(edge(gate, label) for gate in X for label in ("t2", "t3"))
        self.optional = tuple(sorted(optional))
        self.edge_variables = {
            candidate: z3.Bool("edge_" + "_".join(candidate))
            for candidate in self.optional
        }
        self.edge_universe = tuple(sorted(set(self.structural) | set(self.optional)))
        self.solver = z3.Solver()
        self.assigned = [
            [z3.Bool(f"assigned_{vertex}_{branch}") for branch in range(TARGET)]
            for vertex in self.vertices
        ]
        self.root = [
            [z3.Bool(f"root_{vertex}_{branch}") for branch in range(TARGET)]
            for vertex in self.vertices
        ]
        self.depth = [
            [z3.Int(f"depth_{vertex}_{branch}") for branch in range(TARGET)]
            for vertex in self.vertices
        ]
        self.root_index = [z3.Int(f"root_index_{branch}") for branch in range(TARGET)]
        self._build()

    def active(self, candidate: Edge) -> z3.BoolRef:
        if candidate in self.structural:
            return z3.BoolVal(True)
        return self.edge_variables[candidate]

    def _build(self) -> None:
        order = len(self.vertices)
        incident: dict[Vertex, list[tuple[Vertex, Edge]]] = defaultdict(list)
        for candidate in self.edge_universe:
            left, right = candidate
            incident[left].append((right, candidate))
            incident[right].append((left, candidate))

        for vertex_index in range(order):
            self.solver.add(
                z3.PbLe(
                    [(self.assigned[vertex_index][branch], 1) for branch in range(TARGET)],
                    1,
                )
            )

        for branch in range(TARGET):
            self.solver.add(
                z3.PbEq([(self.root[v][branch], 1) for v in range(order)], 1)
            )
            self.solver.add(
                z3.PbLe([(self.assigned[v][branch], 1) for v in range(order)], MAX_BAG_ORDER)
            )
            self.solver.add(0 <= self.root_index[branch], self.root_index[branch] < order)
            for vertex_index, vertex in enumerate(self.vertices):
                self.solver.add(0 <= self.depth[vertex_index][branch])
                self.solver.add(self.depth[vertex_index][branch] < order)
                self.solver.add(
                    z3.Implies(
                        self.root[vertex_index][branch],
                        z3.And(
                            self.assigned[vertex_index][branch],
                            self.root_index[branch] == vertex_index,
                            self.depth[vertex_index][branch] == 0,
                        ),
                    )
                )
                parents = [
                    z3.And(
                        self.active(candidate),
                        self.assigned[self.index[neighbour]][branch],
                        self.depth[self.index[neighbour]][branch]
                        < self.depth[vertex_index][branch],
                    )
                    for neighbour, candidate in incident[vertex]
                ]
                self.solver.add(
                    z3.Implies(
                        z3.And(
                            self.assigned[vertex_index][branch],
                            z3.Not(self.root[vertex_index][branch]),
                        ),
                        z3.And(self.depth[vertex_index][branch] >= 1, z3.Or(parents)),
                    )
                )

        # Branch labels are immaterial.  Ordering their root indices removes
        # the full 7! symmetry without removing any model.
        for branch in range(TARGET - 1):
            self.solver.add(self.root_index[branch] < self.root_index[branch + 1])

        for first, second in combinations(range(TARGET), 2):
            crossings = []
            for candidate in self.edge_universe:
                left, right = candidate
                u, v = self.index[left], self.index[right]
                crossings.append(
                    z3.And(
                        self.active(candidate),
                        self.assigned[u][first],
                        self.assigned[v][second],
                    )
                )
                crossings.append(
                    z3.And(
                        self.active(candidate),
                        self.assigned[v][first],
                        self.assigned[u][second],
                    )
                )
            self.solver.add(z3.Or(crossings))

    def solve(self, case: Case) -> tuple[Bag, ...] | None:
        assumptions = [
            variable if candidate in case.optional_edges else z3.Not(variable)
            for candidate, variable in self.edge_variables.items()
        ]
        if self.solver.check(*assumptions) != z3.sat:
            return None
        model = self.solver.model()
        bags = []
        for branch in range(TARGET):
            bag = frozenset(
                vertex
                for vertex_index, vertex in enumerate(self.vertices)
                if z3.is_true(model.eval(self.assigned[vertex_index][branch]))
            )
            bags.append(bag)
        answer = canonical_bags(bags)
        verify_model(case, answer)
        return answer


@dataclass(frozen=True)
class Template:
    missing: tuple[Vertex, ...]
    bags: tuple[Bag, ...]
    required_optional_edges: frozenset[Edge]

    def covers(self, case: Case) -> bool:
        if self.missing != case.missing:
            return False
        for renaming in GATE_RENAMINGS:
            bags = rename_bags(self.bags, renaming)
            requirements = rename_edges(self.required_optional_edges, renaming)
            if not requirements <= case.optional_edges:
                continue
            try:
                # Check the advertised monotone certificate using only the
                # fixed structural edges and its listed optional predicate.
                # Surplus optional edges of this particular case play no role.
                verify_literal_model(
                    case.vertices,
                    case.structural_edges | requirements,
                    bags,
                )
            except AssertionError:
                continue
            return True
        return False


def rename_vertex(vertex: Vertex, renaming: dict[Vertex, Vertex]) -> Vertex:
    return renaming.get(vertex, vertex)


def rename_edges(edges: Iterable[Edge], renaming: dict[Vertex, Vertex]) -> frozenset[Edge]:
    return frozenset(
        edge(rename_vertex(left, renaming), rename_vertex(right, renaming))
        for left, right in edges
    )


def rename_bags(bags: Iterable[Bag], renaming: dict[Vertex, Vertex]) -> tuple[Bag, ...]:
    return canonical_bags(
        frozenset(rename_vertex(vertex, renaming) for vertex in bag)
        for bag in bags
    )


def template_key(template: Template) -> tuple[tuple[tuple[str, ...], ...], tuple[Edge, ...]]:
    return (
        tuple(tuple(sorted(bag)) for bag in template.bags),
        tuple(sorted(template.required_optional_edges)),
    )


def canonical_template(template: Template) -> Template:
    """Quotient a symbolic model by all six permutations of the gate."""

    orbit = [
        Template(
            template.missing,
            rename_bags(template.bags, renaming),
            rename_edges(template.required_optional_edges, renaming),
        )
        for renaming in GATE_RENAMINGS
    ]
    return min(orbit, key=template_key)


def cheapest_spanning_tree(bag: Bag, case: Case) -> tuple[Edge, ...]:
    """Choose a lexicographic tree using as few optional edges as possible."""

    if len(bag) == 1:
        return ()
    available = tuple(
        candidate
        for candidate in sorted(case.edges)
        if set(candidate) <= set(bag)
    )
    choices = []
    for tree in combinations(available, len(bag) - 1):
        if connected(bag, frozenset(tree)):
            optional_count = sum(candidate in case.optional_edges for candidate in tree)
            choices.append((optional_count, tree))
    assert choices
    return min(choices)[1]


def template_from_model(case: Case, bags: tuple[Bag, ...]) -> Template:
    """Extract a sufficient monotone edge predicate for one literal model."""

    used: set[Edge] = set()
    for bag in bags:
        used.update(cheapest_spanning_tree(bag, case))
    for left, right in combinations(bags, 2):
        choices = sorted(
            candidate
            for candidate in case.edges
            if (candidate[0] in left and candidate[1] in right)
            or (candidate[1] in left and candidate[0] in right)
        )
        assert choices
        choices.sort(key=lambda candidate: (candidate in case.optional_edges, candidate))
        used.add(choices[0])
    required = frozenset(candidate for candidate in used if candidate in case.optional_edges)
    template = canonical_template(Template(case.missing, canonical_bags(bags), required))
    assert template.covers(case)
    return template


def greedy_template_cover(cases: tuple[Case, ...]) -> tuple[Template, ...]:
    """Build and then greedily compress a proof-producing template catalogue."""

    require_z3()
    by_missing: dict[tuple[Vertex, ...], list[Case]] = defaultdict(list)
    for case in cases:
        by_missing[case.missing].append(case)

    selected: list[Template] = []
    for missing, group in sorted(by_missing.items()):
        solver = MinorSolver(group[0])
        raw: list[Template] = []
        for case in group:
            verify_case_hypotheses(case)
            if any(template.covers(case) for template in raw):
                continue
            model = solver.solve(case)
            assert model is not None
            candidate = template_from_model(case, model)
            if candidate not in raw:
                raw.append(candidate)

        coverage = [
            frozenset(index for index, case in enumerate(group) if template.covers(case))
            for template in raw
        ]

        # Remove duplicate and dominated columns before solving the exact set
        # cover over the generated symbolic-template pool.
        retained = []
        for index, covered in enumerate(coverage):
            if any(
                covered < other
                or (covered == other and template_key(raw[other_index]) < template_key(raw[index]))
                for other_index, other in enumerate(coverage)
                if other_index != index
            ):
                continue
            retained.append(index)
        assert retained

        choose = [z3.Bool(f"choose_{'_'.join(missing)}_{index}") for index in retained]
        optimizer = z3.Optimize()
        for case_index in range(len(group)):
            alternatives = [
                choose[position]
                for position, template_index in enumerate(retained)
                if case_index in coverage[template_index]
            ]
            assert alternatives
            optimizer.add(z3.Or(alternatives))
        optimizer.minimize(z3.Sum([z3.If(variable, 1, 0) for variable in choose]))
        assert optimizer.check() == z3.sat
        model = optimizer.model()
        selected.extend(
            raw[template_index]
            for position, template_index in enumerate(retained)
            if z3.is_true(model.eval(choose[position]))
        )

    # Final independent coverage check.
    assert all(any(template.covers(case) for template in selected) for case in cases)
    return tuple(selected)


def frozen_templates(family: str) -> tuple[Template, ...]:
    """Decode the literal, reviewable certificate data for one case family."""

    records = FROZEN_TEMPLATES[family]
    templates = tuple(
        Template(
            tuple(missing),
            tuple(frozenset(bag) for bag in bags),
            frozenset(edge(*candidate) for candidate in requirements),
        )
        for missing, bags, requirements in records
    )
    assert len(templates) == EXPECTED_TEMPLATE_COUNTS[family]
    return templates


def format_bag(bag: Bag) -> str:
    return "{" + ",".join(sorted(bag)) + "}"


def print_templates(family: str, templates: tuple[Template, ...]) -> None:
    print(f"{family}_templates:")
    for index, template in enumerate(templates, 1):
        bags = " ".join(format_bag(bag) for bag in template.bags)
        predicate = " & ".join("".join(candidate) for candidate in sorted(template.required_optional_edges))
        if not predicate:
            predicate = "true"
        print(
            f"  {index:03d} missing={template.missing} "
            f"requires={predicate} bags={bags}"
        )


def main() -> None:
    if not __debug__:
        raise SystemExit("certificate checks require normal Python mode (without -O)")

    parser = argparse.ArgumentParser()
    parser.add_argument("--show-templates", action="store_true")
    parser.add_argument(
        "--regenerate",
        action="store_true",
        help="use Z3 to rediscover templates instead of checking the frozen catalogue",
    )
    parser.add_argument(
        "--family",
        choices=("all", "three", "hard-two", "equal-two"),
        default="all",
    )
    arguments = parser.parse_args()

    jobs = []
    if arguments.family in {"all", "three"}:
        jobs.append(("three-sibling", "three_sibling", three_sibling_cases()))
    if arguments.family in {"all", "hard-two"}:
        jobs.append(("hard-two-sibling", "hard_two_sibling", hard_two_sibling_cases()))
    if arguments.family in {"all", "equal-two"}:
        jobs.append(("equal-two-sibling", "equal_two_sibling", equal_two_sibling_cases()))

    print("COMMON-EXIT FORCED-QUOTIENT CERTIFICATE")
    print(f"minimal_paired_boundaries={len(MINIMAL_BOUNDARIES)}")
    total_cases = 0
    total_templates = 0
    for family, name, cases in jobs:
        templates = (
            greedy_template_cover(cases)
            if arguments.regenerate
            else frozen_templates(family)
        )
        for case in cases:
            verify_case_hypotheses(case)
            assert any(template.covers(case) for template in templates)
        total_cases += len(cases)
        total_templates += len(templates)
        print(f"{name}_cases={len(cases)}")
        print(f"{name}_symbolic_templates={len(templates)}")
        print(f"{name}_all_literal_k7=True")
        if arguments.show_templates:
            print_templates(name, templates)
    print(f"total_cases={total_cases}")
    print(f"total_symbolic_templates={total_templates}")
    print(f"solver_free={not arguments.regenerate}")
    print("independent_branch_set_checks=True")


if __name__ == "__main__":
    main()
