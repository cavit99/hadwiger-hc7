import itertools
import networkx as nx

from full_adhesion_model_counterexample_search import has_clique_minor


L = ("a", "b", "c", "q1", "q2", "q3")
PROFILES = [
    ("c", f"q{i}", "b") for i in range(1, 4)
] + [
    ("b", f"q{i}", "c") for i in range(1, 4)
] + [
    ("c", "c", "a"), ("b", "b", "a"),
    ("a", "b", "b"), ("a", "c", "c"),
]


def quotient(profile):
    g = nx.Graph()
    g.add_nodes_from(L + ("x1", "x2", "x3"))
    for u, v in itertools.combinations(L, 2):
        if frozenset((u, v)) not in {frozenset(("a", "b")), frozenset(("a", "c"))}:
            g.add_edge(u, v)
    g.add_edges_from([("x1", "x2"), ("x2", "x3")])
    for idx, defect in enumerate(profile, 1):
        x = f"x{idx}"
        for label in L:
            if label != defect:
                g.add_edge(x, label)
    return g


def split_graph(g, x, assignment):
    h = g.copy()
    nbrs = list(g.neighbors(x))
    h.remove_node(x)
    u, v = x + "u", x + "v"
    h.add_edge(u, v)
    for n, mode in zip(nbrs, assignment):
        if mode in (1, 3):
            h.add_edge(u, n)
        if mode in (2, 3):
            h.add_edge(v, n)
    return h, tuple(nbrs)


for profile in PROFILES:
    g = quotient(profile)
    print("PROFILE", profile)
    for x in ("x1", "x2", "x3"):
        nbrs = list(g.neighbors(x))
        negatives = []
        for assn in itertools.product((1, 2, 3), repeat=len(nbrs)):
            if 1 not in assn or 2 not in assn:
                continue
            h, _ = split_graph(g, x, assn)
            if not has_clique_minor(h, 7):
                negatives.append(assn)
        both_counts = [sum(a == 3 for a in z) for z in negatives]
        print(x, "degree", len(nbrs), "negative", len(negatives),
              "max_both", max(both_counts, default=-1), "nbrs", nbrs)
        for z in negatives[:3]:
            print(" ", z)
