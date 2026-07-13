#!/usr/bin/env python3
"""Exhaustive small-order test for three portal-class synchronization.

For every labelled 2-connected graph through five vertices, enumerate
triples of proper portal subsets of order at least two.  Distinguish:

* failure of Property B (no set bipartition splits all three classes);
* a connectivity-only failure (a set split exists, but no split has both
  induced sides connected).

The script is a falsification aid, not part of a proof.
"""

from itertools import combinations_with_replacement


def connected(adj: list[int], mask: int) -> bool:
    if mask == 0:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier ^= bit
        vertex = bit.bit_length() - 1
        new = adj[vertex] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def two_connected(adj: list[int]) -> bool:
    n = len(adj)
    full = (1 << n) - 1
    return connected(adj, full) and all(
        connected(adj, full ^ (1 << vertex)) for vertex in range(n)
    )


def graph_from_mask(n: int, graph_mask: int) -> tuple[list[int], list[tuple[int, int]]]:
    adj = [0] * n
    edges: list[tuple[int, int]] = []
    bit = 0
    for left in range(n):
        for right in range(left + 1, n):
            if graph_mask & (1 << bit):
                adj[left] |= 1 << right
                adj[right] |= 1 << left
                edges.append((left, right))
            bit += 1
    return adj, edges


def cut_signature(portal: int, cuts: list[int], full: int) -> int:
    signature = 0
    for index, side in enumerate(cuts):
        if portal & side and portal & (full ^ side):
            signature |= 1 << index
    return signature


def vertices(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(mask.bit_length()) if mask & (1 << index))


def host_with_singleton_triangle(adj: list[int], triple: tuple[int, int, int]) -> list[int]:
    """Add a singleton K3, with its three portal classes equal to triple."""
    n = len(adj)
    host = list(adj) + [0, 0, 0]
    for singleton in range(3):
        vertex = n + singleton
        for other in range(3):
            if other != singleton:
                host[vertex] |= 1 << (n + other)
        portal = triple[singleton]
        host[vertex] |= portal
        for old in range(n):
            if portal & (1 << old):
                host[old] |= 1 << vertex
    return host


def k_connected(adj: list[int], k: int) -> bool:
    """Brute-force vertex-connectivity test, adequate through eight vertices."""
    n = len(adj)
    full = (1 << n) - 1
    if not connected(adj, full):
        return False
    from itertools import combinations

    for order in range(k):
        for removed_tuple in combinations(range(n), order):
            removed = sum(1 << vertex for vertex in removed_tuple)
            remaining = full ^ removed
            if remaining and not connected(adj, remaining):
                return False
    return True


def find_clique_minor(adj: list[int], order: int) -> tuple[int, ...] | None:
    """Return an exact small-graph branch-set model, if one exists."""
    n = len(adj)
    full = (1 << n) - 1
    connected_sets = [mask for mask in range(1, full + 1) if connected(adj, mask)]
    neighbourhood = {}
    for mask in connected_sets:
        neighbours = 0
        for vertex in range(n):
            if mask & (1 << vertex):
                neighbours |= adj[vertex]
        neighbourhood[mask] = neighbours & (full ^ mask)

    def search(
        chosen: tuple[int, ...], used: int, start: int
    ) -> tuple[int, ...] | None:
        if len(chosen) == order:
            return chosen
        if (full ^ used).bit_count() < order - len(chosen):
            return None
        for index in range(start, len(connected_sets)):
            candidate = connected_sets[index]
            if candidate & used:
                continue
            if any(not (neighbourhood[candidate] & old) for old in chosen):
                continue
            result = search(chosen + (candidate,), used | candidate, index + 1)
            if result is not None:
                return result
        return None

    return search((), 0, 0)


def has_clique_minor(adj: list[int], order: int) -> bool:
    return find_clique_minor(adj, order) is not None


def k_colourable(adj: list[int], colours: int) -> bool:
    n = len(adj)
    assignment = [-1] * n
    order = sorted(range(n), key=lambda vertex: adj[vertex].bit_count(), reverse=True)

    def search(position: int) -> bool:
        if position == n:
            return True
        vertex = order[position]
        forbidden = {
            assignment[other]
            for other in range(n)
            if (adj[vertex] & (1 << other)) and assignment[other] >= 0
        }
        for colour in range(colours):
            if colour in forbidden:
                continue
            assignment[vertex] = colour
            if search(position + 1):
                return True
        assignment[vertex] = -1
        return False

    return search(0)


