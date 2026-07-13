# Seven-connectivity breaks a singleton alpha hub except for a two-lobe web

## 1. Setting

Use either hard order-eight row of
`hadwiger_order8_tight_hall_palette_exchange.md`.  Let `B` be its exact
eight-vertex gate, let `K` be the component behind it, and let `R` denote
the nonempty far side.  Thus

\[
                         N_G(K)=B,
\]

and every vertex of `B` has a neighbour in `K`.  Let

\[
 A=\{a_1,a_2\},\qquad C=\{c_1,c_2\}
\]

be the two disjoint terminal pairs in the corresponding row (3.6).
A connected subgraph of `K` **supports** a pair when it has a neighbour at
both gate vertices of that pair.

This note tests the singleton-alpha-hub counterarchitecture from Example
4.2 of the cited file against the actual seven-connectivity hypothesis.

## 2. Component contact load

### Lemma 2.1

Let `t in K`, and let `Q` be a component of `K-t`.  Then

\[
                         |N_B(Q)|\ge6.              \tag{2.1}
\]

If no nested exact seven-cut is allowed, then

\[
                         |N_B(Q)|\ge7.              \tag{2.2}
\]

Consequently, under (2.2), `Q` fails to support at most one of the two
disjoint pairs `A,C`.

### Proof

Every neighbour of `Q` outside `Q` lies in `B union {t}`.  This set
separates `Q` from the far side `R`.  Seven-connectivity gives

\[
                         |N_B(Q)|+1\ge7,
\]

which is (2.1).  Equality makes `N_B(Q) union {t}` an exact seven-cut,
because every displayed vertex is an actual neighbour.  Excluding that
outcome gives (2.2).

Under (2.2), `Q` misses at most one gate vertex.  Since `A,C` are disjoint,
it cannot miss a member of both pairs, and therefore supports at least one
of them.  \(\square\)

## 3. Three hub lobes force the two columns

### Theorem 3.1 (singleton-hub collapse)

Assume no nested exact seven-cut.  If `K-t` has at least three components,
then `K` contains vertex-disjoint connected subgraphs `L_A,L_C` supporting
`A,C`, respectively.  Hence either hard order-eight row contains a `K_7`
minor.

### Proof

Call a component of `K-t` an `A`-supporter or `C`-supporter according to
the two pairs it supports.  By Lemma 2.1 every component has at least one
of these two types.

If two distinct components have the two different types, take them as
`L_A,L_C`.  So suppose no such choice is possible.  After interchanging
the pair names, every component supports `C`, while no component supports
`A`.

Each component therefore misses exactly one of `a_1,a_2`.  If components
of both missing types occur, choose one missing `a_1` and one missing
`a_2`.  Join connected prefixes in those two components to `t`; their
union with `{t}` is a connected subgraph supporting `A`.  Use a third
component, which supports `C`, as `L_C`.

If all components miss the same vertex, say `a_1`, fullness of `K` to `B`
forces the edge `ta_1`.  Any component contacts `a_2`; a path from `t` to
one such contact, together with `t`, gives `L_A`.  Use a different
component as `L_C`.  In both cases the two carriers are disjoint.

Lemma 3.1 of the order-eight note now converts these two carriers into the
explicit `K_7` model.  \(\square\)

### Corollary 3.2 (why the local star counterarchitecture fails)

The singleton-hub construction in Example 4.2 has one component of
`K-t` for each palette leaf.  With at least three such leaves, it cannot
occur inside the exact order-eight gate of a target-free seven-connected
graph unless a nested exact seven-cut occurs.

Thus the counterarchitecture fails the ambient connectivity/descent test,
not the coupled Kempe calculation.  The only singleton-alpha-hub geometry
which survives Theorem 3.1 has

\[
                     K-t\text{ connected, or exactly two components}.
                                                               \tag{3.1}
\]

The first case is a cutvertex-free web.  The second is an exact two-lobe
hub in which both lobes may be needed for one terminal pair.  These are the
two configurations on which crossed minor-operation states must act.

### Lemma 3.3 (exact two-lobe normal form)

Suppose `K-t` has exactly two components `Q_1,Q_2`, and the two protected
columns do not already exist.  Then, after interchanging the two terminal
pairs and their endpoints,

\[
\begin{aligned}
 B-N_B(Q_1)&=\{a_1\},\qquad
 B-N_B(Q_2)=\{a_2\},\cr
 ta_1,ta_2&\notin E(G),
\end{aligned}                                                   \tag{3.2}
\]

while both `Q_1,Q_2` support the whole other pair `C`.

### Proof

Each lobe misses at most one gate vertex.  If the two lobes can be assigned
to different terminal pairs, they are the desired disjoint columns.  Hence
both fail the same pair, say `A`, and both support `C`.  If they missed the
same endpoint of `A`, fullness would make `t` adjacent to that endpoint;
then `t` together with one lobe would support `A`, leaving the other lobe
for `C`.  Therefore their missing endpoints are distinct, giving the first
line of (3.2).

If `t` contacted `a_1`, then `t union Q_1` (with a shortest prefix to an
`a_2` contact) would support `A`, while `Q_2` supports `C`.  The symmetric
argument applies to `a_2`.  Thus both displayed edges are absent.  Since
each lobe has only its one displayed missing gate vertex, both contact both
vertices of `C`.  \(\square\)

The two-lobe survivor is therefore not an arbitrary web.  The hub and its
two incident lobe edges form the faithful coupled star, the two lobes have
opposite singleton defects on one terminal pair, and the other terminal
pair is duplicated on both lobes.  This is exactly the capacity-state
geometry in which the coupled Kempe lock and crossed operation states are
aligned on the same literal split.

## 4. Interface with the dynamic programme

Take one faithful internal edge in each of the two lobes of the exact
two-lobe case and colour the two opposite edge-deleted graphs.  The crossed
state theorem in `hadwiger_fixed_model_transition_gate.md` says that their
marked states on the common gate cannot agree.  Therefore a successful
dynamic closure must prove one of the following concrete alternatives:

1. one operation reroutes a lobe so that it supports the other terminal
   pair, giving the two protected columns;
2. the two marked states become equal after the prescribed four-terminal
   frame is fixed, so crossed splicing six-colours `G`; or
3. the states differ on a named gate block, yielding a pinned Kempe fan
   through that block.

The crossed-state theorem itself does not guarantee that two arbitrarily
chosen lobe edges retain the same four-terminal frame.  Establishing that
frame preservation is the remaining dynamic step; it must not be inferred
from the static web alone.
