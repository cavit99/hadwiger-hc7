# Amplifying a single branch-set portal in a near-`K_7` model

**Status:** written proof; separate internal audit GREEN in
[`hc7_single_portal_amplification_audit.md`](hc7_single_portal_amplification_audit.md).

This note removes a single-portal obstruction from a labelled
`K_7`-minus-one-edge model.  Components outside the displayed model are
first absorbed by branch sets in a way which preserves the one missing
adjacency.  The resulting model is spanning.  Seven-connectivity then
forces one of the five branch sets adjacent to the deficient branch set to
contain two distinct attachment vertices.

In a graph which is not six-colourable but whose proper minors are
six-colourable, an edge through one of those two attachments can be deleted
without destroying the labelled near-complete model.  Its five
bichromatic endpoint paths therefore coexist with that fixed model.  The
theorem does not identify their five colours with the five branch-set
labels and does not prove `HC_7`.

## 1. Setting and the exact absorption hypothesis

Let `G` be seven-connected.  Let

\[
                   W,B,C,F_1,F_2,F_3,F_4                 \tag{1.1}
\]

be pairwise disjoint nonempty connected vertex sets.  Assume that every
two of the seven sets are adjacent except `W,B`, which are anticomplete.
Thus (1.1) is a labelled `K_7`-minor model with the single required
adjacency `WB` missing.  Put

\[
              U=W\cup B\cup C\cup F_1\cup\cdots\cup F_4. \tag{1.2}
\]

Assume the following exact safe-absorption condition.  For every component
`Q` of `G-U`, one can choose a member

\[
 \sigma(Q)\in\{W,B,C,F_1,F_2,F_3,F_4\}                  \tag{1.3}
\]

such that `Q` is adjacent to `sigma(Q)` and

\[
 \begin{aligned}
   \sigma(Q)=W&\quad\Longrightarrow\quad E_G(Q,B)=\varnothing,\\
   \sigma(Q)=B&\quad\Longrightarrow\quad E_G(Q,W)=\varnothing.
 \end{aligned}                                          \tag{1.4}
\]

There is no restriction when `sigma(Q)` is one of the other five branch
sets: absorbing `Q` there cannot create an edge between `W` and `B`
themselves.  Conditions (1.3)--(1.4) are precisely what is needed for the
componentwise absorption below.  They are weaker than requiring all
outside components to attach to one prescribed pair of branch sets.

For disjoint vertex sets `X,Y`, write

\[
             P_Y(X)=N_G(X)\cap Y                         \tag{1.5}
\]

for the literal vertices of `Y` adjacent to `X`.  The hypothesis

\[
                         |P_C(B)|=1                       \tag{1.6}
\]

means that the `B-C` interface has one attachment vertex on the `C` side.
It is weaker than saying that there is only one `B-C` edge.  Indeed,
`E_G(B,C)={sr}` with `s\in B,r\in C` implies (1.6), whereas (1.6) still
allows the unique vertex of `C` to have several neighbours in `B`.

### Lemma 1.1 (the root-pair condition is safely absorbable)

Suppose, more strongly, that

\[
          N_G(Q)\subseteq B\cup C
          \quad\text{for every component }Q\text{ of }G-U.       \tag{1.7}
\]

Then (1.3)--(1.4) hold.  One may assign each `B`-only component to `B`,
each `C`-only component to `C`, and each component meeting both sides to
`C`.  In the last case, absorbing the component into `C` creates a new
`C`-side attachment vertex to `B`, distinct from every old vertex of `C`.

#### Proof

The graph `G` is connected, so every component `Q` of `G-U` has a
neighbour in `U`.  Under (1.7), it therefore meets at least one of `B,C`.
The stated assignment always chooses a branch set met by `Q`.  A component
assigned to `B` is `B`-only and hence anticomplete to `W`; no component is
assigned to `W`.  Thus (1.3)--(1.4) hold.

If `Q` meets both sides and is assigned to `C`, choose `q\in Q` adjacent
to `B`.  After absorption, `q` is a `C`-side attachment vertex different
from every old vertex of `C`.  \(\square\)

The orientation of a two-sided component into `C`, rather than into `B`,
is what amplifies a one-portal `B-C` interface.

## 2. Spanning completion and portal amplification

### Theorem 2.1 (single-portal amplification)

Under (1.1)--(1.6), there are pairwise disjoint nonempty connected sets

\[
                   W^+,B^+,D,H_1,H_2,H_3,H_4            \tag{2.1}
\]

with the following properties.

