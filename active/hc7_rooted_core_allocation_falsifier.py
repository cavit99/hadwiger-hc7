"""Adversarial probes for rooted-K4 boundary/packet allocation claims.

This is a research falsifier, not a proof of any positive HC7 statement.
It works in the explicit seven-connected K7-minor-free host K2 join I,
where I is the icosahedral graph, and tests literal rooted branch sets.
"""

from __future__ import annotations

from itertools import combinations


Graph = dict[str, set[str]]


def add_edge(graph: Graph, x: str, y: str) -> None:
    graph.setdefault(x, set()).add(y)
    graph.setdefault(y, set()).add(x)


def remove_edge(graph: Graph, x: str, y: str) -> None:
    graph[x].remove(y)
    graph[y].remove(x)


def two_apex_icosahedron() -> tuple[Graph, set[str], set[str], set[str]]:
    graph: Graph = {}
    upper = [f"U{i}" for i in range(5)]
    lower = [f"L{i}" for i in range(5)]
    for vertex in ["a", "b", "T", "B", *upper, *lower]:
        graph[vertex] = set()
    for i in range(5):
        add_edge(graph, "T", upper[i])
        add_edge(graph, "B", lower[i])
        add_edge(graph, upper[i], upper[(i + 1) % 5])
        add_edge(graph, lower[i], lower[(i + 1) % 5])
        add_edge(graph, upper[i], lower[i])
        add_edge(graph, upper[i], lower[(i - 1) % 5])
    add_edge(graph, "a", "b")
    for apex in ("a", "b"):
        for vertex in set(graph) - {"a", "b"}:
            add_edge(graph, apex, vertex)
    boundary = {"a", "b", *upper}
    return graph, {"T"}, boundary, {"B", *lower}


def connected_candidates(
    graph: Graph,
    root: str,
    all_roots: tuple[str, ...],
    boundary: set[str],
    require_boundary: bool,
    max_size: int | None = None,
) -> list[frozenset[str]]:
    allowed = sorted(set(graph) - (set(all_roots) - {root}))
    answer: list[frozenset[str]] = []
    others = [vertex for vertex in allowed if vertex != root]
    if max_size is None:
        selections = (
            frozenset([root, *(others[i] for i in range(len(others)) if (mask >> i) & 1)])
            for mask in range(1 << len(others))
        )
    else:
        selections = (
            frozenset((root, *extra))
            for size in range(max_size)
            for extra in combinations(others, size)
        )
    for chosen in selections:
        if require_boundary and chosen.isdisjoint(boundary):
            continue
        reached = {next(iter(chosen))}
        frontier = list(reached)
        while frontier:
            vertex = frontier.pop()
            for neighbour in graph[vertex] & chosen:
                if neighbour not in reached:
                    reached.add(neighbour)
                    frontier.append(neighbour)
        if reached == set(chosen):
            answer.append(chosen)
    return sorted(answer, key=lambda part: (len(part), sorted(part)))


def adjacent(graph: Graph, left: frozenset[str], right: frozenset[str]) -> bool:
    return any(y in graph[x] for x in left for y in right)


def rooted_k4(
    graph: Graph,
    roots: tuple[str, str, str, str],
    boundary: set[str],
    require_all_boundary: bool,
    max_bag_size: int | None = None,
) -> tuple[frozenset[str], ...] | None:
    candidates = {
        root: connected_candidates(
            graph,
            root,
            roots,
            boundary,
            require_boundary=require_all_boundary,
            max_size=max_bag_size,
        )
        for root in roots
    }
    order = sorted(roots, key=lambda root: len(candidates[root]))
    chosen: dict[str, frozenset[str]] = {}

    def search(index: int, used: frozenset[str]) -> bool:
        if index == len(order):
            return True
        root = order[index]
        for part in candidates[root]:
            if not part.isdisjoint(used):
                continue
            if any(not adjacent(graph, part, old) for old in chosen.values()):
                continue
            chosen[root] = part
            if search(index + 1, used | part):
                return True
            del chosen[root]
        return False

    if not search(0, frozenset()):
        return None
    return tuple(chosen[root] for root in roots)


