# Independent audit: cycle completion from two adjacent pairs

**Verdict:** **GREEN** for Theorem 2.1 and Corollaries 2.2--2.3 at the exact
revision below.  This is a separate internal mathematical audit, not
external peer review.  The result does not prove `HC_7`.

## Audited revision

This audit checks the complete source file
[`hc7_adjacent_full_pair_cycle_completion.md`](hc7_adjacent_full_pair_cycle_completion.md)
at SHA-256

```text
304b3403faafa0e6328979db807bb65c32067541e6b722049582060b4fbc468d
```

The status-only promoted revision has SHA-256

```text
20c0e37056fab8dff204511a5d776000a90614b3e6d520118be7d4235c2de165
```

It changes only the status paragraph to link this audit; the theorem,
proof, dependencies, and trust boundary are unchanged.

The source was split from the previously GREEN-audited combined draft and
restated without any colouring or shore-response hypothesis.  Its branch-set
argument and both corollaries were independently rechecked below.  No
unresolved mathematical assumption or gap remains at this revision.

## 1. Self-contained hypotheses and branch-set connectivity

The split formulation assumes directly that

```text
A_d, A_e, Q_0, Q_1
```

are four pairwise vertex-disjoint connected subgraphs of `G-S`.  This is the
exact disjointness formerly supplied by placing the defect-one pair and the
boundary-full pair on opposite open shores.  The new direct hypothesis is
sufficient and does not depend on a colouring response.

Let `C` be a cycle in `G[S-{d,e}]`.  It has order between three and six.
Partitioning its cyclic order into three nonempty consecutive arcs gives
pairwise disjoint connected sets `M_1,M_2,M_3`; the three transition edges
make them pairwise adjacent for every possible cycle order, including six.

The seven displayed branch sets are pairwise disjoint.  The four original
subgraphs lie outside `S`; the roots `d,e` are distinct and avoid `C`; and
the three arc sets use only vertices of `C`.  The sets

```text
V(A_d) union {e},   V(A_e) union {d}
```

are connected because exact defect `d` makes `A_d` adjacent to `e`, and
exact defect `e` makes `A_e` adjacent to `d`.

## 2. All twenty-one adjacencies

Every pair of branch sets is adjacent, with the following exhaustive count:

| Branch-set pairs | Count | Supplying edge or hypothesis |
|---|---:|---|
| `Q_0,Q_1` | 1 | their assumed adjacency |
| one `Q_j` and one augmented defect set | 4 | the `Q_j` contact at `e` or `d` |
| one `Q_j` and one cycle arc | 6 | boundary fullness of `Q_j` |
| the two augmented defect sets | 1 | the `A_d`--`A_e` adjacency |
| one augmented defect set and one cycle arc | 6 | (1.2), since the arc avoids `d,e` |
| two distinct cycle arcs | 3 | the three transition edges of `C` |

The total is `1+4+6+1+6+3=21`.  Hence the seven displayed connected,
disjoint sets form an explicit `K_7`-minor model.  No unused boundary vertex
is required.  This is why the proof covers a six-cycle, whereas the earlier
construction for potentially nonadjacent full subgraphs stopped at cycle
order five.

## 3. Forest and odd-path corollaries

Corollary 2.2 is the immediate contrapositive of Theorem 2.1.

For Corollary 2.3, forest normalization implies that neither of two
vertex-disjoint odd cycles in `G[S]` can avoid both roots.  Each cycle meets
`{d,e}`.  Disjointness then forces one root into each cycle and prevents
either cycle from containing the other root; otherwise the second cycle
would contain neither.

Deleting the root from a simple cycle leaves a path between two distinct
neighbours of that root.  If the path has `ell` edges, its original cycle
has `ell+2` edges, so the path has odd length.  The two paths remain
vertex-disjoint and lie in the forest `G[S-{d,e}]`.  This verifies every
assertion of Corollary 2.3.

## 4. Split preservation, comparison, and live scope

The split preserves the complete response-free cycle theorem, the forest
normalization, and the two-rooted odd-path consequence from the GREEN
combined revision.  It removes all merged-response and Kempe-path language.
The stronger direct assumption that all four open subgraphs are pairwise
disjoint is exactly what the branch-set proof needs after removal of the
two-shore notation.

The theorem is not currently an immediate active-spine input.  Maximal
coverage supplies adjacent boundary-full pieces on the connected
split-response shore, but no current theorem also supplies adjacent
defect-one pieces on the opposite merged-response shore.  The closed two-cut
branch supplies adjacent defect-one pieces, but its two full subgraphs are
separate components and its response orientation is different.  The source
states this limitation accurately.

Lemma 1.1 of the audited
[`hc7_order8_strict_reversal_completion.md`](hc7_order8_strict_reversal_completion.md)
is the closest promoted predecessor.  It handles cycles of order at most
five without requiring the two boundary-full subgraphs adjacent.  The
present theorem trades the added adjacency hypothesis for coverage of the
six-cycle.  Corollary 2.3 isolates a parity argument already used inside the
strict-reversal and two-cut proofs.  No external theorem is used.

Subject to its explicit conditional scope, the source is GREEN at the
pinned hash.

## Status-only promotion

After this audit, only the source status line was changed to link this
GREEN audit.  The promoted source has SHA-256

```text
20c0e37056fab8dff204511a5d776000a90614b3e6d520118be7d4235c2de165
```

No theorem statement, proof, dependency, or trust-boundary text changed.
