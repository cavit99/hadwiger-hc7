#!/usr/bin/env python3
"""SAT probe for the order-4/5 palette-tight two-block disk-web cell."""

from itertools import combinations, permutations, product
import sys

from z3 import And, Bool, If, Implies, Int, Not, Or, Solver, Sum, is_true, sat

BOUNDARY = 7
STATE = {
    "10": (0, 0, 1, 2, 3, 4, 5),
    "01": (1, 2, 0, 0, 3, 4, 5),
    "11": (0, 0, 1, 1, 2, 3, 4),
}
ORDER5_TYPES = (
    ((0, 4), (1, 4), (2, 4), (3, 4)),
    ((0, 4), (1, 3), (2, 3), (3, 4)),
    ((0, 1), (0, 4), (1, 2), (2, 3)),
    ((0, 4), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 2), (0, 4), (1, 2), (2, 3)),
    ((0, 4), (1, 2), (1, 3), (2, 3), (3, 4)),
    ((0, 1), (1, 3), (1, 4), (2, 3), (2, 4)),
    ((0, 1), (0, 4), (1, 2), (2, 3), (3, 4)),
    ((0, 1), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4)),
    ((0, 1), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 4), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4)),
    ((0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4)),
    ((0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)),
    ((0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 4)),
    ((0, 1), (0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
    ((0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)),
)
ORDER6_CODES = (
    31, 61, 63, 121, 122, 123, 126, 127, 246, 247, 254, 255, 510, 511,
    633, 635, 639, 659, 663, 671, 691, 692, 693, 694, 695, 700, 701, 703,
    758, 759, 760, 761, 762, 763, 766, 767, 922, 923, 926, 927, 954, 955,
    956, 957, 958, 959, 1022, 1023, 1749, 1751, 1759, 1780, 1781, 1783,
    1788, 1789, 1791, 1880, 1881, 1883, 1884, 1885, 1887, 1915, 1916,
    1917, 1919, 2012, 2013, 2014, 2015, 2046, 2047, 4060, 4061, 4063,
    4095, 5873, 5875, 5879, 5887, 5907, 5911, 5919, 5941, 5943, 5948,
    5949, 5950, 5951, 6007, 6010, 6011, 6014, 6015, 6142, 6143, 6654,
    6655, 7071, 7100, 7101, 7103, 7166, 7167, 8157, 8159, 8191, 15870,
    15871, 16383, 32767,
)


def connected(n, edges):
    adjacency = [set() for _ in range(n)]
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    seen, stack = {0}, [0]
    while stack:
        x = stack.pop()
        for y in adjacency[x] - seen:
            seen.add(y)
            stack.append(y)
    return len(seen) == n


def all_paths(n, edges, source, target, forbidden):
    total = 4 + n
    adjacency = [set() for _ in range(total)]
    for p in (0, 1):
        for q in (2, 3):
            adjacency[p].add(q)
            adjacency[q].add(p)
    for x, y in edges:
        adjacency[4 + x].add(4 + y)
        adjacency[4 + y].add(4 + x)
    for terminal in range(4):
        for x in range(n):
            adjacency[terminal].add(4 + x)
            adjacency[4 + x].add(terminal)

    output = []

    def dfs(x, used, path):
        if x == target:
            output.append(tuple(path))
            return
        for y in adjacency[x]:
            if y not in used and y not in forbidden:
                used.add(y)
                path.append(y)
                dfs(y, used, path)
                path.pop()
                used.remove(y)

    dfs(source, {source} | set(forbidden), [source])
    return output


def required_variables(path):
    req = []
    for x, y in zip(path, path[1:]):
        if x < 4 <= y:
            req.append((y - 4, x))
        elif y < 4 <= x:
            req.append((x - 4, y))
    return frozenset(req)


def concrete_graph(n, edges, masks):
    total = 7 + n
    adjacency = [set() for _ in range(total)]
    # Boundary is complete except for p1p2 and q1q2.
    for x, y in combinations(range(7), 2):
        if {x, y} not in ({0, 1}, {2, 3}):
            adjacency[x].add(y)
            adjacency[y].add(x)
    for x, y in edges:
        adjacency[7 + x].add(7 + y)
        adjacency[7 + y].add(7 + x)
    for x, mask in enumerate(masks):
        for b in range(7):
            if mask & (1 << b):
                adjacency[7 + x].add(b)
                adjacency[b].add(7 + x)
    return adjacency


def connected_mask(mask, adjacency):
    first = (mask & -mask).bit_length() - 1
    seen, stack = {first}, [first]
    while stack:
        x = stack.pop()
        for y in adjacency[x]:
            if mask & (1 << y) and y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen) == mask.bit_count()


