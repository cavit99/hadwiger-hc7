# Exact-six rural carrier: two-pole quotient and the fixed `{v,w}` endgame

**Status:** Theorems 2.1 and 3.1 are proved.  The block-expansion criterion
in Section 4 is proved only for a **local substitution inside the disk
formerly occupied by the contracted pole**.  This note identifies two
separate missing steps: expanding the selected poles, and assigning every
leftover shore component (including the side terminal) to the same disk
page.  Planarity of the selected quotient alone does not imply planarity of
the whole closed shore.

## 1. Locked rural carrier

Work in one terminal shore of the exact order-six Moser separation, with

\[
                         T=U\mathbin{\dot\cup}\{w\},
 \qquad U=\{0,2,4,5,6\}.                            \tag{1.1}
\]

Let `K,A,B` be a supported three-block frame core.  The pair carrier `K`
has trace `{x,y}`; `A,B` carry the other two frame traces.  Let `L` be the
fixed nonempty connected locked region.  Assume the rank-one branch:

\[
                       E(L,A\cup B)=\varnothing.       \tag{1.2}
\]

Write

\[
 Q_*=(N_K(A\cup B)-\{x,y\}),\qquad
 P_*=N_K(L)-\{x,y\}.                                 \tag{1.3}
\]

Every `q in Q_*` is a literal foreign portal.  In a branch with no labelled
peel,

\[
 Q_*\cap P_*=\varnothing,                            \tag{1.4}
\]

and every nonseparating `x-y` path avoiding `q` contains all of `P_*`.
Indeed a common vertex in (1.4), or a path omitting a member of `P_*`,
invokes the audited generalized pair-carrier peel.  The three-bypass
theorem gives `|Q_*|>=3`, and the five-attachment lock gives `|P_*|>=3`.

Choose the supported realization by the rank-first, carrier-minimal rule of
the audited block-terminal theorem.  In the three-connected branch, its
carrier is the literal planar rib of the one-call block-terminal web for
`Q_*,P_*`.

## 2. The carrier plus its two poles is literally planar

The set `A union B` is connected because the two core blocks are adjacent.
Contract it to a vertex `alpha`, and contract `L` to a vertex `beta`.

### Theorem 2.1 (literal two-pole planar quotient)

Let

\[
 R=G[K\cup A\cup B\cup L]/(A\cup B\mapsto\alpha,
                            L\mapsto\beta),           \tag{2.1}
\]

with loops deleted and parallel edges suppressed.  Under the hypotheses of
Section 1, `R` is planar.  More precisely, it is a subgraph of the plane
rib of a web with frame

\[
                         (x,\alpha,y,\beta).           \tag{2.2}
\]

#### Proof

Apply the block-terminal theorem to the induced carrier `K`, using the
whole sets `Q_*` and `P_*`.  Equations (1.3)--(1.4) and the universal
capture property exclude an `x-y | Q_*-P_*` linkage.  Rank-first
carrier-minimality evacuates every nonrib web cell, so the augmented graph

\[
                         K+\alpha Q_*+\beta P_*        \tag{2.3}
\]

is a subgraph of a plane rib with frame (2.2).

The only quotient edges not displayed in (2.3) can join `alpha` or `beta`
to one of the trace roots `x,y`.  They are among the four outer-frame edges
and hence also lie in the rib.  Equation (1.2) excludes the diagonal
`alpha beta`.  There are no other quotient edges by the definitions of
`Q_*` and `P_*`.  Thus every edge of `R` is an edge of the same plane rib.
\(\square\)

This is a literal minor statement: the only contractions are inside the
two named connected sets.  Web-completion edges are used only as a planar
supergraph certificate.  The theorem does not identify either pole with a
single original vertex and does not by itself color the uncontracted
blocks.

## 3. Exact fixed-pair endgame

Let `J_a,J_b` be the two closed terminal shores after deleting `v,w`, so
that

\[
 J_a\cap J_b=U,qquad E(J_a-U,J_b-U)=\varnothing,      \tag{3.1}
\]

and the literal graph on `U` is the five-cycle complementary to the
missing-edge cycle.

### Theorem 3.1 (bilateral cofacial gluing gives a fixed 2-apex pair)

If each `J_i` has a plane embedding in a closed disk whose boundary meets
the graph exactly in the same literal cycle `U`, then

