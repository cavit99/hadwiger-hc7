#!/usr/bin/env python3
"""
Cycle-2 probe: maximum-contact five-part A–B spanning partitions and the
directed transfer / exchange graph on those partitions.

Finite laboratory (explicit scope, not an unbounded proof):
  - Hosts: audited 14-vertex PB path-column expansions, full K2,2 bundles,
    and larger structured path expansions (3 vertices/column) under
    column-respecting and full enumeration where feasible.
  - A,B = opposite endpoint layers (every column has an A–B path).
  - Enumerate ALL spanning partitions of V into five nonempty connected parts,
    each meeting A and B, by adjacency-restricted growth (no branch-set size
    cutoff). Contact graph J: parts adjacent iff a host edge joins them.
  - Maximum-contact = globally maximum |E(J)|.
  - Transfers: move a connected piece S from part i to part j preserving five
    nonempty connected AB-meeting parts and spanning coverage.
  - Analyse reachability, improving rank, lateral rotation components, and
    incomplete local maxima.

Invocation:
  /usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py
  /usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py --host audited
  /usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py --host larger
  /usr/bin/python3 active/hc7_pb_paired_rooted_adversarial_probe.py --mode census
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque
from itertools import combinations, product
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

Vertex = Tuple[int, int]

PB_EDGES: Set[frozenset] = {frozenset((p, r)) for p in (0, 1) for r in range(2, 7)}
PB_EDGES.update(frozenset((2 + i, 2 + ((i + 1) % 5))) for i in range(5))
COLUMNS = list(range(7))
ALL_V14: List[Vertex] = [(x, i) for x in COLUMNS for i in range(2)]
IDX14 = {v: i for i, v in enumerate(ALL_V14)}
N14 = 14
FULL14 = (1 << N14) - 1
A_MASK14 = sum(1 << IDX14[(x, 0)] for x in COLUMNS)
B_MASK14 = sum(1 << IDX14[(x, 1)] for x in COLUMNS)

AUDITED_CROSS = (
    (1, 0, 2, 1), (0, 0, 4, 1), (3, 0, 4, 0), (3, 1, 4, 0), (3, 1, 4, 1),
    (1, 0, 5, 0), (1, 1, 5, 0), (1, 1, 5, 1), (0, 0, 3, 1), (1, 0, 4, 0),
    (0, 1, 6, 0), (0, 1, 6, 1), (2, 0, 3, 0), (2, 0, 3, 1), (2, 1, 3, 0),
    (0, 0, 2, 0), (0, 0, 2, 1), (0, 1, 2, 0), (0, 1, 2, 1), (4, 0, 5, 0),
    (4, 1, 5, 0), (4, 1, 5, 1), (2, 1, 6, 0), (5, 1, 6, 1), (0, 1, 5, 1),
    (1, 0, 6, 0), (1, 0, 6, 1), (1, 1, 6, 0), (1, 1, 6, 1), (1, 0, 3, 0),
)

FOUR_COLOUR_WORDS = (
    "1021", "0040", "0041", "0140", "0141", "3140",
    "1050", "0031", "1140", "1141", "0060", "2030",
    "2031", "2130", "0020", "4150", "2060", "2160",
    "2161", "5061", "5160", "5161", "0051", "0150",
    "0151", "1061", "1030", "1031", "1130", "1131",
)

K = 5  # number of parts


def build_adj14(cross_edges: Sequence[Tuple[Vertex, Vertex]]) -> List[int]:
    adj = [0] * N14

    def add(u: Vertex, v: Vertex) -> None:
        iu, iv = IDX14[u], IDX14[v]
        adj[iu] |= 1 << iv
        adj[iv] |= 1 << iu

    for x in COLUMNS:
        add((x, 0), (x, 1))
    for u, v in cross_edges:
        add(u, v)
    return adj


def cross_from_tuples(tuples) -> List[Tuple[Vertex, Vertex]]:
    return [((a, i), (b, j)) for a, i, b, j in tuples]


def cross_from_words(words) -> List[Tuple[Vertex, Vertex]]:
    out = []
    for w in words:
        a, i, b, j = int(w[0]), int(w[1]), int(w[2]), int(w[3])
        out.append(((a, i), (b, j)))
    return out


def contact_ok14(adj: List[int]) -> bool:
    for x, y in combinations(COLUMNS, 2):
        contact = any(
            adj[IDX14[(x, i)]] & (1 << IDX14[(y, j)])
            for i in range(2) for j in range(2)
        )
        want = frozenset((x, y)) in PB_EDGES
        if contact != want:
            return False
    return True


def is_connected_mask(adj: List[int], mask: int) -> bool:
    if mask == 0:
        return False
    start = (mask & -mask).bit_length() - 1
    seen = 1 << start
    stack = [start]
    while stack:
        u = stack.pop()
        todo = adj[u] & mask & ~seen
        while todo:
            v = (todo & -todo).bit_length() - 1
            todo &= todo - 1
            seen |= 1 << v
            stack.append(v)
    return seen == mask


def bags_adjacent(adj: List[int], m1: int, m2: int) -> bool:
    x = m1
    while x:
        u = (x & -x).bit_length() - 1
        x &= x - 1
        if adj[u] & m2:
            return True
    return False


def contact_edge_count(adj: List[int], parts: Sequence[int]) -> int:
    return sum(
        1
        for i, j in combinations(range(len(parts)), 2)
        if bags_adjacent(adj, parts[i], parts[j])
    )


def mask_meets_ab(mask: int, a_mask: int, b_mask: int) -> bool:
    return bool(mask & a_mask) and bool(mask & b_mask)


def connected_subsets_containing(
    adj: List[int], universe: int, root: int
) -> List[int]:
    """All connected submasks of universe that contain root (incl. {root})."""
    # BFS growth from root inside universe
    out: List[int] = []
    # iterative: start with {root}, grow by adding neighbours in universe
    # use stack of (mask, frontier_options)
    root_bit = 1 << root
    stack = [root_bit]
    seen_masks = {root_bit}
    while stack:
        mask = stack.pop()
        out.append(mask)
        # candidates to add: neighbours of mask inside universe \ mask
        cand = 0
        x = mask
        while x:
            u = (x & -x).bit_length() - 1
            x &= x - 1
            cand |= adj[u]
        cand &= universe & ~mask
        while cand:
            v = (cand & -cand).bit_length() - 1
            cand &= cand - 1
            new_mask = mask | (1 << v)
            if new_mask not in seen_masks:
                seen_masks.add(new_mask)
                stack.append(new_mask)
    return out


def enumerate_five_part_ab_spanning(
    adj: List[int], a_mask: int, b_mask: int, full: int
) -> List[Tuple[int, ...]]:
    """
    All unordered spanning partitions into exactly K connected parts, each
    meeting A and B.

    Exact method: repeatedly take the least vertex r of the remaining set and
    choose a connected block containing r (and meeting A,B when required for
    that block). The last block is the remainder. This lists each unordered
    partition once (canonical: blocks ordered by their least vertices).
    """
    partitions: List[Tuple[int, ...]] = []

    def rec(remaining: int, blocks: List[int], parts_left: int) -> None:
        if parts_left == 1:
            if remaining == 0:
                return
            if not is_connected_mask(adj, remaining):
                return
            if not mask_meets_ab(remaining, a_mask, b_mask):
                return
            partitions.append(tuple(sorted(blocks + [remaining])))
            return
        if remaining == 0:
            return
        # least vertex in remaining
        r = (remaining & -remaining).bit_length() - 1
        # each other part needs ≥1 vertex; this block may take at most
        # popcount(remaining) - (parts_left - 1) vertices
        rem_pop = bin(remaining).count("1")
        max_block = rem_pop - (parts_left - 1)
        for S in connected_subsets_containing(adj, remaining, r):
            sz = bin(S).count("1")
            if sz > max_block:
                continue
            if not mask_meets_ab(S, a_mask, b_mask):
                continue
            # leave enough for remaining parts
            left = remaining ^ S
            if bin(left).count("1") < parts_left - 1:
                continue
            blocks.append(S)
            rec(left, blocks, parts_left - 1)
            blocks.pop()

    rec(full, [], K)
    return partitions


def connected_proper_submasks(adj: List[int], part: int) -> List[int]:
    """Nonempty proper connected submasks of part (transfer pieces)."""
    verts = []
    x = part
    while x:
        v = (x & -x).bit_length() - 1
        x &= x - 1
        verts.append(v)
    out = []
    k = len(verts)
    if k <= 1:
        return out
    for r in range(1, k):
        for comb in combinations(verts, r):
            mask = 0
            for v in comb:
                mask |= 1 << v
            if is_connected_mask(adj, mask):
                out.append(mask)
    return out


def legitimate_transfers(
    adj: List[int], parts: Tuple[int, ...], a_mask: int, b_mask: int
) -> List[Tuple[Tuple[int, ...], str]]:
    results: List[Tuple[Tuple[int, ...], str]] = []
    seen_new: Set[Tuple[int, ...]] = set()
    k = len(parts)
    for i in range(k):
        donor = parts[i]
        for S in connected_proper_submasks(adj, donor):
            donor2 = donor ^ S
            if not is_connected_mask(adj, donor2):
                continue
            if not mask_meets_ab(donor2, a_mask, b_mask):
                continue
            for j in range(k):
                if j == i:
                    continue
                recv = parts[j]
                if not bags_adjacent(adj, S, recv):
                    continue
                recv2 = recv | S
                # recv2 connected because S attaches and both connected? Not always
                # if S attaches at one point yes. Safer to check.
                if not is_connected_mask(adj, recv2):
                    continue
                if not mask_meets_ab(recv2, a_mask, b_mask):
                    continue
                new_parts = []
                for t in range(k):
                    if t == i:
                        new_parts.append(donor2)
                    elif t == j:
                        new_parts.append(recv2)
                    else:
                        new_parts.append(parts[t])
                key = tuple(sorted(new_parts))
                if key in seen_new:
                    continue
                seen_new.add(key)
                sv = []
                x = S
                while x:
                    v = (x & -x).bit_length() - 1
                    x &= x - 1
                    sv.append(v)
                cert = f"move{sv}:donor{i}->recv{j}"
                results.append((key, cert))
    return results


def analyse_exchange(
    name: str,
    adj: List[int],
    a_mask: int,
    b_mask: int,
    full: int,
    verbose_certs: int = 3,
) -> Dict[str, object]:
    n = len(adj)
    print(f"\n======== exchange analysis: {name} (n={n}) ========", flush=True)
    parts_list = enumerate_five_part_ab_spanning(adj, a_mask, b_mask, full)
    print(f"spanning five-part AB partitions: {len(parts_list)}", flush=True)
    if not parts_list:
        return {
            "name": name,
            "n": n,
            "num_partitions": 0,
            "max_contact": None,
            "num_complete": 0,
            "num_incomplete_max": 0,
            "stuck_incomplete_max": 0,
            "incomplete_local_maxima": 0,
            "note": "no spanning five-part AB partition",
        }

    contacts = [contact_edge_count(adj, p) for p in parts_list]
    max_c = max(contacts)
    complete_idxs = [i for i, c in enumerate(contacts) if c == 10]
    max_idxs = [i for i, c in enumerate(contacts) if c == max_c]
    incomplete_max = [i for i in max_idxs if contacts[i] < 10]

    hist: Dict[int, int] = defaultdict(int)
    for c in contacts:
        hist[c] += 1
    print(f"contact histogram: {dict(sorted(hist.items()))}", flush=True)
    print(
        f"max_contact={max_c} complete={len(complete_idxs)} "
        f"max_parts={len(max_idxs)} incomplete_max={len(incomplete_max)}",
        flush=True,
    )

    index_of = {p: i for i, p in enumerate(parts_list)}
    out_edges: Dict[int, List[Tuple[int, str, int, int]]] = defaultdict(list)

    expand_all = len(parts_list) <= 2500
    seeds = list(range(len(parts_list))) if expand_all else list(dict.fromkeys(max_idxs + complete_idxs))
    if not expand_all:
        # add boundary ranks
        for i, c in enumerate(contacts):
            if c >= max_c - 1 and i not in seeds:
                seeds.append(i)
            if len(seeds) > 800:
                break

    print(f"enumerating transfers from {len(seeds)} seeds (expand_all={expand_all})...", flush=True)
    for i in seeds:
        p = parts_list[i]
        for new_p, cert in legitimate_transfers(adj, p, a_mask, b_mask):
            j = index_of.get(new_p)
            if j is None:
                continue
            out_edges[i].append((j, cert, contacts[i], contacts[j]))

    improving = []
    lateral = []
    worsening = []
    for u, edges in out_edges.items():
        for v, cert, cf, ct in edges:
            if ct > cf:
                improving.append((u, v, cert, cf, ct))
            elif ct == cf:
                lateral.append((u, v, cert, cf, ct))
            else:
                worsening.append((u, v, cert, cf, ct))

    print(
        f"transfer edges: total={sum(len(v) for v in out_edges.values())} "
        f"improving={len(improving)} lateral={len(lateral)} worsening={len(worsening)}",
        flush=True,
    )

    def reachable_from(sources: Iterable[int]) -> Set[int]:
        seen: Set[int] = set(sources)
        dq = deque(sources)
        while dq:
            u = dq.popleft()
            for v, _, _, _ in out_edges.get(u, []):
                if v not in seen:
                    seen.add(v)
                    dq.append(v)
        return seen

    complete_set = set(complete_idxs)
    reach_complete_count = 0
    stuck_incomplete_max = []
    for i in incomplete_max:
        if i not in out_edges and i not in seeds:
            stuck_incomplete_max.append(i)
            continue
        reach = reachable_from([i])
        if reach & complete_set:
            reach_complete_count += 1
        else:
            stuck_incomplete_max.append(i)

    # lateral components on max
    max_set = set(max_idxs)
    lat_adj: Dict[int, Set[int]] = defaultdict(set)
    for u, v, cert, cf, ct in lateral:
        if u in max_set and v in max_set and cf == max_c:
            lat_adj[u].add(v)
            lat_adj[v].add(u)

    visited: Set[int] = set()
    components: List[List[int]] = []
    for i in max_idxs:
        if i in visited:
            continue
        if i not in seeds and i not in lat_adj:
            continue
        comp = []
        dq = deque([i])
        visited.add(i)
        while dq:
            u = dq.popleft()
            comp.append(u)
            for v in lat_adj.get(u, []):
                if v not in visited:
                    visited.add(v)
                    dq.append(v)
        components.append(comp)

    # incomplete local maxima: no contact-improving out-edge
    incomplete_local_max = []
    for i in seeds:
        if contacts[i] >= 10:
            continue
        if any(e[3] > e[2] for e in out_edges.get(i, [])):
            continue
        incomplete_local_max.append(i)

    # among ALL partitions (if expand_all), also check non-seed incomplete local max impossible
    if incomplete_max:
        print(
            f"INCOMPLETE maximum-contact: {len(incomplete_max)}; "
            f"reach complete: {reach_complete_count}; stuck: {len(stuck_incomplete_max)}",
            flush=True,
        )
        for t, i in enumerate(incomplete_max[:verbose_certs]):
            p = parts_list[i]
            miss = [
                (a, b)
                for a, b in combinations(range(K), 2)
                if not bags_adjacent(adj, p[a], p[b])
            ]
            print(
                f"  incomp_max[{t}]: c={contacts[i]} sizes={[bin(m).count('1') for m in p]} "
                f"missing={miss} masks={list(p)}",
                flush=True,
            )
    else:
        if max_c == 10:
            print("All maximum-contact partitions are COMPLETE (J≅K5).", flush=True)
        else:
            print(
                f"No incomplete_max entries; max_contact={max_c} "
                f"(complete count={len(complete_idxs)}).",
                flush=True,
            )

    print(
        f"incomplete local maxima (no improving transfer): {len(incomplete_local_max)}",
        flush=True,
    )
    for t, i in enumerate(incomplete_local_max[:verbose_certs]):
        p = parts_list[i]
        miss = [
            (a, b)
            for a, b in combinations(range(K), 2)
            if not bags_adjacent(adj, p[a], p[b])
        ]
        outs = out_edges.get(i, [])
        print(
            f"  local_max_incomp[{t}]: c={contacts[i]} sizes={[bin(m).count('1') for m in p]} "
            f"missing={miss} out_deg={len(outs)} lateral="
            f"{sum(1 for e in outs if e[3]==e[2])} masks={list(p)}",
            flush=True,
        )
        if outs:
            print(f"    sample: {outs[0][1]} -> c={outs[0][3]}", flush=True)

    # sample improving chain from min contact to max
    low = min(range(len(parts_list)), key=lambda i: contacts[i])
    if low not in out_edges:
        for new_p, cert in legitimate_transfers(adj, parts_list[low], a_mask, b_mask):
            j = index_of.get(new_p)
            if j is not None:
                out_edges[low].append((j, cert, contacts[low], contacts[j]))
    parent: Dict[int, Optional[int]] = {low: None}
    dq = deque([low])
    found_max = None
    steps = 0
    while dq and steps < 50000:
        steps += 1
        u = dq.popleft()
        if contacts[u] == max_c:
            found_max = u
            break
        if u not in out_edges and len(out_edges) < 10000:
            for new_p, cert in legitimate_transfers(adj, parts_list[u], a_mask, b_mask):
                j = index_of.get(new_p)
                if j is not None:
                    out_edges[u].append((j, cert, contacts[u], contacts[j]))
        for v, _, _, _ in out_edges.get(u, []):
            if v not in parent:
                parent[v] = u
                dq.append(v)
    if found_max is not None:
        path = []
        cur: Optional[int] = found_max
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        path.reverse()
        print(
            f"sample path min->max: len={len(path)-1} contacts={[contacts[i] for i in path]}",
            flush=True,
        )
    else:
        print("no transfer path min->max found within BFS budget.", flush=True)

    print(
        f"lateral components on max (expanded): {len(components)} "
        f"sizes={[len(c) for c in components[:12]]}",
        flush=True,
    )

    # Does every non-complete seed have an improving edge when max_c==10?
    noncomplete_seeds = [i for i in seeds if contacts[i] < max_c]
    with_imp = sum(1 for i in noncomplete_seeds if any(e[3] > e[2] for e in out_edges.get(i, [])))
    print(
        f"non-max seeds: {len(noncomplete_seeds)}; with improving transfer: {with_imp}",
        flush=True,
    )

    # Non-worsening reachability to complete (full graph when |parts| is moderate)
    bad_nw = None
    lat_complete_components = None
    if max_c == 10 and len(parts_list) <= 15000:
        print("building full transfer graph for non-worsening analysis...", flush=True)
        full_out: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)
        for i, p in enumerate(parts_list):
            for new_p, _cert in legitimate_transfers(adj, p, a_mask, b_mask):
                j = index_of.get(new_p)
                if j is not None:
                    full_out[i].append((j, contacts[i], contacts[j]))

        def reach_nw(src: int) -> bool:
            seen_r = {src}
            dq_r = deque([src])
            while dq_r:
                u = dq_r.popleft()
                if u in complete_set:
                    return True
                for v, cf, ct in full_out[u]:
                    if ct < cf:
                        continue
                    if v not in seen_r:
                        seen_r.add(v)
                        dq_r.append(v)
            return False

        incomplete_all = [i for i, c in enumerate(contacts) if c < 10]
        bad_nw = sum(1 for i in incomplete_all if not reach_nw(i))
        print(
            f"non-worsening reach: incomplete={len(incomplete_all)} "
            f"failing={bad_nw}",
            flush=True,
        )

        # lateral components among complete partitions
        lat_c: Dict[int, Set[int]] = defaultdict(set)
        for u, edges in full_out.items():
            if contacts[u] != 10:
                continue
            for v, cf, ct in edges:
                if ct == 10:
                    lat_c[u].add(v)
                    lat_c[v].add(u)
        seen_c: Set[int] = set()
        lat_sizes = []
        for i in complete_idxs:
            if i in seen_c:
                continue
            dq_c = deque([i])
            seen_c.add(i)
            sz = 0
            while dq_c:
                u = dq_c.popleft()
                sz += 1
                for v in lat_c.get(u, []):
                    if v not in seen_c:
                        seen_c.add(v)
                        dq_c.append(v)
            lat_sizes.append(sz)
        lat_complete_components = len(lat_sizes)
        print(
            f"lateral components among complete: {lat_complete_components} "
            f"sizes={sorted(lat_sizes, reverse=True)[:6]}",
            flush=True,
        )

    return {
        "name": name,
        "n": n,
        "num_partitions": len(parts_list),
        "contact_histogram": dict(sorted(hist.items())),
        "max_contact": max_c,
        "num_complete": len(complete_idxs),
        "num_max_partitions": len(max_idxs),
        "num_incomplete_max": len(incomplete_max),
        "incomplete_max_reach_complete": reach_complete_count,
        "stuck_incomplete_max": len(stuck_incomplete_max),
        "num_improving_edges": len(improving),
        "num_lateral_edges": len(lateral),
        "num_worsening_edges": len(worsening),
        "lateral_components_on_max": len(components),
        "incomplete_local_maxima": len(incomplete_local_max),
        "expand_all": expand_all,
        "bad_nonworsening": bad_nw,
        "lateral_complete_components": lat_complete_components,
        "sample_incomplete_local_max_masks": [
            list(parts_list[i]) for i in incomplete_local_max[:3]
        ],
        "sample_complete_masks": [list(parts_list[i]) for i in complete_idxs[:2]],
        "sample_incomplete_max_masks": [list(parts_list[i]) for i in incomplete_max[:3]],
    }


def full_bundles14() -> List[Tuple[Vertex, Vertex]]:
    out = []
    for e in PB_EDGES:
        x, y = tuple(e)
        for i, j in product(range(2), repeat=2):
            out.append(((x, i), (y, j)))
    return out


def build_larger_path_column(levels: int, cross_mode: str):
    verts: List[Tuple[int, int]] = [(c, t) for c in COLUMNS for t in range(levels)]
    n = len(verts)
    idx = {v: i for i, v in enumerate(verts)}
    adj = [0] * n

    def add(u, v):
        iu, iv = idx[u], idx[v]
        adj[iu] |= 1 << iv
        adj[iv] |= 1 << iu

    for c in COLUMNS:
        for t in range(levels - 1):
            add((c, t), (c, t + 1))

    if cross_mode == "full_ends":
        for e in PB_EDGES:
            x, y = tuple(e)
            for tx in (0, levels - 1):
                for ty in (0, levels - 1):
                    add((x, tx), (y, ty))
            if levels >= 3:
                mid = levels // 2
                add((x, mid), (y, mid))
    elif cross_mode == "single_ladder":
        for e in PB_EDGES:
            x, y = tuple(e)
            for t in range(levels):
                add((x, t), (y, t))
    elif cross_mode == "sparse_ends":
        for e in PB_EDGES:
            x, y = tuple(e)
            add((x, 0), (y, 0))
            add((x, levels - 1), (y, levels - 1))
    elif cross_mode == "audited_lift":
        for a, i, b, j in AUDITED_CROSS:
            ta = 0 if i == 0 else levels - 1
            tb = 0 if j == 0 else levels - 1
            add((a, ta), (b, tb))
    else:
        raise ValueError(cross_mode)

    a_mask = sum(1 << idx[(c, 0)] for c in COLUMNS)
    b_mask = sum(1 << idx[(c, levels - 1)] for c in COLUMNS)
    full = (1 << n) - 1
    return adj, a_mask, b_mask, full


def has_complete_five_pack_nonspanning(adj, a_mask, b_mask, full) -> bool:
    """Existence of five pairwise-disjoint AB-connected bags with complete contact.
    No size cutoff: enumerate AB bags by growth is hard; use all subsets for n<=14
    and for n=21 use recursive pack of AB-connected sets via connected growth of bags.
    """
    n = len(adj)
    if n <= 14:
        bags = []
        for mask in range(1, full + 1):
            if mask_meets_ab(mask, a_mask, b_mask) and is_connected_mask(adj, mask):
                bags.append(mask)
        m = len(bags)
        adjb = [0] * m
        for i in range(m):
            for j in range(i + 1, m):
                if bags[i] & bags[j] == 0 and bags_adjacent(adj, bags[i], bags[j]):
                    adjb[i] |= 1 << j
                    adjb[j] |= 1 << i

        def rec(start, chosen, used):
            if len(chosen) == 5:
                return True
            for i in range(start, m):
                if bags[i] & used:
                    continue
                if any(not ((adjb[i] >> c) & 1) for c in chosen):
                    continue
                chosen.append(i)
                if rec(i + 1, chosen, used | bags[i]):
                    return True
                chosen.pop()
            return False

        return rec(0, [], 0)
    # larger: only report via spanning complete partitions (caller)
    return False


def node_connectivity_ge5(adj: List[int]) -> bool:
    n = len(adj)
    full = (1 << n) - 1
    if n > 16:
        # too heavy for exhaustive; use min degree as weak filter only
        return min(bin(adj[i]).count("1") for i in range(n)) >= 5
    for size in range(5):
        for deleted in combinations(range(n), size):
            dmask = 0
            for i in deleted:
                dmask |= 1 << i
            rem = full ^ dmask
            if not is_connected_mask(adj, rem):
                return False
    return True


def four_colourable(adj: List[int]) -> bool:
    n = len(adj)
    if n > 16:
        return False  # unknown; do not claim
    order = sorted(range(n), key=lambda i: -bin(adj[i]).count("1"))
    colour = [-1] * n

    def rec(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        used = 0
        nbr = adj[v]
        while nbr:
            u = (nbr & -nbr).bit_length() - 1
            nbr &= nbr - 1
            if colour[u] >= 0:
                used |= 1 << colour[u]
        for c in range(4):
            if (used >> c) & 1:
                continue
            colour[v] = c
            if rec(pos + 1):
                return True
            colour[v] = -1
        return False

    return rec(0)


def run_census() -> None:
    hosts = [
        ("audited_combined_negative", cross_from_tuples(AUDITED_CROSS)),
        ("four_colour_combined_negative", cross_from_words(FOUR_COLOUR_WORDS)),
        ("full_K22_bundles", full_bundles14()),
    ]
    print("=== census (complete five-pack exhaustive; no size-cut negatives) ===")
    for name, cross in hosts:
        adj = build_adj14(cross)
        assert contact_ok14(adj), name
        k5 = node_connectivity_ge5(adj)
        chi4 = four_colourable(adj) if k5 else None
        # complete via spanning partition max contact
        parts = enumerate_five_part_ab_spanning(adj, A_MASK14, B_MASK14, FULL14)
        max_c = max((contact_edge_count(adj, p) for p in parts), default=-1)
        pr = max_c == 10
        print(f"{name}: kappa5={k5} 4col={chi4} max_contact={max_c} complete_pack={pr} nparts={len(parts)}")


def run_exchange(host_filter: str) -> List[Dict[str, object]]:
    reports: List[Dict[str, object]] = []
    if host_filter in ("all", "audited", "14"):
        for name, cross in [
            ("audited_combined_negative", cross_from_tuples(AUDITED_CROSS)),
            ("four_colour_combined_negative", cross_from_words(FOUR_COLOUR_WORDS)),
        ]:
            adj = build_adj14(cross)
            assert contact_ok14(adj), name
            reports.append(analyse_exchange(name, adj, A_MASK14, B_MASK14, FULL14))
    if host_filter in ("all", "full", "14"):
        adj = build_adj14(full_bundles14())
        assert contact_ok14(adj)
        reports.append(analyse_exchange("full_K22_bundles", adj, A_MASK14, B_MASK14, FULL14))
    if host_filter in ("all", "larger"):
        for levels, mode in [
            (3, "sparse_ends"),
            (3, "single_ladder"),
            (3, "audited_lift"),
            (3, "full_ends"),
        ]:
            adj, a_mask, b_mask, full = build_larger_path_column(levels, mode)
            name = f"path_L{levels}_{mode}"
            reports.append(analyse_exchange(name, adj, a_mask, b_mask, full, verbose_certs=2))
    return reports


def main(argv: Optional[Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("exchange", "census"), default="exchange")
    parser.add_argument(
        "--host", choices=("all", "audited", "full", "14", "larger"), default="all"
    )
    args = parser.parse_args(argv)

    if args.mode == "census":
        run_census()
        return

    reports = run_exchange(args.host)
    print("\n======== CYCLE-2 SUMMARY ========")
    for r in reports:
        print(
            f"{r['name']}: parts={r.get('num_partitions')} max_c={r.get('max_contact')} "
            f"complete={r.get('num_complete')} incomp_max={r.get('num_incomplete_max')} "
            f"stuck={r.get('stuck_incomplete_max')} "
            f"incomp_local_max={r.get('incomplete_local_maxima')} "
            f"lat_comp={r.get('lateral_components_on_max')}"
        )

    print("\n--- exchange lemma diagnostics ---")
    any_stuck = any((r.get("stuck_incomplete_max") or 0) > 0 for r in reports)
    any_incomp_local = any((r.get("incomplete_local_maxima") or 0) > 0 for r in reports)
    any_complete = any((r.get("num_complete") or 0) > 0 for r in reports)
    print(f"any_incomplete_max_stuck_away_from_complete: {any_stuck}")
    print(f"any_incomplete_local_maxima: {any_incomp_local}")
    print(f"any_host_with_complete_pack: {any_complete}")
    if any_incomp_local:
        print(
            "OBSTRUCTION: incomplete local maximum under contact-improving "
            "connected-piece transfers (see certificates)."
        )
    elif any_complete and not any_stuck:
        print(
            "POSITIVE FINITE PATTERN: whenever complete packs exist, no incomplete "
            "maximum-contact partition is stuck away from complete; check local-max data."
        )
    # tautology note
    print(
        "NOTE: a globally maximum-contact incomplete partition cannot have a "
        "contact-increasing transfer to complete (contact already maximal). "
        "Stuck incomplete_max is therefore automatic when max_contact<10. "
        "The nontrivial signal is incomplete_local_maxima and lateral rotation "
        "structure among max-contact partitions when max_contact=10."
    )


if __name__ == "__main__":
    main()
