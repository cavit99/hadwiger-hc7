#!/usr/bin/env python3
"""Verify the multicoloured-boundary-carrier response barrier.

The program is dependency-free.  It checks the labelled near-K7 model,
the exact order-seven separation, the displayed colourings, and exhaustively
enumerates the relevant six-colourings up to global palette permutation.
"""

from __future__ import annotations

from itertools import combinations


P, Q, TOP, BOTTOM = "p", "q", "t", "b"
UPPER = tuple(f"u{i}" for i in range(5))
LOWER = tuple(f"w{i}" for i in range(5))
BASE = (TOP, BOTTOM) + UPPER + LOWER
VERTICES = frozenset((P, Q) + BASE)
Z = "w3"


def edge(x: str, y: str) -> tuple[str, str]:
    return tuple(sorted((x, y)))


EDGES: set[tuple[str, str]] = set()
for i in range(5):
    EDGES.update(
        {
            edge(TOP, UPPER[i]),
            edge(BOTTOM, LOWER[i]),
            edge(UPPER[i], UPPER[(i + 1) % 5]),
            edge(LOWER[i], LOWER[(i + 1) % 5]),
            edge(UPPER[i], LOWER[i]),
            edge(UPPER[i], LOWER[(i - 1) % 5]),
        }
    )
for apex in (P, Q):
    for vertex in BASE:
        EDGES.add(edge(apex, vertex))
EDGES.add(edge(P, Q))


A = frozenset({"u3"})
D = frozenset({"u1", "w1"})
U = frozenset({P, "u4", "w3", "w4"})
V1 = frozenset({TOP, "u0"})
V2 = frozenset({"u2"})
V3 = frozenset({BOTTOM, "w0", "w2"})
V4 = frozenset({Q})
MODEL = (A, D, U, V1, V2, V3, V4)

SPLIT_Z = frozenset({Z})
SPLIT_W = frozenset({P, "u4", "w4"})
BOUNDARY = frozenset({BOTTOM, P, Q, "u3", "u4", "w2", "w4"})
MERGED_ROWS = (D | SPLIT_W, V1, V2, V3, V4)


def adjacency(
    vertices: frozenset[str], edges: set[tuple[str, str]]
) -> dict[str, set[str]]:
    result = {vertex: set() for vertex in vertices}
    for x, y in edges:
        result[x].add(y)
        result[y].add(x)
    return result


ADJACENCY = adjacency(VERTICES, EDGES)


def connected(
    vertices: frozenset[str], edges: set[tuple[str, str]] = EDGES
) -> bool:
    if not vertices:
        return False
    adjacent = adjacency(frozenset(set().union(*edges)), edges)
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        vertex = todo.pop()
        for neighbour in adjacent[vertex] & set(vertices) - seen:
            seen.add(neighbour)
            todo.append(neighbour)
    return seen == set(vertices)


def touch(left: frozenset[str], right: frozenset[str]) -> bool:
    return any(edge(x, y) in EDGES for x in left for y in right)


def components(vertices: frozenset[str]) -> list[frozenset[str]]:
    unseen = set(vertices)
    result: list[frozenset[str]] = []
    while unseen:
        start = next(iter(unseen))
        seen = {start}
        todo = [start]
        while todo:
            vertex = todo.pop()
            for neighbour in ADJACENCY[vertex] & unseen - seen:
                seen.add(neighbour)
                todo.append(neighbour)
        unseen -= seen
        result.append(frozenset(seen))
    return result


def verify_host_and_model() -> None:
    # Seven-connectivity, with BOUNDARY as a cut of order seven.
    for order in range(7):
        for deleted in combinations(VERTICES, order):
            assert connected(VERTICES - frozenset(deleted))
    assert len(BOUNDARY) == 7
    outside = VERTICES - BOUNDARY
    outside_components = components(outside)
    assert sorted(map(len, outside_components)) == [1, 6]
    assert SPLIT_Z in outside_components
    for component in outside_components:
        assert all(touch(component, frozenset({vertex})) for vertex in BOUNDARY)

    # A spanning K7-minus-one-edge model, missing only A--D.
    assert frozenset().union(*MODEL) == VERTICES
    assert sum(map(len, MODEL)) == len(VERTICES)
    assert all(connected(part) for part in MODEL)
    for i, left in enumerate(MODEL):
        for j, right in enumerate(MODEL[i + 1 :], i + 1):
            if {i, j} == {0, 1}:
                assert not touch(left, right)
            else:
                assert touch(left, right)

    assert U == SPLIT_Z | SPLIT_W
    assert touch(SPLIT_Z, SPLIT_W)
    assert touch(A, SPLIT_Z) and touch(A, SPLIT_W)
    assert not touch(SPLIT_Z, D)
    assert BOUNDARY == frozenset(ADJACENCY[Z])

    assert all(connected(row) for row in MERGED_ROWS)
    assert all(
        touch(MERGED_ROWS[i], MERGED_ROWS[j])
        for i in range(5)
        for j in range(i + 1, 5)
    )
    assert all(touch(A, row) for row in MERGED_ROWS)
    assert frozenset().union(*(row & BOUNDARY for row in MERGED_ROWS)) == (
        BOUNDARY - A
    )
    assert MERGED_ROWS[0] & BOUNDARY == frozenset({P, "u4", "w4"})
    assert all(
        edge(x, y) in EDGES
        for x, y in combinations(MERGED_ROWS[0] & BOUNDARY, 2)
    )