\[
                         G-\{v,w\}\text{ is planar}.   \tag{3.2}
\]

Consequently `G` is six-colourable.

#### Proof

Draw `J_a` in the inside of the cycle `U` and, after reflection if
necessary, draw `J_b` in its outside.  The drawings agree on the five
literal boundary vertices and edges.  Equation (3.1) says there is no
unaccounted edge between the two open disks, so their union is a plane
drawing of `G-{v,w}`.

The Four Color Theorem gives a four-colouring of that graph.  Give `v,w`
two fresh colours (whether or not they are adjacent).  This is a proper
six-colouring of `G`, contrary to the counterexample hypothesis. \(\square\)

Thus the exact structural target is not generic planarity of a selected
carrier.  It is cofacial planarity of both whole closed shores with the
same literal five-cycle boundary.  Achieving it makes the **actual fixed
pair** `{v,w}` a 2-apex pair; equivalently it gives the stronger conclusion
that `G-{v,w}` is planar, not merely `K_5`-minor-free.

## 4. The precise expansion obstruction

Theorem 2.1 contracts two reserved blocks.  Expanding such a pole is a
finite-boundary society problem with a sharp topological criterion.

### Lemma 4.1 (local disk substitution criterion)

Let `R` be a plane graph, let `z` be a vertex, and choose a closed disk
`Delta_z` meeting `R` exactly in `z` and one initial segment of each edge
incident with `z`.  List those edge ends in their cyclic order on
`partial(Delta_z)`.  Replace `R cap Delta_z` by a connected graph
`X` drawn wholly inside `Delta_z`, assigning to every old edge end a
specified attachment vertex of `X`.  Such a local replacement exists if
and only if the society consisting of `X` and those attachment occurrences
has a disk embedding in which the occurrences appear on the disk boundary
in that cyclic order (up to reversal).

#### Proof

For sufficiency, place the prescribed disk embedding of `X` inside
`Delta_z` and join corresponding boundary occurrences to the old edge ends
by pairwise disjoint arcs in a collar of its boundary.  Necessity is
immediate from the definition of a local replacement: restrict its drawing
to `Delta_z`. \(\square\)

Applied to Theorem 2.1, the two selected pole societies are `A union B`
and `L`, with rotations supplied by the single block-terminal rib.
Therefore the **selected quotient subgraph** has an exact dichotomy:

1. both pole societies have the required disk embeddings, so this selected
   carrier-and-poles subgraph expands planarly; or
2. one pole society has a rotation obstruction.

The second outcome is a local obstruction.  The audited companion
tree-pole rotation theorem
`../results/hc7_exact7_tree_pole_rotation_exchange.md` converts failure
of a selected connector's rotation, without portal enumeration, to two
literal disjoint carriers joining alternating attachment occurrences.
It embeds only the selected connector, not the induced pole.  Even when both
poles expand, however, vertices of the closed shore outside
`K union A union B union L`, and the side terminal, have not yet been
embedded or assigned.

## 5. Remaining implication

The whole-shore assignment part is now governed by the audited spanning
rural quotient theorem
`../results/hc7_exact7_spanning_rural_quotient.md`.  It does not assume
that component absorption preserves connectivity or capture.  It returns
an actual low carrier cut, a shared portal, a set-terminal cross, a proper
bilateral three-gated cell, or a planar quotient in which every shore
vertex belongs to the carrier or one of the two poles.

To finish the rural branch one must therefore prove the following stronger
exact statement on **each** terminal shore:

> Every rank-first supported rural core either (i) expands its two selected
> poles and admits a compatible assignment of **every leftover shore
> component and the side terminal** to a disk embedding of the entire
> closed shore with boundary `U`, or (ii) a pole/leftover rotation
> obstruction yields a literal `K_7` model or a common bilateral equality
> state.

If both whole shores satisfy (i), Theorem 3.1 closes the conditional cell
with the fixed pair `{v,w}`.  The former nonspanning-carrier gap is closed
at quotient level.  The exact remaining work is to expand each **induced**
pole society, or convert one of the literal cut/cross/gate/alternating-path
certificates into a `K_7`, a common boundary state, or the same fixed pair.
That conversion must discharge the attained decorated-state duty; raw
contact alone is insufficient.