def check_rooted_model(
    graph: Graph,
    roots: tuple[str, str, str, str],
    model: tuple[frozenset[str], ...],
    boundary: set[str],
) -> None:
    assert len(model) == 4
    assert all(root in bag for root, bag in zip(roots, model, strict=True))
    assert all(model[i].isdisjoint(model[j]) for i, j in combinations(range(4), 2))
    assert all(not bag.isdisjoint(boundary) for bag in model)
    for bag in model:
        reached = {next(iter(bag))}
        frontier = list(reached)
        while frontier:
            vertex = frontier.pop()
            for neighbour in graph[vertex] & bag:
                if neighbour not in reached:
                    reached.add(neighbour)
                    frontier.append(neighbour)
        assert reached == set(bag)
    assert all(adjacent(graph, model[i], model[j]) for i, j in combinations(range(4), 2))


def exact_reselection_cycle() -> None:
    graph, _, boundary, _ = two_apex_icosahedron()
    remove_edge(graph, "T", "U0")
    remove_edge(graph, "L2", "U2")
    roots = ("T", "U0", "L2", "U2")
    first = (
        frozenset({"T", "a"}),
        frozenset({"U0", "U1"}),
        frozenset({"L2", "b"}),
        frozenset({"U2"}),
    )
    second = (
        frozenset({"T", "b"}),
        frozenset({"U0", "U1"}),
        frozenset({"L2", "a"}),
        frozenset({"U2"}),
    )
    check_rooted_model(graph, roots, first, boundary)
    check_rooted_model(graph, roots, second, boundary)
    assert sorted(map(len, first)) == sorted(map(len, second)) == [1, 2, 2, 2]
    assert {vertex for bag in first for vertex in bag} == {
        vertex for bag in second for vertex in bag
    }
    first_contacts = tuple(not bag.isdisjoint(boundary) for bag in first)
    second_contacts = tuple(not bag.isdisjoint(boundary) for bag in second)
    assert first_contacts == second_contacts == (True, True, True, True)
    print("reselection cycle GREEN")
    print("roots", roots)
    print("model_1", tuple(tuple(sorted(bag)) for bag in first))
    print("model_2", tuple(tuple(sorted(bag)) for bag in second))
    print("contact_vector", first_contacts, "bag_sizes", sorted(map(len, first)))


def f1_probe() -> None:
    graph, left, boundary, right = two_apex_icosahedron()
    failures = []
    cases = 0
    for z in sorted(left):
        for d in sorted(right):
            for u, t in combinations(sorted(boundary), 2):
                if u not in graph[z] or t not in graph[d]:
                    continue
                host = {vertex: set(neighbours) for vertex, neighbours in graph.items()}
                remove_edge(host, z, u)
                remove_edge(host, d, t)
                roots = (z, u, d, t)
                unrestricted = rooted_k4(host, roots, boundary, False)
                assert unrestricted is not None
                cases += 1
                boundary_full = rooted_k4(host, roots, boundary, True)
                if boundary_full is None:
                    failures.append((roots, unrestricted))
    print("F1 cases", cases, "failures", len(failures))
    for roots, model in failures[:10]:
        print("F1 counterexample roots", roots, "model", model)


def components(graph: Graph, deleted: set[str]) -> list[set[str]]:
    unseen = set(graph) - deleted
    answer = []
    while unseen:
        start = next(iter(unseen))
        reached = {start}
        frontier = [start]
        unseen.remove(start)
        while frontier:
            vertex = frontier.pop()
            for neighbour in graph[vertex] - deleted:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    reached.add(neighbour)
                    frontier.append(neighbour)
        answer.append(reached)
    return answer


