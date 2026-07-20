#!/usr/bin/env python3
"""Exact probe of Hegde--Thomas 1--7 enlargements of the PB.

The pentagonal bipyramid is a triangulation, so enlargement types 2, 4,
6 and 7 have no instance.  This script enumerates types 1, 3 and 5 and
tests for a K5 minor whose bags admit five distinct original PB labels.
It is exploratory evidence, not a promoted proof.
"""

from collections import Counter
from itertools import combinations


POLES = ("p", "q")
RIM = tuple(f"r{i}" for i in range(5))
VERTICES = POLES + RIM


def edge(u, v):
    return tuple(sorted((u, v)))


def pb_edges():
    result = {edge(x, r) for x in POLES for r in RIM}
    result |= {edge(RIM[i], RIM[(i + 1) % 5]) for i in range(5)}
    return result


EDGES = pb_edges()
ROTATION = {
    "p": RIM,
    "q": ("r0", "r4", "r3", "r2", "r1"),
}
for i in range(5):
    ROTATION[f"r{i}"] = (
        "p",
        f"r{(i + 1) % 5}",
        "q",
        f"r{(i - 1) % 5}",
    )

FACES = []
for pole in POLES:
    for i in range(5):
        FACES.append(frozenset((pole, RIM[i], RIM[(i + 1) % 5])))


def contiguous(block, rotation):
    """Whether a nonempty proper block is a cyclic interval."""
    marks = [x in block for x in rotation]
    transitions = sum(
        marks[i] != marks[(i + 1) % len(marks)] for i in range(len(marks))
    )
    return transitions == 2


def split_partitions(vertex, conforming, along=None):
    """Unordered neighbour bipartitions satisfying the requested kind."""
    rotation = ROTATION[vertex]
    neighbours = set(rotation)
    output = []
    seen = set()
    for size in range(2, len(rotation) - 1):
        for chosen_tuple in combinations(rotation, size):
            chosen = frozenset(chosen_tuple)
            other = frozenset(neighbours - chosen)
            key = tuple(sorted((tuple(sorted(chosen)), tuple(sorted(other)))))
            if key in seen:
                continue
            seen.add(key)
            is_conforming = contiguous(chosen, rotation)
            if is_conforming != conforming:
                continue
            if along is not None:
                face_neighbours = tuple(set(along) - {vertex})
                assert len(face_neighbours) == 2
                if (face_neighbours[0] in chosen) == (face_neighbours[1] in chosen):
                    continue
            output.append((chosen, other))
    return output


def one_split(vertex, partition):
    """Return a vertex split and its original-label fibres."""
    first, second = partition
    clones = (f"{vertex}0", f"{vertex}1")
    vertices = tuple(x for x in VERTICES if x != vertex) + clones
    edges = {e for e in EDGES if vertex not in e}
    edges.add(edge(*clones))
    for neighbour in first:
        edges.add(edge(clones[0], neighbour))
    for neighbour in second:
        edges.add(edge(clones[1], neighbour))
    fibres = {x: {x} for x in VERTICES if x != vertex}
    fibres[vertex] = set(clones)
    return vertices, edges, fibres


def double_split(u, upart, v, vpart):
    """Construct the type-5 split, naming clone 0 as the old-edge clone."""
    ua, ub = upart
    va, vb = vpart
    if v not in ua:
        ua, ub = ub, ua
    if u not in va:
        va, vb = vb, va
    uc = (f"{u}0", f"{u}1")
    vc = (f"{v}0", f"{v}1")
    vertices = tuple(x for x in VERTICES if x not in (u, v)) + uc + vc
    edges = {e for e in EDGES if u not in e and v not in e}
    edges |= {edge(*uc), edge(*vc), edge(uc[0], vc[0]), edge(uc[1], vc[1])}
    for neighbour in ua - {v}:
        edges.add(edge(uc[0], neighbour))
    for neighbour in ub - {v}:
        edges.add(edge(uc[1], neighbour))
    for neighbour in va - {u}:
        edges.add(edge(vc[0], neighbour))
    for neighbour in vb - {u}:
        edges.add(edge(vc[1], neighbour))
    fibres = {x: {x} for x in VERTICES if x not in (u, v)}
    fibres[u] = set(uc)
    fibres[v] = set(vc)
    return vertices, edges, fibres


