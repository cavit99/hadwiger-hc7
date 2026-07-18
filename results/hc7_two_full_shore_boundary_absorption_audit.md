# Independent audit: two-full-shore boundary absorption

**Verdict:** GREEN.

**Current audited source hash:**
`f66559a43b49cdf77963f3dd64066f71da9defd69a111107e030e5a626602d8d`

This audit used a separate rerun and an independent branch-set minor
checker.  It confirms the reduction and the complete order-eight/nine
census in `hc7_two_full_shore_boundary_absorption.md`.

## 1. Mathematical reduction

Contracting the two anticomplete connected shores separately produces two
nonadjacent vertices, each complete to the literal boundary.  Thus
`I_2 vee G[S]` is genuinely a minor of the host.  If the boundary has
chromatic number at least six, `HC_6` gives a boundary `K_6` model and one
full shore gives the seventh bag.

If a vertex-minimal five-chromatic induced boundary core omits a boundary
vertex `s`, `HC_5` gives a `K_5` model in that core.  The bags
`A union {s}` and `B` are connected, disjoint, adjacent to one another,
and adjacent to every model bag.  They therefore give a literal `K_7`.
Consequently a live five-chromatic boundary must itself be
vertex-five-critical.  This verifies every noncomputational step.

## 2. Independent finite verification

The graph6 decoder was compared with nauty adjacency matrices.  A separate
static-order colouring solver reproduced the DSATUR classifications.  The
minor test was also rerun by direct enumeration of connected, pairwise
adjacent branch-set partitions rather than deletion/contraction recursion.
All per-candidate answers agreed.

The independent totals are

```text
order 8:  424 connected minimum-degree-four graphs,
          7 vertex-five-critical graphs, 0 join survivors;
order 9:  15471 connected minimum-degree-four graphs,
          236 vertex-five-critical graphs, 1 join survivor.
```

The unique survivor is graph6 `HCp`f~~`.  It has two adjacent universal
vertices, while the remaining seven vertices induce the cycle

```text
0-3-6-2-5-1-4-0.
```

Hence it is exactly `K_2 vee C_7`.  The full join with `I_2` has Hadwiger
number six: after splitting off the universal `K_2`, the remaining
`I_2 vee C_7` is the planar bipyramid and has no `K_5` minor.

## 3. Provenance and trust boundary

The order-eight conclusion independently duplicates
`archive/hadwiger_exact8_critical_core_elimination.md`, which gives a
Gallai reduction and explicit certificates for its seven critical cores.
No earlier repository theorem was found giving the order-nine unique
`K_2 vee C_7` classification.

The promoted theorem remains computer-assisted.  Its trust boundary is
nauty's complete unlabeled generation, two small exact colouring routines,
two independent exact clique-minor routines, and the Python runtime.
