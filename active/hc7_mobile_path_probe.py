"""Small exhaustive probe for the lex-minimal mobile-path carrier.

The six foreign labels induce K2 join C4.  The seventh carrier is an
actual path whose endpoints own disjoint label sets of size at least two;
the remaining at most two labels may occur at internal path vertices.
Searches for seven pairwise touching disjoint connected vertex sets.
This is a falsification aid, not a proof certificate.
"""

from __future__ import annotations

from itertools import combinations, product


def has_k7_minor(adj: list[int]) -> tuple[int, ...] | None:
    n = len(adj)
    connected: list[int] = []
    for mask in range(1, 1 << n):
        seed = mask & -mask
        seen = seed
        while True:
            nxt = seen
            x = seen
            while x:
                bit = x & -x
                x -= bit
                nxt |= adj[bit.bit_length() - 1] & mask
            if nxt == seen:
                break
            seen = nxt
        if seen == mask:
            connected.append(mask)

    # Canonical ordering by least vertex prevents permutation blowup.
    def search(chosen: tuple[int, ...], used: int, start: int):
        if len(chosen) == 7:
            return chosen
        need = 7 - len(chosen)
        if n - used.bit_count() < need:
            return None
        for idx in range(start, len(connected)):
            s = connected[idx]
            if s & used:
                continue
            ok = True
            for t in chosen:
                # Some edge has one end in s and one in t.
                nbr = 0
                x = s
                while x:
                    bit = x & -x
                    x -= bit
                    nbr |= adj[bit.bit_length() - 1]
                if not (nbr & t):
                    ok = False
                    break
            if ok:
                out = search(chosen + (s,), used | s, idx + 1)
                if out is not None:
                    return out
        return None

    return search((), 0, 0)


def graph(path_n: int, left: set[int], right: set[int], mobile: dict[int, set[int]]):
    # foreign 0,1 are common rows; 2,3,4,5 form a C4.
    n = 6 + path_n
    adj = [0] * n

    def edge(u: int, v: int):
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    edge(0, 1)
    for x in (0, 1):
        for y in (2, 3, 4, 5):
            edge(x, y)
    for x, y in ((2, 3), (3, 4), (4, 5), (5, 2)):
        edge(x, y)
    for i in range(path_n - 1):
        edge(6 + i, 6 + i + 1)
    for q in left:
        edge(6, q)
    for q in right:
        edge(6 + path_n - 1, q)
    for q, places in mobile.items():
        for i in places:
            edge(6 + i, q)
    return adj


def main():
    # Representative hardest ownership sizes 2+2+2.  Enumerate partitions,
    # and require union of mobile internal portals to contain every internal
    # vertex (the extremal sparse contact placement).
    labels = set(range(6))
    for path_n in range(7, 9):
        internal = set(range(1, path_n - 1))
        checked = 0
        for left_t in combinations(range(6), 2):
            left = set(left_t)
            for right_t in combinations(sorted(labels - left), 2):
                right = set(right_t)
                mob = sorted(labels - left - right)
                # Assign each internal point nonemptily to either/both mobile
                # labels.  Also require both mobile labels to occur.
                for choices in product((1, 2, 3), repeat=len(internal)):
                    places = {mob[0]: set(), mob[1]: set()}
                    for i, c in zip(sorted(internal), choices):
                        if c & 1:
                            places[mob[0]].add(i)
                        if c & 2:
                            places[mob[1]].add(i)
                    if not all(places.values()):
                        continue
                    checked += 1
                    adj = graph(path_n, left, right, places)
                    witness = has_k7_minor(adj)
                    if witness is None:
                        print("NO", path_n, left, right, places)
                        print("min labelled row", min_labelled_row(adj, path_n))
                        return
        print("all yes", path_n, checked)


def min_labelled_row(adj: list[int], path_n: int):
    """Assign path vertices to R=6 or one of six old labelled bags.

    Return the smallest surviving R branch in a label-preserving K3vC4
    model, or None.  Intended only for the first tiny counterexample.
    """
    n = 6 + path_n
    # Required foreign edges: K2 join C4; R must meet all six.
    req = {(0, 1)}
    req |= {(x, y) for x in (0, 1) for y in (2, 3, 4, 5)}
    req |= {(2, 3), (3, 4), (4, 5), (2, 5)}
    req |= {(6, y) for y in range(6)}
    best = None
    best_asn = None
    for asn in product(range(7), repeat=path_n):
        if 6 not in asn:
            continue
        bags = [1 << i for i in range(6)] + [0]
        for i, lab in enumerate(asn):
            bags[lab] |= 1 << (6 + i)
        good = True
        for bag in bags:
            seed = bag & -bag
            seen = seed
            while True:
                nxt = seen
                x = seen
                while x:
                    bit = x & -x
                    x -= bit
                    nxt |= adj[bit.bit_length() - 1] & bag
                if nxt == seen:
                    break
                seen = nxt
            if seen != bag:
                good = False
                break
        if not good:
            continue
        for i, j in req:
            nbr = 0
            x = bags[i]
            while x:
                bit = x & -x
                x -= bit
                nbr |= adj[bit.bit_length() - 1]
            if not nbr & bags[j]:
                good = False
                break
        if good and (best is None or bags[6].bit_count() < best):
            best = bags[6].bit_count()
            best_asn = asn
    return best, best_asn


if __name__ == "__main__":
    main()
