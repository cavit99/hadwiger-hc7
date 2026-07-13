#!/usr/bin/env python3
"""Search for an atomic pair-mode that contradicts a 1-vs-2 owner split.

Normalize the minimum-fragment shore D to own only opposite frames 0 and 3;
the other shore H then owns frames 1,2,4,5.  Atomic three-block ownership
gives D a two-block packet for every perfect-matching mode on the six C6
roots.  For each possible D packet and each available H frame, this script
tests the literal four-helper boundary quotient for a K7 minor.  A mode for
which all three possible D packets are positive would eliminate the entire
atomic low-owner case by one reusable ownership argument.
"""

from __future__ import annotations

import itertools

import networkx as nx


def k_minor_model(graph: nx.Graph, k: int = 7):
    vertices = tuple(graph)
    n = len(vertices)
    index = {vertex: i for i, vertex in enumerate(vertices)}
    adjacency = [0] * n
    for u, v in graph.edges():
        i, j = index[u], index[v]
        adjacency[i] |= 1 << j
        adjacency[j] |= 1 << i
    neighbour_union = [0] * (1 << n)
    connected = []
    for mask in range(1, 1 << n):
        low = mask & -mask
        i = low.bit_length() - 1
        neighbour_union[mask] = neighbour_union[mask ^ low] | adjacency[i]
        reached = low
        while True:
            expanded = reached | (neighbour_union[reached] & mask)
            if expanded == reached:
                break
            reached = expanded
        if reached == mask:
            connected.append(mask)
    connected.sort(key=lambda mask: (mask.bit_count(), mask))

    def adjacent(a, b):
        return not a & b and bool(neighbour_union[a] & b)

    def search(chosen, candidates, used):
        if len(chosen) == k:
            return chosen
        needed = k - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [
                other
                for other in candidates[pos + 1 :]
                if not other & (used | bag) and adjacent(bag, other)
            ]
            if len(nxt) >= needed - 1:
                answer = search(chosen + [bag], nxt, used | bag)
                if answer is not None:
                    return answer
        return None

    return search([], connected, 0)


def perfect_matchings(vertices: tuple[int, ...]):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        remainder = vertices[1:index] + vertices[index + 1 :]
        for rest in perfect_matchings(remainder):
            yield (tuple(sorted((first, second))),) + rest


def frame_demands(frame: int):
    return (
        ((frame - 2) % 6, (frame - 1) % 6),
        ((frame + 2) % 6, (frame + 3) % 6),
    )


def quotient(d_packet, h_packet):
    # 0..5 are cycle roots, 6 is universal z; 7,8 are D pieces and
    # 9,10 are H pieces.
    graph = nx.Graph()
    graph.add_nodes_from(range(11))
    for u, v in itertools.combinations(range(6), 2):
        if (u - v) % 6 not in (1, 5):
            graph.add_edge(u, v)
    graph.add_edges_from((6, root) for root in range(6))
    graph.add_edge(7, 8)
    graph.add_edge(9, 10)
    for helper, demand in zip((7, 8), d_packet):
        graph.add_edges_from((helper, root) for root in demand)
    for helper, demand in zip((9, 10), h_packet):
        graph.add_edges_from((helper, root) for root in demand)
    return graph


def main() -> None:
    h_frames = (1, 2, 4, 5)
    positive = {}
    witnesses = {}
    quotient_cache = {}
    for mode in perfect_matchings(tuple(range(6))):
        packet_status = []
        for omitted in range(3):
            d_packet = tuple(mode[index] for index in range(3) if index != omitted)
            available = []
            for frame in h_frames:
                h_packet = frame_demands(frame)
                key = (tuple(sorted(d_packet)), frame)
                if key not in quotient_cache:
                    quotient_cache[key] = k_minor_model(
                        quotient(d_packet, h_packet)
                    )
                model = quotient_cache[key]
                if model is not None:
                    available.append(frame)
                    witnesses[(mode, omitted, frame)] = model
            packet_status.append(tuple(available))
        positive[mode] = tuple(packet_status)

    winning = [mode for mode, status in positive.items() if all(status)]
    print("perfect matching modes", len(positive))
    print("winning modes", len(winning))
    if not winning:
        for mode, status in positive.items():
            print("mode", mode, "H-frame choices", status)
    for mode in winning:
        print("mode", mode, "H-frame choices", positive[mode])
        for omitted, frames in enumerate(positive[mode]):
            frame = frames[0]
            print(
                " omitted block", omitted,
                "frame", frame,
                "bags", witnesses[(mode, omitted, frame)],
            )


if __name__ == "__main__":
    main()
