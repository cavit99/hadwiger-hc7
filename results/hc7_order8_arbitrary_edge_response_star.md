# A critical-edge response star in an all-boundary column system

**Status:** written proof; separately audited **GREEN** in
[`hc7_order8_arbitrary_edge_response_star_audit.md`](hc7_order8_arbitrary_edge_response_star_audit.md).
This note proves an unbounded host-level reduction inside the two-component
boundary-of-order-eight branch.  It does not prove the remaining
response-coupling theorem or `HC_7`.

## 1. Setting

Let `G` be a seven-connected graph such that

\[
 \chi(G)=7,
 \qquad \chi(M)\le 6\text{ for every proper minor }M\text{ of }G.
 \tag{1.1}
\]

Let `S` be an eight-vertex set for which `G-S` has exactly two components
`C,D`, each adjacent to every literal vertex of `S`.

We use the following consequence of the prescribed-omission theorem.  It is
proved here because the extra all-boundary limb is the point needed later.

## 2. Preserving seven first edges in an eight-fan

### Lemma 2.1 (prescribed-first-edge all-boundary fan)

Fix `v in C` and seven distinct incident edges

\[
                         vv_1,\ldots,vv_7              \tag{2.1}
\]

whose other ends belong to `C union S`.  At least one of the following
holds.

1. A nonempty connected proper subset of `C` has full neighbourhood of
   order seven.
2. For one of the edges in (2.1), a nonempty connected proper subset of
   `C` is a strict crossing-edge response side with full neighbourhood of
   order eight.
3. There is an eight-fan from `v` to all eight vertices of `S` whose limbs
   begin with the seven edges in (2.1) and one further edge at `v`.

In outcome 2, “response side” has its usual operation-specific meaning:
deleting the displayed crossing edge gives a boundary equality partition
which is legal on the edge-deleted closed side and on the opposite closed
shore but is rejected by the intact operated side.

#### Proof

First suppose that there is no eight-fan from `v` to `S` in
`G[C union S]`.  The fan form of Menger's theorem gives a separator of
order at most seven between `v` and `S`.  The component containing `v`
has a genuine full-neighbourhood separation: the opposite open component
`D` lies beyond it.  Seven-connectivity makes its full neighbourhood have
order exactly seven.  It is a proper subset of `C`, because a surviving
vertex of `S` has a neighbour in `C` outside the `v`-component.  This is
outcome 1.

Hence take an arbitrary eight-fan, and let `B` be its set of eight first
neighbours at `v`.  Direct every edge of `G[(C-v) union S]` in both
directions and then delete every arc leaving `S`, so that the members of
`S` are sinks.  Let `M` be the strict gammoid on

\[
                    N_G(v)\cap(C\cup S)                \tag{2.2}
\]

represented by this directed graph with target set `S`.  A source which
already belongs to `S` is linked to itself by the length-zero path.  The
eight-fan says exactly that `B` is an independent set of order eight in
`M`, and therefore a basis.

Let `P={v_1,\ldots,v_7}` be the set of prescribed first neighbours.  Since
the graph is simple, `|P|=7`.  At most seven members of `S` lie in `P`, so
choose

\[
                              r\in S-P.                 \tag{2.3}
\]

Apply the prescribed-omission theorem to (2.1) with omitted vertex `r`.
Its separator alternative gives outcome 1 or, under (1.1), outcome 2.
Otherwise, after deleting the common initial vertex `v`, its seven paths
link `P` to `S-{r}` in the directed representation above.  Thus `P` is
independent in `M`.

Matroid augmentation between the independent set `P` and the basis `B`
gives `b in B-P` such that `P union {b}` is independent.  This set has
order eight, so a witnessing linkage ends at all eight members of `S`.
Prepend to its paths the seven prescribed edges and the edge `vb`.  The
result is an eight-fan ending at all of `S`, and its first edges include
every edge in (2.1).  This is outcome 3.
\(\square\)

## 3. The response star

### Theorem 3.1 (arbitrary critical edge in paired columns)

Fix `v in C` and an edge

\[
                         e=vx,\qquad x\in (C-v)\cup S. \tag{3.1}
\]

Then at least one of the following holds.

1. A nonempty connected proper subset of `C` or `D` has an actual full
   neighbourhood of order seven.
2. A nonempty connected proper subset of `C` is a strict generic
   order-eight response-side descent for one of seven specified edges at
   `v`.
3. There are adjacent connected root subgraphs `R_C,R_D` and seven
   pairwise disjoint connected columns

   \[
                              L_s\qquad(s\in S-\{p\})  \tag{3.2}
   \]

   for some `p in S`, with the following properties.

   - The roots and columns are pairwise disjoint, and each root is adjacent
     to every column.
   - One distinguished target column `T` contains `x`.
   - Five distinct source columns `T_beta`, one for every colour
     `beta ne alpha` in a six-colouring of `G-e`, contain distinct
     neighbours `v_beta` of `v`.
   - For every `beta ne alpha`, the graph contains a literal
     `T_beta`--`T` path whose first vertex is `v_beta`, whose last vertex is
     `x`, and which is obtained from an `alpha,beta` Kempe path by deleting
     `v`.

   The target, five source columns and the one remaining auxiliary column
   are all distinct.  No palette colour is identified with a boundary
   label or with a column except through the literal first neighbour
   `v_beta`.

#### Proof

Six-colour `G-e`.  Its endpoints have one colour, say

\[
                              c(v)=c(x)=\alpha,         \tag{3.3}
\]

