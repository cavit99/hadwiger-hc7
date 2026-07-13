#!/usr/bin/env python3
"""Classify the HC7 C5+2K1 exact-state Property-B signatures."""

from __future__ import annotations

from collections import Counter, defaultdict


def rotate(bits, k):
    s = bits[:5]
    d = bits[5:]
    return tuple(s[(i - k) % 5] for i in range(5)) + tuple(
        d[(i - k) % 5] for i in range(5)
    )


def reflect(bits):
    # e_i -> e_{-i-1}; d_i={e_i,e_{i+2}} -> d_{-i-3}
    s = bits[:5]
    d = bits[5:]
    return tuple(s[(-i - 1) % 5] for i in range(5)) + tuple(
        d[(-i - 3) % 5] for i in range(5)
    )


def orbit(bits):
    ans = set()
    for flip in (False, True):
        b = tuple(1 - x for x in bits) if flip else bits
        for k in range(5):
            x = rotate(b, k)
            ans.add(x)
            ans.add(reflect(x))
    return ans


def valid(bits):
    s = bits[:5]
    d = bits[5:]
    for i in range(5):
        # Exact edge block e_i.
        if len({s[i], d[i], d[(i + 3) % 5]}) < 2:
            return False
        # Exact singleton core vertex v_i.
        vals = (s[(i + 1) % 5], s[(i + 2) % 5],
                s[(i + 3) % 5], d[(i + 1) % 5])
        if len(set(vals)) < 2:
            return False
    return True


def valid_partial(vals):
    s = vals[:5]
    d = vals[5:]
    for i in range(5):
        if not ({s[i], d[i], d[(i + 3) % 5]} >= {0, 1}):
            return False
        block = {s[(i + 1) % 5], s[(i + 2) % 5],
                 s[(i + 3) % 5], d[(i + 1) % 5]}
        if not (block >= {0, 1}):
            return False
    return True


def minimal_partial(vals):
    if not valid_partial(vals):
        return False
    for j, x in enumerate(vals):
        if x == 2:
            continue
        w = list(vals)
        w[j] = 2
        if valid_partial(tuple(w)):
            return False
    return True


def orbit_partial(vals):
    ans = set()
    for flip in (False, True):
        b = tuple((1 - x if x < 2 else 2) for x in vals) if flip else vals
        for k in range(5):
            x = rotate(b, k)
            ans.add(x)
            ans.add(reflect(x))
    return ans


def transitions(bits):
    """Number of single-state flips that keep a Property-B coloring."""
    out = []
    for j in range(10):
        b = list(bits)
        b[j] ^= 1
        if valid(tuple(b)):
            out.append(j)
    return tuple(out)


def main():
    valid_bits = []
    for mask in range(1 << 10):
        bits = tuple((mask >> i) & 1 for i in range(10))
        if valid(bits):
            valid_bits.append(bits)
    seen = set()
    reps = []
    for bits in valid_bits:
        if bits in seen:
            continue
        o = orbit(bits)
        seen.update(o)
        reps.append(min(o))
    print("valid labeled", len(valid_bits))
    print("orbits D5 x swap", len(reps))
    hist = Counter()
    for b in valid_bits:
        hist[(sum(b[:5]), sum(b[5:]), len(transitions(b)))] += 1
    print("histogram (single ones,double ones,valid single flips):")
    for key, value in sorted(hist.items()):
        print(key, value)
    print("orbit representatives s|d and orbit size, flippable indices:")
    for b in sorted(reps):
        print("".join(map(str, b[:5])), "|", "".join(map(str, b[5:])),
              "orbit", len(orbit(b)), "flips", transitions(b))

    partials = []
    for code in range(3 ** 10):
        x = code
        vals = []
        for _ in range(10):
            vals.append(x % 3)
            x //= 3
        vals = tuple(vals)
        if minimal_partial(vals):
            partials.append(vals)
    seen = set()
    preps = []
    for vals in partials:
        if vals in seen:
            continue
        o = orbit_partial(vals)
        seen.update(o)
        preps.append(min(o))
    print("minimal partial labeled", len(partials))
    print("minimal partial orbits", len(preps))
    for b in sorted(preps):
        show = lambda x: "-" if x == 2 else str(x)
        print("".join(map(show, b[:5])), "|", "".join(map(show, b[5:])),
              "orbit", len(orbit_partial(b)))


if __name__ == "__main__":
    main()
