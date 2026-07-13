import itertools
import networkx as nx


MISSING = {tuple(sorted(e)) for e in [(0,1),(0,2),(0,5),(1,2),(1,5),(2,4),(4,5)]}


def base_graph(cross_to):
    g = nx.Graph()
    boundary = [0, 1, 2, 4, 5]
    g.add_nodes_from(boundary + ["l", "m1", "m2", "p4", "p5"])
    for u, v in itertools.combinations(boundary, 2):
        if tuple(sorted((u, v))) not in MISSING:
            g.add_edge(u, v)
    g.add_edges_from([
        ("l", 0), ("l", 5),
        ("m1", 1), ("m2", 2), ("m1", "m2"),
        ("l", cross_to),
        ("p4", 4), ("p5", 5), ("p4", "p5"),
    ])
    # The 4--5 path meets the m-rail at the cut between p4 and p5.
    # Model this by allowing either half to attach to either m-side.
    return g


def connected_masks(g):
    nodes = list(g)
    masks = []
    for bits in range(1, 1 << len(nodes)):
        s = {nodes[i] for i in range(len(nodes)) if bits >> i & 1}
        if nx.is_connected(g.subgraph(s)):
            masks.append(frozenset(s))
    return masks


def find_k_model(g, k):
    masks = connected_masks(g)
    adj = {}
    for a in masks:
        adj[a] = []
        for b in masks:
            if a.isdisjoint(b) and any(g.has_edge(x, y) for x in a for y in b):
                adj[a].append(b)

    def rec(chosen, candidates):
        if len(chosen) == k:
            return chosen
        if len(chosen) + len(candidates) < k:
            return None
        while candidates:
            a = candidates.pop()
            nxt = [b for b in candidates if b.isdisjoint(a) and b in adj[a]
                   and all(b in adj[c] for c in chosen)]
            ans = rec(chosen + [a], nxt)
            if ans:
                return ans
        return None

    return rec([], masks[:])


for cross_to in ["m1", "m2"]:
    for hit_side in ["m1", "m2"]:
        g = base_graph(cross_to)
        g.add_edge("p4", hit_side)
        g.add_edge("p5", hit_side)
        model = find_k_model(g, 4)
        print(cross_to, hit_side, model)

print("shared-vertex models")
for cross_to in ["u", "x", "v"]:
    g = nx.Graph()
    boundary = [0, 1, 2, 4, 5]
    g.add_nodes_from(boundary + ["l", "u", "x", "v", "p4", "p5"])
    for a, b in itertools.combinations(boundary, 2):
        if tuple(sorted((a, b))) not in MISSING:
            g.add_edge(a, b)
    g.add_edges_from([
        ("l", 0), ("l", 5), ("l", cross_to),
        (1, "u"), ("u", "x"), ("x", "v"), ("v", 2),
        (4, "p4"), ("p4", "x"), ("x", "p5"), ("p5", 5),
    ])
    print(cross_to, find_k_model(g, 4))


def theta_y_graph(hit_rail, hit_position):
    g = nx.Graph()
    boundary = [0, 1, 2, 4, 5]
    g.add_nodes_from(boundary)
    for a, b in itertools.combinations(boundary, 2):
        if tuple(sorted((a, b))) not in MISSING:
            g.add_edge(a, b)
    # Two minimal three-terminal rail trees.
    g.add_edges_from([
        (0, "p0"), ("p0", "cL"),
        (5, "p5"), ("p5", "cL"),
        ("l", "cL"),
        (1, "p1"), ("p1", "cM"),
        (2, "p2"), ("p2", "cM"),
        ("m", "cM"),
        ("l", "m"),
    ])
    edge_positions = {
        "L0": ("p0", "cL"), "L5": ("p5", "cL"),
        "Lj": ("l", "cL"),
        "M1": ("p1", "cM"), "M2": ("p2", "cM"),
        "Mj": ("m", "cM"),
    }
    vertex_positions = {
        "p0": "p0", "p5": "p5", "cL": "cL", "l": "l",
        "p1": "p1", "p2": "p2", "cM": "cM", "m": "m",
    }
    if hit_position in edge_positions:
        a, b = edge_positions[hit_position]
        g.remove_edge(a, b)
        x = "x"
        g.add_edges_from([(a, x), (x, b)])
    else:
        x = vertex_positions[hit_position]
    g.add_edge(4, x)
    return g


print("Y-tree first-hit models for external 45 prefix")
for pos in ["p0", "L0", "cL", "L5", "p5", "Lj", "l",
            "p1", "M1", "cM", "M2", "p2", "Mj", "m"]:
    rail = "L" if pos in {"p0", "L0", "cL", "L5", "p5", "Lj", "l"} else "M"
    g = theta_y_graph(rail, pos)
    print(pos, bool(find_k_model(g, 4)), find_k_model(g, 4))

print("bad-region extra target portals/bridges")
for four_pos in ["p0", "cL", "p1", "cM"]:
    for target, target_pos in [(2, "p0"), (2, "p1"), (5, "p0"), (5, "p1")]:
        g = theta_y_graph("L", four_pos)
        # theta_y_graph already adds the 4 attachment. Add a second portal edge
        # from the target boundary label into the bad region.
        g.add_edge(target, target_pos)
        model = find_k_model(g, 4)
        print(four_pos, target, target_pos, bool(model), model)
