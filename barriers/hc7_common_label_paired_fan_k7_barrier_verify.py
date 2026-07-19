#!/usr/bin/env python3
"""Verify the exact common-label paired-fan stress test."""

from contextlib import redirect_stdout
from io import StringIO
from itertools import combinations
from pathlib import Path
import runpy


BASE = Path(__file__).with_name(
    "hc7_order_eight_selected_kempe_fan_barrier_verify.py"
)
with redirect_stdout(StringIO()):
    DATA = runpy.run_path(str(BASE))

V = set(DATA["VERTICES"])
ADJ = DATA["ADJ"]
S = {"p", "q", "t", "d", "u0", "w0", "u2", "w2"}
C = {"u3", "u4", "w3", "w4"}
C_OPP = {"u1", "w1"}


def adjacent_sets(left, right):
    return any(y in ADJ[x] for x in left for y in right)


def proper(host, colouring, deleted=()):
    host = set(host)
    deleted = {frozenset(edge) for edge in deleted}
    assert set(colouring) == host
    return all(
        colouring[x] != colouring[y]
        for x in host
        for y in ADJ[x] & host
        if x < y and frozenset((x, y)) not in deleted
    )


def connected(vertices):
    return DATA["connected"](set(vertices))


def boundary_full(component):
    return all(ADJ[s] & component for s in S)


BAGS = {
    "U": {"t", "u2", "u3", "u4", "w3", "w4"},
    "X": {"d"},
    "Y": {"u0", "u1"},
    "D": {"p"},
    "F1": {"q"},
    "F2": {"w0"},
    "F3": {"w1", "w2"},
}

assert set().union(*BAGS.values()) == V
assert sum(map(len, BAGS.values())) == len(V)
assert all(connected(bag) for bag in BAGS.values())
for left, right in combinations(BAGS, 2):
    expected = {left, right} != {"X", "Y"}
    assert adjacent_sets(BAGS[left], BAGS[right]) == expected

assert set(DATA["components"](V - S)) == {frozenset(C), frozenset(C_OPP)}
assert boundary_full(C) and boundary_full(C_OPP)

boundary_labels = {
    "t": "U",
    "u2": "U",
    "d": "X",
    "u0": "Y",
    "p": "D",
    "q": "F1",
    "w0": "F2",
    "w2": "F3",
}
assert set(boundary_labels) == S
assert all(vertex in BAGS[label] for vertex, label in boundary_labels.items())
assert C <= BAGS["U"]
assert connected(BAGS["U"] - C)
assert adjacent_sets(BAGS["U"] - C, C)

P = ("u3", "u4", "w4")
fan = (
    ("u4", "t"),
    ("u4", "p"),
    ("u4", "q"),
    ("w4", "w0"),
    ("u3", "w2"),
)
terminals = {path[-1] for path in fan}
assert terminals == {"t", "p", "q", "w0", "w2"}
assert all(y in ADJ[x] for path in fan for x, y in zip(path, path[1:]))
assert all((set(path) - set(P)) == {path[-1]} for path in fan)
assert all(
    not (set(left) - set(P)) & (set(right) - set(P))
    for left, right in combinations(fan, 2)
)

E = ("u3", "w2")
F = ("w4", "w0")
ico_colours = {
    "EE": (0, 1, 1, 2, 1, 3, 2, 3, 0, 3, 0, 3),
    "EP": (0, 0, 1, 2, 3, 2, 3, 3, 1, 2, 1, 2),
    "PE": (0, 1, 1, 2, 1, 3, 2, 3, 0, 2, 0, 3),
    "PP": (0, 1, 1, 2, 1, 2, 3, 3, 0, 3, 0, 2),
}
ico_order = ("t", "d", "u0", "u1", "u2", "u3", "u4",
             "w0", "w1", "w2", "w3", "w4")
colourings = {}
for signature, values in ico_colours.items():
    colouring = dict(zip(ico_order, values))
    colouring.update({"p": 4, "q": 5})
    deleted = []
    if signature[0] == "E":
        deleted.append(E)
    if signature[1] == "E":
        deleted.append(F)
    assert proper(V, colouring, deleted)
    assert (colouring[E[0]] == colouring[E[1]]) == (signature[0] == "E")
    assert (colouring[F[0]] == colouring[F[1]]) == (signature[1] == "E")
    colourings[signature] = colouring

Q = {"d", "p", "q", "u1", "u2", "w0", "w2"}
assert set(DATA["components"](V - Q)) == {
    frozenset({"w1"}),
    frozenset({"t", "u0", "u3", "u4", "w3", "w4"}),
}

extensions = {
    "EE": {
        "d": 0, "p": 1, "q": 2, "u1": 3, "u2": 0,
        "w0": 4, "w2": 4, "w3": 5, "w4": 3, "u4": 0,
        "t": 4, "u0": 5, "u3": 3, "w1": 5,
    },
    "EP": {
        "d": 0, "p": 1, "q": 2, "u1": 3, "u2": 4,
        "w0": 4, "w2": 3, "w3": 4, "w4": 5, "u4": 3,
        "t": 5, "u0": 0, "u3": 0, "w1": 5,
    },
    "PE": {
        "d": 0, "p": 1, "q": 2, "u1": 3, "u2": 0,
        "w0": 4, "w2": 3, "w3": 4, "w4": 3, "u4": 0,
        "t": 4, "u0": 5, "u3": 5, "w1": 5,
    },
}
for signature, extension in extensions.items():
    assert proper(V, extension)
    response = colourings[signature]
    for left, right in combinations(sorted(Q), 2):
        assert (extension[left] == extension[right]) == (
            response[left] == response[right]
        )

print(
    "GREEN paired-fan stress test: exact labels, five direct limbs, "
    "EE/EP/PE/PP responses and compatible order-seven boundary verified"
)
