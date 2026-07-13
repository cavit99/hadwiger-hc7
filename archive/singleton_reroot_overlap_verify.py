#!/usr/bin/env python3
"""Dependency-free checks for the singleton re-root overlap note.

The script checks only finite quotient statements:

* the optional-edge K4 certificates;
* the fixed two-Moser overlap has the displayed K6 model but no K7 model;
* the cross-saturated 5--6 split has the displayed K7 model; and
* the exceptional atlas graph M+13 has the degree/neighbourhood invariant
  used in the hand proof.
"""

from itertools import combinations


def edge(a, b):
    return frozenset((a, b))


def adjacent_sets(edges, left, right):
    return any(edge(x, y) in edges for x in left for y in right)


def connected(edges, vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    seen = {next(iter(vertices))}
    todo = list(seen)
    while todo:
        x = todo.pop()
        for y in vertices - seen:
            if edge(x, y) in edges:
                seen.add(y)
                todo.append(y)
    return seen == vertices


def is_model(edges, bags):
    return (
        all(bags[i].isdisjoint(bags[j])
            for i, j in combinations(range(len(bags)), 2))
        and all(connected(edges, bag) for bag in bags)
        and all(adjacent_sets(edges, bags[i], bags[j])
                for i, j in combinations(range(len(bags)), 2))
    )


def partitions(sequence, number):
    """Yield every partition of sequence into number nonempty blocks."""
    blocks = []

    def visit(position):
        if position == len(sequence):
            if len(blocks) == number:
                yield tuple(frozenset(block) for block in blocks)
            return
        item = sequence[position]
        for block in blocks:
            block.append(item)
            yield from visit(position + 1)
            block.pop()
        if len(blocks) < number:
            blocks.append([item])
            yield from visit(position + 1)
            blocks.pop()

    yield from visit(0)


def has_minor(vertices, edges, order):
    for used_order in range(order, len(vertices) + 1):
        for used in combinations(vertices, used_order):
            for bags in partitions(used, order):
                if is_model(edges, bags):
                    return True, bags
    return False, None


def moser_edges(center="v", outer=("p", "q")):
    p, q = outer
    return {
        edge(center, x) for x in ("1", "2", "3", "4")
    } | {
        edge("1", "2"), edge("3", "4"), edge(p, q),
        edge(p, "3"), edge(p, "4"), edge(q, "1"), edge(q, "2"),
    }


def main():
    # New neighbourhood J=N(0), in the crossed-frame labels.
    j_edges = moser_edges()
    assert is_model(
        j_edges | {edge("p", "2")},
        tuple(map(frozenset, (("v", "2"), ("3",), ("4",), ("p",)))),
    )
    assert edge("1", "q") in j_edges
    assert is_model(
        j_edges | {edge("q", "4")},
        tuple(map(frozenset, (("v", "4"), ("1",), ("2",), ("q",)))),
    )
    assert edge("3", "p") in j_edges

    # The fixed overlap of the old and new pure Moser frames.
    overlap_vertices = ("0", "v", "1", "2", "3", "4", "5", "6", "p", "q")
    overlap_edges = set(j_edges)
    overlap_edges |= {edge("0", x) for x in ("v", "1", "2", "3", "4", "p", "q")}
    overlap_edges |= {edge("v", x) for x in ("5", "6")}
    overlap_edges |= {
        edge("1", "6"), edge("2", "6"), edge("3", "5"),
        edge("4", "5"), edge("5", "6"),
    }
    fixed_k6 = tuple(map(frozenset, (
        ("0",), ("v",), ("1",), ("2",), ("3", "5", "6"),
        ("4", "p", "q"),
    )))
    assert is_model(overlap_edges, fixed_k6)
    assert not has_minor(overlap_vertices, overlap_edges, 7)[0]

    # Quotient of a cross-saturated split of the common exterior.
    split_edges = set(j_edges)
    split_edges |= {edge("0", x) for x in ("v", "1", "2", "3", "4", "p", "q")}
    split_edges.add(edge("A", "B"))
    for shore in ("A", "B"):
        split_edges.add(edge(shore, "v"))
        for x in ("1", "2", "3", "4"):
            split_edges.add(edge(shore, x))
    split_k7 = tuple(map(frozenset, (
        ("A",), ("B",), ("0", "1"), ("v",), ("2", "p", "q"),
        ("3",), ("4",),
    )))
    assert is_model(split_edges, split_k7)

    # M+13: every degree-four vertex has three induced neighbour edges.
    standard_moser = {
        edge("c", x) for x in ("1", "2", "3", "4")
    } | {
        edge("1", "2"), edge("1", "6"), edge("2", "6"),
        edge("3", "4"), edge("3", "5"), edge("4", "5"),
        edge("5", "6"),
    }
    m_plus = standard_moser | {edge("1", "3")}
    vertices = ("c", "1", "2", "3", "4", "5", "6")
    degrees = {x: sum(edge(x, y) in m_plus for y in vertices if y != x)
               for x in vertices}
    degree_four = {x for x in vertices if degrees[x] == 4}
    assert degree_four == {"c", "1", "3"}
    for x in degree_four:
        neighbours = {y for y in vertices if edge(x, y) in m_plus}
        induced_edges = sum(edge(a, b) in m_plus
                            for a, b in combinations(neighbours, 2))
        assert induced_edges == 3

    print("optional-edge K4 certificates: verified")
    print("fixed overlap: K6 verified and K7 exhaustively absent")
    print("cross-saturated split: K7 certificate verified")
    print("M+13 degree/neighbourhood invariant: verified")


if __name__ == "__main__":
    main()
