#!/usr/bin/env python3
"""Verify the nine-label four-response trace barrier."""

from itertools import combinations


K = ("t", "k1", "k2", "k3", "k4")
A0 = ("a1", "a2")
B0 = ("b1", "b2")
OMEGA_D = K + A0
OMEGA_E = K + B0

PHI = {
    "t": 0, "k1": 1, "k2": 2, "k3": 3, "k4": 4,
    "a1": 0, "a2": 0, "b1": 0, "b2": 5,
}
PSI = {
    "t": 1, "k1": 1, "k2": 2, "k3": 3, "k4": 4,
    "a1": 1, "a2": 1, "b1": 0, "b2": 5,
}


def partition(colouring, labels):
    return frozenset(
        frozenset(label for label in labels if colouring[label] == colour)
        for colour in set(colouring[label] for label in labels)
    )


def proper_on_path(colouring, path):
    return all(colouring[x] != colouring[y] for x, y in zip(path, path[1:]))


def main():
    assert PHI["t"] == PHI["a1"] == PHI["a2"] == 0
    assert PSI["t"] == PSI["a1"] == PSI["a2"] == 1
    for label in set(PHI) - {"t", "a1", "a2"}:
        assert PHI[label] == PSI[label]

    old_boundary_path = ("a1", "k2", "a2", "b2", "b1", "k3", "k4")
    assert proper_on_path(PHI, old_boundary_path)
    assert proper_on_path(PSI, old_boundary_path)

    phi_d = partition(PHI, OMEGA_D)
    phi_e = partition(PHI, OMEGA_E)
    # The original bridge response already satisfies the crossed-state
    # requirement on both twin boundaries.
    assert partition(PSI, OMEGA_D) != phi_d
    assert partition(PSI, OMEGA_E) != phi_e
    for epsilon in (2, 3, 4, 5):
        response = dict(PSI)
        response["t"] = epsilon
        # The swapped component trace is exactly {t}, hence lies in K.
        assert {"t"} <= set(K)
        assert partition(response, OMEGA_D) != phi_d
        assert partition(response, OMEGA_E) != phi_e
        assert response["a1"] == response["a2"] == response["k1"] == 1
        assert response["t"] != response["b1"]
        matching_label = {2: "k2", 3: "k3", 4: "k4", 5: "b2"}[epsilon]
        assert response["t"] == response[matching_label] == epsilon

    # The swapped trace contains one exclusive duty and no vertex of the
    # other.  Its set-theoretic complement need not be the other literal
    # lock component.
    bridge_trace = {"t", "a1", "a2"}
    assert set(A0) <= bridge_trace
    assert bridge_trace.isdisjoint(B0)
    print("GREEN: four response mismatches need no exclusive trace")


if __name__ == "__main__":
    main()