def find_k7_model(adjacency):
    total = len(adjacency)
    connected_sets = [
        mask
        for mask in range(1, 1 << total)
        if mask.bit_count() <= total - 6 and connected_mask(mask, adjacency)
    ]
    neighbour_union = {}
    for mask in connected_sets:
        union = set()
        for x in range(total):
            if mask & (1 << x):
                union |= adjacency[x]
        neighbour_union[mask] = sum(1 << x for x in union)
    connected_sets.sort(key=lambda mask: (mask.bit_count(), mask))

    def search(chosen, used, start):
        if len(chosen) == 7:
            return tuple(chosen)
        if total - used.bit_count() < 7 - len(chosen):
            return None
        for index in range(start, len(connected_sets)):
            mask = connected_sets[index]
            if mask & used:
                continue
            if any(not (neighbour_union[mask] & old) for old in chosen):
                continue
            result = search(chosen + [mask], used | mask, index + 1)
            if result is not None:
                return result
        return None

    return search([], 0, 0)


def variable_edge(x, y):
    if x < 7 <= y:
        return y - 7, x
    if y < 7 <= x:
        return x - 7, y
    return None


def model_requirements(model, adjacency):
    required = set()
    # A concrete spanning tree in every branch set.
    for mask in model:
        vertices = {x for x in range(len(adjacency)) if mask & (1 << x)}
        root = min(vertices)
        seen, stack = {root}, [root]
        while stack:
            x = stack.pop()
            neighbours = sorted(
                adjacency[x] & vertices,
                key=lambda y: variable_edge(x, y) is not None,
            )
            for y in neighbours:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
                    variable = variable_edge(x, y)
                    if variable is not None:
                        required.add(variable)
        assert seen == vertices

    # One concrete adjacency edge for every pair of bags.
    for i, first in enumerate(model):
        first_vertices = [x for x in range(len(adjacency)) if first & (1 << x)]
        for second in model[i + 1:]:
            second_vertices = [x for x in range(len(adjacency)) if second & (1 << x)]
            choices = [
                (variable_edge(x, y) is not None, x, y)
                for x in first_vertices
                for y in second_vertices
                if y in adjacency[x]
            ]
            assert choices
            _, x, y = min(choices)
            variable = variable_edge(x, y)
            if variable is not None:
                required.add(variable)
    return frozenset(required)