def valid_colouring(
    colouring: dict[str, int],
    vertices: frozenset[str],
    edges: set[tuple[str, str]],
) -> bool:
    return set(colouring) == set(vertices) and all(
        colouring[x] != colouring[y] for x, y in edges
    )


def contracted_graph(
    first: str, second: str
) -> tuple[
    frozenset[str],
    set[tuple[str, str]],
    dict[str, str],
]:
    image = f"<{first}{second}>"
    vertices = (VERTICES - {first, second}) | {image}
    edges: set[tuple[str, str]] = set()
    for x, y in EDGES:
        x_image = image if x in {first, second} else x
        y_image = image if y in {first, second} else y
        if x_image != y_image:
            edges.add(edge(x_image, y_image))
    mapping = {
        vertex: image if vertex in {first, second} else vertex
        for vertex in VERTICES
    }
    return frozenset(vertices), edges, mapping


def contracted_vertex_set(
    part: frozenset[str], image: str
) -> tuple[frozenset[str], set[tuple[str, str]], dict[str, str]]:
    vertices = (VERTICES - part) | {image}
    edges: set[tuple[str, str]] = set()
    for x, y in EDGES:
        x_image = image if x in part else x
        y_image = image if y in part else y
        if x_image != y_image:
            edges.add(edge(x_image, y_image))
    mapping = {
        vertex: image if vertex in part else vertex for vertex in VERTICES
    }
    return frozenset(vertices), edges, mapping


def deleted_graph(
    vertex: str,
) -> tuple[frozenset[str], set[tuple[str, str]], dict[str, str]]:
    vertices = VERTICES - {vertex}
    edges = {pair for pair in EDGES if vertex not in pair}
    return frozenset(vertices), edges, {v: v for v in vertices}


def canonical_colourings(
    vertices: frozenset[str],
    edges: set[tuple[str, str]],
    colour_limit: int = 6,
) -> list[dict[str, int]]:
    """Enumerate colourings once each up to a global palette permutation."""

    adjacent = adjacency(vertices, edges)
    colouring: dict[str, int] = {}
    output: list[dict[str, int]] = []

    def search() -> None:
        if len(colouring) == len(vertices):
            output.append(dict(colouring))
            return

        uncoloured = [vertex for vertex in vertices if vertex not in colouring]
        vertex = max(
            uncoloured,
            key=lambda item: (
                len({colouring[n] for n in adjacent[item] if n in colouring}),
                len(adjacent[item]),
                item,
            ),
        )
        forbidden = {
            colouring[neighbour]
            for neighbour in adjacent[vertex]
            if neighbour in colouring
        }
        used = set(colouring.values())
        # A new colour is introduced only as the next integer.  This is the
        # standard restricted-growth-string representative of a palette orbit.
        for colour in range(min(colour_limit - 1, len(used)) + 1):
            if colour in forbidden:
                continue
            if colour not in used and colour != len(used):
                continue
            colouring[vertex] = colour
            search()
            del colouring[vertex]

    search()
    return output


def boundary_partition(
    colouring: dict[str, int], mapping: dict[str, str]
) -> tuple[tuple[str, ...], ...]:
    blocks: dict[int, list[str]] = {}
    for vertex in BOUNDARY:
        blocks.setdefault(colouring[mapping[vertex]], []).append(vertex)
    return tuple(sorted(tuple(sorted(block)) for block in blocks.values()))


def saturated_endpoint(
    colouring: dict[str, int],
    mapping: dict[str, str],
    endpoint: str,
    mate: str,
) -> bool:
    alpha = colouring[mapping[endpoint]]
    neighbour_colours = {
        colouring[mapping[neighbour]]
        for neighbour in ADJACENCY[endpoint] - {mate}
    }
    return set(range(6)) - {alpha} <= neighbour_colours


