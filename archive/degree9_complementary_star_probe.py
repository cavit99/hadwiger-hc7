#!/usr/bin/env python3
"""Exact K7-minor probe for the complementary R0 star lock."""

from pure_moser_degree9_model_occupancy_probe import has_k7


def find_k7(vertices, edges):
    n = len(vertices)
    index = {x: i for i, x in enumerate(vertices)}
    adjacency = [0] * n
    for edge in edges:
        x, y = edge
        adjacency[index[x]] |= 1 << index[y]
        adjacency[index[y]] |= 1 << index[x]

    def connected(mask):
        reached = mask & -mask
        while True:
            nxt = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                nxt |= adjacency[bit.bit_length() - 1] & mask
            if nxt == reached:
                return reached == mask
            reached = nxt

    connected_masks = [m for m in range(1, 1 << n) if connected(m)]
    neighbours = [0] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        neighbours[mask] = neighbours[mask - bit] | adjacency[bit.bit_length()-1]
    connected_masks.sort(key=lambda m: (m.bit_count(), m))

    def search(chosen, candidates, used):
        if len(chosen) == 7:
            return chosen
        need = 7 - len(chosen)
        for pos, bag in enumerate(candidates):
            if bag & used:
                continue
            nxt = [other for other in candidates[pos + 1:]
                   if not other & (used | bag) and neighbours[bag] & other]
            if len(nxt) >= need - 1:
                out = search(chosen + [bag], nxt, used | bag)
                if out is not None:
                    return out
        return None

    model = search([], connected_masks, 0)
    if model is None:
        return None
    return [tuple(vertices[i] for i in range(n) if mask >> i & 1) for mask in model]


def build(leaves: int):
    vertices = ["v", "h", "1", "2", "3", "4", "6", "K", "L", "R", "r"]
    vertices += [f"x{i}" for i in range(leaves)]
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    # Pure Moser graph, with 5 absorbed into R and 6 retained literally.
    for x in ("h", "1", "2", "3", "4", "R", "6"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "R"), ("4", "R"), ("R", "6"),
    ):
        add(a, b)

    # Exterior roots and the conservative rooted-K4 contacts.
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("R", "r"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "6")
    add("6", "L")
    add("6", "R")
    add("L", "R")
    add("L", "r")
    add("R", "r")

    # R0 is a star rooted at r.  Each root-free lobe is simultaneously a
    # K-portal and an R5-portal, and hence cannot be transferred to either.
    for i in range(leaves):
        x = f"x{i}"
        add("r", x)
        add("K", x)
        add("R", x)
    return tuple(vertices), edges