def solve_type(n, edges):
    solver = Solver()
    contact = [[Bool(f"x_{i}_{b}") for b in range(BOUNDARY)] for i in range(n)]

    internal_degree = [0] * n
    internal_adjacency = [set() for _ in range(n)]
    for x, y in edges:
        internal_degree[x] += 1
        internal_degree[y] += 1
        internal_adjacency[x].add(y)
        internal_adjacency[y].add(x)

    # Full attachment and minimum degree seven.
    for b in range(BOUNDARY):
        solver.add(Or(*(contact[i][b] for i in range(n))))
    for i in range(n):
        solver.add(
            Sum(*(If(contact[i][b], 1, 0) for b in range(BOUNDARY)))
            + internal_degree[i]
            >= 7
        )

    # Existential extensions of split states 10 and 01.
    for state in ("10", "01"):
        colors = [Int(f"c_{state}_{i}") for i in range(n)]
        for color in colors:
            solver.add(0 <= color, color < 6)
        for x, y in edges:
            solver.add(colors[x] != colors[y])
        for i in range(n):
            for b in range(BOUNDARY):
                solver.add(Implies(contact[i][b], colors[i] != STATE[state][b]))

    # Universal failure of state 11.
    for coloring in product(range(6), repeat=n):
        if any(coloring[x] == coloring[y] for x, y in edges):
            continue
        conflicts = [
            contact[i][b]
            for i in range(n)
            for b in range(BOUNDARY)
            if coloring[i] == STATE["11"][b]
        ]
        solver.add(Or(*conflicts) if conflicts else False)

    def add_joint_extension(tag, groups, group_edges, equal_pair=None):
        """Require a state-11 coloring after one internal minor operation."""
        colors = [Int(f"c_11_{tag}_{i}") for i in range(len(groups))]
        for color in colors:
            solver.add(0 <= color, color < 6)
        for x, y in group_edges:
            solver.add(colors[x] != colors[y])
        for i, group in enumerate(groups):
            for b in range(BOUNDARY):
                hits = Or(*(contact[x][b] for x in group))
                solver.add(Implies(hits, colors[i] != STATE["11"][b]))
        if equal_pair is not None:
            solver.add(colors[equal_pair[0]] == colors[equal_pair[1]])

    # Boundary-minor criticality: every internal vertex/edge deletion and
    # every internal edge contraction creates the joint state 11.
    edge_set = set(edges)
    for deleted in range(n):
        vertices = [x for x in range(n) if x != deleted]
        index = {x: i for i, x in enumerate(vertices)}
        groups = [(x,) for x in vertices]
        operation_edges = {
            tuple(sorted((index[x], index[y])))
            for x, y in edges
            if deleted not in (x, y)
        }
        add_joint_extension(f"dv{deleted}", groups, operation_edges)

    for edge_index, (x, y) in enumerate(edges):
        singleton_groups = [(z,) for z in range(n)]
        deletion_edges = edge_set - {(x, y)}
        add_joint_extension(
            f"de{edge_index}",
            singleton_groups,
            deletion_edges,
            equal_pair=(x, y),
        )

        vertices = [z for z in range(n) if z != y]
        index = {z: i for i, z in enumerate(vertices)}
        groups = [((x, y) if z == x else (z,)) for z in vertices]
        contraction_edges = set()
        for a, b in edges:
            aa = x if a == y else a
            bb = x if b == y else b
            if aa != bb:
                contraction_edges.add(tuple(sorted((index[aa], index[bb]))))
        add_joint_extension(f"ce{edge_index}", groups, contraction_edges)

    # Every nonempty interior set has at least four neighbours in J_D.
    for bits in range(1, 1 << n):
        shore = {i for i in range(n) if bits & (1 << i)}
        fixed_neighbours = {
            y
            for x in shore
            for y in internal_adjacency[x]
            if y not in shore
        }
        terminal_neighbours = [
            Or(*(contact[i][b] for i in shore))
            for b in range(4)
        ]
        solver.add(
            Sum(*(If(value, 1, 0) for value in terminal_neighbours))
            + len(fixed_neighbours)
            >= 4
        )

    # Forbid every pair of vertex-disjoint prescribed paths.
    p_paths = all_paths(n, edges, 0, 1, {2, 3})
    q_paths = all_paths(n, edges, 2, 3, {0, 1})
    blockers = set()
    for p_path in p_paths:
        p_vertices = set(p_path)
        for q_path in q_paths:
            if p_vertices.isdisjoint(q_path):
                blockers.add(required_variables(p_path) | required_variables(q_path))
    minimal_blockers = {
        blocker
        for blocker in blockers
        if not any(other < blocker for other in blockers)
    }
    for blocker in minimal_blockers:
        solver.add(Not(And(*(contact[i][b] for i, b in blocker))))

    while solver.check() == sat:
        model = solver.model()
        masks = tuple(
            sum(
                1 << b
                for b in range(BOUNDARY)
                if is_true(model.evaluate(contact[i][b], model_completion=True))
            )
            for i in range(n)
        )
        adjacency = concrete_graph(n, edges, masks)
        clique_model = find_k7_model(adjacency)
        if clique_model is None:
            return masks
        requirements = model_requirements(clique_model, adjacency)
        if not requirements:
            solver.add(False)
        else:
            solver.add(
                Not(And(*(contact[i][b] for i, b in requirements)))
            )
    return None


def graph_types(n):
    possible = list(combinations(range(n), 2))
    for bits in range(1 << len(possible)):
        edges = tuple(
            possible[i]
            for i in range(len(possible))
            if bits & (1 << i)
        )
        if connected(n, edges):
            yield edges


def canonical_code(n, edges):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    possible = list(combinations(range(n), 2))
    best = None
    for permutation in permutations(range(n)):
        image = {
            tuple(sorted((permutation[x], permutation[y])))
            for x, y in edge_set
        }
        code = sum(1 << i for i, edge in enumerate(possible) if edge in image)
        best = code if best is None else min(best, code)
    return best


def order5_types():
    # Verify, without NetworkX, that the archived representatives cover all
    # connected five-vertex graphs up to isomorphism.
    archived = {canonical_code(5, edges) for edges in ORDER5_TYPES}
    generated = {canonical_code(5, edges) for edges in graph_types(5)}
    assert len(archived) == len(ORDER5_TYPES) == 21
    assert archived == generated
    return ORDER5_TYPES


def edges_from_code(n, code):
    possible = list(combinations(range(n), 2))
    return tuple(edge for i, edge in enumerate(possible) if code & (1 << i))


def order6_types():
    types = tuple(edges_from_code(6, code) for code in ORDER6_CODES)
    assert len(types) == len(set(ORDER6_CODES)) == 112
    assert all(connected(6, edges) for edges in types)
    assert all(canonical_code(6, edges) == code for code, edges in zip(ORDER6_CODES, types))
    return types


def main():
    order = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    tested = 0
    if order == 5:
        types = order5_types()
    elif order == 6:
        types = order6_types()
    else:
        types = graph_types(order)
    for edges in types:
        tested += 1
        masks = solve_type(order, edges)
        if masks is not None:
            print(f"SAT order={order} edges={edges} masks={masks}")
            return
    print(f"UNSAT order={order} labelled_connected_types={tested}")


if __name__ == "__main__":
    main()
