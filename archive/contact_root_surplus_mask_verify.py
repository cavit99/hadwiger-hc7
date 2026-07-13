"""Verify the five maximal bad mask orbits in Proposition 2.3.

Mask 0 is the uncontacted helper. Masks 1..4 are contacted bags.
The three bits are the three rooted pieces.
"""

from functools import reduce
from itertools import permutations, product
from operator import or_


def partitions_of_five_into_three():
    result = []

    def visit(i, blocks):
        if i == 5:
            if len(blocks) == 3:
                result.append(tuple(tuple(block) for block in blocks))
            return
        for k in range(len(blocks)):
            blocks[k].append(i)
            visit(i + 1, blocks)
            blocks[k].pop()
        if len(blocks) < 3:
            blocks.append([i])
            visit(i + 1, blocks)
            blocks.pop()

    visit(0, [])
    return result


PARTITIONS = partitions_of_five_into_three()


def block_union(masks, block):
    return reduce(or_, (masks[i] for i in block), 0)


def good(masks):
    return any(
        all(
            any(i > 0 for i in block) and block_union(masks, block) == 7
            for block in partition
        )
        for partition in PARTITIONS
    )


def two_helper_good(masks):
    """Theorem 2.4: U helps p, contacted h helps q, others all see k."""
    for helper in range(1, 5):
        for p, q, k in permutations(range(3)):
            if not (masks[0] & (1 << p)):
                continue
            if not (masks[helper] & (1 << q)):
                continue
            if all(
                masks[j] & (1 << k)
                for j in range(1, 5)
                if j != helper
            ):
                return True
    return False


def good_with_helpers(masks):
    return good(masks) or two_helper_good(masks)


def permute_mask(mask, coordinate_permutation):
    result = 0
    for old in range(3):
        if mask & (1 << old):
            result |= 1 << coordinate_permutation[old]
    return result


def canonical(masks):
    candidates = []
    for coordinate_permutation in permutations(range(3)):
        moved = [
            permute_mask(mask, coordinate_permutation) for mask in masks
        ]
        for label_permutation in permutations(range(1, 5)):
            candidates.append(
                (moved[0],) + tuple(moved[i] for i in label_permutation)
            )
    return min(candidates)


def main():
    bad = [
        masks for masks in product(range(1, 8), repeat=5) if not good(masks)
    ]
    maximal = []
    for masks in bad:
        is_maximal = True
        for i, mask in enumerate(masks):
            for bit in (1, 2, 4):
                if mask & bit:
                    continue
                enlarged = list(masks)
                enlarged[i] |= bit
                if not good(tuple(enlarged)):
                    is_maximal = False
                    break
            if not is_maximal:
                break
        if is_maximal:
            maximal.append(masks)

    expected = {
        (3, 3, 3, 7, 7),
        (7, 1, 2, 4, 7),
        (7, 3, 3, 3, 7),
        (7, 3, 3, 5, 5),
        (7, 3, 3, 5, 6),
    }
    observed = {canonical(masks) for masks in maximal}

    assert len(PARTITIONS) == 25
    assert len(bad) == 13908
    assert len(maximal) == 108
    assert observed == expected, (observed, expected)

    helper_bad = [
        masks
        for masks in product(range(1, 8), repeat=5)
        if not good_with_helpers(masks)
    ]
    helper_maximal = []
    for masks in helper_bad:
        is_maximal = True
        for i, mask in enumerate(masks):
            for bit in (1, 2, 4):
                if mask & bit:
                    continue
                enlarged = list(masks)
                enlarged[i] |= bit
                if not good_with_helpers(tuple(enlarged)):
                    is_maximal = False
                    break
            if not is_maximal:
                break
        if is_maximal:
            helper_maximal.append(masks)

    helper_expected = {
        (1, 1, 3, 7, 7),
        (1, 1, 6, 6, 6),
        (1, 3, 3, 5, 5),
        (3, 1, 2, 7, 7),
        (3, 1, 3, 6, 6),
        (3, 3, 3, 3, 3),
        (7, 1, 1, 1, 1),
        (7, 1, 1, 6, 6),
        (7, 1, 2, 4, 7),
        (7, 1, 2, 5, 6),
    }
    helper_observed = {canonical(masks) for masks in helper_maximal}
    assert len(helper_bad) == 5778
    assert len(helper_maximal) == 330
    assert helper_observed == helper_expected

    def matched_good(masks):
        helper = masks[0]
        roots = masks[1:]
        for paired_root in range(3):
            singleton_roots = [
                roots[i] for i in range(3) if i != paired_root
            ]
            if (
                all(mask == 7 for mask in singleton_roots)
                and (roots[paired_root] | helper) == 7
            ):
                return True
        return False

    matched_bad = [
        masks
        for masks in product(range(1, 8), repeat=4)
        if not matched_good(masks)
    ]
    matched_maximal = []
    for masks in matched_bad:
        is_maximal = True
        for i, mask in enumerate(masks):
            for bit in (1, 2, 4):
                if mask & bit:
                    continue
                enlarged = list(masks)
                enlarged[i] |= bit
                if not matched_good(tuple(enlarged)):
                    is_maximal = False
                    break
            if not is_maximal:
                break
        if is_maximal:
            matched_maximal.append(masks)

    def matched_canonical(masks):
        candidates = []
        for coordinate_permutation in permutations(range(3)):
            moved = [
                permute_mask(mask, coordinate_permutation) for mask in masks
            ]
            for label_permutation in permutations(range(1, 4)):
                candidates.append(
                    (moved[0],)
                    + tuple(moved[i] for i in label_permutation)
                )
        return min(candidates)

    matched_expected = {
        (3, 3, 7, 7),
        (7, 3, 3, 7),
        (7, 3, 5, 7),
    }
    matched_observed = {
        matched_canonical(masks) for masks in matched_maximal
    }
    assert len(matched_bad) == 2340
    assert len(matched_maximal) == 36
    assert matched_observed == matched_expected
    print(
        "verified: 5 base triple-root, 10 two-helper triple-root, "
        "and 3 matched-frame maximal bad orbits"
    )


if __name__ == "__main__":
    main()
