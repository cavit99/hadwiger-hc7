#!/usr/bin/env python3
"""Search four-colour transversals of the icosahedron for rooted K4 models."""

from itertools import combinations, product


N = 12
TOP, BOTTOM = 0, 11
A = list(range(1, 6))
B = list(range(6, 11))

adj = [0] * N


def add(u: int, v: int) -> None:
    adj[u] |= 1 << v
    adj[v] |= 1 << u


for i in range(5):
    add(TOP, A[i])
    add(BOTTOM, B[i])
    add(A[i], A[(i + 1) % 5])
    add(B[i], B[(i + 1) % 5])
    add(A[i], B[i])
    add(A[i], B[(i - 1) % 5])


def connected(mask: int) -> bool:
    if not mask:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length() - 1
        new = adj[v] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def touch(x: int, y: int) -> bool:
    z = x
    neighbours = 0
    while z:
        bit = z & -z
        z -= bit
        neighbours |= adj[bit.bit_length() - 1]
    return bool(neighbours & y)


def rooted_k4(roots: tuple[int, int, int, int]) -> tuple[int, ...] | None:
    root_mask = sum(1 << r for r in roots)
    candidates: list[list[int]] = []
    full = (1 << N) - 1
    for root in roots:
        allowed = full ^ (root_mask ^ (1 << root))
        values = []
        sub = allowed
        while sub:
            if sub & (1 << root) and connected(sub):
                values.append(sub)
            sub = (sub - 1) & allowed
        values.sort(key=int.bit_count)
        candidates.append(values)

    order = sorted(range(4), key=lambda i: len(candidates[i]))
    chosen = [0] * 4

    def search(pos: int, used: int) -> bool:
        if pos == 4:
            return True
        i = order[pos]
        for mask in candidates[i]:
            if mask & used:
                continue
            if any(chosen[j] and not touch(mask, chosen[j]) for j in range(4)):
                continue
            chosen[i] = mask
            if search(pos + 1, used | mask):
                return True
            chosen[i] = 0
        return False

    return tuple(chosen) if search(0, 0) else None


def colourings() -> list[tuple[int, ...]]:
    order = sorted(range(N), key=lambda v: -adj[v].bit_count())
    colours = [-1] * N
    out = []

    def search(pos: int, used: int) -> None:
        if pos == N:
            if used == 0b1111:
                out.append(tuple(colours))
            return
        v = order[pos]
        forbidden = 0
        neighbours = adj[v]
        for u in range(N):
            if neighbours >> u & 1 and colours[u] >= 0:
                forbidden |= 1 << colours[u]
        for colour in range(4):
            if forbidden >> colour & 1:
                continue
            if pos == 0 and colour != 0:
                continue
            colours[v] = colour
            search(pos + 1, used | (1 << colour))
            colours[v] = -1

    search(0, 0)
    return out


def main() -> None:
    assert all(a.bit_count() == 5 for a in adj)
    cs = colourings()
    transversals: dict[tuple[int, ...], tuple[int, ...]] = {}
    for colouring in cs:
        classes = [[v for v, c in enumerate(colouring) if c == i] for i in range(4)]
        for roots in product(*classes):
            key = tuple(sorted(roots))
            transversals.setdefault(key, colouring)

    print(f"colourings modulo one fixed colour: {len(cs)}")
    print(f"distinct transversal root sets: {len(transversals)}")
    for number, (roots, colouring) in enumerate(transversals.items(), 1):
        model = rooted_k4(roots)
        if model is None:
            print("counterexample roots:", roots)
            print("colouring:", colouring)
            return
        if number % 50 == 0:
            print(f"checked {number}")
    print("all transversal root sets have a rooted K4 model")


if __name__ == "__main__":
    main()
