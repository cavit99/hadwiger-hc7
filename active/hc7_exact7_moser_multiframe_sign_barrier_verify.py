#!/usr/bin/env python3
"""Verify the explicit Moser multi-frame wheel barrier."""

ORDER = (0, 1, 2, 5, 6, 3, 4)
FRAMES = {
    "13": (2, 4),
    "14": (2, 3),
    "23": (1, 4),
    "24": (1, 3),
}


def rim_arc(a, b, step):
    i = ORDER.index(a)
    out = [a]
    while out[-1] != b:
        i = (i + step) % len(ORDER)
        out.append(ORDER[i])
    return tuple(out)


def disjoint(pair_a, pair_b):
    return set(pair_a).isdisjoint(pair_b)


def alternate(pair_a, pair_b):
    a, b = pair_a
    c, d = pair_b
    arc = set(rim_arc(a, b, 1)[1:-1])
    return (c in arc) != (d in arc)


def main():
    for frame, (left, right) in FRAMES.items():
        left_to_5 = rim_arc(left, 5, 1)
        six_to_right = rim_arc(6, right, 1)
        five_to_zero = rim_arc(5, 0, -1)
        zero_to_six = rim_arc(0, 6, -1)

        hard = {
            "omit0": (left_to_5, six_to_right),
            "omitL": (six_to_right, five_to_zero),
            "omitR": (zero_to_six, left_to_5),
        }
        for name, (first, second) in hard.items():
            assert disjoint(first, second), (frame, name, first, second)

        assert alternate((0, 5), (left, right)), frame
        assert alternate((0, 6), (left, right)), frame

    print("verified: 12 hard disjoint path pairs; 8 favourable alternations")


if __name__ == "__main__":
    main()

