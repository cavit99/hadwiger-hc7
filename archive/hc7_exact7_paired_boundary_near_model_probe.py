#!/usr/bin/env python3
"""Historical discovery probe for small paired-state boundary cores.

The exact width-two frontier theorem now supersedes this shallow census.
"""

from itertools import combinations, permutations, product


VERTICES = ("c", "a1", "t1", "a2", "t2", "a3", "t3")
BLOCKS = (("a1", "t1"), ("a2", "t2"), ("a3", "t3"))


def edge(u: str, v: str) -> tuple[str, str]:
    return tuple(sorted((u, v)))


def has_small_core(edges: set[tuple[str, str]]) -> tuple | None:
    vertices = set(VERTICES)
    for terminals in combinations(VERTICES, 3):
        terminal_set = set(terminals)
        if not any(edge(u, v) in edges for u, v in combinations(terminals, 2)):
            continue
        remainder = vertices - terminal_set
        for size in (1, 2):
            for core in combinations(remainder, size):
                core_set = set(core)
                if size == 2 and edge(*core) not in edges:
                    continue
                if all(
                    any(edge(root, terminal) in edges for root in core)
                    for terminal in terminals
                ):
                    anchors = tuple(sorted(remainder - core_set))
                    if len(anchors) >= 2:
                        return terminals, core, anchors
    return None


def main() -> None:
    choices = []
    for block in BLOCKS:
        choices.append(tuple(edge("c", vertex) for vertex in block))
    for left, right in combinations(BLOCKS, 2):
        choices.append(tuple(edge(u, v) for u in left for v in right))

    failures = []
    for selected in product(*choices):
        edges = set(selected)
        witness = has_small_core(edges)
        if witness is None:
            failures.append(tuple(sorted(edges)))
    print("minimal boundaries", 2**3 * 4**3)
    print("failures", len(failures))
    for failure in failures[:20]:
        print(failure)

    allowed = {
        edge(u, v)
        for u, v in combinations(VERTICES, 2)
        if {u, v} not in (set(block) for block in BLOCKS)
    }
    required_classes = tuple(set(choice) for choice in choices)
    ordered_allowed = tuple(sorted(allowed))
    maximal = []
    for mask in range(1 << len(ordered_allowed)):
        edges = {
            candidate
            for index, candidate in enumerate(ordered_allowed)
            if mask >> index & 1
        }
        if any(not edges & required for required in required_classes):
            continue
        if has_small_core(edges) is not None:
            continue
        if any(
            has_small_core(edges | {candidate}) is None
            for candidate in allowed - edges
        ):
            continue
        maximal.append(frozenset(edges))

    label_actions = []
    for pair_order in permutations(range(3)):
        for flips in product((0, 1), repeat=3):
            action = {"c": "c"}
            for source_index, target_index in enumerate(pair_order):
                source = BLOCKS[source_index]
                target = BLOCKS[target_index]
                for endpoint in range(2):
                    action[source[endpoint]] = target[endpoint ^ flips[source_index]]
            label_actions.append(action)

    def canonical(edges: frozenset[tuple[str, str]]) -> tuple:
        return min(
            tuple(sorted(edge(action[u], action[v]) for u, v in edges))
            for action in label_actions
        )

    orbits = sorted({canonical(edges) for edges in maximal})
    print("maximal failures", len(maximal))
    print("paired-label orbits", len(orbits))
    for orbit in orbits:
        print("orbit", orbit)


if __name__ == "__main__":
    main()