def anchored_k5(vertices, edges, fibres, require_whole_fibres=False):
    """Return a K5 model whose bags have an SDR of old labels, if one exists."""
    n = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    adjacency = [0] * n
    for u, v in edges:
        i, j = index[u], index[v]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i

    connected = []
    external = {}
    label_masks = {}
    for mask in range(1, 1 << n):
        reached = mask & -mask
        while True:
            enlarged = reached
            work = reached
            while work:
                bit = work & -work
                work -= bit
                enlarged |= adjacency[bit.bit_length() - 1] & mask
            if enlarged == reached:
                break
            reached = enlarged
        if reached != mask:
            continue
        connected.append(mask)
        neighbours = 0
        work = mask
        while work:
            bit = work & -work
            work -= bit
            neighbours |= adjacency[bit.bit_length() - 1]
        external[mask] = neighbours
        label_masks[mask] = set()
        for label, fibre in fibres.items():
            membership = [bool(mask & (1 << index[v])) for v in fibre]
            if (
                all(membership)
                if require_whole_fibres
                else any(membership)
            ):
                label_masks[mask].add(label)

    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def has_sdr(bags, position=0, used=frozenset()):
        if position == len(bags):
            return True
        for label in label_masks[bags[position]] - used:
            if has_sdr(bags, position + 1, used | {label}):
                return True
        return False

    def extend(chosen, start):
        if len(chosen) == 5:
            return tuple(chosen) if has_sdr(chosen) else None
        for position in range(start, len(connected)):
            mask = connected[position]
            if any(mask & old for old in chosen):
                continue
            if any(not (external[mask] & old) for old in chosen):
                continue
            answer = extend(chosen + [mask], position + 1)
            if answer is not None:
                return answer
        return None

    return extend([], 0)


def incident_faces(u, v):
    return [face for face in FACES if u in face and v in face]


def main():
    # Type 1: every nonconfluent pair.  In the triangulation this is every
    # nonedge, because two distinct vertices are confluent iff adjacent.
    type1 = []
    for u, v in combinations(VERTICES, 2):
        if edge(u, v) in EDGES:
            continue
        graph = (VERTICES, EDGES | {edge(u, v)}, {x: {x} for x in VERTICES})
        type1.append((u, v, anchored_k5(*graph, require_whole_fibres=True) is not None))
    assert type1 and all(item[-1] for item in type1)

    type3 = []
    for vertex in VERTICES:
        for partition in split_partitions(vertex, conforming=False):
            type3.append(
                (
                    vertex,
                    partition,
                    anchored_k5(
                        *one_split(vertex, partition), require_whole_fibres=True
                    )
                    is not None,
                )
            )
    assert type3 and all(item[-1] for item in type3)

    type5 = []
    for u, v in EDGES:
        faces = incident_faces(u, v)
        assert len(faces) == 2
        for first, second in (faces, faces[::-1]):
            for upart in split_partitions(u, conforming=True, along=first):
                for vpart in split_partitions(v, conforming=True, along=second):
                    graph = double_split(u, upart, v, vpart)
                    type5.append(
                        (
                            u,
                            v,
                            first,
                            second,
                            upart,
                            vpart,
                            anchored_k5(*graph) is not None,
                            anchored_k5(
                                *graph, require_whole_fibres=True
                            )
                            is not None,
                        )
                    )
    assert type5 and all(item[-2] for item in type5)
    type5_failures = [item for item in type5 if not item[-1]]

    print(
        "PB Hegde-Thomas enlargement probe:",
        f"type1={len(type1)}",
        "type2=0",
        f"type3={len(type3)}",
        "type4=0",
        f"type5={len(type5)}",
        "type6=0",
        "type7=0",
        f"type5_whole-label_failures={len(type5_failures)}",
    )
    if type5_failures:
        kinds = Counter(
            tuple(sorted("pole" if x in POLES else "rim" for x in item[:2]))
            for item in type5_failures
        )
        print("type-5 whole-label failure kinds:", dict(kinds))
        print("first type-5 whole-label failure:", type5_failures[0][:-2])


if __name__ == "__main__":
    main()
