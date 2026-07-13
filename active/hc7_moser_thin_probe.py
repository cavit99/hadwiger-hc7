"""Exhaustive minor probe for the pure-Moser crossed/rural tube residue.

This is a falsification aid.  It realizes the two crossed paths in C1 by
length-two paths and realizes a cut of C2 by an induced path whose boundary
contacts are the extremal same-pair defects forced by seven-connectivity.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement

from hc7_mobile_path_probe import has_k7_minor


MOSER = {
    (0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 6),
    (2, 6), (3, 4), (3, 5), (4, 5), (5, 6),
}


def make_graph(path_n: int, defect_left: int, defect_right: int):
    # 0..6 boundary, 7=v, 8=p05, 9=p24, 10.. rural path.
    n = 10 + path_n
    adj = [0] * n

    def edge(a: int, b: int):
        adj[a] |= 1 << b
        adj[b] |= 1 << a

    for a, b in MOSER:
        edge(a, b)
    for a in range(7):
        edge(7, a)
    edge(0, 8)
    edge(8, 5)
    edge(2, 9)
    edge(9, 4)
    for i in range(path_n - 1):
        edge(10 + i, 10 + i + 1)

    # The end shores miss the two displayed defects.  Every internal point
    # meets the common five labels, which is forced by delta>=7 once the two
    # exceptional labels have unique portals at opposite ends.
    for s in range(7):
        if s != defect_left:
            edge(10, s)
        if s != defect_right:
            edge(10 + path_n - 1, s)
    for i in range(1, path_n - 1):
        for s in range(7):
            if s not in {defect_left, defect_right}:
                edge(10 + i, s)
    return adj


def names(path_n: int):
    return [str(i) for i in range(7)] + ["v", "p05", "p24"] + [f"x{i}" for i in range(path_n)]


def k4_carriers_for_triangle():
    """Boundary traces of K4 models in the fixed crossed page."""
    adj = make_graph(2, 1, 4)[:10]
    # Remove rural incidences accidentally retained in the first ten masks.
    mask = (1 << 10) - 1
    adj = [a & mask for a in adj]
    connected = []
    for s in range(1, 1 << 10):
        seed = s & -s
        seen = seed
        while True:
            nxt = seen
            x = seen
            while x:
                bit = x & -x
                x -= bit
                nxt |= adj[bit.bit_length() - 1] & s
            if nxt == seen:
                break
            seen = nxt
        if seen == s and s & 0x7F:
            connected.append(s)

    nbr = {}
    for s in connected:
        out = 0
        x = s
        while x:
            bit = x & -x
            x -= bit
            out |= adj[bit.bit_length() - 1]
        nbr[s] = out

    models = {}

    def rec(chosen, used, start):
        if len(chosen) == 4:
            ordered = tuple(sorted(chosen, key=lambda s: (s & 0x7F, s)))
            trace = tuple(s & 0x7F for s in ordered)
            models.setdefault(trace, ordered)
            return
        for i in range(start, len(connected)):
            s = connected[i]
            if s & used or any(not (nbr[s] & t) for t in chosen):
                continue
            rec(chosen + [s], used | s, i + 1)

    rec([], 0, 0)
    return models


def probe_triangle():
    models = k4_carriers_for_triangle()
    defects = [0]
    defects += [1 << i for i in range(7)]
    defects += [(1 << i) | (1 << j) for i, j in combinations(range(7), 2)]
    bad = []
    all_s = (1 << 7) - 1
    valid = []
    for ds in combinations_with_replacement(defects, 3):
        if ds[0] & ds[1] & ds[2]:
            continue
        valid.append(ds)
        contacts = [all_s ^ d for d in ds]
        witness = next(
            (m for m in models if all(all(trace & c for trace in m) for c in contacts)),
            None,
        )
        if witness is None:
            bad.append(ds)
            if len(bad) <= 5:
                print("triangle bad", ds)
    print("triangle carrier models", len(models), "states", len(valid), "bad", len(bad))
    if not bad:
        uncovered = set(range(len(valid)))
        covers = {}
        for trace in models:
            hit = {
                k for k, ds in enumerate(valid)
                if all(all(t & (all_s ^ d) for t in trace) for d in ds)
            }
            if hit:
                covers[trace] = hit
        chosen = []
        while uncovered:
            trace = max(covers, key=lambda t: len(covers[t] & uncovered))
            gain = covers[trace] & uncovered
            chosen.append(trace)
            uncovered -= gain
        label = [str(i) for i in range(7)] + ["v", "p05", "p24"]
        print("greedy frames", len(chosen))
        for trace in chosen:
            actual = models[trace]
            print([[label[i] for i in range(10) if s >> i & 1] for s in actual], "covers", len(covers[trace]))
        # Test a stronger hand-proof target: every partition of N into one
        # singleton and three pairs is the exact boundary trace of a K4 model.
        exact = []
        for q in range(7):
            rest = [x for x in range(7) if x != q]
            matchings = set()
            for a in rest[1:]:
                p1 = tuple(sorted((rest[0], a)))
                rem = [x for x in rest if x not in p1]
                for b in rem[1:]:
                    p2 = tuple(sorted((rem[0], b)))
                    p3 = tuple(sorted(x for x in rem if x not in p2))
                    matchings.add(tuple(sorted((p1, p2, p3))))
            for matching in matchings:
                target = sorted([1 << q] + [sum(1 << x for x in p) for p in matching])
                if not any(sorted(m) == target for m in models):
                    exact.append((q, matching))
        print("exact 1+2+2+2 failures", len(exact), exact[:10])
        return



def main():
    probe_triangle()
    # A singleton full rural shore.
    singleton = make_graph(2, 1, 4)
    # Contract the rural path edge in the input construction: vertex 11 into
    # 10 and take the union of their boundary contacts.
    n = len(singleton)
    keep = [i for i in range(n) if i != 11]
    remap = {old: new for new, old in enumerate(keep)}
    sadj = [0] * len(keep)
    edges = set()
    for a in range(n):
        for b in range(a + 1, n):
            if singleton[a] >> b & 1:
                aa = 10 if a == 11 else a
                bb = 10 if b == 11 else b
                if aa != bb:
                    edges.add(tuple(sorted((remap[aa], remap[bb]))))
    for a, b in edges:
        sadj[a] |= 1 << b
        sadj[b] |= 1 << a
    smodel = has_k7_minor(sadj)
    slabel = [str(i) for i in range(7)] + ["v", "p05", "p24", "x"]
    print("singleton", "K7" if smodel else "NO")
    if smodel:
        print([[slabel[i] for i in range(len(slabel)) if m >> i & 1] for m in smodel])

    for defects in ((1, 4), (4, 1), (3, 2), (2, 3)):
        for path_n in range(2, 3):
            adj = make_graph(path_n, *defects)
            model = has_k7_minor(adj)
            label = names(path_n)
            print(defects, path_n, "K7" if model else "NO")
            if model:
                print([[label[i] for i in range(len(label)) if m >> i & 1] for m in model])


if __name__ == "__main__":
    main()