def all_icosahedral_five_cuts_f1_probe() -> None:
    graph, _, _, _ = two_apex_icosahedron()
    base = sorted(set(graph) - {"a", "b"})
    cuts = []
    for cut_tuple in combinations(base, 5):
        cut = set(cut_tuple)
        parts = components(graph, cut | {"a", "b"})
        if len(parts) >= 2:
            cuts.append((cut, parts))
    print("icosahedral five-cuts", len(cuts), "component profiles", sorted({tuple(sorted(map(len, p))) for _, p in cuts}))
    failures = []
    cases = 0
    for cut, parts in cuts:
        boundary = {"a", "b", *cut}
        # Every bipartition of the components is an actual separation; it
        # suffices to test one component against the union of all others.
        for left in parts:
            right = set(graph) - boundary - left
            if not right:
                continue
            for z in sorted(left):
                for u in sorted(boundary & graph[z]):
                    for d in sorted(right):
                        for t in sorted((boundary & graph[d]) - {u}):
                            host = {vertex: set(neighbours) for vertex, neighbours in graph.items()}
                            remove_edge(host, z, u)
                            remove_edge(host, d, t)
                            roots = (z, u, d, t)
                            cases += 1
                            model = rooted_k4(host, roots, boundary, True)
                            if model is None:
                                failures.append((boundary, roots))
                                print("F1 exact failure", sorted(boundary), roots)
                                return
    print("all-cut F1 cases", cases, "failures", len(failures))


def two_apex_pentagonal_tube(
    bands: int,
) -> tuple[Graph, set[str], set[str], set[str]]:
    """K2 joined to a triangulated pentagonal tube with `bands+1` rings.

    The middle ring is the literal seven-boundary after adding the apices.
    """
    assert bands >= 2 and bands % 2 == 0
    graph: Graph = {"a": set(), "b": set(), "T": set(), "B": set()}
    rings = [[f"R{layer}_{i}" for i in range(5)] for layer in range(bands + 1)]
    for ring in rings:
        for vertex in ring:
            graph[vertex] = set()
        for i in range(5):
            add_edge(graph, ring[i], ring[(i + 1) % 5])
    for layer in range(bands):
        inner, outer = rings[layer], rings[layer + 1]
        for i in range(5):
            add_edge(graph, inner[i], outer[i])
            add_edge(graph, inner[i], outer[(i - 1) % 5])
    for i in range(5):
        add_edge(graph, "T", rings[0][i])
        add_edge(graph, "B", rings[-1][i])
    add_edge(graph, "a", "b")
    for apex in ("a", "b"):
        for vertex in set(graph) - {"a", "b"}:
            add_edge(graph, apex, vertex)
    middle = bands // 2
    boundary = {"a", "b", *rings[middle]}
    left = {"T", *(vertex for ring in rings[:middle] for vertex in ring)}
    right = {"B", *(vertex for ring in rings[middle + 1 :] for vertex in ring)}
    return graph, left, boundary, right


def tube_f1_small_model_probe() -> None:
    graph, left, boundary, right = two_apex_pentagonal_tube(2)
    middle = sorted(boundary - {"a", "b"})
    left_front = sorted(vertex for vertex in left if vertex.startswith("R0_"))
    right_front = sorted(vertex for vertex in right if vertex.startswith("R2_"))
    cases = 0
    failures = []
    for z in left_front:
        for u in middle:
            if u not in graph[z]:
                continue
            for d in right_front:
                for t in middle:
                    if t == u or t not in graph[d]:
                        continue
                    host = {vertex: set(neighbours) for vertex, neighbours in graph.items()}
                    remove_edge(host, z, u)
                    remove_edge(host, d, t)
                    roots = (z, u, d, t)
                    cases += 1
                    model = rooted_k4(
                        host,
                        roots,
                        boundary,
                        require_all_boundary=True,
                        max_bag_size=3,
                    )
                    if model is None:
                        failures.append(roots)
    print("tube F1 cases", cases, "without size<=3 model", len(failures))
    print("tube unresolved sample", failures[:10])


if __name__ == "__main__":
    exact_reselection_cycle()
    f1_probe()
    all_icosahedral_five_cuts_f1_probe()
    tube_f1_small_model_probe()
