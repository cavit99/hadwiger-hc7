# Independent internal audit of the all-boundary fan theorem

**Verdict:** GREEN for the theorem and its explicitly stated trust boundary.

## Audited revision and verdict

This audit checks the complete source file
[`hc7_order8_all_boundary_source_fan.md`](hc7_order8_all_boundary_source_fan.md)
at SHA-256

```text
6b474d1ffdfd622b9993ba4c879b2b777079e9c289fd4c9855bc838997264efc
```

This final source revision differs from the proof revision originally checked
only in its opening status paragraph: the pending-audit wording was replaced
by a link to this completed audit.  Replacing that paragraph by its prior
text reproduces the originally checked SHA-256
`8434ffb7ed7c4f2b445995faa3cae45a1deba83adb1f6cf8f4b647475d05f0fb`.
The theorem statements, proofs, minimum-shore application, and trust boundary
are byte-for-byte unchanged.

**Verdict: GREEN for Theorems 1.1 and 2.1, with exactly the trust boundary
stated in the source.**  The minimum-shore paragraph is also correct as an
application of the separately audited generic exact-seven restart theorem;
it is not an additional conclusion of Theorem 1.1.

The audit does not promote a near-`K_7` rotation, a compatible boundary
colouring, or the active order-eight target.  In particular, the fan
terminals lie in the separator, whereas the two roots required by the
rotation theorem lie inside its connector.

## 1. Audit of Theorem 1.1

### 1.1 Contraction and the fan alternative

Contracting a spanning tree of the nonempty connected subgraph `P` produces
one vertex `p` and leaves every member of `S` as a distinct literal vertex.
All other vertices of `C` remain literal.  Thus the fan form of Menger's
theorem applies to `p` and the eight-set `S` in

```text
H = G[C union S]/P.
```

An eight-fan has eight paths with pairwise distinct ends in the eight-set
`S`, hence uses every member of `S` exactly once.  No path can contain a
different member of `S` internally: that vertex is the end of another fan
path, and the fan paths are disjoint away from `p`.  Stopping at the first
member of `S` is therefore safe.  On lifting `p` back to `P`, each path can
start at the literal endpoint in `P` of its first edge; the paths may overlap
inside `P`, exactly as the theorem permits, and are pairwise disjoint outside
`P`.

### 1.2 Retaining prescribed direct edges

Each prescribed edge `p_i s_i` has image `p s_i` after the contraction.
Because the `s_i` are distinct and the eight fan ends exhaust `S`, replacing
the fan path ending at `s_i` by this one-edge path does not meet another fan
path away from `p`.  All replacements can be made simultaneously.  When the
contraction is lifted, the chosen image edge is lifted using its specified
preimage `p_i s_i`.  Repeated vertices among the `p_i` cause intersections
only inside `P`, which are allowed.  The prescribed-edge assertion is
therefore valid.

### 1.3 The Menger separator and its literal lift

If no eight-fan exists, the fan form of Menger gives

```text
Z subseteq V(H)-{p},  |Z| <= 7,
```

such that the component of `H-Z` containing `p` contains no vertex of
`S-Z`.  Its lift inside `C` is a nonempty connected vertex set `A` containing
`P`.  Since `C` is a component of `G-S`, every neighbour of `A` outside `C`
lies in `S`; componenthood in `H-Z` then gives `N_G(A) subseteq Z`.

There is an `s in S-Z` because `|S|=8>|Z|`.  The equality `N_G(C)=S`
provides an `s-C` edge.  Its end in `C` cannot lie in `A`, since otherwise
`s` would belong to the `p`-component of `H-Z`.  Hence `A` is a proper
subset of `C`.

The set `A` is one nonempty side of `G-N_G(A)`.  The chosen `s`, as well as
every vertex in the assumed other component of `G-S`, is outside
`A union N_G(A)`, so the opposite open side is nonempty.  Thus `N_G(A)` is a
genuine vertex separator.  Seven-connectivity and `N_G(A) subseteq Z` give