because otherwise the deleted edge could be restored.  For every other
colour `beta`, the `alpha,beta` component containing `v` also contains
`x`; otherwise interchanging the two colours on the component containing
one endpoint but not the other would make `e` proper and six-colour `G`.
Choose a simple `v`--`x` path `P_beta` in that component.  Let `vv_beta`
be its first edge.  The five vertices `v_beta` have their five distinct
alternate colours, so these first edges are pairwise distinct and are
different from `e`.

Seven-connectivity gives `d_G(v)>=7`.  Choose one further incident edge
different from `e` and the five displayed first edges.  Apply Lemma 2.1
to these seven edges.  Its first two outcomes give outcome 1 or 2 here.
In its third outcome, exactly one of the eight fan limbs has an
unprescribed first edge.  Let `p` be its end in `S`, and put the whole
`v`--`p` limb into `R_C`.  Each of the six critical first edges and the
auxiliary edge starts a different remaining limb, so they have seven
distinct ends in `S-{p}`.

Choose `w in D` adjacent to `p`.  Apply the ordinary eight-fan argument in
`G[D union S]`.  If it fails, the proof of Lemma 2.1 gives outcome 1.
Otherwise normalize its `p`-limb to the direct edge `wp` and put
`R_D={w}`.  For `s in S-{p}`, join the two fan tails ending at `s`:

\[
                  L_s=(P_s^C-v)\cup(P_s^D-w).          \tag{3.4}
\]

The common end `s` makes each column connected.  Fan disjointness and the
fact that `C,D` are different components make the seven columns pairwise
disjoint and disjoint from the roots.  The edge `pw` joins the roots, and
the first edges of the two fans make both roots adjacent to every column.

The limb beginning with `e` contains `x`, so it is the target column `T`.
The five limbs beginning with `vv_beta` give five distinct source columns
containing the corresponding `v_beta`.  Finally,
`P_beta-v` is a literal path from `v_beta` to `x`.  It may run through the
roots or through other columns, but its endpoints have the asserted
literal ownership.  This proves outcome 3.  \(\square\)

## 4. Contact consequences

Let `J` be the contact graph of the seven columns in outcome 3.  Thus two
labels are adjacent in `J` exactly when their literal columns have an edge
between them.  The two roots and a `K_5` model in `J` lift to an explicit
`K_7`-minor model in `G`; hence `J` is `K_5`-minor-free in a surviving
host.

### Corollary 4.1 (forced noncontacting source columns)

With `T` denoting the target column:

1. if `d_J(T)<=3`, at least two of the five source columns do not contact
   `T`;
2. if `J` is the pentagonal bipyramid and `T` is a rim vertex, at least one
   source column does not contact `T`;
3. if `J` is the pentagonal bipyramid and `T` is a pole, no noncontacting
   source is forced: the unique nonneighbour of `T` can be the auxiliary
   column.

#### Proof

Besides `T`, the seven columns consist of the five sources and one
auxiliary column.  In the first case `T` has at least three nonneighbours,
at most one of which is auxiliary.  A rim vertex of the pentagonal
bipyramid has exactly two nonneighbours, while a pole has exactly one.
The conclusions follow.  \(\square\)

### Corollary 4.2 (clean Kempe-path augmentation)

Suppose a source column `T_beta` does not contact `T`.  If the path
`P_beta-v` contains a `T_beta`--`T` subpath whose internal vertices avoid
both roots and all seven columns, then the column system can be changed,
without changing its roots or boundary labels, so that its contact graph
contains `J+T_beta T`.

In particular, if `J` is the pentagonal bipyramid, this gives an explicit
`K_7`-minor model in `G`.

#### Proof

Truncate the displayed subpath at its last vertex in `T_beta` and its first
subsequent vertex in `T`.  Absorb its internal vertices into
`T_beta`.  This preserves connectedness, disjointness, both root contacts,
all old column contacts and all boundary labels, while adding the missing
contact with `T`.  The pentagonal bipyramid is edge-maximal
`K_5`-minor-free, so the enlarged contact graph contains a `K_5` minor;
together with the two roots this lifts to a `K_7` minor.  \(\square\)

## 5. Exact gain and trust boundary

The theorem embeds one arbitrary critical edge and all five of its Kempe
locks into one paired all-boundary column system.  It therefore removes the
previous palette-to-label ambiguity at the **ends** of the five response
paths: ownership is certified by literal first edges, not inferred from
colour names.

The following limitations are essential.

- The order-eight descent in outcome 2 can be returned by any one of the
  seven prescribed edges.  It is a strict generic response-side descent,
  not necessarily a descent preserving the response selected from `e`.
- A Kempe path can meet a root or one or more old columns before reaching
  `T`.  Such a dirty path cannot be treated as a new contact.  Splitting an
  intermediate column while retaining its two root contacts and its old
  named contacts is precisely the unresolved label-preserving step.
- In the low-degree branch of the seven-vertex contact theorem, the
  low-degree column need not be `T`.  Corollary 4.1(1) is deliberately
  conditional on the target itself having degree at most three.
- In the pentagonal-bipyramid branch, a pole target may have the auxiliary
  column as its sole nonneighbour.  Criticality has not yet forced a
  response path to that column.
- The theorem does not produce a common equality partition on an
  order-seven boundary and does not close the two-component order-eight
  interface.

Thus the remaining theorem is sharply localized: use operation-specific
nonextension either to split a dirty intermediate column label-faithfully,
to force a response path to the exceptional auxiliary column, or to return
an exact order-seven compatible separation or a response-preserving strict
descent.

## 6. Dependencies

- the prescribed-omission theorem at an eight-vertex boundary;
- the paired all-boundary column decoder;
- the seven-column contact classification; and
- ordinary Kempe interchange and strict-gammoid augmentation.