1. The sets in (2.1) partition `V(G)`.
2. Every two sets in (2.1) are adjacent except `W^+,B^+`, which are
   anticomplete.
3. The donor branch set `D` has at least two distinct attachment vertices
   to `B^+`:

   \[
                         |P_D(B^+)|\ge2.                 \tag{2.2}
   \]

Thus the deficient branch sets are enlargements of the old `W,B` and the
new model is spanning.  Choosing, among the five branch sets adjacent to
`B^+`, one maximizing `|P_D(B^+)|` is a canonical re-choice with value at
least two.  A model satisfying (1.6) cannot be maximal for this
attachment-vertex parameter.

#### Proof

For each old branch set `X` in (1.1), enlarge `X` by the union of all
components `Q` for which `sigma(Q)=X`; call the result `X^+`.  Each
enlarged set is connected, since every assigned component has an edge to
its old branch set.  Distinct components of `G-U` are anticomplete, so the
seven enlarged sets are pairwise disjoint and partition `V(G)`.  Every old
branch-set adjacency survives.

The sets `W^+,B^+` remain anticomplete.  There was no old `W-B` edge.  A
component assigned to `W` has no edge to `B` by (1.4), a component
assigned to `B` has no edge to `W`, and two distinct outside components
have no edge between them.  Consequently

\[
              W^+,B^+,C^+,F_1^+,F_2^+,F_3^+,F_4^+      \tag{2.3}
\]

is a spanning labelled `K_7`-minus-one-edge model.

The full neighbourhood `N_G(B^+)` separates the nonempty connected set
`B^+` from the nonempty connected set `W^+`.  Seven-connectivity gives

\[
                         |N_G(B^+)|\ge7.                 \tag{2.4}
\]

Because (2.3) is spanning and `W^+` is anticomplete to `B^+`,

\[
 N_G(B^+)\subseteq C^+\cup F_1^+\cup F_2^+\cup F_3^+\cup F_4^+. \tag{2.5}
\]

The five sets on the right are disjoint.  By the pigeonhole principle,
one of them, call it `D`, contains at least two distinct vertices adjacent
to `B^+`.  Take the remaining four sets as `H_1,\ldots,H_4`.  This proves
(2.1)--(2.2).  Since the initial donor `C` had only one literal attachment
vertex by (1.6), the maximizing re-choice strictly increases that
parameter.  \(\square\)

### Corollary 2.2 (model-independent spanning normalization)

The conclusion that some neighbouring branch set contains two attachment
vertices does not require (1.6).  Under (1.1)--(1.4), the safe absorption
above yields a spanning labelled `K_7`-minus-one-edge model in which one
of the five branch sets adjacent to the deficient branch set contains at
least two of its attachment vertices.

#### Proof

The proof of Theorem 2.1 before its final sentence does not use (1.6).
\(\square\)

## 3. A model edge whose deletion preserves the model

### Theorem 3.1 (deletion-persistent critical edge)

Use the spanning model (2.1) and choose distinct vertices

\[
             d_1,d_2\in P_D(B^+).
\]

For `j=1,2`, choose an edge

\[
                    e_j=b_jd_j,qquad b_j\in B^+.       \tag{3.1}
\]

Then `e_1,e_2` are distinct and the following hold.

1. Deleting `e_1` leaves the seven sets in (2.1) as the same spanning
   labelled `K_7`-minus-one-edge model: `e_2` retains the `B^+-D`
   adjacency.
2. Contracting `e_1` merges `B^+,D`; that merged branch set together with
   `W^+,H_1,H_2,H_3,H_4` is a `K_6`-minor model in `G/e_1`.

Assume in addition that `G` is not six-colourable and every proper minor
of `G` is six-colourable.  Then

\[
                         \chi(G-e_1)=\chi(G/e_1)=6.       \tag{3.2}
\]

In every proper six-colouring of `G-e_1`, the ends `b_1,d_1` have one
common colour `alpha`.  For each of the other five colours `beta`, those
ends lie in the same component of the subgraph induced by colours
`alpha,beta`.  Equivalently, `G-e_1` contains five colour-distinguished
bichromatic `b_1-d_1` paths, all in one host which still contains the
spanning labelled model from item 1.

#### Proof

The distinct donor vertices `d_1,d_2` make the edges in (3.1) distinct.
After deleting `e_1`, the edge `e_2` still joins the connected branch sets
`B^+,D`; all other model adjacencies are unchanged.  This proves item 1.

