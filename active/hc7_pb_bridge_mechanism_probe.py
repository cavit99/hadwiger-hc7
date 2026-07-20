#!/usr/bin/env python3
"""Exact bridge-mechanism probe on the retained finite PB examples.

This is finite evidence, not an unbounded bridge theorem.  The default run
uses only data already fixed elsewhere in the repository:

* every five-connected, non-four-colourable PB partition of orders 7--9
  from ``hc7_pb_small_full_hypothesis_search.py``;
* every prefix of the six default doubly-confined type-5 trajectories, plus
  the complete allowed lift for each persistent-cut trajectory; and
* the two PB barrier graphs whose verifiers have GREEN audits.

For every one of the twenty labelled PB frames, the probe checks the exact
hypotheses of the component transfer lemma, Corollary 2.2 (an alternating
connected column split), Theorem 2.1 (adjacent-rim linkage), and Theorem 2.1
(two-column absorption).  Every positive mechanism is lifted to five
literal, disjoint, connected and pairwise adjacent bags, each containing a
different whole column.  Consequently its certificate works for every
choice of one A-root and one B-root in each column.

The bridge diagnostics deliberately distinguish overlapping interval hulls
from genuine crossing: a crossing needs four distinct alternating attachment
vertices.  They also test the complete adjacent-rim Two Paths instance before
reporting a bridge-chain composition, and test a proposed separator in the
whole graph F rather than only in its owner column.

Expected invocation from the repository root:

    .venv/bin/python active/hc7_pb_bridge_mechanism_probe.py
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field
from hashlib import sha256
from itertools import combinations, product
import importlib.util
import json
from pathlib import Path
import shutil
import sys
from types import ModuleType
from typing import Iterable, Iterator, Sequence

import networkx as nx


ROOT = Path(__file__).resolve().parents[1]
SMALL_PATH = ROOT / "active" / "hc7_pb_small_full_hypothesis_search.py"
TYPE5_PATH = ROOT / "active" / "hc7_pb_type5_confined_lift_search.py"
FOUR_COLOUR_BARRIER = (
    ROOT / "barriers" / "hc7_pentagonal_bipyramid_four_colour_combined_negative_verify.py"
)
SPLIT_LINKAGE_BARRIER = (
    ROOT / "barriers" / "hc7_pentagonal_bipyramid_split_linkage_planarity_barrier_verify.py"
)

EXPECTED_HASHES = {
    SMALL_PATH: "b122c772e3c78b6825422279a4991d4b86d9dce6c3e1da0c6185a6e21fdc5b9c",
    TYPE5_PATH: "7965133526ba653101f6ac5d2d607954df6dd450879a7f663b0dac6f12f720d3",
    FOUR_COLOUR_BARRIER: "661d1970107c2a2d312e6ea011b79f77ec82504372d39c9d0d019ad0e627682c",
    SPLIT_LINKAGE_BARRIER: "4a482657438d9a4c92b63f76d5d3bfaf190f16f5e838c8a61638446d1be9390b",
}


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def verify_dependency_hashes() -> None:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"retained input changed: {path} has SHA-256 {actual}")


verify_dependency_hashes()
small = load_module("hc7_bridge_small", SMALL_PATH)
type5 = load_module("hc7_bridge_type5", TYPE5_PATH)


@dataclass(frozen=True)
class Instance:
    name: str
    graph: nx.Graph
    parts: tuple[frozenset[int], ...]
    family: str
    full_hypothesis: bool
    endpoint_multiplicity: int = 0


@dataclass(frozen=True)
class Frame:
    a: int
    b: int
    rim: tuple[int, int, int, int, int]


@dataclass
class Counts:
    instances: dict[str, int] = field(default_factory=dict)
    full_instances: int = 0
    endpoint_instances: int = 0
    frames: int = 0
    shortest_paths: int = 0
    off_path_components: int = 0
    path_cases_with_bridges: int = 0
    maximum_bridges_on_one_path: int = 0
    transfer_witnesses: int = 0
    alternating_splits: int = 0
    adjacent_linkages: int = 0
    absorptions: int = 0
    bridge_pairs: int = 0
    overlapping_hull_pairs: int = 0
    genuinely_crossing_pairs: int = 0
    crossing_path_cases: int = 0
    crossing_without_named_mechanism: int = 0
    overlap_without_crossing_pairs: int = 0
    bridge_chain_compositions: int = 0
    two_paths_local_failure_kinds: dict[str, int] = field(default_factory=dict)
    laminar_no_host_separator: int = 0


def emit(kind: str, payload: dict[str, object]) -> None:
    print(f"{kind} {json.dumps(payload, sort_keys=True, separators=(',', ':'))}")


def literal_assignment(path: Path, name: str) -> object:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            return ast.literal_eval(node.value)
    raise RuntimeError(f"literal assignment {name} not found in {path}")


def graph_from_barrier(path: Path, edge_name: str, name: str) -> Instance:
    raw_edges = literal_assignment(path, edge_name)
    graph = nx.Graph()
    graph.add_nodes_from(range(14))
    graph.add_edges_from((2 * x + i, 2 * y + j) for x, i, y, j in raw_edges)
    graph.add_edges_from((2 * label, 2 * label + 1) for label in range(7))
    parts = tuple(frozenset((2 * label, 2 * label + 1)) for label in range(7))
    return Instance(name, graph, parts, "audited_barrier", False)


def mask_part(mask: int) -> frozenset[int]:
    return frozenset(small.bit_vertices(mask))


def small_instances() -> Iterator[Instance]:
    geng = shutil.which("geng")
    if geng is None:
        raise RuntimeError("geng is required for the retained order<=9 census")
    partition_counts: dict[int, int] = {}
    endpoint_counts: dict[int, int] = {}
    for order in range(7, 10):
        partition_counts[order] = 0
        endpoint_counts[order] = 0
        for graph6, graph in small.graph6_stream(geng, order):
            adjacency = small.adjacency_masks(graph)
            if not small.is_five_connected(adjacency):
                continue
            if small.is_four_colourable(adjacency):
                continue
            for index, masks in enumerate(small.connected_pb_partitions(order, adjacency)):
                parts = tuple(mask_part(mask) for mask in masks)
                multiplicity = 1
                for part in parts:
                    multiplicity *= len(part) ** 2
                partition_counts[order] += 1
                endpoint_counts[order] += multiplicity
                yield Instance(
                    f"small:n={order}:g6={graph6}:partition={index}",
                    graph.copy(),
                    parts,
                    "small_full",
                    True,
                    multiplicity,
                )
    if partition_counts != {7: 0, 8: 1, 9: 63}:
        raise AssertionError(f"retained PB partition counts changed: {partition_counts}")
    if sum(endpoint_counts.values()) != 858:
        raise AssertionError(f"retained endpoint count changed: {endpoint_counts}")


def type5_instances() -> Iterator[Instance]:
    exceptional = type5.exceptional_instances()[:6]
    for exceptional_instance in exceptional:
        seed = (
            type5.DEFAULT_SEED
            + 14 * 1_000_003
            + exceptional_instance.index * 1_009
        )
        lift = type5.build_lift(exceptional_instance, 14, seed)
        trajectory = type5.adversarial_trajectory(lift)
        for prefix in range(len(trajectory.added_edges) + 1):
            graph = type5.prefix_graph(lift, trajectory, prefix)
            yield Instance(
                (
                    f"type5:index={exceptional_instance.index}:"
                    f"outcome={trajectory.outcome}:prefix={prefix}"
                ),
                graph,
                tuple(mask_part(mask) for mask in lift.parts),
                "type5_prefix",
                trajectory.outcome == "full_hypothesis"
                and prefix == len(trajectory.added_edges),
            )
        if trajectory.outcome == "persistent_small_cut":
            complete = type5.graph_from_edges(14, lift.allowed_edges)
            yield Instance(
                f"type5:index={exceptional_instance.index}:complete_allowed",
                complete,
                tuple(mask_part(mask) for mask in lift.parts),
                "type5_complete_allowed",
                False,
            )


def all_instances() -> Iterator[Instance]:
    yield from small_instances()
    yield from type5_instances()
    yield graph_from_barrier(
        FOUR_COLOUR_BARRIER,
        "CROSS_EDGES",
        "barrier:four_colour_combined_negative",
    )
    yield graph_from_barrier(
        SPLIT_LINKAGE_BARRIER,
        "CROSS",
        "barrier:split_linkage_planarity",
    )


def touches(graph: nx.Graph, left: Iterable[int], right: Iterable[int]) -> bool:
    right_set = set(right)
    return any(neighbour in right_set for vertex in left for neighbour in graph[vertex])


def quotient(instance: Instance) -> nx.Graph:
    result = nx.Graph()
    result.add_nodes_from(range(7))
    for left, right in combinations(range(7), 2):
        if touches(instance.graph, instance.parts[left], instance.parts[right]):
            result.add_edge(left, right)
    return result


def validate_instance(instance: Instance) -> None:
    graph = instance.graph
    if set().union(*instance.parts) != set(graph):
        raise AssertionError(f"{instance.name}: columns do not span")
    if sum(map(len, instance.parts)) != len(graph):
        raise AssertionError(f"{instance.name}: columns overlap")
    if not all(nx.is_connected(graph.subgraph(part)) for part in instance.parts):
        raise AssertionError(f"{instance.name}: disconnected column")
    degrees = sorted(dict(quotient(instance).degree()).values())
    if degrees != [4, 4, 4, 4, 4, 5, 5]:
        raise AssertionError(f"{instance.name}: quotient is not PB")
    if instance.full_hypothesis:
        adjacency = small.adjacency_masks(graph)
        if not small.is_five_connected(adjacency):
            raise AssertionError(f"{instance.name}: not five-connected")
        if small.is_four_colourable(adjacency):
            raise AssertionError(f"{instance.name}: unexpectedly four-colourable")


def frames(instance: Instance) -> tuple[Frame, ...]:
    contact = quotient(instance)
    apices = tuple(vertex for vertex, degree in contact.degree() if degree == 5)
    if len(apices) != 2 or contact.has_edge(*apices):
        raise AssertionError(f"{instance.name}: bad PB apices")
    rim_vertices = tuple(vertex for vertex in contact if vertex not in apices)
    frame_set = set()
    for a, b in (apices, apices[::-1]):
        for start in rim_vertices:
            neighbours = sorted(set(contact[start]) & set(rim_vertices))
            if len(neighbours) != 2:
                raise AssertionError("rim is not a cycle")
            for second in neighbours:
                order = [start, second]
                while len(order) < 5:
                    choices = (set(contact[order[-1]]) & set(rim_vertices)) - {order[-2]}
                    order.append(next(iter(choices)))
                if contact.has_edge(order[-1], order[0]):
                    frame_set.add(Frame(a, b, tuple(order)))
    result = tuple(sorted(frame_set, key=lambda f: (f.a, f.b, f.rim)))
    if len(result) != 20:
        raise AssertionError(f"{instance.name}: expected 20 PB frames, got {len(result)}")
    return result


def frame_json(frame: Frame) -> dict[str, object]:
    return {"a": frame.a, "b": frame.b, "rim": list(frame.rim)}


def connected_subsets(graph: nx.Graph, vertices: Iterable[int]) -> tuple[frozenset[int], ...]:
    ordered = tuple(sorted(vertices))
    subsets = []
    for mask in range(1, 1 << len(ordered)):
        subset = frozenset(ordered[index] for index in range(len(ordered)) if mask & (1 << index))
        if nx.is_connected(graph.subgraph(subset)):
            subsets.append(subset)
    return tuple(sorted(subsets, key=lambda item: (len(item), tuple(item))))


def validate_bags(
    instance: Instance,
    bags: Sequence[Iterable[int]],
    owned_columns: Sequence[int],
) -> None:
    bag_sets = tuple(frozenset(bag) for bag in bags)
    if len(bag_sets) != 5 or len(set(owned_columns)) != 5:
        raise AssertionError("certificate needs five differently owned bags")
    if sum(map(len, bag_sets)) != len(set().union(*bag_sets)):
        raise AssertionError("certificate bags overlap")
    if not all(nx.is_connected(instance.graph.subgraph(bag)) for bag in bag_sets):
        raise AssertionError("certificate has a disconnected bag")
    if not all(
        touches(instance.graph, bag_sets[left], bag_sets[right])
        for left, right in combinations(range(5), 2)
    ):
        raise AssertionError("certificate bags are not pairwise adjacent")
    for bag, owner in zip(bag_sets, owned_columns):
        if not instance.parts[owner] <= bag:
            raise AssertionError("certificate lost its whole owned column")


def bag_certificate(
    instance: Instance,
    frame: Frame,
    bags: Sequence[Iterable[int]],
    owned: Sequence[int],
    extra: dict[str, object],
) -> dict[str, object]:
    payload: dict[str, object] = {
        "instance": instance.name,
        "frame": frame_json(frame),
        "bags": [sorted(bag) for bag in bags],
        "owned_columns": list(owned),
        "root_scope": "whole-column ownership covers every A/B endpoint choice",
    }
    payload.update(extra)
    return payload


def shortest_set_paths(
    graph: nx.Graph,
    column: frozenset[int],
    sources: frozenset[int],
    targets: frozenset[int],
) -> tuple[tuple[int, ...], ...]:
    induced = graph.subgraph(column)
    distances = {
        (source, target): nx.shortest_path_length(induced, source, target)
        for source in sources
        for target in targets
    }
    minimum = min(distances.values())
    paths = {
        tuple(path)
        for pair, distance in distances.items()
        if distance == minimum
        for path in nx.all_shortest_paths(induced, *pair)
    }
    return tuple(sorted(paths))


def transfer_witness(
    instance: Instance,
    frame: Frame,
    position: int,
    path: tuple[int, ...],
) -> tuple[dict[str, object] | None, tuple[frozenset[int], ...]]:
    owner = frame.rim[position]
    path_set = frozenset(path)
    remaining = instance.parts[owner] - path_set
    components = tuple(
        sorted(
            (
                frozenset(component)
                for component in nx.connected_components(
                    instance.graph.subgraph(remaining)
                )
            ),
            key=lambda item: (min(item), len(item)),
        )
    ) if remaining else ()
    previous = frame.rim[(position - 1) % 5]
    following = frame.rim[(position + 1) % 5]
    for component in components:
        if not touches(instance.graph, component, instance.parts[previous]):
            continue
        if not touches(instance.graph, component, instance.parts[following]):
            continue
        bags = (
            instance.parts[frame.a] | (instance.parts[owner] - component),
            instance.parts[frame.b],
            component | instance.parts[following],
            instance.parts[frame.rim[(position + 2) % 5]],
            instance.parts[frame.rim[(position + 3) % 5]]
            | instance.parts[frame.rim[(position + 4) % 5]],
        )
        owned = (
            frame.a,
            frame.b,
            following,
            frame.rim[(position + 2) % 5],
            frame.rim[(position + 3) % 5],
        )
        validate_bags(instance, bags, owned)
        return bag_certificate(
            instance,
            frame,
            bags,
            owned,
            {
                "rim_position": position,
                "path": list(path),
                "two_sided_component": sorted(component),
            },
        ), components
    return None, components


def cyclic_order(frame: Frame, owner: int) -> tuple[int, ...]:
    if owner == frame.a:
        return frame.rim
    if owner == frame.b:
        return (frame.rim[0],) + tuple(reversed(frame.rim[1:]))
    position = frame.rim.index(owner)
    return (
        frame.a,
        frame.rim[(position + 1) % 5],
        frame.b,
        frame.rim[(position - 1) % 5],
    )


def alternating_quadruple(
    order: tuple[int, ...],
    left_contacts: set[int],
    right_contacts: set[int],
) -> tuple[int, int, int, int] | None:
    for indices in combinations(range(len(order)), 4):
        labels = tuple(order[index] for index in indices)
        if all(
            labels[index] in (left_contacts if index % 2 == 0 else right_contacts)
            for index in range(4)
        ):
            return labels
        if all(
            labels[index] in (right_contacts if index % 2 == 0 else left_contacts)
            for index in range(4)
        ):
            return labels
    return None


def anchored_k5(graph: nx.Graph, old_vertices: set[object]) -> tuple[frozenset[object], ...] | None:
    vertices = tuple(sorted(graph, key=repr))
    subsets = []
    for mask in range(1, 1 << len(vertices)):
        subset = frozenset(vertices[index] for index in range(len(vertices)) if mask & (1 << index))
        if not subset & old_vertices:
            continue
        if nx.is_connected(graph.subgraph(subset)):
            subsets.append(subset)
    subsets.sort(key=lambda item: (len(item), tuple(sorted(map(repr, item)))))

    def extend(start: int, chosen: tuple[frozenset[object], ...]):
        if len(chosen) == 5:
            return chosen
        for index in range(start, len(subsets)):
            candidate = subsets[index]
            if any(candidate & old for old in chosen):
                continue
            if any(not touches(graph, candidate, old) for old in chosen):
                continue
            answer = extend(index + 1, chosen + (candidate,))
            if answer is not None:
                return answer
        return None

    return extend(0, ())


def alternating_split(
    instance: Instance, frame: Frame
) -> dict[str, object] | None:
    contact = quotient(instance)
    for owner in (frame.a, frame.b) + frame.rim:
        vertices = tuple(sorted(instance.parts[owner]))
        anchor = vertices[0]
        for size in range(1, len(vertices)):
            for chosen in combinations(vertices[1:], size - 1):
                left = frozenset((anchor,) + chosen)
                right = instance.parts[owner] - left
                if not nx.is_connected(instance.graph.subgraph(left)):
                    continue
                if not nx.is_connected(instance.graph.subgraph(right)):
                    continue
                order = cyclic_order(frame, owner)
                left_contacts = {
                    label for label in order if touches(instance.graph, left, instance.parts[label])
                }
                right_contacts = {
                    label
                    for label in order
                    if touches(instance.graph, right, instance.parts[label])
                }
                quad = alternating_quadruple(order, left_contacts, right_contacts)
                if quad is None:
                    continue

                clone_left = ("split", 0)
                clone_right = ("split", 1)
                split_graph = nx.Graph()
                old = set(range(7)) - {owner}
                split_graph.add_nodes_from(old | {clone_left, clone_right})
                split_graph.add_edge(clone_left, clone_right)
                split_graph.add_edges_from(
                    edge for edge in contact.edges() if owner not in edge
                )
                for label in contact[owner]:
                    if touches(instance.graph, left, instance.parts[label]):
                        split_graph.add_edge(clone_left, label)
                    if touches(instance.graph, right, instance.parts[label]):
                        split_graph.add_edge(clone_right, label)
                quotient_model = anchored_k5(split_graph, old)
                if quotient_model is None:
                    raise AssertionError("alternating split lost the audited quotient K5")
                expansion = {label: instance.parts[label] for label in old}
                expansion[clone_left] = left
                expansion[clone_right] = right
                bags = tuple(
                    frozenset().union(*(expansion[vertex] for vertex in quotient_bag))
                    for quotient_bag in quotient_model
                )
                owned = tuple(
                    next(vertex for vertex in quotient_bag if vertex in old)
                    for quotient_bag in quotient_model
                )
                validate_bags(instance, bags, owned)
                return bag_certificate(
                    instance,
                    frame,
                    bags,
                    owned,
                    {
                        "owner": owner,
                        "left": sorted(left),
                        "right": sorted(right),
                        "cyclic_order": list(order),
                        "alternating_labels": list(quad),
                    },
                )
    return None


def adjacent_linkage_at(
    instance: Instance, frame: Frame, position: int
) -> tuple[frozenset[int], frozenset[int]] | None:
    left = frame.rim[position]
    right = frame.rim[(position + 1) % 5]
    previous = frame.rim[(position - 1) % 5]
    following = frame.rim[(position + 2) % 5]
    carrier = instance.parts[left] | instance.parts[right]
    subsets = connected_subsets(instance.graph, carrier)
    first = tuple(
        subset for subset in subsets
        if touches(instance.graph, subset, instance.parts[frame.a])
        and touches(instance.graph, subset, instance.parts[frame.b])
    )
    second = tuple(
        subset for subset in subsets
        if touches(instance.graph, subset, instance.parts[previous])
        and touches(instance.graph, subset, instance.parts[following])
    )
    for x_set in first:
        for y_set in second:
            if not x_set & y_set:
                return x_set, y_set
    return None


def adjacent_linkage(
    instance: Instance, frame: Frame
) -> tuple[dict[str, object] | None, dict[int, tuple[frozenset[int], frozenset[int]]]]:
    witnesses = {}
    certificate = None
    for position in range(5):
        witness = adjacent_linkage_at(instance, frame, position)
        if witness is None:
            continue
        witnesses[position] = witness
        if certificate is not None:
            continue
        x_set, y_set = witness
        previous = frame.rim[(position - 1) % 5]
        bags = (
            instance.parts[frame.a] | x_set,
            instance.parts[frame.b],
            instance.parts[previous] | y_set,
            instance.parts[frame.rim[(position + 2) % 5]],
            instance.parts[frame.rim[(position + 3) % 5]],
        )
        owned = (
            frame.a,
            frame.b,
            previous,
            frame.rim[(position + 2) % 5],
            frame.rim[(position + 3) % 5],
        )
        validate_bags(instance, bags, owned)
        certificate = bag_certificate(
            instance,
            frame,
            bags,
            owned,
            {"rim_position": position, "X": sorted(x_set), "Y": sorted(y_set)},
        )
    return certificate, witnesses


def absorption(instance: Instance, frame: Frame) -> dict[str, object] | None:
    carrier = tuple(sorted(instance.parts[frame.a] | instance.parts[frame.rim[0]]))
    for assignment in product((0, 1, 2), repeat=len(carrier)):
        x_one = frozenset(vertex for vertex, mark in zip(carrier, assignment) if mark == 1)
        x_two = frozenset(vertex for vertex, mark in zip(carrier, assignment) if mark == 2)
        d_one = instance.parts[frame.rim[1]] | x_one
        d_two = instance.parts[frame.rim[2]] | x_two
        if not nx.is_connected(instance.graph.subgraph(d_one)):
            continue
        if not nx.is_connected(instance.graph.subgraph(d_two)):
            continue
        if not touches(instance.graph, d_one, instance.parts[frame.rim[3]]):
            continue
        if not touches(instance.graph, d_one, instance.parts[frame.rim[4]]):
            continue
        if not touches(instance.graph, d_two, instance.parts[frame.rim[4]]):
            continue
        bags = (
            instance.parts[frame.b],
            d_one,
            d_two,
            instance.parts[frame.rim[3]],
            instance.parts[frame.rim[4]],
        )
        owned = (
            frame.b,
            frame.rim[1],
            frame.rim[2],
            frame.rim[3],
            frame.rim[4],
        )
        validate_bags(instance, bags, owned)
        return bag_certificate(
            instance,
            frame,
            bags,
            owned,
            {"X1": sorted(x_one), "X2": sorted(x_two)},
        )
    return None


def bridge_records(
    instance: Instance,
    frame: Frame,
    position: int,
    path: tuple[int, ...],
    carrier_two_columns: bool = False,
) -> tuple[dict[str, object], ...]:
    path_set = set(path)
    owner = frame.rim[position]
    carrier = set(instance.parts[owner])
    if carrier_two_columns:
        carrier |= set(instance.parts[frame.rim[(position + 1) % 5]])
    records = []
    for component in nx.connected_components(instance.graph.subgraph(carrier - path_set)):
        attachments = tuple(
            index
            for index, vertex in enumerate(path)
            if any(instance.graph.has_edge(vertex, other) for other in component)
        )
        if not attachments:
            raise AssertionError("an R-bridge component has no attachment")
        records.append(
            {
                "component": frozenset(component),
                "attachments": attachments,
                "interval": (min(attachments), max(attachments)),
            }
        )
    return tuple(
        sorted(
            records,
            key=lambda record: (record["interval"], sorted(record["component"])),
        )
    )


def genuinely_crosses(left: Sequence[int], right: Sequence[int]) -> bool:
    for first in combinations(left, 2):
        for second in combinations(right, 2):
            a, c = sorted(first)
            b, d = sorted(second)
            if a < b < c < d or b < a < d < c:
                return True
    return False


def hulls_overlap(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return max(left[0], right[0]) <= min(left[1], right[1])


def hulls_laminar(left: tuple[int, int], right: tuple[int, int]) -> bool:
    a, c = left
    b, d = right
    return c <= b or d <= a or (a <= b and d <= c) or (b <= a and c <= d)


def local_bridge_test_negative(
    instance: Instance,
    frame: Frame,
    position: int,
    path: tuple[int, ...],
    records: tuple[dict[str, object], ...],
) -> bool:
    previous = instance.parts[frame.rim[(position - 1) % 5]]
    following = instance.parts[frame.rim[(position + 2) % 5]]
    gamma_portals = {
        vertex for vertex in set().union(*(record["component"] for record in records), set(path))
        if touches(instance.graph, {vertex}, previous)
    }
    delta_portals = {
        vertex for vertex in set().union(*(record["component"] for record in records), set(path))
        if touches(instance.graph, {vertex}, following)
    }
    for record in records:
        component = set(record["component"])
        if component & gamma_portals and component & delta_portals:
            return False
        low, high = record["interval"]
        open_span = set(path[low + 1 : high])
        if open_span & gamma_portals and open_span & delta_portals:
            return False
    return True


def analyse_path(
    instance: Instance,
    frame: Frame,
    position: int,
    path: tuple[int, ...],
    components: tuple[frozenset[int], ...],
    named_mechanism: bool,
    adjacent_witnesses: dict[int, tuple[frozenset[int], frozenset[int]]],
    counts: Counts,
    adversarial_certificates: dict[str, dict[str, object]],
) -> None:
    records = bridge_records(instance, frame, position, path)
    if len(records) != len(components):
        raise AssertionError("component and bridge enumerations disagree")
    counts.off_path_components += len(records)
    counts.path_cases_with_bridges += int(bool(records))
    counts.maximum_bridges_on_one_path = max(
        counts.maximum_bridges_on_one_path, len(records)
    )

    crossing = False
    for left, right in combinations(records, 2):
        counts.bridge_pairs += 1
        overlap = hulls_overlap(left["interval"], right["interval"])
        counts.overlapping_hull_pairs += int(overlap)
        if genuinely_crosses(left["attachments"], right["attachments"]):
            crossing = True
            counts.genuinely_crossing_pairs += 1
        elif overlap:
            counts.overlap_without_crossing_pairs += 1
            adversarial_certificates.setdefault(
                "overlap_without_four_distinct_crossing",
                {
                    "instance": instance.name,
                    "frame": frame_json(frame),
                    "rim_position": position,
                    "path": list(path),
                    "left_attachments": list(left["attachments"]),
                    "right_attachments": list(right["attachments"]),
                    "meaning": (
                        "closed interval hulls overlap but no four distinct "
                        "attachments alternate"
                    ),
                },
            )
    if crossing:
        counts.crossing_path_cases += 1
        if not named_mechanism:
            counts.crossing_without_named_mechanism += 1
            adversarial_certificates.setdefault(
                "crossing_without_named_mechanism",
                {
                    "instance": instance.name,
                    "frame": frame_json(frame),
                    "rim_position": position,
                    "path": list(path),
                    "bridges": [
                        {
                            "component": sorted(record["component"]),
                            "attachments": list(record["attachments"]),
                        }
                        for record in records
                    ],
                    "meaning": (
                        "genuine crossing exists but none of the four sufficient "
                        "named mechanisms fires in this frame"
                    ),
                },
            )

    is_laminar = all(
        hulls_laminar(left["interval"], right["interval"])
        and not genuinely_crosses(left["attachments"], right["attachments"])
        for left, right in combinations(records, 2)
    )
    if records and is_laminar:
        for record in records:
            separator = {path[index] for index in record["attachments"]}
            if len(separator) > 4 or len(separator) == len(instance.graph):
                continue
            remaining = instance.graph.copy()
            remaining.remove_nodes_from(separator)
            if not remaining or not nx.is_connected(remaining):
                continue
            counts.laminar_no_host_separator += 1
            adversarial_certificates.setdefault(
                "laminar_column_boundary_not_host_separator",
                {
                    "instance": instance.name,
                    "frame": frame_json(frame),
                    "rim_position": position,
                    "path": list(path),
                    "bridge_component": sorted(record["component"]),
                    "attachment_vertices": sorted(separator),
                    "attachment_intervals": [list(item["interval"]) for item in records],
                    "literal_check": "F minus the complete R-attachment set is connected",
                },
            )
            break

    if position in adjacent_witnesses:
        carrier_records = bridge_records(instance, frame, position, path, True)
        if carrier_records and local_bridge_test_negative(
            instance, frame, position, path, carrier_records
        ):
            x_set, y_set = adjacent_witnesses[position]
            if any(
                record["component"] & x_set and record["component"] & y_set
                for record in carrier_records
            ):
                composition_kind = "global_linkage_splits_one_R_bridge"
            elif sum(
                bool(record["component"] & (x_set | y_set))
                for record in carrier_records
            ) >= 2:
                composition_kind = "global_linkage_composes_multiple_R_bridges"
            else:
                composition_kind = "global_linkage_reallocates_path_and_bridge_vertices"
            counts.bridge_chain_compositions += 1
            counts.two_paths_local_failure_kinds[composition_kind] = (
                counts.two_paths_local_failure_kinds.get(composition_kind, 0) + 1
            )
            adversarial_certificates.setdefault(
                f"whole_two_paths_positive_bridge_local_negative:{composition_kind}",
                {
                    "instance": instance.name,
                    "frame": frame_json(frame),
                    "rim_position": position,
                    "path": list(path),
                    "global_X": sorted(x_set),
                    "global_Y": sorted(y_set),
                    "composition_kind": composition_kind,
                    "carrier_bridges": [
                        {
                            "component": sorted(record["component"]),
                            "attachments": list(record["attachments"]),
                        }
                        for record in carrier_records
                    ],
                    "meaning": (
                        "exact adjacent-rim Two Paths linkage is positive although "
                        "every individual bridge/interior-span test is negative"
                    ),
                },
            )


def main() -> int:
    counts = Counts()
    mechanism_certificates: dict[str, dict[str, object]] = {}
    adversarial_certificates: dict[str, dict[str, object]] = {}
    family_mechanisms: dict[str, dict[str, int]] = {}

    emit(
        "CONFIG",
        {
            "scope": "fixed retained finite examples only; no expanded census",
            "small_orders": [7, 9],
            "type5_seed": type5.DEFAULT_SEED,
            "type5_trajectories": 6,
            "pb_frames_per_instance": 20,
            "claim_scope": "exact per printed finite graph; finite evidence only",
        },
    )

    for instance in all_instances():
        validate_instance(instance)
        counts.instances[instance.family] = counts.instances.get(instance.family, 0) + 1
        counts.full_instances += int(instance.full_hypothesis)
        counts.endpoint_instances += instance.endpoint_multiplicity
        family = family_mechanisms.setdefault(
            instance.family,
            {"frames": 0, "transfer": 0, "alternating": 0, "adjacent": 0, "absorption": 0},
        )
        for frame in frames(instance):
            counts.frames += 1
            family["frames"] += 1
            split_certificate = alternating_split(instance, frame)
            adjacent_certificate, adjacent_witnesses = adjacent_linkage(instance, frame)
            absorption_certificate = absorption(instance, frame)
            if split_certificate is not None:
                counts.alternating_splits += 1
                family["alternating"] += 1
                mechanism_certificates.setdefault("alternating_split", split_certificate)
            if adjacent_certificate is not None:
                counts.adjacent_linkages += 1
                family["adjacent"] += 1
                mechanism_certificates.setdefault("adjacent_linkage", adjacent_certificate)
            if absorption_certificate is not None:
                counts.absorptions += 1
                family["absorption"] += 1
                mechanism_certificates.setdefault("two_column_absorption", absorption_certificate)

            frame_has_transfer = False
            for position in range(5):
                owner = frame.rim[position]
                u_set = frozenset(
                    vertex for vertex in instance.parts[owner]
                    if touches(instance.graph, {vertex}, instance.parts[frame.a])
                )
                w_set = frozenset(
                    vertex for vertex in instance.parts[owner]
                    if touches(instance.graph, {vertex}, instance.parts[frame.b])
                )
                if not u_set or not w_set:
                    raise AssertionError("PB quotient has an empty pole portal set")
                for path in shortest_set_paths(instance.graph, instance.parts[owner], u_set, w_set):
                    counts.shortest_paths += 1
                    transfer_certificate, components = transfer_witness(
                        instance, frame, position, path
                    )
                    if transfer_certificate is not None:
                        counts.transfer_witnesses += 1
                        frame_has_transfer = True
                        mechanism_certificates.setdefault(
                            "component_transfer", transfer_certificate
                        )
                    named = any(
                        certificate is not None
                        for certificate in (
                            transfer_certificate,
                            split_certificate,
                            adjacent_certificate,
                            absorption_certificate,
                        )
                    )
                    analyse_path(
                        instance,
                        frame,
                        position,
                        path,
                        components,
                        named,
                        adjacent_witnesses,
                        counts,
                        adversarial_certificates,
                    )
            if frame_has_transfer:
                family["transfer"] += 1

    if counts.instances.get("small_full") != 64 or counts.endpoint_instances != 858:
        raise AssertionError("small retained corpus coverage is incomplete")
    if counts.instances.get("type5_prefix") != 77:
        raise AssertionError("the six retained type-5 trajectories changed")
    if counts.instances.get("type5_complete_allowed") != 3:
        raise AssertionError("expected three persistent-cut completions")
    if counts.instances.get("audited_barrier") != 2:
        raise AssertionError("audited PB barrier coverage is incomplete")

    emit(
        "DATASET_SUMMARY",
        {
            "instances": counts.instances,
            "full_hypothesis_instances": counts.full_instances,
            "small_endpoint_instances_covered_universally": counts.endpoint_instances,
            "family_mechanisms": family_mechanisms,
        },
    )
    for mechanism, certificate in sorted(mechanism_certificates.items()):
        emit("MECHANISM_CERTIFICATE", {"mechanism": mechanism, **certificate})
    for finding, certificate in sorted(adversarial_certificates.items()):
        emit("ADVERSARIAL_CERTIFICATE", {"finding": finding, **certificate})
    if counts.bridge_pairs == 0:
        emit(
            "EVIDENCE_LIMIT",
            {
                "finding": "no_multi_bridge_shortest_path_in_frozen_corpus",
                "shortest_paths_checked": counts.shortest_paths,
                "maximum_owner_column_bridges": counts.maximum_bridges_on_one_path,
                "consequence": (
                    "the frozen corpus has no power to test crossing-versus-laminar "
                    "interval-pair assertions"
                ),
            },
        )
    emit(
        "SUMMARY",
        {
            "frames": counts.frames,
            "shortest_paths": counts.shortest_paths,
            "off_path_components": counts.off_path_components,
            "path_cases_with_off_path_components": counts.path_cases_with_bridges,
            "maximum_owner_column_bridges_on_one_path": counts.maximum_bridges_on_one_path,
            "mechanism_positive_path_or_frames": {
                "component_transfer_paths": counts.transfer_witnesses,
                "alternating_split_frames": counts.alternating_splits,
                "adjacent_linkage_frames": counts.adjacent_linkages,
                "two_column_absorption_frames": counts.absorptions,
            },
            "adversarial": {
                "bridge_pairs_examined": counts.bridge_pairs,
                "overlapping_interval_hull_pairs": counts.overlapping_hull_pairs,
                "genuinely_crossing_attachment_pairs": counts.genuinely_crossing_pairs,
                "genuine_crossing_path_cases": counts.crossing_path_cases,
                "crossing_without_named_mechanism": counts.crossing_without_named_mechanism,
                "overlap_without_four_distinct_crossing_pairs": (
                    counts.overlap_without_crossing_pairs
                ),
                "whole_two_paths_positive_bridge_local_negative": counts.bridge_chain_compositions,
                "two_paths_local_failure_kinds": counts.two_paths_local_failure_kinds,
                "laminar_attachment_sets_not_host_separators": counts.laminar_no_host_separator,
            },
            "interpretation": (
                "exact on this frozen finite corpus; neither positive coverage nor "
                "nonfindings prove an unbounded theorem"
            ),
        },
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