def main() -> None:
    first_connectivity_only = None
    first_non_property_b = None
    first_host4_connectivity_only = None
    first_host4_non_property_b = None
    first_target_free_connectivity_only = None
    first_target_free_non_property_b = None
    counts = {
        "graphs": 0,
        "triples": 0,
        "connectivity_only": 0,
        "non_property_b": 0,
        "host4_connectivity_only": 0,
        "host4_non_property_b": 0,
        "target_free_connectivity_only": 0,
        "target_free_non_property_b": 0,
    }

    for n in range(3, 6):
        full = (1 << n) - 1
        edge_count = n * (n - 1) // 2
        portals = [
            mask
            for mask in range(1, full)
            if mask.bit_count() >= 2
        ]
        all_cuts = [mask for mask in range(1, full) if mask & 1]

        for graph_mask in range(1 << edge_count):
            adj, edges = graph_from_mask(n, graph_mask)
            if not two_connected(adj):
                continue
            counts["graphs"] += 1
            connected_cuts = [
                mask
                for mask in all_cuts
                if connected(adj, mask) and connected(adj, full ^ mask)
            ]
            arbitrary_signatures = {
                portal: cut_signature(portal, all_cuts, full) for portal in portals
            }
            connected_signatures = {
                portal: cut_signature(portal, connected_cuts, full) for portal in portals
            }

            for triple in combinations_with_replacement(portals, 3):
                counts["triples"] += 1
                arbitrary = (
                    arbitrary_signatures[triple[0]]
                    & arbitrary_signatures[triple[1]]
                    & arbitrary_signatures[triple[2]]
                )
                linked = (
                    connected_signatures[triple[0]]
                    & connected_signatures[triple[1]]
                    & connected_signatures[triple[2]]
                )
                if linked:
                    continue
                record = {
                    "n": n,
                    "edges": edges,
                    "portals": tuple(vertices(mask) for mask in triple),
                }
                host4 = k_connected(host_with_singleton_triangle(adj, triple), 4)
                target_free = False
                if host4:
                    target_free = not has_clique_minor(
                        host_with_singleton_triangle(adj, triple), 5
                    )
                if not arbitrary:
                    counts["non_property_b"] += 1
                    if first_non_property_b is None:
                        first_non_property_b = record
                    if host4:
                        counts["host4_non_property_b"] += 1
                        if first_host4_non_property_b is None:
                            first_host4_non_property_b = record
                    if target_free:
                        counts["target_free_non_property_b"] += 1
                        if first_target_free_non_property_b is None:
                            first_target_free_non_property_b = record
                else:
                    counts["connectivity_only"] += 1
                    if first_connectivity_only is None:
                        first_connectivity_only = record
                    if host4:
                        counts["host4_connectivity_only"] += 1
                        if first_host4_connectivity_only is None:
                            first_host4_connectivity_only = record
                    if target_free:
                        counts["target_free_connectivity_only"] += 1
                        if first_target_free_connectivity_only is None:
                            first_target_free_connectivity_only = record

    print("PASS: exhaustive labelled search completed for n <= 5")
    print(counts)
    print("first non-Property-B obstruction:", first_non_property_b)
    print("first connectivity-only obstruction:", first_connectivity_only)
    print("first 4-connected-host non-Property-B obstruction:", first_host4_non_property_b)
    print("first 4-connected-host connectivity-only obstruction:", first_host4_connectivity_only)
    print("first target-free non-Property-B obstruction:", first_target_free_non_property_b)
    print("first target-free connectivity-only obstruction:", first_target_free_connectivity_only)

    # Dynamic diamond test: add an apex v adjacent to singleton vertices
    # b1,b2, but not b3, and vary its nonempty foot set in the old diamond.
    # The selected p3 expansion lists are uncolourable whenever 0 is a foot,
    # although some such static states still belong to a 4-colourable graph.
    diamond = [
        (1 << 1) | (1 << 2) | (1 << 3),
        (1 << 0) | (1 << 2) | (1 << 3),
        (1 << 0) | (1 << 1),
        (1 << 0) | (1 << 1),
    ]
    diamond_host = host_with_singleton_triangle(diamond, (0b0101, 0b1001, 0b1110))
    for feet in range(1, 1 << 4):
        apex = len(diamond_host)
        dynamic = list(diamond_host) + [0]
        for neighbour in (4, 5):
            dynamic[apex] |= 1 << neighbour
            dynamic[neighbour] |= 1 << apex
        for old in range(4):
            if feet & (1 << old):
                dynamic[apex] |= 1 << old
                dynamic[old] |= 1 << apex
        model = find_clique_minor(dynamic, 5)
        print(
            "dynamic diamond feet",
            vertices(feet),
            "4-colourable=",
            k_colourable(dynamic, 4),
            "K5 model=",
            None if model is None else tuple(vertices(branch) for branch in model),
        )


if __name__ == "__main__":
    main()
