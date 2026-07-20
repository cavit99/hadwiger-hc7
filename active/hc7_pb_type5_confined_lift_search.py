#!/usr/bin/env python3
"""Deterministic adversarial search in doubly confined type-5 PB lifts.

This is a heuristic experiment over an unbounded family, not a finite
classification and not a proof of the paired-rooted target.  Its individual
checks are exact.  It starts from sampled exceptional labelled type-5
pentagonal-bipyramid enlargement, replaces its nine vertices by connected
pieces, and adds only edges allowed by that enlargement.  The two split
fibres are then merged back into the original seven connected columns.

Both nominated root sets meet every column and are confined to the retained
side (side zero) in the two split fibres.  A fixed-seed edge trajectory first
repairs an explicit vertex cut of order at most four; once five-connectivity
is reached, it adds an edge monochromatic in an exact four-colouring.  Thus a
trajectory stops with one of three exact outcomes:

* a five-connected, non-four-colourable full-hypothesis instance;
* a cut of order at most four that persists in every allowed completion; or
* a four-colouring of the complete allowed lift.

Full-hypothesis instances are tested by the retained exhaustive paired-K5
solver.  Positive models and first model-producing edge prefixes are printed
as directly checkable JSON records.  A negative result is exact for that
printed finite instance, but nonfindings across sampled lifts remain only
heuristic evidence.

Expected invocation from the repository root:

    .venv/bin/python active/hc7_pb_type5_confined_lift_search.py

The fixed default run has six trajectories: three stop at persistent cuts;
the other three satisfy the full hypotheses and all three have exact paired
models.  Its terminal summary reports zero counterexample candidates.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations
import importlib.util
import json
from pathlib import Path
import random
import sys
from types import ModuleType
from typing import Iterable

import networkx as nx


ROOT = Path(__file__).resolve().parents[1]
SMALL_SEARCH = ROOT / "active" / "hc7_pb_small_full_hypothesis_search.py"
TYPE5_GENERATOR = ROOT / "active" / "hc7_pentagonal_bipyramid_enlargement_probe.py"
TYPE5_VERIFIER = (
    ROOT / "results" / "hc7_pentagonal_bipyramid_type5_endpoint_allocation_verify.py"
)
DEFAULT_SEED = 20_260_720


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


small = load_module("hc7_pb_small_search", SMALL_SEARCH)
pb = load_module("hc7_pb_type5_generator", TYPE5_GENERATOR)
type5_verify = load_module("hc7_pb_type5_verifier", TYPE5_VERIFIER)


Edge = tuple[int, int]


@dataclass(frozen=True)
class ExceptionalType5:
    index: int
    u: int
    v: int
    vertices: frozenset[object]
    edges: frozenset[frozenset[object]]


@dataclass(frozen=True)
class Lift:
    order: int
    exceptional: ExceptionalType5
    seed: int
    module_of: tuple[object, ...]
    start_edges: frozenset[Edge]
    allowed_edges: frozenset[Edge]
    parts: tuple[int, ...]
    a_mask: int
    b_mask: int


@dataclass(frozen=True)
class CutCertificate:
    cut: tuple[int, ...]
    components: tuple[int, ...]


@dataclass(frozen=True)
class Trajectory:
    outcome: str
    added_edges: tuple[Edge, ...]
    cut: CutCertificate | None = None
    colouring: tuple[int, ...] | None = None


def canonical_edge(left: int, right: int) -> Edge:
    return (left, right) if left < right else (right, left)


def graph_from_edges(order: int, edges: Iterable[Edge]) -> nx.Graph:
    graph = nx.Graph()
    graph.add_nodes_from(range(order))
    graph.add_edges_from(edges)
    return graph


def graph6(graph: nx.Graph) -> str:
    return nx.to_graph6_bytes(graph, header=False).decode("ascii").strip()


def mask_vertices(mask: int) -> list[int]:
    return list(small.bit_vertices(mask))


def base_label(label: object) -> int:
    return label[0] if isinstance(label, tuple) else label


def stable_base_edge(edge: frozenset[object]) -> tuple[object, object]:
    left, right = sorted(edge, key=repr)
    return left, right


def exceptional_instances() -> tuple[ExceptionalType5, ...]:
    exceptional = []
    instances = sorted(
        type5_verify.type5_instances(pb),
        key=lambda item: (
            item[0],
            item[1],
            tuple(sorted(map(repr, item[2]))),
            tuple(
                sorted(tuple(sorted(map(repr, edge))) for edge in item[3])
            ),
        ),
    )
    for index, (u, v, vertices, edges) in enumerate(instances):
        unsplit = tuple(sorted(set(pb.BASE) - {u, v}))
        if pb.rooted_k5(vertices, edges, unsplit) is not None:
            continue
        exceptional.append(
            ExceptionalType5(
                index=index,
                u=u,
                v=v,
                vertices=frozenset(vertices),
                edges=frozenset(edges),
            )
        )
    if len(exceptional) != 20:
        raise RuntimeError(f"expected 20 exceptional type-5 instances, got {len(exceptional)}")
    return tuple(exceptional)


def build_lift(instance: ExceptionalType5, order: int, seed: int) -> Lift:
    labels = tuple(sorted(instance.vertices, key=repr))
    if order < len(labels):
        raise ValueError(f"order {order} is below the nine-vertex type-5 base")
    root_labels = tuple(
        sorted(
            (set(pb.BASE) - {instance.u, instance.v})
            | {(instance.u, 0), (instance.v, 0)},
            key=repr,
        )
    )
    rng = random.Random(seed)
    sizes = {label: 1 for label in labels}
    first_extra_targets = list(root_labels)
    rng.shuffle(first_extra_targets)
    for _ in range(order - len(labels)):
        if first_extra_targets:
            label = first_extra_targets.pop()
        else:
            label = rng.choice(labels)
        sizes[label] += 1

    modules: dict[object, tuple[int, ...]] = {}
    module_of: list[object] = []
    next_vertex = 0
    for label in labels:
        module = tuple(range(next_vertex, next_vertex + sizes[label]))
        modules[label] = module
        module_of.extend([label] * len(module))
        next_vertex += len(module)
    assert next_vertex == order

    start_edges: set[Edge] = set()
    for label in labels:
        module = modules[label]
        for position in range(1, len(module)):
            parent = module[rng.randrange(position)]
            start_edges.add(canonical_edge(module[position], parent))
    for base_edge in sorted(instance.edges, key=lambda edge: tuple(sorted(map(repr, edge)))):
        left_label, right_label = stable_base_edge(base_edge)
        left = rng.choice(modules[left_label])
        right = rng.choice(modules[right_label])
        start_edges.add(canonical_edge(left, right))

    allowed_edges: set[Edge] = set()
    base_edges = instance.edges
    for left in range(order):
        for right in range(left + 1, order):
            left_label = module_of[left]
            right_label = module_of[right]
            if left_label == right_label or frozenset((left_label, right_label)) in base_edges:
                allowed_edges.add((left, right))
    if not start_edges <= allowed_edges:
        raise AssertionError("sparse lift contains an edge outside its allowed completion")

    part_masks = []
    for old_label in pb.BASE:
        mask = 0
        for label, module in modules.items():
            if base_label(label) == old_label:
                mask |= sum(1 << vertex for vertex in module)
        part_masks.append(mask)

    a_mask = 0
    b_mask = 0
    for label in root_labels:
        module = modules[label]
        a_mask |= 1 << module[0]
        b_mask |= 1 << (module[1] if len(module) > 1 else module[0])

    lift = Lift(
        order=order,
        exceptional=instance,
        seed=seed,
        module_of=tuple(module_of),
        start_edges=frozenset(start_edges),
        allowed_edges=frozenset(allowed_edges),
        parts=tuple(part_masks),
        a_mask=a_mask,
        b_mask=b_mask,
    )
    verify_lift(lift, graph_from_edges(order, start_edges))
    return lift


def verify_lift(lift: Lift, graph: nx.Graph) -> None:
    adjacency = small.adjacency_masks(graph)
    full = (1 << lift.order) - 1
    if sum(lift.parts) != full:
        raise AssertionError("columns do not partition the lift")
    if any(lift.parts[i] & lift.parts[j] for i in range(7) for j in range(i)):
        raise AssertionError("lift columns overlap")
    if not all(small.connected_mask(part, adjacency) for part in lift.parts):
        raise AssertionError("a lift column is disconnected")
    if not small.contact_is_pentagonal_bipyramid(lift.parts, adjacency):
        raise AssertionError("lift column contact graph is not the pentagonal bipyramid")
    if not all(lift.a_mask & part and lift.b_mask & part for part in lift.parts):
        raise AssertionError("a nominated root set misses a column")
    graph_edges = {canonical_edge(*edge) for edge in graph.edges()}
    if not graph_edges <= lift.allowed_edges:
        raise AssertionError("lift graph has a forbidden edge")


def component_masks(mask: int, adjacency: tuple[int, ...]) -> tuple[int, ...]:
    components = []
    unseen = mask
    while unseen:
        reached = unseen & -unseen
        frontier = reached
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            new = adjacency[vertex] & mask & ~reached
            reached |= new
            frontier |= new
        components.append(reached)
        unseen &= ~reached
    return tuple(components)


def first_small_cut(adjacency: tuple[int, ...]) -> CutCertificate | None:
    order = len(adjacency)
    full = (1 << order) - 1
    for size in range(5):
        for cut in combinations(range(order), size):
            removed = sum(1 << vertex for vertex in cut)
            remaining = full ^ removed
            if small.connected_mask(remaining, adjacency):
                continue
            return CutCertificate(cut=cut, components=component_masks(remaining, adjacency))
    return None


def find_four_colouring(adjacency: tuple[int, ...]) -> tuple[int, ...] | None:
    """Return an exact four-colouring, or None if none exists."""
    order = len(adjacency)
    colours = [-1] * order

    def search(coloured: int) -> bool:
        if coloured == order:
            return True
        best = -1
        best_key = (-1, -1)
        for vertex in range(order):
            if colours[vertex] >= 0:
                continue
            used = {
                colours[other]
                for other in small.bit_vertices(adjacency[vertex])
                if colours[other] >= 0
            }
            key = (len(used), adjacency[vertex].bit_count())
            if key > best_key:
                best = vertex
                best_key = key
        forbidden = {
            colours[other]
            for other in small.bit_vertices(adjacency[best])
            if colours[other] >= 0
        }
        for colour in range(4):
            if colour in forbidden:
                continue
            colours[best] = colour
            if search(coloured + 1):
                return True
            colours[best] = -1
        return False

    return tuple(colours) if search(0) else None


def choose_edge(
    candidates: Iterable[Edge],
    graph: nx.Graph,
    lift: Lift,
    colouring: tuple[int, ...] | None,
    rng: random.Random,
) -> Edge:
    ranked = []
    for edge in sorted(candidates):
        left, right = edge
        same_colour = int(colouring is not None and colouring[left] == colouring[right])
        cross_piece = int(lift.module_of[left] != lift.module_of[right])
        degree_pressure = -(graph.degree(left) + graph.degree(right))
        ranked.append(
            ((same_colour, degree_pressure, cross_piece, rng.randrange(1 << 30)), edge)
        )
    if not ranked:
        raise ValueError("cannot choose from an empty edge collection")
    return max(ranked)[1]


def edge_crosses_components(edge: Edge, components: tuple[int, ...]) -> bool:
    left, right = edge
    left_component = next(i for i, mask in enumerate(components) if mask & (1 << left))
    right_component = next(i for i, mask in enumerate(components) if mask & (1 << right))
    return left_component != right_component


def adversarial_trajectory(lift: Lift) -> Trajectory:
    rng = random.Random(lift.seed ^ 0x5EED5EED)
    graph = graph_from_edges(lift.order, lift.start_edges)
    missing = set(lift.allowed_edges - lift.start_edges)
    added = []

    while True:
        adjacency = small.adjacency_masks(graph)
        cut = first_small_cut(adjacency)
        colouring = find_four_colouring(adjacency)
        if cut is None and colouring is None:
            if not small.is_five_connected(adjacency):
                raise AssertionError("cut search disagrees with five-connectivity checker")
            if small.is_four_colourable(adjacency):
                raise AssertionError("colouring search disagrees with retained checker")
            return Trajectory("full_hypothesis", tuple(added))

        if cut is not None:
            candidates = [
                edge
                for edge in missing
                if not any(vertex in cut.cut for vertex in edge)
                and edge_crosses_components(edge, cut.components)
            ]
            if not candidates:
                complete = graph_from_edges(lift.order, lift.allowed_edges)
                complete_adjacency = small.adjacency_masks(complete)
                remaining = ((1 << lift.order) - 1) ^ sum(1 << v for v in cut.cut)
                if small.connected_mask(remaining, complete_adjacency):
                    raise AssertionError("claimed persistent cut is repaired in allowed completion")
                return Trajectory("persistent_small_cut", tuple(added), cut=cut)
        else:
            assert colouring is not None
            candidates = [
                edge for edge in missing if colouring[edge[0]] == colouring[edge[1]]
            ]
            if not candidates:
                complete = graph_from_edges(lift.order, lift.allowed_edges)
                if any(
                    colouring[left] == colouring[right] for left, right in complete.edges()
                ):
                    raise AssertionError("claimed completion colouring is not proper")
                return Trajectory(
                    "four_colourable_completion", tuple(added), colouring=colouring
                )

        edge = choose_edge(candidates, graph, lift, colouring, rng)
        graph.add_edge(*edge)
        missing.remove(edge)
        added.append(edge)


def prefix_graph(lift: Lift, trajectory: Trajectory, prefix: int) -> nx.Graph:
    edges = set(lift.start_edges)
    edges.update(trajectory.added_edges[:prefix])
    return graph_from_edges(lift.order, edges)


def verify_model(
    model: tuple[int, ...], adjacency: tuple[int, ...], a_mask: int, b_mask: int
) -> None:
    if len(model) != 5:
        raise AssertionError("paired model does not have five bags")
    if any(not bag or not (bag & a_mask) or not (bag & b_mask) for bag in model):
        raise AssertionError("paired model has a bag missing a nominated root set")
    if any(model[i] & model[j] for i in range(5) for j in range(i)):
        raise AssertionError("paired model bags overlap")
    if not all(small.connected_mask(bag, adjacency) for bag in model):
        raise AssertionError("paired model has a disconnected bag")
    if not all(
        small.bags_adjacent(model[i], model[j], adjacency)
        for i in range(5)
        for j in range(i)
    ):
        raise AssertionError("paired model bags are not pairwise adjacent")


def exact_paired_model(lift: Lift, graph: nx.Graph) -> tuple[tuple[int, ...] | None, int]:
    adjacency = small.adjacency_masks(graph)
    connected = small.connected_subsets(adjacency)
    model = small.paired_rooted_k5(adjacency, connected, lift.a_mask, lift.b_mask)
    if model is not None:
        verify_model(model, adjacency, lift.a_mask, lift.b_mask)
    return model, len(connected)


def first_model_prefix(
    lift: Lift,
    trajectory: Trajectory,
    full_model: tuple[int, ...],
) -> tuple[int, tuple[int, ...], dict[int, tuple[int, ...] | None]]:
    full_prefix = len(trajectory.added_edges)
    cache: dict[int, tuple[int, ...] | None] = {full_prefix: full_model}

    def model_at(prefix: int) -> tuple[int, ...] | None:
        if prefix not in cache:
            cache[prefix] = exact_paired_model(
                lift, prefix_graph(lift, trajectory, prefix)
            )[0]
        return cache[prefix]

    low = 0
    high = full_prefix
    while low < high:
        middle = (low + high) // 2
        if model_at(middle) is None:
            low = middle + 1
        else:
            high = middle
    first = low
    first_model = model_at(first)
    if first_model is None:
        raise AssertionError("model-prefix binary search lost a positive endpoint")
    if first > 0 and model_at(first - 1) is not None:
        raise AssertionError("reported model transition is not the first positive prefix")
    return first, first_model, cache


def certificate_base(lift: Lift, graph: nx.Graph) -> dict[str, object]:
    return {
        "order": lift.order,
        "exceptional_index": lift.exceptional.index,
        "split_edge": [lift.exceptional.u, lift.exceptional.v],
        "seed": lift.seed,
        "graph6": graph6(graph),
        "edges": [list(edge) for edge in sorted(graph.edges())],
        "parts": [mask_vertices(part) for part in lift.parts],
        "A": mask_vertices(lift.a_mask),
        "B": mask_vertices(lift.b_mask),
    }


def emit(kind: str, payload: dict[str, object]) -> None:
    print(f"{kind} {json.dumps(payload, sort_keys=True, separators=(',', ':'))}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-order", type=int, default=14)
    parser.add_argument("--max-order", type=int, default=14)
    parser.add_argument("--trials", type=int, default=1)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument(
        "--instance-limit",
        type=int,
        default=6,
        help="number of the 20 exceptional labelled type-5 bases to sample",
    )
    parser.add_argument(
        "--exact-full-limit",
        type=int,
        default=3,
        help="maximum full-hypothesis trajectories receiving the expensive paired-K5 test",
    )
    parser.add_argument(
        "--max-certificates",
        type=int,
        default=1,
        help="maximum blocked-family certificates to print (model transitions are always printed)",
    )
    args = parser.parse_args()
    if args.min_order < 11 or args.max_order < args.min_order:
        parser.error("require 11 <= min-order <= max-order")
    if args.trials < 1 or not 1 <= args.instance_limit <= 20:
        parser.error("require trials >= 1 and 1 <= instance-limit <= 20")
    if args.exact_full_limit < 0 or args.max_certificates < 0:
        parser.error("limits must be nonnegative")

    exceptional = exceptional_instances()[: args.instance_limit]
    emit(
        "CONFIG",
        {
            "base_seed": args.seed,
            "orders": [args.min_order, args.max_order],
            "trials": args.trials,
            "exceptional_instances": len(exceptional),
            "exact_full_limit": args.exact_full_limit,
            "claim_scope": "heuristic trajectories; exact checks on each reported finite graph",
        },
    )

    outcome_counts: dict[str, int] = {}
    paired_counts = {
        "present": 0,
        "absent": 0,
        "full_untested": 0,
        "not_full": 0,
    }
    exact_full_tests = 0
    blocked_certificates = 0
    counterexamples = 0

    for order in range(args.min_order, args.max_order + 1):
        for instance in exceptional:
            for trial in range(args.trials):
                seed = args.seed + order * 1_000_003 + instance.index * 1_009 + trial
                lift = build_lift(instance, order, seed)
                trajectory = adversarial_trajectory(lift)
                outcome_counts[trajectory.outcome] = outcome_counts.get(trajectory.outcome, 0) + 1
                trace: dict[str, object] = {
                    "order": order,
                    "exceptional_index": instance.index,
                    "trial": trial,
                    "seed": seed,
                    "outcome": trajectory.outcome,
                    "start_edges": len(lift.start_edges),
                    "added_edges": len(trajectory.added_edges),
                }

                if trajectory.outcome != "full_hypothesis":
                    paired_counts["not_full"] += 1
                    emit("TRACE", trace)
                    if blocked_certificates >= args.max_certificates:
                        continue
                    if trajectory.outcome == "persistent_small_cut":
                        assert trajectory.cut is not None
                        complete = graph_from_edges(order, lift.allowed_edges)
                        payload = certificate_base(lift, complete)
                        payload.update(
                            {
                                "cut": list(trajectory.cut.cut),
                                "components_after_cut": [
                                    mask_vertices(mask) for mask in trajectory.cut.components
                                ],
                                "meaning": "the cut persists in the complete allowed lift",
                            }
                        )
                        emit("CUT_CERTIFICATE", payload)
                    else:
                        assert trajectory.colouring is not None
                        complete = graph_from_edges(order, lift.allowed_edges)
                        payload = certificate_base(lift, complete)
                        payload.update(
                            {
                                "four_colouring": list(trajectory.colouring),
                                "meaning": "this colours the complete allowed lift",
                            }
                        )
                        emit("COLOUR_CERTIFICATE", payload)
                    blocked_certificates += 1
                    continue

                full_prefix = len(trajectory.added_edges)
                full_graph = prefix_graph(lift, trajectory, full_prefix)
                verify_lift(lift, full_graph)
                adjacency = small.adjacency_masks(full_graph)
                if not small.is_five_connected(adjacency) or small.is_four_colourable(adjacency):
                    raise AssertionError(
                        "full-hypothesis trajectory failed its exact terminal checks"
                    )

                if exact_full_tests >= args.exact_full_limit:
                    paired_counts["full_untested"] += 1
                    trace["paired_result"] = "UNTESTED_LIMIT"
                    trace["graph6"] = graph6(full_graph)
                    emit("TRACE", trace)
                    continue

                exact_full_tests += 1
                model, connected_count = exact_paired_model(lift, full_graph)
                trace.update(
                    {
                        "graph6": graph6(full_graph),
                        "connected_subsets": connected_count,
                    }
                )
                if model is None:
                    paired_counts["absent"] += 1
                    counterexamples += 1
                    trace["paired_result"] = "ABSENT_EXHAUSTIVE"
                    emit("TRACE", trace)
                    payload = certificate_base(lift, full_graph)
                    payload.update(
                        {
                            "five_connected": True,
                            "four_colourable": False,
                            "paired_rooted_K5": False,
                            "connected_subsets_checked": connected_count,
                            "meaning": (
                                "exact finite counterexample candidate to the paired-rooted target"
                            ),
                        }
                    )
                    emit("COUNTEREXAMPLE_CANDIDATE", payload)
                    continue

                paired_counts["present"] += 1
                trace["paired_result"] = "PRESENT"
                emit("TRACE", trace)
                first, transition_model, cache = first_model_prefix(lift, trajectory, model)
                after = prefix_graph(lift, trajectory, first)
                payload = certificate_base(lift, full_graph)
                payload["full_graph6"] = payload.pop("graph6")
                payload["full_edges"] = payload.pop("edges")
                payload.update(
                    {
                        "first_full_prefix": full_prefix,
                        "first_model_prefix": first,
                        "model_transition_edge": (
                            list(trajectory.added_edges[first - 1]) if first else None
                        ),
                        "before_graph6": (
                            graph6(prefix_graph(lift, trajectory, first - 1))
                            if first
                            else None
                        ),
                        "after_graph6": graph6(after),
                        "after_edges": [list(edge) for edge in sorted(after.edges())],
                        "model_after": [mask_vertices(bag) for bag in transition_model],
                        "exact_prefixes_tested": sorted(cache),
                        "meaning": (
                            "paired model already present in the sparse starting lift"
                            if first == 0
                            else "model absent immediately before and present after this edge"
                        ),
                    }
                )
                emit("MODEL_TRANSITION_CERTIFICATE", payload)

    emit(
        "SUMMARY",
        {
            "outcomes": outcome_counts,
            "paired_results": paired_counts,
            "exact_full_tests": exact_full_tests,
            "counterexample_candidates": counterexamples,
            "interpretation": (
                "Exact for printed finite instances; absence across sampled trajectories "
                "is heuristic evidence only."
            ),
        },
    )
    return 1 if counterexamples else 0


if __name__ == "__main__":
    sys.exit(main())
