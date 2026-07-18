# Audit of the connected-row cyclic-corner dichotomy

**Verdict: GREEN.**  This is a separate internal audit, not external peer
review.

**Audited source revision:**
[`hc7_connected_row_cyclic_corner_dichotomy.md`](hc7_connected_row_cyclic_corner_dichotomy.md)

**Audited SHA-256:**
`cc3c6012b32e8f0116e4c3863ad9cbd7199620419ab2d8df9b3de517000029c2`

The promoted revision differs from the previously audited source only in
the status line: `independent audit pending` was replaced by `separate
internal audit`.  Reversing that metadata-only edit reproduces the prior
audited SHA-256
`67e6c26aa4b118f1df7c7e5bfebe95d818e56165a043182988cdd18c494ced30`.
The mathematical statement and proof are unchanged.

## Dependency and the matching-defect construction

Lemma 2.1 uses Theorem 4.2 of
[`hc7_degree8_contact_allocation.md`](hc7_degree8_contact_allocation.md),
whose source hash
`84c47863546f9800db24bf042e60952221dcf3649b4076170259efa9fde78049`
has a separate GREEN audit.  The substitution made here preserves every
hypothesis of that theorem:

- each singleton boundary label `b_j` is replaced everywhere by one
  connected set `P_j`;
- a mixed branch set is enlarged to `P_j union C_i` only for a present
  `P_j`--`C_i` adjacency;
- the five `C_i` remain cyclically adjacent and each contains a specified
  neighbour of `v`;
- `v` is adjacent to every `P_j`; and
- `D` is adjacent to the seven labels `P_0,P_1,P_2,C_0,C_1,C_2,C_3`.

The displayed sets in (1.3) make all six expanded branch sets and `D`
pairwise disjoint.  The allocation table never uses an edge between two
vertices of `B`; replacing the three boundary vertices by pairwise adjacent
connected sets therefore loses no required edge.  If `D` is anticomplete to
`C_4`, the allocation table places `C_4` with one of the other seven labels,
so the enlarged branch set still has an edge to `D`.  Thus every one of the
six local branch sets is adjacent to `D`.

## The explicit seven-branch-set model

The seven sets in (2.3) are connected and pairwise disjoint.  All twenty-one
required adjacencies are present:

- the three `P_j` are pairwise adjacent;
- every `P_j` is adjacent to each of the three sector branch sets because
  those sets contain only `C_0,C_1,C_2,C_3`, apart from the harmless added
  `C_4` in `C_4 union C_0`;
- the sector sets are pairwise adjacent through `C_0C_1`, `C_1C_2`, and
  `C_3C_4`; and
- (1.6) gives every adjacency from `D` to the other six sets, using `C_0`
  for `C_4 union C_0` and `C_2` or `C_3` for `C_2 union C_3`.

No adjacency from `D` to `C_4` and no edge inside `B` is used.

## Exact separator and strict descent

For Lemma 3.1, `X=C_i` consists of `r=u_i` and vertices of `L`, while the
missed set `P_j` lies in `R union {b_j}`.  Since `P_j` is anticomplete to
`X`, `S=N_G(X)` is a genuine separator and decomposes as
`S_L dotunion S_T dotunion S_R`.

Deleting

`K_R=(T-{r}) union S_R`

separates the surviving set `X` from the surviving nonempty set
`P_j cap R`: a path from `X` to `R` must leave through `r`, and every
`R`-neighbour of `r` is in `S_R`.  Hence seven-connectivity gives
`|K_R|=6+|S_R|>=7`.  When `|S_R|=1`, this is an actual nontrivial
order-seven separation.  In particular, every component on either side has
all seven separator vertices in its neighbourhood; otherwise its
neighbourhood would have order at most six.

For every component `A` of `X-{r}`, connectedness of `X` gives
`r in N_G(A)`.  No two such components are adjacent, no vertex of `A` has a
neighbour in `R`, and every neighbour outside `X` lies in `S`.  Therefore

`N_G(A) subseteq {r} union S_L union S_T`.

The anticomplete set `P_j` survives outside `A union N_G(A)`, so this is a
nontrivial full-neighbourhood separation.  Seven-connectivity and the exact
partition of `S` give

`7 <= |N_G(A)| <= |S|+1-|S_R|`.

Thus `|S_R|>=2` yields the claimed strict inequality
`|N_G(A)|<|S|`.  The named root `r` belongs to the new boundary, and the
named missed connected set `P_j` remains on the opposite side.

## Boundary-free-row thickening

Lemma 5.1 is correct in all three choices of the selected boundary vertex.
The boundary-free connected set `Q_0` can be joined either to `a`, using the
assumed `aQ_0` edge, or to `Q_s` or `Q_t`, using the assumed pairwise row
adjacencies.  The three resulting sets remain disjoint, connected and
pairwise adjacent, and their intersections with `T` are exactly their named
singletons.  Because `Q_0` is nonempty, lies in `R union T`, and avoids `T`,
the selected enlarged set genuinely meets `R`.

This is a one-defect tool only.  If adjoining `Q_0` preserves the selected
anticompleteness, Lemma 3.1 applies; if it creates the missing adjacency,
that adjacency is supplied by `Q_0`.  The lemma neither assigns `Q_0` to
several rows simultaneously nor proves that `Q_0` is disjoint from the
connected set `D` reserved as the seventh branch set.

## Precise remaining limitations

No gap remains in the statements proved in this note.  They are conditional
on the pairwise-disjoint configuration in (1.3), which is not yet derived
from the active degree-eight setup.  In particular, the note does not prove:

1. a choice of the three `P_j` disjoint from a connected `D` retaining all
   seven contacts in (1.6);
2. preservation of the other six labels, the cyclic connected-set system,
   or a common boundary-colouring partition after the strict descent;
3. compatible six-colourings across the returned order-seven separation;
   or
4. simultaneous thickening for more than one rooted missing pair.

These are host-level completion obligations, not consequences of the local
incidence and separator theorem audited here.