After contracting `e_1`, the image of `B^+\cup D` is connected.  It is
adjacent to `W^+` through the old `DW^+` adjacency and to every `H_i`.
The five sets `W^+,H_1,\ldots,H_4` are pairwise adjacent.  They and the
merged branch set form the asserted `K_6` model.

Both `G-e_1` and `G/e_1` are proper minors, so they are six-colourable.
If `G/e_1` were five-colourable, expand the contracted vertex over the two
ends of `e_1`, retain its colour on one end, and give the other end a fresh
sixth colour.  This would six-colour `G`, a contradiction.  Thus
`chi(G/e_1)=6`.  If `G-e_1` were five-colourable, either its two ends had
different colours, in which case the edge could be restored, or they had
one common colour, in which case recolouring one end with a fresh sixth
colour would permit the edge to be restored.  Both alternatives
six-colour `G`.  This proves (3.2).

In any six-colouring of `G-e_1`, the ends of `e_1` have the same colour;
otherwise restoring the edge six-colours `G`.  Fix another colour `beta`.
If the two ends lay in different `alpha,beta` components, interchange
`alpha,beta` on the component containing one end.  The ends would then
have different colours, again allowing `e_1` to be restored.  This is
impossible.  Hence they lie in one bichromatic component for every
`beta`, which supplies the five paths.  \(\square\)

The point of Theorem 3.1 is simultaneous rather than numerical: the
deleted critical edge and all five of its Kempe paths coexist with a fixed
spanning labelled near-complete model.  Deleting a unique model edge would
have destroyed that model.

## 4. The contracted-edge application

In the application from a minimal contraction bag, the displayed lifted
model has branch sets

\[
                         A,W,B_1,\ldots,B_5             \tag{4.1}
\]

and its sole missing adjacency is `W-B_2`.  Every component outside that
model attaches only to `A\cup W` and is anticomplete to every `B_i`.
Use the generic notation

\[
 B=B_2,\qquad C=B_1,qquad
 \{F_1,F_2,F_3,F_4\}=\{A,B_3,B_4,B_5\}.                \tag{4.2}
\]

For each outside component, assign it to `A` if it meets `A`, and otherwise
to `W`.  In the latter case it is anticomplete to `B_2`.  Thus
(1.3)--(1.4) hold.  If the original `B_1` side contains a unique
`B_2`-attachment vertex—in particular, if there is a unique
`B_1-B_2` edge—Theorems 2.1 and 3.1 replace that edge by a canonical
deletion-persistent interface with two donor-side attachment vertices.

## 5. Parameter-uniform form

### Corollary 5.1

Let `t>=4`.  In a `t`-connected graph, suppose a spanning labelled
`K_t`-minus-one-edge model has deficient branch sets `W,B`.  Then one of
the `t-2` branch sets adjacent to `B` contains at least two distinct
vertices adjacent to `B`.

#### Proof

The full neighbourhood of `B` separates `B` from `W`, so it has order at
least `t`.  Since the model is spanning and `W` is anticomplete to `B`,
that neighbourhood is distributed among the other `t-2` branch sets.
Therefore some one contains at least

\[
                         \left\lceil\frac{t}{t-2}\right\rceil=2
\]

attachment vertices.  \(\square\)

For a nonspanning model, the same conclusion follows whenever its outside
components satisfy the safe-absorption condition analogous to
(1.3)--(1.4).

## 6. Exact scope

The safe-absorption hypothesis is essential to the spanning completion.
It ensures that assigning a component to one branch set does not create
the missing adjacency between the two deficient branch sets.  The theorem
does not assert that an arbitrary `K_7^-` model has this property.

Theorem 2.1 amplifies a **donor-side attachment vertex**, not merely an
edge count.  A unique `B-C` edge is a sufficient input, but the actual
hypothesis permits several edges incident with one vertex of `C`.

The canonical re-choice maximizes the number of donor-side attachment
vertices among the five neighbouring branch sets of the spanning model.
It need not preserve a different normalization which first minimizes the
order of a contracted root branch set.  Absorbing outside components can
increase that order.

Finally, the five bichromatic paths in Theorem 3.1 are palette-labelled,
not branch-set-labelled.  Their colours do not identify the five named
branch sets.  The theorem yields neither an explicit `K_7`-minor model nor
a common boundary colouring at an order-seven separation.  Its precise
gain is that the former single-interface case can always be replaced by a
spanning model with a deletion-persistent critical model edge and two
literal donor-side attachment vertices.

## 7. Dependency

- [minimal contraction-bag normalization](hc7_contracted_edge_k6_model_normalization.md),
  which supplies the attachment restriction in the contracted-edge
  application.
