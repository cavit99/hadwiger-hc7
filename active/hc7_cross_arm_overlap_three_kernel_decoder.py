#!/usr/bin/env python3
"""Exploratory proof-producing decoder for rigid overlap-three cells.

This deliberately separates original support edges from the adjacencies of
a terminal-rooted three-connected kernel.  It is an active experiment, not
yet a proof dependency.
"""

from __future__ import annotations

import argparse
import itertools


def pair(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def partitions(items: tuple[int, ...], block_count: int):
    blocks: list[list[int]] = []

    def visit(index: int):
        if index == len(items):
            if len(blocks) == block_count:
                yield tuple(tuple(block) for block in blocks)
            return
        item = items[index]
        for position in range(len(blocks)):
            blocks[position].append(item)
            yield from visit(index + 1)
            blocks[position].pop()
        if len(blocks) < block_count:
            blocks.append([item])
            yield from visit(index + 1)
            blocks.pop()

    yield from visit(0)


def connected(edge_mask: int, pair_index: dict[tuple[int, int], int], vertices: tuple[int, ...]) -> bool:
    reached = {vertices[0]}
    frontier = [vertices[0]]
    while frontier:
        u = frontier.pop()
        for v in vertices:
            if v not in reached and edge_mask >> pair_index[pair(u, v)] & 1:
                reached.add(v)
                frontier.append(v)
    return len(reached) == len(vertices)


def touch(edge_mask: int, pair_index: dict[tuple[int, int], int], left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    return any(edge_mask >> pair_index[pair(u, v)] & 1 for u in left for v in right)


def partition_specs(n: int, target: int):
    pair_index = {e: i for i, e in enumerate(itertools.combinations(range(n), 2))}
    answer = []
    for support_size in range(target, n + 1):
        for support in itertools.combinations(range(n), support_size):
            for bags in partitions(support, target):
                internal = []
                for bag in bags:
                    if len(bag) <= 1:
                        trees = (0,)
                    else:
                        bag_pairs = tuple(itertools.combinations(bag, 2))
                        trees_list = []
                        for chosen in itertools.combinations(bag_pairs, len(bag) - 1):
                            reached = {bag[0]}
                            while True:
                                old = len(reached)
                                reached.update(v for u, v in chosen if u in reached)
                                reached.update(u for u, v in chosen if v in reached)
                                if len(reached) == old:
                                    break
                            if len(reached) == len(bag):
                                trees_list.append(sum(1 << pair_index[pair(u, v)] for u, v in chosen))
                        trees = tuple(trees_list)
                    internal.append(trees)
                cross = tuple(
                    sum(1 << pair_index[pair(u, v)] for u in a for v in b)
                    for a, b in itertools.combinations(bags, 2)
                )
                answer.append((bags, tuple(internal), cross))
    return tuple(answer)


def has_k_minor(edge_mask: int, specs) -> tuple[tuple[int, ...], ...] | None:
    for bags, internal, cross in specs:
        if not all(edge_mask & mask for mask in cross):
            continue
        good = True
        for trees in internal:
            if not any(edge_mask & tree == tree for tree in trees):
                good = False
                break
        if good:
            return bags
    return None


def local_allowed_six() -> tuple[tuple[int, int], ...]:
    pairs = tuple(itertools.combinations(range(6), 2))
    answer = []
    for edges in range(1 << 15):
        def adjacent(u: int, v: int) -> bool:
            return bool(edges >> pairs.index(pair(u, v)) & 1)

        exact = False
        for x, y in pairs:
            if not adjacent(x, y):
                continue
            core = tuple(v for v in range(6) if v not in (x, y))
            if all(adjacent(u, v) for u, v in itertools.combinations(core, 2)) and all(
                adjacent(x, z) or adjacent(y, z) for z in core
            ):
                exact = True
                break
        literal = any(
            all(adjacent(u, v) for u, v in itertools.combinations(five, 2))
            for five in itertools.combinations(range(6), 5)
        )
        if exact and not literal:
            ones = sum(1 << i for i in range(15) if edges >> i & 1)
            zeros = ((1 << 15) - 1) ^ ones
            answer.append((ones, zeros))
    assert len(answer) == 375
    return tuple(answer)


LOCAL_SIX = local_allowed_six()


def build_cell(arm_order: int):
    if arm_order == 5:
        n = 9
        a = tuple(range(6))
        common = (0, 1, 2)
        x = common + (6,)
        p, q = 7, 8
        terminals = (3, 4, 5, 6, 7, 8)
    elif arm_order == 6:
        n = 10
        a = tuple(range(6))
        common = (0, 1, 2)
        x = common + (6, 7)
        p, q = 8, 9
        terminals = (3, 4, 5, 6, 7, 8, 9)
    else:
        raise ValueError(arm_order)
    supports_six = [a]
    literal_fives = []
    if arm_order == 5:
        literal_fives.extend((x + (p,), x + (q,)))
    else:
        supports_six.extend((x + (p,), x + (q,)))
    for omitted in common:
        base = tuple(v for v in a if v != omitted)
        supports_six.extend((base + (p,), base + (q,)))
    return n, a, common, x, p, q, terminals, tuple(supports_six), tuple(literal_fives)


def global_patterns(support: tuple[int, ...], all_pair_index: dict[tuple[int, int], int]):
    local_pairs = tuple(itertools.combinations(range(6), 2))
    indices = tuple(all_pair_index[pair(support[u], support[v])] for u, v in local_pairs)
    patterns = []
    for local_ones, local_zeros in LOCAL_SIX:
        ones = sum(1 << indices[i] for i in range(15) if local_ones >> i & 1)
        zeros = sum(1 << indices[i] for i in range(15) if local_zeros >> i & 1)
        patterns.append((ones, zeros))
    return tuple(patterns)


def joined_states(arm_order: int):
    n, a, common, x, p, q, terminals, supports, literal_fives = build_cell(arm_order)
    all_pairs = tuple(itertools.combinations(range(n), 2))
    pair_index = {e: i for i, e in enumerate(all_pairs)}
    constraints = [global_patterns(s, pair_index) for s in supports]
    fixed_ones = 0
    for five in literal_fives:
        for edge in itertools.combinations(five, 2):
            fixed_ones |= 1 << pair_index[edge]
    states: set[tuple[int, int]] = set()

    def visit(done: frozenset[int], ones: int, zeros: int):
        if ones & zeros:
            return
        if len(done) == len(constraints):
            states.add((ones, zeros))
            return
        selected = -1
        compatible = None
        for i, patterns in enumerate(constraints):
            if i in done:
                continue
            options = [pat for pat in patterns if not (pat[0] & zeros or pat[1] & ones)]
            if compatible is None or len(options) < len(compatible):
                selected, compatible = i, options
        assert compatible is not None
        seen = set()
        for pones, pzeros in compatible:
            new = (ones | pones, zeros | pzeros)
            if new not in seen:
                seen.add(new)
                visit(done | {selected}, *new)

    visit(frozenset(), fixed_ones, 0)
    return build_cell(arm_order), all_pairs, pair_index, states


def completions(states: set[tuple[int, int]], pair_count: int):
    full = (1 << pair_count) - 1
    for ones, zeros in states:
        unknown = full & ~(ones | zeros)
        bits = [1 << i for i in range(pair_count) if unknown >> i & 1]
        for choice in range(1 << len(bits)):
            yield ones | sum(bit for i, bit in enumerate(bits) if choice >> i & 1)


def common_rooted_k4(
    edges: int,
    n: int,
    a: tuple[int, ...],
    common: tuple[int, ...],
    p: int,
    q: int,
) -> tuple[int, tuple[tuple[int, ...], ...]] | None:
    pair_index = {e: i for i, e in enumerate(itertools.combinations(range(n), 2))}
    for root in common:
        available = tuple(v for v in a if v != root)
        for support_size in (4, 5):
            for support in itertools.combinations(available, support_size):
                for bags in partitions(support, 4):
                    if not all(connected(edges, pair_index, bag) for bag in bags):
                        continue
                    if not all(touch(edges, pair_index, left, right) for left, right in itertools.combinations(bags, 2)):
                        continue
                    if all(
                        all(any(edges >> pair_index[pair(named, vertex)] & 1 for vertex in bag) for bag in bags)
                        for named in (root, p, q)
                    ):
                        return root, bags
    return None


def cycle_masks(terminals: tuple[int, ...], pair_index: dict[tuple[int, int], int]):
    first = terminals[0]
    for tail in itertools.permutations(terminals[1:]):
        order = (first,) + tail
        if order[1] > order[-1]:
            continue
        mask = sum(
            1 << pair_index[pair(order[i], order[(i + 1) % len(order)])]
            for i in range(len(order))
        )
        yield order, mask


def fan_masks(terminals: tuple[int, ...], pair_index: dict[tuple[int, int], int]):
    """All labelled copies of F_k=K_1 join P_{k-1}."""
    for centre in terminals:
        rest = tuple(v for v in terminals if v != centre)
        for path in itertools.permutations(rest):
            if path[0] > path[-1]:
                continue
            mask = sum(1 << pair_index[pair(centre, v)] for v in rest)
            mask |= sum(1 << pair_index[pair(path[i], path[i + 1])] for i in range(len(path) - 1))
            yield (centre, path), mask


def k34_masks(terminals: tuple[int, ...], pair_index: dict[tuple[int, int], int]):
    assert len(terminals) == 7
    for left in itertools.combinations(terminals, 3):
        right = tuple(v for v in terminals if v not in left)
        mask = sum(1 << pair_index[pair(u, v)] for u in left for v in right)
        yield (left, right), mask


def wheel_masks(terminals: tuple[int, ...], pair_index: dict[tuple[int, int], int]):
    """All labelled wheels with one terminal hub and all other terminals on the rim."""
    for centre in terminals:
        rim = tuple(v for v in terminals if v != centre)
        first = rim[0]
        for tail in itertools.permutations(rim[1:]):
            cycle = (first,) + tail
            if cycle[1] > cycle[-1]:
                continue
            mask = sum(1 << pair_index[pair(centre, v)] for v in rim)
            mask |= sum(
                1 << pair_index[pair(cycle[i], cycle[(i + 1) % len(cycle)])]
                for i in range(len(cycle))
            )
            yield (centre, cycle), mask


def is_three_connected(mask: int, vertices: tuple[int, ...], pair_index: dict[tuple[int, int], int]) -> bool:
    if len(vertices) < 4:
        return False
    for removed_size in (0, 1, 2):
        for removed in itertools.combinations(vertices, removed_size):
            remaining = tuple(v for v in vertices if v not in removed)
            reached = {remaining[0]}
            frontier = [remaining[0]]
            while frontier:
                u = frontier.pop()
                for v in remaining:
                    if v not in reached and mask >> pair_index[pair(u, v)] & 1:
                        reached.add(v)
                        frontier.append(v)
            if len(reached) != len(remaining):
                return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm-order", type=int, choices=(5, 6), required=True)
    parser.add_argument("--carrier", choices=("none", "cycle", "fan", "adaptive-fan", "wheel", "split-wheel", "k34", "kernel"), default="none")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    cell, pairs, pair_index, states = joined_states(args.arm_order)
    n, a, common, x, p, q, terminals, supports, literal_fives = cell
    print(f"arm_order={args.arm_order} n={n} terminals={terminals} constraints={len(supports)} literal={len(literal_fives)} joined={len(states)}")
    unknown_hist = {}
    for ones, zeros in states:
        unknown_hist[(len(pairs) - (ones | zeros).bit_count())] = unknown_hist.get(len(pairs) - (ones | zeros).bit_count(), 0) + 1
    print("unknown_hist", sorted(unknown_hist.items()))
    specs = partition_specs(n, 7)
    total = direct = common_count = 0
    examples = []
    seen = set()
    for edges in completions(states, len(pairs)):
        if edges in seen:
            continue
        seen.add(edges)
        total += 1
        common_model = common_rooted_k4(edges, n, a, common, p, q)
        if common_model is not None:
            common_count += 1
            continue
        model = has_k_minor(edges, specs)
        if model is not None:
            direct += 1
        elif len(examples) < 3:
            examples.append(edges)
        if args.limit and total >= args.limit:
            break
    print(f"original_completions={total} common={common_count} original_k7={direct} original_survivors={total-common_count-direct}")
    for edges in examples:
        missing = [e for i, e in enumerate(pairs) if not (edges >> i & 1)]
        print("survivor_nonedges", missing)

    if args.carrier != "none":
        original_survivors = []
        seen.clear()
        for edges in completions(states, len(pairs)):
            if edges in seen:
                continue
            seen.add(edges)
            if common_rooted_k4(edges, n, a, common, p, q) is None and has_k_minor(edges, specs) is None:
                original_survivors.append(edges)
        if args.carrier == "split-wheel":
            larger_n = n + 1
            carrier_vertex = n
            larger_pairs = tuple(itertools.combinations(range(larger_n), 2))
            larger_index = {edge: i for i, edge in enumerate(larger_pairs)}
            larger_specs = partition_specs(larger_n, 7)

            def lift(mask: int) -> int:
                return sum(
                    1 << larger_index[edge]
                    for i, edge in enumerate(pairs)
                    if mask >> i & 1
                )

            bad = []
            tested = 0
            for edges in original_survivors:
                good = tuple(
                    terminal
                    for terminal in terminals
                    if all(edges >> pair_index[pair(terminal, vertex)] & 1 for vertex in common)
                )
                if len(good) != 5:
                    bad.append(("bad-good-set", edges))
                    continue
                bad_root = next(vertex for vertex in terminals if vertex not in good)
                first = good[0]
                for tail in itertools.permutations(good[1:]):
                    rim = (first,) + tail
                    if rim[1] > rim[-1]:
                        continue
                    virtual = sum(
                        1 << larger_index[pair(rim[i], rim[(i + 1) % 5])]
                        for i in range(5)
                    )
                    virtual |= sum(
                        1 << larger_index[pair(carrier_vertex, vertex)] for vertex in good
                    )
                    virtual |= 1 << larger_index[pair(carrier_vertex, bad_root)]
                    tested += 1
                    if has_k_minor(lift(edges) | virtual, larger_specs) is None:
                        bad.append((bad_root, rim, edges))
            print(f"carrier=split-wheel patterns={tested} bad_patterns={len(bad)}")
            for record in bad[:10]:
                print("bad_split_wheel", record)
            return
        if args.carrier == "cycle":
            carriers = tuple(cycle_masks(terminals, pair_index))
        elif args.carrier == "fan":
            carriers = tuple(fan_masks(terminals, pair_index))
        elif args.carrier == "adaptive-fan":
            carriers = ()
        elif args.carrier == "k34":
            carriers = tuple(k34_masks(terminals, pair_index))
        elif args.carrier == "wheel":
            carriers = tuple(wheel_masks(terminals, pair_index))
        else:
            carriers = ()
        if args.carrier == "adaptive-fan":
            bad = []
            for order, cycle in cycle_masks(terminals, pair_index):
                fan_by_centre = []
                for centre in terminals:
                    virtual = cycle | sum(
                        1 << pair_index[pair(centre, v)] for v in terminals if v != centre
                    )
                    fan_by_centre.append((centre, virtual))
                survivor = None
                for edges in original_survivors:
                    if all(has_k_minor(edges | virtual, specs) is None for _, virtual in fan_by_centre):
                        survivor = edges
                        break
                if survivor is not None:
                    bad.append((order, survivor))
            print(f"carrier=adaptive-fan cycle_orders=60 bad_orders={len(bad)}")
            for order, edges in bad[:10]:
                missing = [e for i, e in enumerate(pairs) if not (edges >> i & 1)]
                print("bad_adaptive_fan", order, "nonedges", missing)
        elif args.carrier != "kernel":
            bad = []
            for label, virtual in carriers:
                survivor = None
                for edges in original_survivors:
                    if has_k_minor(edges | virtual, specs) is None:
                        survivor = edges
                        break
                if survivor is not None:
                    bad.append((label, survivor))
            print(f"carrier={args.carrier} patterns={len(carriers)} bad_patterns={len(bad)}")
            for label, edges in bad[:10]:
                missing = [e for i, e in enumerate(pairs) if not (edges >> i & 1)]
                print("bad_carrier", label, "nonedges", missing)
        else:
            terminal_pair_mask = sum(1 << pair_index[e] for e in itertools.combinations(terminals, 2))
            witness = None
            tested = 0
            for edges in original_survivors:
                missing = terminal_pair_mask & ~edges
                bits = [1 << i for i in range(len(pairs)) if missing >> i & 1]
                for count in range(len(bits) + 1):
                    for chosen in itertools.combinations(bits, count):
                        kernel = (edges & terminal_pair_mask) | sum(chosen)
                        if not is_three_connected(kernel, terminals, pair_index):
                            continue
                        tested += 1
                        if has_k_minor(edges | kernel, specs) is None:
                            witness = (edges, kernel)
                            break
                    if witness:
                        break
                if witness:
                    break
            print(f"carrier=kernel tested_three_connected={tested} bad={witness is not None}")
            if witness:
                edges, kernel = witness
                original_missing = [e for i, e in enumerate(pairs) if not (edges >> i & 1)]
                kernel_edges = [e for e in itertools.combinations(terminals, 2) if kernel >> pair_index[e] & 1]
                print("bad_original_nonedges", original_missing)
                print("bad_kernel_edges", kernel_edges)


if __name__ == "__main__":
    main()
