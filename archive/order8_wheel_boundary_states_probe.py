"""Extension-state probe for the exact atomic order-eight wheel side."""

from itertools import combinations

from z3 import Int, Or, Solver, sat


B = ("x", "p", "q", "c0", "c2", "c4", "c5", "z")
K = ("v0", "v1", "v2", "v3", "h")
V = B + K


def norm(a, b):
    return tuple(sorted((a, b)))


edges = set()
# Boundary inherited from K7-(C6+K1), restricted to c0,c2,c4,c5,z.
old = ("c0", "c2", "c4", "c5")
idx = {"c0": 0, "c2": 2, "c4": 4, "c5": 5}
for a, b in combinations(old, 2):
    if (idx[a] - idx[b]) % 6 not in (1, 5):
        edges.add(norm(a, b))
for a in old:
    edges.add(norm("z", a))
edges.add(norm("x", "c0"))

# Wheel.
for i in range(4):
    edges.add(norm(f"v{i}", f"v{(i + 1) % 4}"))
    edges.add(norm("h", f"v{i}"))

contacts = {
    "v0": ("x", "c5", "c0", "z", "p"),
    "v1": ("c5", "c2", "c0", "z", "p"),
    "v2": ("c2", "c4", "c0", "z", "q"),
    "v3": ("c4", "x", "c0", "z", "q"),
    "h": ("c0", "z", "p", "q"),
}
for v, row in contacts.items():
    for b in row:
        edges.add(norm(v, b))


def partitions(n, max_blocks=6):
    a = [0] * n

    def rec(i, top):
        if i == n:
            yield tuple(a)
            return
        for x in range(min(top + 1, max_blocks - 1) + 1):
            a[i] = x
            yield from rec(i + 1, max(top, x))

    yield from rec(1, 0)


def extends(part, deleted=None, equal=None):
    deleted = deleted or set()
    equal = equal or []
    bcount = max(part) + 1
    color = {v: Int(f"c_{v}") for v in K}
    s = Solver()
    for v in K:
        s.add(color[v] >= 0, color[v] < 6)

    def val(v):
        return part[B.index(v)] if v in B else color[v]

    for a, b in edges - deleted:
        s.add(val(a) != val(b))
    for a, b in equal:
        s.add(val(a) == val(b))
    return s.check() == sat


def extension_witness(part, deleted=None, equal=None):
    deleted = deleted or set()
    equal = equal or []
    color = {v: Int(f"w_{v}") for v in K}
    s = Solver()
    for v in K:
        s.add(color[v] >= 0, color[v] < 6)

    def val(v):
        return part[B.index(v)] if v in B else color[v]

    for a, b in edges - deleted:
        s.add(val(a) != val(b))
    for a, b in equal:
        s.add(val(a) == val(b))
    if s.check() != sat:
        return None
    model = s.model()
    return tuple(model.eval(color[v]).as_long() for v in K)


def proper_boundary(part):
    return all(
        part[B.index(a)] != part[B.index(b)]
        for a, b in edges
        if a in B and b in B
    )


parts = [p for p in partitions(len(B)) if proper_boundary(p)]
base = {p for p in parts if extends(p)}
print("proper boundary partitions", len(parts), "base extensions", len(base))

internal = sorted(e for e in edges if e[0] in K and e[1] in K)
new_families = {}
for e in internal:
    deleted = {e}
    dext = {p for p in parts if extends(p, deleted=deleted)}
    cext = {p for p in parts if extends(p, deleted=deleted, equal=[e])}
    new_families[e] = cext - base
    print(
        e,
        "delete +", len(dext - base),
        "contract +", len(cext - base),
        "delete total", len(dext),
        "contract total", len(cext),
    )
    active_patterns = {}
    for part in dext - base:
        restriction = tuple(part[B.index(u)] for u in ("x", "c2", "c4", "c5"))
        # Canonicalize only the four active roots.
        names = {}
        pattern = tuple(names.setdefault(x, len(names)) for x in restriction)
        active_patterns[pattern] = active_patterns.get(pattern, 0) + 1
    print(" active new", sorted(active_patterns.items()))

common = set.intersection(*(new_families[e] for e in internal))
print("common new states for all internal edges", len(common))
if common:
    print("sample", sorted(common)[:10])

def exact_old_trace(part):
    return len({part[B.index(u)] for u in ("c0", "c2", "c4", "c5", "z")}) == 5

print("common new exact-old-trace", sorted(p for p in common if exact_old_trace(p)))
print("base exact-old-trace sample", sorted(p for p in base if exact_old_trace(p))[:20])

sigma = (0, 0, 0, 1, 2, 3, 4, 0)
tau = (0, 1, 1, 2, 3, 4, 5, 1)
print("sigma base witness", extension_witness(sigma))
print("tau base witness", extension_witness(tau))
for e in internal:
    print("tau", e, extension_witness(tau, deleted={e}, equal=[e]))


def same_off_vertex(a, b, index):
    rest = [i for i in range(len(B)) if i != index]
    return all((a[i] == a[j]) == (b[i] == b[j]) for i in rest for j in rest)


print("one-shadow common-new/base pairs")
shown = 0
for t in sorted(p for p in common if exact_old_trace(p)):
    for s0 in sorted(p for p in base if exact_old_trace(p)):
        for i, label in enumerate(B):
            if same_off_vertex(t, s0, i) and any(
                ((t[i] == t[j]) != (s0[i] == s0[j]))
                for j in range(len(B)) if j != i
            ):
                print(label, "tau", t, "sigma", s0)
                shown += 1
                break
        if shown >= 20:
            break
    if shown >= 20:
        break

sigma_selector = (0, 1, 1, 1, 0, 2, 3, 4)
tau_selector = (0, 1, 1, 1, 2, 3, 4, 5)
print("selector sigma witness", extension_witness(sigma_selector))
print("selector tau base", extension_witness(tau_selector))
for e in internal:
    print("selector tau", e, extension_witness(tau_selector, deleted={e}, equal=[e]))