def census(
    graph: tuple[frozenset[str], set[tuple[str, str]], dict[str, str]],
    spoke: str | None = None,
) -> tuple[int, int, int, int, tuple[int, int, int] | None]:
    vertices, edges, mapping = graph
    colourings = canonical_colourings(vertices, edges)
    assert all(len(set(colouring.values())) == 6 for colouring in colourings)
    partitions = {
        boundary_partition(colouring, mapping) for colouring in colourings
    }
    all_six = [
        colouring
        for colouring in colourings
        if len({colouring[mapping[v]] for v in BOUNDARY}) == 6
    ]
    six_partitions = {
        boundary_partition(colouring, mapping) for colouring in all_six
    }

    # The fixed triangle makes the merged row multicoloured in every state.
    for colouring in colourings:
        assert len(
            {
                colouring[mapping[v]]
                for v in MERGED_ROWS[0] & BOUNDARY
            }
        ) == 3

    saturation = None
    if spoke is not None:
        both = only_z = only_spoke = 0
        for colouring in colourings:
            z_saturated = saturated_endpoint(colouring, mapping, Z, spoke)
            spoke_saturated = saturated_endpoint(
                colouring, mapping, spoke, Z
            )
            if z_saturated and spoke_saturated:
                both += 1
            elif z_saturated:
                only_z += 1
            elif spoke_saturated:
                only_spoke += 1
            else:
                raise AssertionError("a contraction response saturates neither end")
        saturation = both, only_z, only_spoke

    return (
        len(colourings),
        len(partitions),
        len(all_six),
        len(six_partitions),
        saturation,
    )


def verify_displayed_colourings() -> None:
    # A global six-colouring.  Its restriction to G-Z uses only five colours
    # on BOUNDARY, so the missing sixth colour extends to Z.
    global_colouring = {
        "w4": 0,
        "w3": 1,
        "u4": 2,
        "u3": 0,
        "w2": 2,
        BOTTOM: 3,
        "w1": 0,
        "w0": 1,
        "u0": 3,
        "u1": 2,
        TOP: 1,
        "u2": 3,
        P: 4,
        Q: 5,
    }
    assert valid_colouring(global_colouring, VERTICES, EDGES)
    assert len({global_colouring[v] for v in BOUNDARY}) == 5

    # The six-block trace displayed in Section 3.  It is the pullback from
    # the far shore of a colouring after contracting the path w2-w3-w4.
    far_response = {
        P: 0,
        Q: 1,
        TOP: 2,
        "u0": 3,
        "u1": 4,
        "u2": 5,
        "w0": 5,
        "w1": 3,
        BOTTOM: 2,
        "u3": 3,
        "u4": 5,
        "w2": 4,
        "w4": 4,
    }
    deleted_vertices, deleted_edges, _ = deleted_graph(Z)
    assert valid_colouring(far_response, deleted_vertices, deleted_edges)
    assert len({far_response[v] for v in BOUNDARY}) == 6
    repeated = {
        colour: {v for v in BOUNDARY if far_response[v] == colour}
        for colour in set(far_response.values())
    }
    assert {
        frozenset(block) for block in repeated.values() if len(block) > 1
    } == {frozenset({"w2", "w4"})}

    path = frozenset({"w2", Z, "w4"})
    quotient_vertices, quotient_edges, quotient_map = contracted_vertex_set(
        path, "<w2-w3-w4>"
    )
    quotient_colouring = {
        vertex: (
            4 if vertex == "<w2-w3-w4>" else far_response[vertex]
        )
        for vertex in quotient_vertices
    }
    assert valid_colouring(
        quotient_colouring, quotient_vertices, quotient_edges
    )
    assert all(quotient_map[v] == "<w2-w3-w4>" for v in path)

    # A fully endpoint-saturated response to contracting Z--BOTTOM.
    response = {
        BOTTOM: 2,
        P: 1,
        Q: 0,
        TOP: 5,
        "u0": 3,
        "u1": 2,
        "u2": 4,
        "u3": 3,
        "u4": 4,
        "w0": 4,
        "w1": 3,
        "w2": 5,
        Z: 2,
        "w4": 5,
    }
    deleted_edge_set = EDGES - {edge(Z, BOTTOM)}
    assert valid_colouring(response, VERTICES, deleted_edge_set)
    assert response[Z] == response[BOTTOM]
    assert len({response[v] for v in BOUNDARY}) == 6
    identity = {vertex: vertex for vertex in VERTICES}
    assert saturated_endpoint(response, identity, Z, BOTTOM)
    assert saturated_endpoint(response, identity, BOTTOM, Z)


def verify_census() -> None:
    assert census(deleted_graph(Z)) == (20, 10, 10, 5, None)

    for spoke in (P, Q):
        assert census(contracted_graph(Z, spoke), spoke) == (
            20,
            10,
            10,
            5,
            (10, 0, 10),
        )

    for spoke in (BOTTOM, "u3", "u4", "w2", "w4"):
        assert census(contracted_graph(Z, spoke), spoke) == (
            8,
            4,
            6,
            3,
            (4, 2, 2),
        )


if __name__ == "__main__":
    verify_host_and_model()
    verify_displayed_colourings()
    verify_census()
    print(
        "GREEN: exact-seven multicoloured-carrier barrier; "
        "all seven spoke contractions have saturated nonextendible responses"
    )