```text
7 <= |N_G(A)| <= |Z| <= 7.
```

Consequently `|N_G(A)|=7` and, because of containment and equal cardinality,
`N_G(A)=Z`.  This proves the exact order-seven separation claimed in outcome
2.  No colouring compatibility is inferred.

### 1.4 Minimum-shore scope

In the stated minimum-shore application, the order-seven side `A` is
strictly smaller than the previously selected generic response shore because
`A` is a proper subset of `C` and `C` lies properly inside that shore.  The
hypothetical-counterexample assumptions built into a generic response
interface supply a six-colouring of every edge-deleted proper minor.  An
edge between `A` and `N_G(A)` and such a colouring therefore give the data
required by the audited generic restart theorem.  This justifies excluding
outcome 2 only in that particular minimum-shore setting.  The source
correctly declines to call an arbitrary order-seven return strict or to
claim preservation of an old equality partition.

## 2. Audit of Theorem 2.1

### 2.1 Construction of the fan tree

For each lifted fan path, taking the suffix beginning at its last vertex of
`P` leaves a path `L_s` whose unique vertex on `P` is `x_s`.  Distinct fan
paths remain disjoint outside `P`.  When `P` is a path, adjoining these
pendant paths to `P` creates a tree `T_P`: each `L_s` meets the existing
spine in exactly one vertex and two different limbs have no vertex in common
outside the spine.

For nonempty `Q subseteq S`, the set `T_P(Q)` is connected and lies in `C`.
Deleting the terminal `s` from each `L_s` retains the attachment `x_s`, even
when `L_s` is the single edge `x_s s`.  It also retains the predecessor of
`s`, so `T_P(Q)` has a literal edge to `s`.  The source now correctly claims
only disjointness from `S`; omission of one separator vertex does not imply
disjointness from an entire inherited branch set containing it.

### 2.2 Necessity of disjoint intervals

Any connected subgraph of the tree `T_P` that contains `L_s-s` for every
`s in Q_i` contains every attachment `x_s` and the unique tree paths between
those attachments.  Those paths contain the whole minimal spine interval
`I_P(Q_i)`.  Therefore two such vertex-disjoint connected subgraphs force
the two intervals to be vertex-disjoint.  This also covers singleton `Q_i`:
then `L_s-s` contains `x_s`, so the one-vertex interval is genuinely forced.

### 2.3 Sufficiency and extension to a connected partition

If the two spine intervals are disjoint, `T_P(Q_1)` and `T_P(Q_2)` are
connected and vertex-disjoint.  Their respective limbs cannot meet outside
`P`, and each limb meets `P` only at an attachment in its own interval.

If these two rooted subgraphs are not adjacent, a shortest path between
them in connected `G[C]` has all internal vertices outside both.  Adding its
internal vertices to the first subgraph preserves disjointness and
connectedness and makes the two subgraphs adjacent.  After contracting the
two sets, their joining edge can be included in a spanning tree of the
connected quotient.  Removing that tree edge leaves exactly two tree
components.  Lifting them partitions all vertices of `C` into two nonempty,
connected, adjacent sets containing the respective rooted subgraphs.  This
proves both directions of Theorem 2.1 and the enlargement assertion.

## 3. Exact trust boundary

The following are proved:

1. a host-level eight-fan to the eight literal boundary vertices, or an
   actual order-seven full-neighbourhood separation;
2. simultaneous retention of any prescribed `P-S` edges with distinct
   boundary ends; and
3. the exact interval criterion for dividing the rooted fan limbs between
   two connected adjacent sides of `C`.

The following are not proved and are not used in the audit verdict:

- that a separator vertex represents its entire inherited branch set;
- that the interval subgraphs avoid such branch sets without an additional
  containment hypothesis;
- that two prescribed roots inside a near-`K_7` connector reach the two
  interval subgraphs disjointly;
- that the interval condition is forced;
- that the order-seven separation carries a common equality partition; or
- that `HC_7` or the active order-eight branch is closed.

Subject to this explicit trust boundary, the two theorem statements and
their proofs are complete.