def build_two_spines(length: int):
    vertices = ["v", "h", "1", "2", "3", "4", "6", "K", "L", "R", "r"]
    left = [f"a{i}" for i in range(length)] + ["b"]
    right = [f"c{i}" for i in range(length)] + ["d"]
    vertices += left + right
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for x in ("h", "1", "2", "3", "4", "R", "6"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "R"), ("4", "R"), ("R", "6"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("R", "r"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "6")
    add("6", "L")
    add("6", "R")
    add("L", "R")

    # R0 has two root-to-leaf spines.  Every internal spine vertex is a
    # K-portal.  The first leaf owns the sole L0 contact and the second
    # owns the sole R5 contact.
    for path in (left, right):
        add("r", path[0])
        for x, y in zip(path, path[1:]):
            add(x, y)
        for x in path[:-1]:
            add("K", x)
    add("b", "L")
    add("d", "R")
    return tuple(vertices), edges


def build_one_spine(length: int):
    vertices = ["v", "h", "1", "2", "3", "4", "6", "K", "L", "R", "r"]
    path = [f"a{i}" for i in range(length)] + ["z"]
    vertices += path
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for x in ("h", "1", "2", "3", "4", "R", "6"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "R"), ("4", "R"), ("R", "6"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("R", "r"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "6")
    add("6", "L")
    add("6", "R")
    add("L", "R")
    add("r", path[0])
    for x, y in zip(path, path[1:]):
        add(x, y)
    for x in path[:-1]:
        add("K", x)
    add("z", "L")
    add("z", "R")
    return tuple(vertices), edges


def build_outer_split_unique_r0():
    """Conservative quotient for an R5 split and one K--R0 portal."""
    vertices = ("v", "h", "1", "2", "3", "4", "6", "K", "L",
                "X", "Y", "p", "r")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for x in ("h", "1", "2", "3", "4", "Y", "6"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "Y"), ("4", "Y"), ("Y", "6"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("Y", "r"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "6")
    add("6", "L")
    add("K", "X")
    add("K", "Y")
    add("X", "Y")
    add("X", "L")
    add("K", "p")
    add("p", "r")
    add("r", "L")
    add("r", "Y")
    return vertices, edges


def build_outer_r0_owner(k_r0: bool, l0_owner: str):
    """R5=X|Y, both K-contact; all R0 contact lies in X."""
    vertices = ("v", "h", "1", "2", "3", "4", "6", "K", "L",
                "X", "Y", "r")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for x in ("h", "1", "2", "3", "4", "Y", "6"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "6"), ("2", "6"),
        ("3", "4"), ("3", "Y"), ("4", "Y"), ("Y", "6"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("Y", "r"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "6")
    add("6", "L")
    add("K", "X")
    add("K", "Y")
    add("X", "Y")
    add("X", "r")
    add(l0_owner, "L")
    add("L", "r")
    if k_r0:
        add("K", "r")
    else:
        add("6", "r")
    return vertices, edges


def build_double_complementary_cross(k_r0: bool, j_l0: bool):
    """Conservative quotient for K-C and J-D in both complementary cells."""
    vertices = ("v", "h", "1", "2", "3", "4", "K", "D", "J", "C", "L", "R")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    # Pure Moser, with 6 in D and 5 in C.
    for x in ("h", "1", "2", "3", "4", "C", "D"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", "C"), ("4", "C"), ("C", "D"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("J", "R"):
        for y in ("h", "3", "4"):
            add(x, y)

    add("K", "D")
    add("J", "C")
    add("D", "L")       # K not L
    add("C", "R")       # J not R
    add("L", "R")
    add("K" if k_r0 else "D", "R")
    add("J" if j_l0 else "C", "L")
    add("K", "C")
    add("J", "D")
    return vertices, edges


def build_mixed_r0_split(l6_owner: str, l_owner: str):
    """Left complementary/right same-bag, with J portals on both R0 sides."""
    vertices = ("v", "h", "1", "2", "3", "4", "K", "D", "J", "C", "L", "X", "Y")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for x in ("h", "1", "2", "3", "4", "C", "D"):
        add("v", x)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", "C"), ("4", "C"), ("C", "D"),
    ):
        add(a, b)
    for x in ("K", "L"):
        for y in ("h", "1", "2"):
            add(x, y)
    for x in ("J", "Y"):
        for y in ("h", "3", "4"):
            add(x, y)
    add("K", "D")
    add("J", "C")
    add("D", "L")
    add("C", "L")
    add("K", "C")
    add("J", "X")
    add("J", "Y")
    add("X", "Y")
    add("L", l_owner)
    bag, side = l6_owner.split("-")
    add(bag, side)
    return vertices, edges


def build_mixed_double_spine(c5: str, c_l0: str, l6_r0: str):
    """Mixed residue: W=J+root lobe, Q=R0 residue, C=X|Y."""
    vertices = ("v", "h", "1", "2", "3", "4", "K", "D", "W", "X", "Y", "L", "Q")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", c5, "D"):
        add("v", z)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", c5), ("4", c5), (c5, "D"),
    ):
        add(a, b)
    for z in ("K", "L"):
        for y in ("h", "1", "2"):
            add(z, y)
    for y in ("h", "3", "4"):
        add("W", y)
    add("K", "D")
    add("D", "L")
    add("W", "Q")
    add("Q", "L")
    add(l6_r0, "Q")
    add("X", "Y")
    add("W", "X")
    add("K", "Y")
    add(c_l0, "L")
    return vertices, edges


def build_double_same_bag():
    """Conservative quotient of two exceptional root-bearing lobes."""
    vertices = ("v", "h", "1", "2", "3", "4", "K", "D", "J", "C", "U", "Q", "V", "R")
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", "C", "D"):
        add("v", z)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", "C"), ("4", "C"), ("C", "D"),
    ):
        add(a, b)
    for z in ("K", "U"):
        for y in ("h", "1", "2"):
            add(z, y)
    for z in ("J", "V"):
        for y in ("h", "3", "4"):
            add(z, y)
    # Internal gates, exceptional root-lobe contacts, residues, and the two
    # retained opposite carrier edges.
    for a, b in (
        ("K", "D"), ("J", "C"), ("K", "U"), ("U", "Q"),
        ("J", "V"), ("V", "R"), ("Q", "R"),
        ("C", "Q"), ("D", "R"),
    ):
        add(a, b)
    return vertices, edges


def build_double_same_spines(length: int, capacity: int = 0,
                             distributed_capacity: int = 0):
    """Two ordered same-bag spines with optional exact-row capacity.

    The ``kx*`` vertices lie in the left outer bag and are simplicial on
    the edge K--u0; hence every left root prefix has ``capacity + 1``
    distinct neighbours in that outer bag (K itself plus the kx vertices).
    The ``jy*`` vertices are the symmetric right-hand capacity vertices.
    The first ``distributed_capacity`` vertices on each side are joined
    to every vertex of their spine, not just its root.  This realizes an
    exact (or strict) seven-connectivity-sized lobe boundary while still
    admitting the width-five sharpness certificate when one capacity
    vertex per side is distributed.
    They are useful for checking that the width-five obstruction persists
    after the separator-row multiplicities forced by seven-connectivity are
    retained.
    """
    left = [f"u{i}" for i in range(length)]
    right = [f"w{i}" for i in range(length)]
    left_capacity = [f"kx{i}" for i in range(capacity)]
    right_capacity = [f"jy{i}" for i in range(capacity)]
    vertices = ["v", "h", "1", "2", "3", "4", "K", "D", "J", "C", "Q", "R",
                *left, *right, *left_capacity, *right_capacity]
    edges = set()

    def add(a, b):
        edges.add(frozenset((a, b)))

    for z in ("h", "1", "2", "3", "4", "C", "D"):
        add("v", z)
    for a, b in (
        ("h", "1"), ("h", "2"), ("h", "3"), ("h", "4"),
        ("1", "2"), ("1", "D"), ("2", "D"),
        ("3", "4"), ("3", "C"), ("4", "C"), ("C", "D"),
    ):
        add(a, b)
    for y in ("h", "1", "2"):
        add("K", y)
        add(left[0], y)
    for y in ("h", "3", "4"):
        add("J", y)
        add(right[0], y)
    add("K", "D")
    add("J", "C")
    for x in left:
        add("K", x)
    for x in left_capacity:
        add("K", x)
        add("u0", x)
    for x in left_capacity[:distributed_capacity]:
        for u in left[1:]:
            add(x, u)
    for x, y in zip(left, left[1:]):
        add(x, y)
    add(left[-1], "Q")
    for x in right:
        add("J", x)
    for x in right_capacity:
        add("J", x)
        add("w0", x)
    for x in right_capacity[:distributed_capacity]:
        for w in right[1:]:
            add(x, w)
    for x, y in zip(right, right[1:]):
        add(x, y)
    add(right[-1], "R")
    add("Q", "R")
    add("C", "Q")
    add("D", "R")
    return tuple(vertices), edges


def min_balanced_ordinary_sum(vertices, edges):
    """Exact rooted spanning-K4 potential for the four fixed roots."""
    roots = ("K", "u0", "J", "w0")
    idx = {v: i for i, v in enumerate(vertices)}
    root_ids = {idx[r]: i for i, r in enumerate(roots)}
    forbidden = {idx[x] for x in ("v", "h", "1", "2", "3", "4")}
    free = [i for i in range(len(vertices)) if i not in root_ids and i not in forbidden]
    adj = [0] * len(vertices)
    for edge in edges:
        a, b = (idx[x] for x in edge)
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    def connected(mask):
        reached = mask & -mask
        while True:
            nxt = reached
            bits = reached
            while bits:
                bit = bits & -bits
                bits ^= bit
                nxt |= adj[bit.bit_length() - 1] & mask
            if nxt == reached:
                return reached == mask
            reached = nxt

    best = None
    witness = None
    # Base-4 assignments of every nonroot vertex.
    for code in range(4 ** len(free)):
        bags = [1 << idx[r] for r in roots]
        x = code
        for vertex in free:
            bags[x & 3] |= 1 << vertex
            x >>= 2
        if not all(connected(mask) for mask in bags):
            continue
        ok = True
        for i in range(4):
            neigh = 0
            bits = bags[i]
            while bits:
                bit = bits & -bits
                bits ^= bit
                neigh |= adj[bit.bit_length() - 1]
            for j in range(i + 1, 4):
                if not neigh & bags[j]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        d_owner = next(i for i, bag in enumerate(bags) if bag >> idx["D"] & 1)
        c_owner = next(i for i, bag in enumerate(bags) if bag >> idx["C"] & 1)
        if d_owner not in (0, 1) or c_owner not in (2, 3):
            continue
        ordinary_left = 1 - d_owner
        ordinary_right = 5 - c_owner
        potential = bags[ordinary_left].bit_count() + bags[ordinary_right].bit_count()
        if best is None or potential < best:
            best = potential
            witness = [[vertices[i] for i in range(len(vertices)) if bag >> i & 1]
                       for bag in bags]
    return best, witness


def min_fill_width(vertices, edges):
    adj = {v: set() for v in vertices}
    for edge in edges:
        a, b = tuple(edge)
        adj[a].add(b)
        adj[b].add(a)
    order = []
    width = 0
    while adj:
        def score(v):
            n = adj[v]
            missing = sum(b not in adj[a] for i, a in enumerate(n)
                          for b in list(n)[i + 1 :])
            return missing, len(n), v
        v = min(adj, key=score)
        n = list(adj[v])
        width = max(width, len(n))
        order.append((v, tuple(sorted(n))))
        for i, a in enumerate(n):
            for b in n[i + 1 :]:
                adj[a].add(b)
                adj[b].add(a)
        for a in n:
            adj[a].remove(v)
        del adj[v]
    return width, order


def elimination_order_at_most(vertices, edges, bound):
    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    initial = [0] * n
    for edge in edges:
        a, b = (index[x] for x in edge)
        initial[a] |= 1 << b
        initial[b] |= 1 << a
    failed = set()

    def rec(alive, adj):
        if alive == 0:
            return ()
        key = (alive, tuple(adj[i] & alive for i in range(n) if alive >> i & 1))
        if key in failed:
            return None
        candidates = [i for i in range(n) if alive >> i & 1
                      and (adj[i] & alive).bit_count() <= bound]
        candidates.sort(key=lambda i: ((adj[i] & alive).bit_count(), vertices[i]))
        for v in candidates:
            neigh_mask = adj[v] & alive & ~(1 << v)
            nxt = list(adj)
            bits = neigh_mask
            while bits:
                bit = bits & -bits
                bits ^= bit
                u = bit.bit_length() - 1
                nxt[u] |= neigh_mask & ~(1 << u)
            out = rec(alive & ~(1 << v), tuple(nxt))
            if out is not None:
                return (vertices[v],) + out
        failed.add(key)
        return None

    return rec((1 << n) - 1, tuple(initial))


def main():
    for leaves in range(1, 4):
        vertices, edges = build(leaves)
        width, order = min_fill_width(vertices, edges)
        order5 = elimination_order_at_most(vertices, edges, 5)
        print(leaves, len(vertices), has_k7(vertices, edges), "width", width,
              "order5", order5)
        if leaves == 1:
            print("ordering", order)
    for length in range(1, 3):
        vertices, edges = build_two_spines(length)
        print("two-spines", length, len(vertices), has_k7(vertices, edges))


if __name__ == "__main__":
    main()
