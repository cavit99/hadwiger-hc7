# Internal audit of single-portal amplification

**Verdict: GREEN for the exact source revision identified below.**

This is an internal mathematical audit, not external peer review.  Two
independent internal checks reached the same verdict: one checked the
safe-absorption, connectivity-counting, and critical-edge arguments
directly; the other rechecked the complete frozen source against its stated
scope.

## 1. Audited source

The audited theorem is
[`hc7_single_portal_amplification.md`](hc7_single_portal_amplification.md)
at SHA-256

```text
b4315f0adaff165acfbd338c7b1def8f3bddf8cae4d8d16501b9708c9c3252e6
```

The audit covers the whole file at that hash:

- Lemma 1.1;
- Theorem 2.1 and Corollary 2.2;
- Theorem 3.1;
- the contracted-edge application;
- Corollary 5.1; and
- the limitations in Section 6.

Relative to the frozen mathematical revision checked independently, this
revision changes only the status line to link this audit.  No conclusion in
this audit applies automatically to a later source revision with a different
hash.

## 2. Hypotheses and terminology

The seven displayed sets form a labelled `K_7`-minus-one-edge model: they
are pairwise disjoint, nonempty and connected, and their sole absent
branch-set adjacency is `W-B`.

The safe-absorption hypothesis is explicit.  For every component outside
the model union, it supplies one old branch set which that component meets.
The only extra restrictions are exactly those needed when the chosen set
is one of the deficient pair:

- a component assigned to `W` is anticomplete to `B`; and
- a component assigned to `B` is anticomplete to `W`.

No stronger claim that every near-complete model admits such an assignment
is made.

The source correctly distinguishes

\[
                         |P_C(B)|=1
\]

from the stronger statement that `E(B,C)` consists of one edge.  A unique
edge implies a unique `C`-side attachment vertex, but several edges can
share that one vertex.  The conclusion amplifies the number of distinct
donor-side attachment vertices, not merely the number of interface edges.

## 3. Safe absorption and the spanning model

For every old branch set `X`, the proof adjoins all outside components
assigned to `X`.  The resulting set is connected because each assigned
component has an edge to the old connected set `X`.  Different components
of `G-U` are disjoint and anticomplete, so the seven enlarged branch sets
remain pairwise disjoint and together cover `V(G)`.

Every old required adjacency survives enlargement.  The missing
adjacency also survives:

1. the old sets `W,B` were anticomplete;
2. a component absorbed into one of them is anticomplete to the other by
   the safe-assignment hypothesis; and
3. components absorbed into opposite sides are different components of
   `G-U`, and hence are anticomplete.

Thus the displayed enlarged sets really form a spanning labelled
`K_7`-minus-one-edge model.

Lemma 1.1 is also correct.  Under the stronger condition that every
outside component attaches only to `B\cup C`, a one-sided component can
be assigned to its side.  A component meeting both sides is deliberately
assigned to `C`.  Such a component contains a new vertex adjacent to `B`,
so this orientation creates a new `C`-side attachment vertex rather than
silently enlarging the deficient branch set.

## 4. Seven-connectivity and attachment multiplicity

In the spanning model, `N_G(B^+)` is a genuine vertex cut.  The connected
set `B^+` survives on one side after its full neighbourhood is deleted,
while the nonempty connected set `W^+` survives on another side because
the two sets are anticomplete.  Seven-connectivity therefore gives

\[
                         |N_G(B^+)|\ge7.
\]

Spanningness is essential in the next step.  Every neighbour of `B^+`
lies in one of the other six branch sets, and none lies in `W^+`.
Consequently the full neighbourhood is distributed among precisely the
five branch sets adjacent to `B^+`.  Seven vertices in five disjoint sets
force one of those branch sets to contain at least two distinct
`B^+`-attachment vertices.

This proves both the donor multiplicity in Theorem 2.1 and the
model-independent Corollary 2.2.  The word *canonical* in the source has
the limited and valid extremal meaning stated there: after forming the
spanning model, choose a neighbouring branch set maximizing the number of
its attachment vertices.  The maximizing donor can differ from the old
set `C`, and this optimization need not preserve a separate normalization
which minimizes a contracted root branch set.

## 5. Persistent deletion and contracted `K_6` model

Choose two distinct donor-side attachment vertices and one incident edge
at each.  The edges are distinct even if their ends in `B^+` coincide.
Deleting the first leaves the second, so the same seven branch sets still
realize the labelled `K_7`-minus-one-edge model.

Contracting the first edge merges `B^+` with the donor.  The merged set is
connected and is adjacent to `W^+` through the donor, while the four
remaining branch sets retain all their old adjacencies.  The merged set,
`W^+`, and those four sets therefore form the claimed explicit `K_6`
model in the contraction.

Under the additional hypothesis that `G` is not six-colourable and every
proper minor is six-colourable, both the deletion and contraction have
chromatic number exactly six:

- a five-colouring of the contraction expands by giving one endpoint a
  fresh sixth colour; and
- a five-colouring of the deletion either already separates the endpoint
  colours, or one endpoint can again receive a fresh sixth colour.

Either case would six-colour `G`.

In every six-colouring of the edge deletion, the endpoints have the same
colour, since otherwise the edge could be restored.  If they were in
different two-colour components for one alternate colour, a Kempe
interchange on one endpoint component would separate their colours and
again permit restoration.  Hence all five bichromatic endpoint paths
exist in the same edge-deleted host in which the labelled model persists.

No path-disjointness or branch-set allocation is inferred from this
argument.

## 6. Contracted-edge application

The substitution in Section 4 is correct.  In the lifted model

\[
                         A,W,B_1,\ldots,B_5,
\]

put `B=B_2`, `C=B_1`, and use `A,B_3,B_4,B_5` as the other four branch
sets.  The only missing pair is `W-B_2`.

The minimal contraction-bag normalization says that an outside component
attaches only to `A\cup W` and is anticomplete to every `B_i`.  Assign it
to `A` whenever it meets `A`, and otherwise to `W`.  In the latter case
it is anticomplete to `B_2`, so the safe-absorption condition holds.  Thus
a unique `B_1`-side portal—or, more strongly, a unique `B_1-B_2` edge—is
legitimately replaced by the spanning two-portal normalization.

## 7. Uniform form

Corollary 5.1 is correct.  In a `t`-connected spanning
`K_t`-minus-one-edge model, the deficient branch set has a full
neighbourhood of order at least `t`, all contained in the other `t-2`
neighbouring branch sets.  For every `t>=4`,

\[
                 \left\lceil\frac{t}{t-2}\right\rceil=2,
\]

so one branch set contains two attachment vertices.  The nonspanning
extension is correctly made conditional on the corresponding
safe-absorption hypothesis.

## 8. Exact trust boundary

The source proves a genuine unbounded normalization, but it does **not**
prove any of the following:

1. a `K_7` minor;
2. a colour-compatible order-seven separation;
3. that the five bichromatic paths are internally disjoint;
4. that their five palette colours correspond to the five named branch
   sets;
5. that the new donor is the old set `C`;
6. that the re-choice preserves minimum contracted-root order; or
7. that every arbitrary nonspanning `K_7^-` model admits safe absorption.

These exclusions are stated in the source.  In particular, the theorem
does not commit the palette-to-branch-set fallacy.  Its precise gain is a
spanning near-complete model with a deletion-persistent critical model edge
and two literal donor-side attachment vertices.

Subject to that trust boundary, both internal audits found no gap in the
stated results.
